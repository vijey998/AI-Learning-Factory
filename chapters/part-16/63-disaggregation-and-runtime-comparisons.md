# 63. Disaggregation and Runtime Comparisons

Status: **Drafted.**

Part 16: Serving LLMs as a System

## Learning outcome

Compare pinned runtime architectures and calculate when KV transfer negates disaggregation gains.

## Prerequisites

CH-50, CH-52, CH-59, CH-62.

<a id="t-63-01"></a>
## Prefill/decode disaggregation

Coverage ID: `T-63-01`.

Prefill and decode have different resource profiles. Prefill processes many prompt tokens in parallel and is often compute-intensive; decode handles one new token per sequence and often streams weights/KV under a tight latency loop. Disaggregation places them on different worker pools and transfers KV state at the boundary.

Benefits include independent scaling and reduced interference. Costs include routing, KV transfer, failure coordination, and another queue. It only wins when saved interference or better utilization exceeds those costs under the real workload.

The prefill worker must hand off more than an untyped byte buffer: model revision, sequence and position metadata, KV layout, precision, and ownership of each cache block must agree. A partial or duplicated transfer needs an idempotent protocol or explicit request failure; silently decoding from incomplete KV state can yield plausible but invalid text.

<a id="t-63-02"></a>
## vLLM internals

Coverage ID: `T-63-02`.

vLLM centers serving around a scheduler, block-managed KV cache, continuous batching, optimized attention kernels, and model executors. Current releases include multiple parallel modes, prefix caching, chunked prefill, graph capture/compilation, and hardware plugins. These capabilities are version- and backend-dependent.

Its PagedAttention lineage reduces KV fragmentation, while scheduling integrates new work between iterations. Do not treat a project name as one static architecture: pin commit/release, engine generation, backend, model, and flags.

<a id="t-63-03"></a>
## TensorRT-LLM internals

Coverage ID: `T-63-03`.

TensorRT-LLM builds optimized inference engines around NVIDIA GPUs, with graph transformations, fused kernels, quantization choices, KV/cache management, batching, and distributed execution. Build-time and runtime profiles can specialize shapes and features for performance.

The benefit comes with platform specificity and engine lifecycle work. Unsupported model operations, changing shapes, or mismatched plugin/driver versions can trigger rebuilds or fallbacks. Benchmark the generated engine and exact software stack.

<a id="t-63-04"></a>
## llama.cpp architecture comparison

Coverage ID: `T-63-04`.

llama.cpp emphasizes portable local inference through its ggml tensor library, GGUF artifacts, quantized CPU kernels, memory mapping, and optional accelerator backends. It can offload layers while retaining CPU execution. This makes it suitable for laptops and heterogeneous devices.

vLLM targets throughput-oriented serving across varied accelerators; TensorRT-LLM specializes NVIDIA deployments; llama.cpp prioritizes compact portable execution. All can evolve. Compare required hardware, model coverage, scheduling, quantization, operational complexity, latency distribution, and reproducibility rather than declaring a universal winner.

<a id="t-63-05"></a>
## Transfer overhead

Coverage ID: `T-63-05`.

For $L$ layers, $H_{kv}$ KV heads, head dimension $d$, context $T$, and $b$ bytes per element, KV bytes per sequence are approximately $2LTH_{kv}db$. With 32 layers, 8 KV heads, $d=128$, $T=8192$, and BF16, this is 1 GiB (about 1.07 GB decimal). At an effective 25 GB/s, transfer alone is about 43 ms, excluding serialization, synchronization, and queueing.

If disaggregation saves 30 ms of contention but adds 50 ms end to end, it loses on latency. It may still win fleet throughput, so evaluate both. Prefix placement, RDMA, compression, and overlap change the equation but do not erase it.

## Four recurring perspectives

- **Follow the Token:** trace the representation and its ownership across the execution boundary.
- **Follow the Gradient:** identify synchronized or sharded learning state; for inference-only paths, state explicitly that no gradient exists.
- **Follow the Byte:** calculate persistent state, temporary buffers, transfers, and the relevant bandwidth tier.
- **Follow the Request:** include admission, scheduling, cancellation, failure, and externally visible latency.

## Lab and exit check

Pin one release each of vLLM, TensorRT-LLM, and llama.cpp. Fill a matrix for hardware, artifact, scheduling, KV management, quantization, compilation, and fallback behavior. Calculate KV transfer for at least three contexts and identify the break-even saved time.

Do not compare default commands as if they were equivalent configurations. Match model revision, precision, maximum context, prompt/output distributions, sampling, concurrency, and acceptance quality; list any feature that cannot be matched.

## Primary references

- [vLLM documentation](https://docs.vllm.ai/), accessed 2026-09-19.
- Kwon et al., [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://arxiv.org/abs/2309.06180), 2023.
- [TensorRT-LLM documentation](https://nvidia.github.io/TensorRT-LLM/), accessed 2026-09-19.
- [llama.cpp repository](https://github.com/ggml-org/llama.cpp), accessed 2026-09-19.
