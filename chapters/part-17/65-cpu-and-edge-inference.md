# 65. CPU and Edge Inference

Status: **Drafted.**

Part 17: LLMs on Your Laptop

## Learning outcome

Measure CPU decode with controlled thread counts and explain memory bandwidth effects.

## Prerequisites

CH-64.

<a id="t-65-01"></a>
## Edge constraints

Coverage ID: `T-65-01`.

Edge deployment begins with a budget: usable RAM, memory bandwidth, supported instructions, cores, power, cooling, storage, startup limit, and required context/output rate. The device may be offline, shared with a UI, or limited to a few watts. “Runs” is weaker than “meets sustained latency without exhausting memory or degrading the host.”

Model choice must include artifact size, KV growth, workspace, tokenizer, and application state. Reserve operating-system headroom. A model that uses every byte in a clean benchmark will fail when the real application allocates buffers.

<a id="t-65-02"></a>
## CPU inference

Coverage ID: `T-65-02`.

Autoregressive decode repeatedly streams model weights for matrix-vector-like work. At low batch size it is frequently memory-bandwidth-bound. A simple ceiling is effective memory bandwidth divided by bytes read per token. If a 4.5 GB quantized weight image must effectively be read once per token and measured bandwidth is 45 GB/s, the optimistic ceiling is about 10 tokens/s before KV traffic and other overhead.

Prefill has more matrix-matrix reuse and can behave differently. Measure prompt processing and decode separately. Cache state, NUMA placement, memory channels, model quantization, and context length all matter.

The bandwidth division is a roofline-style upper bound, not a prediction. Weight pages may remain in last-level cache for very small models, some tensors may be reused or repacked, and KV reads grow with context. Measure bytes through hardware counters where possible; otherwise call the assumed bytes/token an estimate and reconcile it with resident-set size and observed bandwidth.

<a id="t-65-03"></a>
## SIMD

Coverage ID: `T-65-03`.

Single Instruction Multiple Data executes one instruction over vector lanes. x86 AVX2/AVX-512, Arm NEON/SVE, and matrix extensions offer different widths and operations. Quantized kernels unpack values, accumulate into wider types, and apply scales. Alignment, tails, and conversion overhead can reduce theoretical gains.

Binaries should dispatch to features detected at runtime or ship conservative targets. Compiling for an instruction unavailable on the destination gives an illegal-instruction crash, not a graceful slowdown.

<a id="t-65-04"></a>
## CPU vectorization

Coverage ID: `T-65-04`.

Useful vectorization depends on contiguous layout and loop structure. Packed quantized blocks should match the kernel's load and dot-product pattern. Compilers may auto-vectorize simple loops, but production runtimes often use architecture-specific kernels because dequantization and horizontal reductions need careful scheduling.

Verify generated instructions or profiler samples. A “vectorized” source expression may compile to scalar work because of aliasing, misalignment, or unsupported dtype conversion.

<a id="t-65-05"></a>
## CPU threading

Coverage ID: `T-65-05`.

More threads help until memory bandwidth saturates or overhead dominates. Physical cores, simultaneous multithreading, NUMA nodes, and competing processes change the curve. Thread pools should avoid oversubscription between application, BLAS, and runtime layers.

Benchmark 1, 2, 4, … threads with affinity controlled. Report median and tail decode latency and system responsiveness. If eight threads equal sixteen, the extra threads may only consume power. On multi-socket systems, first-touch allocation and NUMA-local execution can matter more than thread count.

## Four recurring perspectives

- **Follow the Token:** trace the representation and its ownership across the execution boundary.
- **Follow the Gradient:** identify synchronized or sharded learning state; for inference-only paths, state explicitly that no gradient exists.
- **Follow the Byte:** calculate persistent state, temporary buffers, transfers, and the relevant bandwidth tier.
- **Follow the Request:** include admission, scheduling, cancellation, failure, and externally visible latency.

## Lab and exit check

Run one pinned quantized model and prompt with controlled context and output. Sweep thread counts, discard warmup, and report prompt tokens/s, decode tokens/s, p95 token latency, memory use, bandwidth counters if available, CPU power/temperature, and host responsiveness. Explain the saturation point with bytes per token.

Repeat one point with threads pinned within a NUMA node and one spanning nodes. Record whether the model pages were first-touched locally; otherwise a topology conclusion may actually be a memory-placement artifact.

## Primary references

- [llama.cpp performance documentation and source](https://github.com/ggml-org/llama.cpp), accessed 2026-09-19.
- [Intel Intrinsics Guide](https://www.intel.com/content/www/us/en/docs/intrinsics-guide/index.html), accessed 2026-09-19.
- [Arm ACLE](https://arm-software.github.io/acle/), accessed 2026-09-19.
