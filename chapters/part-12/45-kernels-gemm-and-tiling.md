# 45. Kernels, GEMM and Tiling

Status: **Drafted**

## Prerequisites and learning outcomes

You should know warps, GPU memory, arithmetic intensity, and profiling. By the end, you can explain tiled matrix multiplication, estimate traffic, and identify which intermediate writes fusion removes.

<a id="t-45-01"></a>
## GPU kernels

A **kernel** is a function launched over many GPU threads. A launch defines a grid of blocks; a block is scheduled on one SM, and its threads execute in warps. Threads in a block may cooperate through shared memory and barriers. Blocks must be independent because their order is not guaranteed.

For vector addition, thread i loads x[i] and y[i], adds them, and stores z[i]. With FP32 that is about 12 bytes moved for one addition: extremely memory-bound. More threads do not change this ratio; they expose enough work to approach bandwidth. A correct kernel guards i < n because grids are rounded up.

<a id="t-45-02"></a>
## GEMM

GEMM computes $C_{M\times N}=A_{M\times K}B_{K\times N}$. Counting multiply and add as two FLOPs, it performs about $2MNK$ FLOPs. For $M=N=K=4096$, that is 137.4 GFLOPs. Reading A and B and writing C once in BF16 moves about 100.7 MB, while a naive per-output loop can move orders of magnitude more.

The same traffic is 96 MiB; the distinction matters when comparing with a bandwidth reported in GiB/s. If a synchronized kernel takes 1.0 ms, the arithmetic rate is 137.4 TFLOP/s and the compulsory-traffic rate is 96 GiB/s. Neither number alone proves the bottleneck because actual traffic can exceed the compulsory minimum and the kernel may read or write C depending on its epilogue.

<a id="t-45-03"></a>
## Tiling creates reuse

A tiled kernel assigns a block an output tile, then advances through K in chunks. It loads A and B tiles into shared memory and reuses each value for many multiply-accumulates; registers hold smaller accumulator tiles. For a 32-by-32 output tile and K chunk 32, two FP16 tiles cost 4096 bytes and support 65,536 FLOPs: 16 FLOPs/byte before output traffic. Larger tiles increase reuse but consume more shared memory and registers, potentially reducing occupancy.

<a id="t-45-04"></a>
## Tensor Core MMA

Tensor Cores execute matrix multiply-accumulate instructions on small fragments: conceptually \(D=AB+C\). Exact shapes and types depend on GPU architecture. Libraries decompose large GEMM into thread-block, warp, and instruction tiles and often accumulate in FP32 even when inputs are FP16/BF16. High peak throughput requires suitable dimensions, layout, alignment, and a pipeline that keeps operands available.

<a id="t-45-05"></a>
## Kernel launch overhead

The CPU prepares a launch, the runtime submits it, and the GPU schedules it. Fixed cost is negligible for a large GEMM but can dominate dozens of tiny kernels. CPU timing may measure asynchronous submission rather than completed work. Warm up, synchronize outside the interval, and use GPU events or a profiler.

<a id="t-45-06"></a>
## Kernel fusion

Suppose a linear layer writes a [B,T,D] BF16 tensor, then bias, GELU, and dropout each read and write it. At B=8,T=2048,D=4096 the tensor is 128 MiB. Three separate elementwise passes add roughly 768 MiB of reads and writes. A fused epilogue keeps partial results in registers and writes once. Fusion can backfire if register pressure spills or extra recomputation exceeds saved traffic.

## Four perspectives and exit check

- **Follow the Token:** one hidden row participates in GEMMs for Q, K, V and MLP projections.
- **Follow the Gradient:** training launches related activation- and weight-gradient GEMMs; inference has no backward pass.
- **Follow the Byte:** tiling turns repeated HBM loads into on-chip reuse; fusion removes round trips.
- **Follow the Request:** prompt and batch dimensions choose GEMM shapes and kernel efficiency.

Failures include bad edge masks, bank conflicts, uncoalesced access, spilling, and missing synchronization in benchmarks. For a non-square case such as M=511, N=769, K=1024, calculate $2MNK$, identify edge tiles, and name materializations a fused activation avoids. Explain why a 128-by-128 tile can lose to 64-by-64 even though its nominal reuse is greater.

## Primary references

- NVIDIA, [CUDA C++ Programming Guide](https://docs.nvidia.com/cuda/cuda-c-programming-guide/), version-sensitive; accessed 2026-09-19.
- NVIDIA, [Parallel Thread Execution ISA](https://docs.nvidia.com/cuda/parallel-thread-execution/), version-sensitive; accessed 2026-09-19.
- NVIDIA, [CUTLASS documentation](https://docs.nvidia.com/cutlass/), version-sensitive; accessed 2026-09-19. Pin GPU architecture, toolkit, driver, library commit, dtype, and shapes.
