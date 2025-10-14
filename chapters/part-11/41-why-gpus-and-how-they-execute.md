# 41. Why GPUs and How They Execute

Status: **Drafted.**

Part 11: GPU Fundamentals

## Learning outcome

Map a tensor operation to threads, warps, blocks, streaming multiprocessors, and arithmetic units without confusing the programming model with fixed hardware.

<a id="t-41-01"></a>
## CPU vs GPU

A CPU spends substantial silicon on sophisticated cores, large caches, branch prediction, and low-latency execution for a few instruction streams. A GPU devotes more resources to throughput across many threads and hides latency by switching among ready warps. This is a design emphasis, not a rule that CPUs are serial or GPUs are universally faster.

Small, irregular, branch-heavy work may favor CPUs. Large tensor operations expose thousands of similar operations and amortize launch and transfer costs, favoring GPUs. The host CPU still schedules work, prepares inputs, and runs control-heavy code.

<a id="t-41-02"></a>
## Why GPUs

Transformer training and inference repeatedly apply matrix multiplication, attention, normalization, and elementwise functions across many elements. The same program acts on different data, yielding abundant parallelism. GPUs also provide high device-memory bandwidth and specialized matrix units.

Speed requires enough work. A one-token, tiny-matrix operation may underfill the machine. Shapes, dtypes, memory layout, fusion, and batch size decide whether theoretical throughput is reachable.

<a id="t-41-03"></a>
## GPU anatomy

At a useful abstraction, an NVIDIA GPU contains streaming multiprocessors (SMs), an on-chip cache hierarchy, memory controllers connected to device memory, and engines for data movement. Each SM contains warp schedulers, register files, load/store units, scalar/vector arithmetic pipelines often called CUDA cores, special-function units, and Tensor Cores on architectures that provide them.

Exact counts and capabilities change by architecture. Treat product tables and the matching CUDA Programming Guide as versioned sources. As of September 2026, do not carry a tile shape or throughput number from one NVIDIA architecture to another without checking its compute capability.

<a id="t-41-04"></a>
## SMs

Blocks are assigned to SMs. An SM can host multiple blocks when registers, shared memory, thread slots, and block limits permit. Resident warps form the pool from which schedulers issue instructions. *Occupancy* is the ratio of active warps to the supported maximum, but maximum occupancy is not automatically maximum performance; extra registers or shared memory may reduce occupancy while enabling less memory traffic.

<a id="t-41-05"></a>
## Threads

A CUDA thread is a logical execution instance with indices identifying its element or tile. Consider vector addition for $n=1{,}000{,}000$: launch enough threads so thread $i$ computes `c[i] = a[i] + b[i]`, with a bounds check for excess threads. Threads have private logical state, usually allocated in registers when possible.

The programming model promises semantics, not a permanently dedicated core per thread. A thread can execute many instructions and may wait while another warp runs.

<a id="t-41-06"></a>
## Warps

On NVIDIA CUDA GPUs, threads execute in groups called warps, currently 32 threads in the documented programming model. A warp issues a common instruction across active lanes. If lanes take different control-flow paths, the machine executes paths with different masks, reducing useful parallel work. This divergence matters inside a warp; different warps may follow different paths independently.

<a id="t-41-07"></a>
## Blocks

A block groups threads that can cooperate through shared memory and block-level synchronization. Blocks should be independent because the scheduler may run them in any order. A grid is the collection of blocks for one kernel launch. For 1,000,000 elements and 256 threads per block, use $\lceil1{,}000{,}000/256\rceil=3907$ blocks.

Block size affects warp utilization and residency. Multiples of 32 avoid a mostly empty final warp within each full block, but the best size must be profiled.

For this particular million-element example, the final block contains 64 useful threads for block sizes 128, 256, and 512: the launch uses 7,813, 3,907, and 1,954 blocks respectively. Those 64 threads occupy two complete warps, so there is no partially active warp in the final block; the remaining warps in that block are wholly masked by the bounds check. This distinction prevents “partial block” from being confused with “partial warp.”

<a id="t-41-08"></a>
## CUDA cores

“CUDA core” is a marketing and architectural name for scalar arithmetic lanes, not an independently programmable CPU core. They execute operations such as FP32 arithmetic according to the SM's pipelines. Core counts alone do not predict application speed; instruction mix, clocks, memory traffic, occupancy, and issue utilization matter.

<a id="t-41-09"></a>
## Tensor Cores

Tensor Cores accelerate matrix multiply-accumulate on tiles using supported dtypes and layouts. Framework GEMMs can use them when shapes, alignment, dtype, and libraries allow. Mixed-precision training often multiplies low-precision inputs and accumulates at higher precision. Tensor Cores do not make every operation fast: softmax, indexing, small reductions, and poorly shaped GEMMs may bottleneck elsewhere.

<a id="t-41-10"></a>
## Registers

Registers are the fastest per-thread storage, allocated from an SM's finite register file. High register use can reduce resident blocks; if the compiler cannot keep values in registers, *spills* go to local memory, which resides in device memory and is much slower despite the name. Inspect compiler resource reports and profiler counters rather than guessing.

## Four recurring perspectives

- **Follow the Token:** token representations become rows and tiles distributed across threads and warps.
- **Follow the Gradient:** backward kernels expose similar parallelism but execute different operations and retain or recompute activations.
- **Follow the Byte:** registers and shared memory are scarce on-chip resources; device memory supplies much larger but slower storage.
- **Follow the Request:** launch dimensions and shapes derive from current batch, sequence, heads, and hidden width.

## Lab and exit check

Map a 1,000,000-element addition and a tiled matrix multiplication onto grid, blocks, warps, and lanes. Calculate blocks for 128, 256, and 512 threads; state separately how many threads, full warps, and partially active warps do useful work in the last block. On a CUDA system, inspect kernel register use and compare several block sizes without assuming occupancy predicts the winner.

## References

- NVIDIA, [CUDA C++ Programming Guide](https://docs.nvidia.com/cuda/cuda-c-programming-guide/) (version-sensitive; accessed September 2026).
- NVIDIA, [GPU Performance Background User's Guide](https://docs.nvidia.com/deeplearning/performance/dl-performance-gpu-background/index.html) (accessed September 2026).
