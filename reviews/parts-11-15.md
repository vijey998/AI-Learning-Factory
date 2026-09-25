# Internal review: Parts 11–15

Date: 2026-09-19  
Scope: Chapters 41–60  
Review type: AI-assisted internal technical and editorial review; not an independent expert review.

## Review standard

This pass checked factual precision, hardware and distributed-systems claims, dimensional consistency, decimal-versus-binary units, calculations, worked examples, exercises, and primary-source posture. It preserved every curriculum anchor and chapter status line. It did not execute CUDA/NCCL benchmarks, reproduce cited paper results, validate behavior across GPU generations, or independently verify every external URL. Those remain release-gate work.

## Changes made

| Part | Focus of review | Material strengthening |
|---|---|---|
| 11, GPU fundamentals | Execution hierarchy, memory movement, rooflines, profiling | Corrected the partial-block/partial-warp exercise, made GB/GiB conversions explicit, added full-traffic arithmetic-intensity accounting, and distinguished logical effective bandwidth from controller traffic. |
| 12, kernels and runtimes | GEMM traffic, Triton semantics, compilation, graph amortization | Added exact MiB and throughput checks, corrected the Triton example so runtime length is not a compile-time constant, added irregular-shape and graph-recompilation tests, and clarified strict break-even accounting. |
| 13, inference mechanics | Forward shapes, KV state, decoding distributions, latency and memory budgets | Added element-to-byte derivations, cache-growth assertions, a fully worked top-k/top-p example with statistical expectations, and a consistent 24 GB/GiB capacity calculation. |
| 14, efficient inference | IO-aware attention, paging, scheduling, speculative decoding, quantization | Quantified page-boundary waste, made scheduling budget arithmetic concrete, added an end-to-end speculative-decoding counterexample, and calculated INT4 reconstruction error plus metadata-adjusted storage. |
| 15, distributed LLMs | Sharded state, partitioning, collectives, links, recovery | Added decimal/binary state totals, separated logical collective payload from per-rank wire bytes, corrected mixed GiB/GB/s all-reduce timing, and disambiguated checkpoint overhead denominators. |

## Calculation findings

- For 1,000,000 elements, block sizes 128, 256, and 512 all leave 64 useful threads in the final block. That is two full warps, not a partially active warp.
- A BF16 4096-by-4096 projection over 512 rows performs about 17.2 GFLOPs. Counting one input read, one weight read, and one output write gives 40 MiB of compulsory traffic and about 410 FLOP/byte, below the 512 FLOP/byte weight-only estimate.
- The reviewed KV example is dimensionally consistent: 32 layers, 8 KV heads, head width 128, and BF16 require 131,072 bytes per token per sequence; 8,192 tokens use exactly 1 GiB of logical KV payload.
- A 1 GiB ring all-reduce over eight ranks moves about 1.75 GiB per rank. This takes 35 ms at 50 GiB/s but about 37.6 ms at 50 decimal GB/s; the earlier mixed-unit calculation was corrected.
- Four minutes of synchronous checkpointing after 30 minutes of useful compute is 13.3% overhead relative to compute time and 11.8% of the resulting 34-minute wall-clock cycle.

## Evidence and citation posture

The chapters cite primary papers for Roofline, FlashAttention, PagedAttention, speculative decoding, quantization methods, ZeRO, model parallelism, pipeline parallelism, GShard, and bandwidth-optimal all-reduce. Architecture- and implementation-sensitive claims point to official CUDA, PTX, CUTLASS, Nsight, PyTorch, Triton, NCCL, GPUDirect, vLLM, and MLPerf documentation and are labelled as version-sensitive where appropriate. Product-specific peak numbers were intentionally avoided in favor of measured sustainable rates and pinned environments.

## Residual risks and required independent work

1. Run the CUDA, Triton, compiler, CUDA Graph, and profiler exercises on at least two materially different GPU architectures; retain traces, generated code, compiler diagnostics, and raw timing samples.
2. Execute cached-versus-uncached decoding, prefix reuse, paged allocation, speculative sampling, and quantization tests against pinned runtime commits and model revisions.
3. Run the distributed exercises on real intra-node and inter-node GPU topologies. Verify collective ordering, per-rank traffic, overlap, failure timeouts, checkpoint publication, and resharded resume.
4. Have a GPU-kernel specialist independently review Chapters 41–48 and an inference-runtime specialist independently review Chapters 49–56.
5. Have a distributed-training specialist independently review Chapters 57–60, especially version-specific FSDP2 semantics and topology-dependent NCCL behavior.
6. Perform a separate automated link and bibliographic-metadata check. This scoped review did not edit the central bibliography.

## Internal disposition

The scoped chapters are materially stronger and suitable for implementation testing and independent technical review. The manuscript checker passes after these edits. This review does not promote chapter status and must not be represented as external peer review, hardware validation, or reproduction of the cited results.
