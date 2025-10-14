# 59. Collectives and Interconnects

Status: **Drafted.**

Part 15: Distributed LLMs

## Learning outcome

Match each parallel strategy to collectives and estimate transfer time.

## Prerequisites

CH-58.

<a id="t-59-01"></a>
## Broadcast

Coverage ID: `T-59-01`.

Broadcast copies one root tensor to all ranks. Use it for configuration or synchronized control state, not gradient averaging. Broadcasting a huge checkpoint from one root may bottleneck that host; sharded parallel reads are often better. Every rank must participate in the same communicator order.

<a id="t-59-02"></a>
## All-reduce

Coverage ID: `T-59-02`.

All-reduce combines tensors elementwise and leaves the result everywhere. DDP uses it for gradients. A ring moves roughly $2(N-1)/N$ times the tensor size per rank. For a 1 GiB buffer over eight ranks, that is about 1.75 GiB. At an effective 50 GiB/s, bandwidth time alone is 35 ms; at 50 decimal GB/s it is about 37.6 ms. Latency, protocol overhead already absent from the effective rate, and contention can add more.

<a id="t-59-03"></a>
## All-gather

Coverage ID: `T-59-03`.

All-gather concatenates one shard from every rank and returns the full logical tensor to all. FSDP uses it to materialize weights before a module. The gathered tensor raises peak memory; its allocation and release timing matter alongside transfer speed.

<a id="t-59-04"></a>
## Reduce-scatter

Coverage ID: `T-59-04`.

Reduce-scatter reduces corresponding elements and leaves each rank one output shard. FSDP uses it for gradients. Reduce-scatter plus all-gather decomposes the logical work of all-reduce while letting ranks retain only owned state between phases.

<a id="t-59-05"></a>
## All-to-all

Coverage ID: `T-59-05`.

All-to-all sends distinct slices between all rank pairs. Expert parallelism uses it for token dispatch and return. Uneven splits and hot experts create tails. Many peer exchanges stress topology differently from a ring, so payload alone is not enough to predict time.

<a id="t-59-06"></a>
## NCCL

Coverage ID: `T-59-06`.

NCCL implements GPU collectives and selects algorithms and transports from topology and runtime conditions. Applications still define communicator membership and call order. Record NCCL version, topology, rank mapping, sizes, environment overrides, and observed overlap. A collective microbenchmark cannot prove application overlap.

<a id="t-59-07"></a>
## PCIe

Coverage ID: `T-59-07`.

PCIe connects GPUs, CPUs, NICs, and storage through root complexes and switches. Quoted generation bandwidth is a link maximum. Peer bandwidth depends on lane width, path, protocol overhead, and concurrent traffic. A path staging through host memory differs radically from direct peer access.

<a id="t-59-08"></a>
## NVLink

Coverage ID: `T-59-08`.

NVLink provides high-bandwidth GPU peer connectivity on supported platforms. Link count and capability vary by generation and SKU. Never import a bandwidth value from a different system; measure the real peer pair in both directions.

<a id="t-59-09"></a>
## NVSwitch

Coverage ID: `T-59-09`.

NVSwitch forms a switched GPU fabric and reduces point-to-point topology asymmetry. It does not abolish contention, and inter-node traffic still reaches a NIC. Concurrent jobs and collectives can share fabric resources.

<a id="t-59-10"></a>
## InfiniBand

Coverage ID: `T-59-10`.

InfiniBand is a common inter-node fabric. GPUDirect RDMA can allow NIC access to GPU memory without CPU staging. End-to-end performance still depends on NIC placement, switch oversubscription, congestion, routing, and GPU-to-NIC affinity.

A first model is $t\approx \alpha s+V/B_{eff}$, with steps $s$, step latency $\alpha$, per-rank wire bytes $V$, and measured effective bandwidth $B_{eff}$. Do not substitute logical tensor size for $V$ without the collective's algorithmic factor. Tiny collectives are latency-bound; large ones are bandwidth-bound. Overlap and stragglers require measurement.

## Four recurring perspectives

- **Follow the Token:** trace the representation and its ownership across the execution boundary.
- **Follow the Gradient:** identify synchronized or sharded learning state; for inference-only paths, state explicitly that no gradient exists.
- **Follow the Byte:** calculate persistent state, temporary buffers, transfers, and the relevant bandwidth tier.
- **Follow the Request:** include admission, scheduling, cancellation, failure, and externally visible latency.

## Lab and exit check

Estimate ring all-reduce time for 16 MiB, 256 MiB, and 1 GiB on eight ranks using explicit hypothetical per-step latency and effective bandwidth. Show the $2(N-1)$ ring phases and the $2(N-1)/N$ per-rank byte factor, keeping GiB with GiB/s. Compare intra-node and inter-node values and explain why peak link bandwidth is not effective bandwidth.

## Primary references

- [NCCL collective operations](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/usage/collectives.html), accessed 2026-09-19.
- [NVIDIA GPUDirect RDMA](https://docs.nvidia.com/cuda/gpudirect-rdma/), accessed 2026-09-19.
- Patarasuk and Yuan, [Bandwidth Optimal All-reduce](https://doi.org/10.1016/j.jpdc.2009.05.002), 2009.
