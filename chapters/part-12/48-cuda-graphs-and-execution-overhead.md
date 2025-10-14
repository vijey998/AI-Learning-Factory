# 48. CUDA Graphs and Execution Overhead

Status: **Drafted**

## Why a fast kernel can make a slow program

When kernels take microseconds, Python, dispatch, driver submission, and synchronization gaps can dominate wall time. This chapter separates computation from orchestration.

<a id="t-48-01"></a>
## CUDA Graphs

A CUDA Graph records GPU operations and dependencies, then instantiates an executable graph. Later iterations launch it as a unit. Capture requires graph-safe behavior: addresses and structure generally remain stable, allocations and CPU synchronization inside capture are restricted, and inputs commonly use long-lived static buffers.

<a id="t-48-02"></a>
## Dispatch overhead

Suppose decode launches 80 kernels averaging 4 microseconds, with 3 microseconds of host gap each. Device work is 320 microseconds and gaps add 240: orchestration consumes 43% of the 560-microsecond path. Faster kernels cannot remove gaps. Fusion reduces launch count; compilation reduces framework overhead; CUDA Graphs reduce repeated submission.

<a id="t-48-03"></a>
## Graph replay

Allocate static inputs/outputs; warm libraries and memory pools on a side stream; synchronize; capture one iteration; instantiate; copy new values into static buffers; replay; consume outputs after stream synchronization. Replay changes values, not topology. Hazards include reading before completion, mutating storage during replay, random-number semantics, and stale pointers. Compare replay with eager across multiple inputs.

<a id="t-48-04"></a>
## Shape specialization

Requests vary in batch, prompt length, and live sequences. Systems use shape buckets, padding, multiple graphs, or leave dynamic regions uncaptured. Padding wastes compute; many variants increase warmup and memory. Decode is easier to capture than arbitrary prefill because token width is one, but changing batch membership still needs stable buffers and masks.

<a id="t-48-05"></a>
## Compilation amortization

Let setup be C, eager latency E, and replay R<E. Break-even reuse is \(N>C/(E-R)\). If setup costs 2 seconds and saves 0.5 ms, equality occurs at 4,000 iterations; a strict net win begins after 4,000, assuming every request hits that graph. At a 75% graph-cache hit rate, the expected saving per request is not 0.5 ms unless the miss path is measured too. Report cold start, warmup, cache hit rate, miss cost, and steady latency. A frequently reloaded service may never amortize an optimization that wins a long benchmark.

## Measurement, perspectives, and exit check

Measure identical inputs across warmed eager, warmed torch.compile, and replay. Separate setup. Use GPU events, repeated trials, synchronization outside intervals, and p50/p95/p99. A profiler should show gaps shrinking.

- **Follow the Token:** values change while addresses and topology remain stable.
- **Follow the Gradient:** training capture must preserve backward and optimizer semantics.
- **Follow the Byte:** static pools trade persistent memory for allocation-free replay.
- **Follow the Request:** scheduling maps variable requests into captured shapes.

Design buckets for batch 1–32 and calculate break-even. Failures include capture before warmup, hidden synchronization, stale buffers, stream mistakes, excessive padding, graph-cache explosion, and reporting replay without setup.

## A concrete bucket policy

One starting policy captures batch capacities 1, 2, 4, 8, 16, and 32. A batch of 11 uses the 16-slot graph and masks five rows. This bounds the number of graph variants but can waste nearly half the work just above a power of two. A traffic trace should reveal whether adding intermediate buckets pays for its compilation and memory. Measure graph-cache misses during bursts, because a policy that looks efficient after a long warmup can produce severe cold tail latency.

Graph replay also does not replace dependency management. Input copies, collective communication, and output consumers must use compatible streams and events. Capturing communication may impose additional version and topology constraints. When a request is cancelled, its masked slot and static buffers still need a defined lifecycle; otherwise stale data can leak into a later replay.

## Primary references

- NVIDIA, [CUDA C++ Programming Guide: CUDA Graphs](https://docs.nvidia.com/cuda/cuda-c-programming-guide/#cuda-graphs), version-sensitive; accessed 2026-09-19.
- NVIDIA, [CUDA Runtime API: Graph Management](https://docs.nvidia.com/cuda/cuda-runtime-api/group__CUDART__GRAPH.html), version-sensitive; accessed 2026-09-19.
- PyTorch, [CUDA semantics: CUDA Graphs](https://docs.pytorch.org/docs/stable/notes/cuda.html#cuda-graphs), version-sensitive; accessed 2026-09-19. Pin driver, toolkit, PyTorch, allocator, graph mode, and shapes.
