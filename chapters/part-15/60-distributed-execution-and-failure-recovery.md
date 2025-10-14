# 60. Distributed Execution and Failure Recovery

Status: **Drafted.**

Part 15: Distributed LLMs

## Learning outcome

Run a two-process CPU simulation and specify the real multi-GPU validation gate.

## Prerequisites

CH-59.

<a id="t-60-01"></a>
## Distributed training failures

Coverage ID: `T-60-01`.

Distributed jobs fail as a group. Classes include mismatched collective order or shape, transport loss, one-rank OOM, numerical divergence, and silent data corruption. A rank throwing before a collective leaves peers waiting for timeout. Logs need rank, host, device, step, last collective, tensor metadata, versions, and topology.

Correctness gates precede scale: compare one-rank and two-rank updates under matched global batch, checksum initial parameters, verify sampler disjointness, resume checkpoints, and inject one process failure.

<a id="t-60-02"></a>
## Distributed inference

Coverage ID: `T-60-02`.

Inference may use data, tensor, pipeline, context, or expert parallelism. Data replicas serve independent requests with little cross-replica token traffic. Model-parallel requests communicate during each token, placing topology directly on latency. Variable output lengths complicate pipeline scheduling.

Conversation state has ownership. Routing a next turn away from its KV or prefix cache forces transfer or recomputation. All ranks also need the same tokenizer, revision, adapter, and sampling semantics.

<a id="t-60-03"></a>
## Stragglers

Coverage ID: `T-60-03`.

Synchronous execution proceeds at the slowest rank. Thermal throttling, network congestion, data stalls, background load, retries, or skewed experts create stragglers. Mean kernel time can remain healthy while collective tails grow.

Collect per-rank timing around compute and collectives and compare distributions. Increasing timeouts merely hides many stragglers and wastes capacity longer.

<a id="t-60-04"></a>
## Multi-GPU execution

Coverage ID: `T-60-04`.

A launcher assigns global rank, local rank, world size, and rendezvous data. Bind the intended device before model allocation. Construct process groups to match topology, such as tensor parallel ranks inside a node and corresponding data ranks across nodes.

A two-process CPU Gloo test validates rank logic and collective math. It cannot validate CUDA streams, NCCL transport, GPU peak memory, or overlap. The target gate records topology, memory, collective traces, numerical comparison, steady throughput, and failure injection on real GPUs.

<a id="t-60-05"></a>
## Checkpoint recovery

Coverage ID: `T-60-05`.

A recoverable checkpoint includes parameters, optimizer and scheduler state, loss-scaler state, data position, RNG states, and sharding metadata. Write a temporary generation, validate all shards and manifest, then atomically publish completion. A directory visible before all ranks finish is not valid.

Checkpoint interval balances overhead with expected lost work. A synchronous four-minute checkpoint after every 30 minutes of useful compute adds $4/30=13.3\%$ overhead relative to compute time and occupies $4/34=11.8\%$ of resulting wall time. Async writes can hide blocking time but consume bandwidth and add consistency risks. Test resharding to another world size; rank-numbered blobs are not inherently portable.

## Four recurring perspectives

- **Follow the Token:** trace the representation and its ownership across the execution boundary.
- **Follow the Gradient:** identify synchronized or sharded learning state; for inference-only paths, state explicitly that no gradient exists.
- **Follow the Byte:** calculate persistent state, temporary buffers, transfers, and the relevant bandwidth tier.
- **Follow the Request:** include admission, scheduling, cancellation, failure, and externally visible latency.

## Lab and exit check

Use `torch.distributed` and Gloo with two CPU processes. All-reduce a scalar and assert the result, then terminate one process before another collective and assert a bounded timeout rather than allowing the test to hang. Save each rank's last-step and last-collective record. Write a separate real-GPU acceptance gate covering NCCL topology, peak memory, overlap, numerics, throughput, checkpoint resume, and rank-failure recovery.

## Primary references

- [PyTorch distributed overview](https://docs.pytorch.org/docs/stable/distributed.html), accessed 2026-09-19.
- [PyTorch Distributed Checkpoint](https://docs.pytorch.org/docs/stable/distributed.checkpoint.html), accessed 2026-09-19.
- [NCCL troubleshooting](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/troubleshooting.html), accessed 2026-09-19.
