# 57. Parallel Training Strategies

Status: **Drafted.**

Part 15: Distributed LLMs

## Learning outcome

Account for parameter, gradient and optimizer storage under replication and sharding.

## Prerequisites

CH-56.

<a id="t-57-01"></a>
## Why one accelerator stops being enough

Coverage ID: `T-57-01`.

A training step must accommodate persistent model state and temporary activations. For (P) parameters trained with mixed-precision Adam, a useful first estimate is 2 bytes of BF16 weights, 2 bytes of gradients, and 8 bytes for two FP32 Adam moments per parameter: roughly (12P) bytes before activations, allocator fragmentation, communication buffers, or a possible FP32 master copy. A 7-billion-parameter model therefore starts near 84 GB. Long sequences may make saved activations the limiting term even when weights fit.

In binary units, 84,000,000,000 bytes is about 78.2 GiB. If the optimizer keeps a separate FP32 master parameter copy, add 28 GB (26.1 GiB), raising this simplified total from 12 to 16 bytes per parameter. State the optimizer implementation: fused and quantized optimizers can use different state and temporary buffers.

Multiple accelerators do not create one magical memory pool. A strategy defines tensor ownership, reconstruction, and communication. Ask which state is replicated, which is sharded, which is transiently gathered, and which operation sits on the critical path.

<a id="t-57-02"></a>
## Data parallelism

Coverage ID: `T-57-02`.

Every rank owns the same model and consumes different examples. For global batch (B) over (N) ranks, each commonly receives (B/N) examples. Ranks reduce local gradients and apply identical updates. It scales throughput and divides activation memory for a fixed global batch, but does not divide model state.

Silent failures include overlapping sampler shards and inconsistent loss normalization. A run can be fast while its effective data distribution or learning rate is wrong. Compare a distributed step with a single-rank reference under the same global batch.

<a id="t-57-03"></a>
## DDP

Coverage ID: `T-57-03`.

Distributed Data Parallel overlaps reduction with backpropagation. When autograd completes a gradient bucket, an all-reduce can begin while earlier layers are still computing. Every rank finishes with the reduced gradient and independently performs the same optimizer step.

The 7B example still carries roughly 84 GB of model state per rank. DDP is attractive when that fits because replication simplifies execution. Bucket sizing controls overlap: tiny buckets expose launch latency; huge buckets start too late. Rank-dependent control flow can leave collectives unmatched and hang the job.

<a id="t-57-04"></a>
## ZeRO

Coverage ID: `T-57-04`.

The Zero Redundancy Optimizer removes replicated state across (N) data-parallel ranks. Under the 2-byte weights, 2-byte gradients, 8-byte moments assumption, DDP uses about 12 bytes per parameter per rank. ZeRO-1 shards optimizer state: (4+8/N). ZeRO-2 also shards gradients: (2+10/N). ZeRO-3 shards parameters too: about (12/N).

These are persistent-state estimates, not peak-memory promises. ZeRO-3 gathers parameters for computation and needs buffers; activations remain unless separately recomputed, offloaded, or sharded. Dividing total observed peak by (N) is therefore incorrect.

<a id="t-57-05"></a>
## FSDP

Coverage ID: `T-57-05`.

PyTorch FSDP2 represents sharded parameters with DTensor. Before a wrapped module executes, ranks all-gather its parameter shards; after use, full parameters can be released. Backward reduce-scatters gradients so each rank retains only its shard. Wrapping boundaries control the size and lifetime of materialized weights.

FSDP trades memory for collectives. One giant unit gathers too much; tiny units create excessive calls. Prefetch can hide communication behind compute but may increase peak memory. Pin the PyTorch version and API: current documentation distinguishes FSDP2 from deprecated FSDP1.

<a id="t-57-06"></a>
## Sharded optimizer state

Coverage ID: `T-57-06`.

Adam keeps first and second moments. A sharded optimizer updates only the owned parameter shard using its reduced gradient shard. For 7B parameters and eight ranks, 56 GB (52.2 GiB) of FP32 moments becomes 7 GB (6.52 GiB) per rank before overhead. Under the chapter's assumptions, the complete ZeRO-3 persistent share is 10.5 GB (9.78 GiB) per rank; temporary all-gathers and activations sit on top.

Checkpoint metadata must map logical parameters to shards. A pile of rank-numbered files is insufficient when recovery uses another world size. Save logical tensor metadata, optimizer mapping, RNG and scheduler state, and validate resharding.

## Four recurring perspectives

- **Follow the Token:** trace the representation and its ownership across the execution boundary.
- **Follow the Gradient:** identify synchronized or sharded learning state; for inference-only paths, state explicitly that no gradient exists.
- **Follow the Byte:** calculate persistent state, temporary buffers, transfers, and the relevant bandwidth tier.
- **Follow the Request:** include admission, scheduling, cancellation, failure, and externally visible latency.

## Lab and exit check

For $P=7\times10^9$, calculate persistent state for DDP and every ZeRO stage at $N=8$, first in bytes and then GiB. Add an explicit activation estimate and a 15% reserve applied to a clearly named subtotal. Explain why gathered modules can still cause an OOM. You pass when you can identify the tensor and collective at each FSDP boundary and explain why activation memory is separate.

## Primary references

- [PyTorch FSDP2 tutorial](https://docs.pytorch.org/tutorials/intermediate/FSDP_tutorial.html), accessed 2026-09-19.
- Rajbhandari et al., [ZeRO](https://arxiv.org/abs/1910.02054), 2020.
- [PyTorch DistributedDataParallel API](https://docs.pytorch.org/docs/stable/generated/torch.nn.parallel.DistributedDataParallel.html).
