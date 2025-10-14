# 46. CUDA, Triton and CUTLASS

Status: **Drafted**

## Prerequisites and learning outcomes

After Chapter 45, you can choose an abstraction level, write a masked fused kernel, validate it, and profile it honestly.

<a id="t-46-01"></a>
## CUDA: explicit control

CUDA C++ exposes kernels, blocks, shared memory, streams, events, and architecture intrinsics. Exact control creates obligations: index arithmetic, bounds, synchronization, layout, occupancy, compilation targets, and error checking. A fused bias-plus-ReLU kernel maps one thread to one element, loads x and bias, computes max(x+b,0), and stores once. Every thread checks the boundary. Test lengths such as 1003; powers of two can hide indexing defects.

<a id="t-46-02"></a>
## Triton: blocked programs

Triton expresses a kernel as many instances of a **program** operating on vector blocks. program_id selects a block; arange, masked loads, and stores describe lanes. Its compiler maps operations to GPU instructions. This makes fused elementwise work and many tiled kernels shorter than CUDA while retaining explicit layouts and block sizes.

<a id="t-46-03"></a>
## CUTLASS-level concepts

CUTLASS composes GEMM from nested device, thread-block, warp, and MMA instruction tiles. An operation specifies layouts, input and accumulator types, pipeline stages, alignment, and an **epilogue** that can fuse scaling, bias, or activation. Vendor libraries remain the default for standard GEMM. CUTLASS helps with specialized layouts, fused epilogues, and new numeric formats. A configuration copied across GPU generations may underperform.

<a id="t-46-04"></a>
## Simple Triton kernel

```python
@triton.jit
def add_relu(x, b, y, n, BLOCK: tl.constexpr):
    offsets = tl.program_id(0) * BLOCK + tl.arange(0, BLOCK)
    mask = offsets < n
    values = tl.load(x + offsets, mask=mask)
    bias = tl.load(b + offsets, mask=mask)
    tl.store(y + offsets, tl.maximum(values + bias, 0.0), mask=mask)
```

Here `n` is a runtime scalar while `BLOCK` is a compile-time specialization parameter. Test NaNs, negatives, multiple dtypes, small inputs, and awkward lengths. Decide and test the NaN contract explicitly because `maximum` behavior must match the chosen framework reference. Compare with `torch.relu(x+b)` using dtype-appropriate tolerance. Correctness comes before speed.

<a id="t-46-05"></a>
## GPU profiling

First verify results. Warm compilation, allocator caches, and clocks. Benchmark with GPU events. Use Nsight Systems for CPU/GPU timing and Nsight Compute for kernel counters. Compare matched shapes, dtypes, and outputs. Inspect bandwidth, Tensor Core use, occupancy, transactions, register spills, and launch gaps. High occupancy can coexist with poor access; lower occupancy may win when each warp does more useful work.

## Four perspectives, failures, and exit check

- **Follow the Token:** rows become lanes and tiles while semantics must match the reference.
- **Follow the Gradient:** a training operator needs backward code and gradient checks.
- **Follow the Byte:** count loads/stores and prove fusion removed an intermediate.
- **Follow the Request:** autotuning and compilation are cold costs; steady traffic sees cached kernels.

Failures include missing masks, wrong strides, overflow, races, synchronization, benchmarking compilation, and comparing different precision. Implement fused add-plus-activation, test irregular shapes, and report cold time, warmed median, p95, and environment.

Include a byte check: two input loads plus one output store imply 6 bytes per BF16 element before transaction overhead. For 16 million elements that is about 91.6 MiB; a 0.20 ms kernel corresponds to about 447 GiB/s of effective logical bandwidth. Compare that value with a same-shape copy benchmark rather than a datasheet peak.

The benchmark must include a meaningful baseline. Comparing a custom kernel only with two unfused Python operations proves little if the framework already has a fused implementation. Compare against the best available framework path, retain identical output precision, and publish cases where the custom kernel loses. Autotuning also belongs in the cost model: record how many candidates were compiled and measured, whether the cache survived process restart, and how an unseen shape behaves.

## Primary references

- NVIDIA, [CUDA C++ Programming Guide](https://docs.nvidia.com/cuda/cuda-c-programming-guide/), version-sensitive; accessed 2026-09-19.
- OpenAI, [Triton tutorials](https://triton-lang.org/main/getting-started/tutorials/), version-sensitive; accessed 2026-09-19.
- NVIDIA, [CUTLASS documentation](https://docs.nvidia.com/cutlass/), version-sensitive; accessed 2026-09-19.
- NVIDIA, [Nsight Compute documentation](https://docs.nvidia.com/nsight-compute/), version-sensitive; accessed 2026-09-19. Pin Python, PyTorch, Triton, toolkit, driver, GPU, and commits.
