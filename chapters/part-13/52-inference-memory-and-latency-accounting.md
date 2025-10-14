# 52. Inference Memory and Latency Accounting

Status: **Drafted**

## Build a budget before measuring

Capacity and speed claims need explicit workload: model revision, precision, B, prompt lengths, generated lengths, concurrency, hardware, and runtime.

<a id="t-52-01"></a>
## Inference memory accounting

Peak device memory is not merely checkpoint size. Track persistent weights, KV cache, live activations, logits, temporary workspaces, compiler/graph pools, communication buffers, allocator fragmentation, and runtime context. Measure both logical tensor bytes and process/device peaks.

<a id="t-52-02"></a>
## Weights plus KV plus activations plus overhead

For P parameters stored at b_w bytes, weights are P*b_w. KV is \(2LBH_{kv}SD_hb_{kv}\). Boundary activation [B,T,D] costs B*T*D*b_a, but peak activation depends on liveness and fused kernels. Add an empirically measured overhead term; do not invent a universal percentage.

Example: 7B BF16 weights are 14.0 GB (about 13.0 GiB). With L=32,Hkv=8,Dh=128,BF16, cache is 128 KiB per token per sequence. Four sequences at S=8192 use 4 GiB KV. A device marketed as 24 GB has about 22.35 GiB, leaving roughly 5.3 GiB after these logical weights and KV; it may still fail because workspaces, runtime state, and fragmentation need that remainder.

<a id="t-52-03"></a>
## Time to first token

TTFT runs from accepted request to first emitted token. Decompose queue delay, tokenization/transfer, cache lookup, prefill, sampling, and stream/network flush. “Model TTFT” may exclude queue and network; label scope. Prompt length strongly affects prefill.

<a id="t-52-04"></a>
## Inter-token latency

Inter-token latency is elapsed time between emitted tokens for one request. It includes scheduling gaps and may vary as batches change. Report a distribution rather than one average.

<a id="t-52-05"></a>
## TPOT

Time per output token often means generation-phase elapsed time divided by generated tokens, commonly excluding the first token. State the formula. The reciprocal approximates per-request tokens/s only under a stable sequence; averages and reciprocals do not commute.

<a id="t-52-06"></a>
## Throughput

Throughput can mean output tokens/s, total tokens/s, or requests/s. Batch and concurrency can improve total throughput while worsening each request's latency. Always pair throughput with latency SLOs, arrival process, and input/output length distributions.

<a id="t-52-07"></a>
## Memory per token

KV bytes/token/sequence equal \(2LH_{kv}D_hb_{kv}\), plus page metadata and internal waste. MQA/GQA reduce Hkv. Beam search and multiple return sequences multiply logical state; prefix sharing may reduce physical duplication.

<a id="t-52-08"></a>
## FLOPs per token

A useful dense-model approximation for one decode token is roughly twice the active parameter count for linear layers, because each weight contributes multiply-add work, plus attention over history and other operations. This is not exact: tied embeddings, MoE activation, quantization, sparsity, and dequantization change it. Prefill amortizes weights across T rows, whereas batch-one decode often streams large weight matrices for one row and becomes bandwidth-bound.

## Measurement protocol and four perspectives

Record wall-clock timestamps at admission, schedule, prefill start/end, each emission, and completion. Use warm and cold runs, synchronize device measurements, and sample memory peaks. Publish p50/p95/p99 and errors/cancellations.

- **Follow the Token:** each emitted token has a queue-to-stream timeline.
- **Follow the Gradient:** inference omits gradients and optimizer state; accidental autograd is a budget bug.
- **Follow the Byte:** separate logical bytes, allocated bytes, and device/process residency.
- **Follow the Request:** batching trades individual latency for system throughput.

Failures include decimal GB/GiB confusion, omitting one of K/V or layers, using maximum context for all traffic, averaging heterogeneous prompts, excluding queueing silently, and calling reciprocal mean latency “throughput.” The exit check derives the sample budget in bytes, converts once to GiB, reserves measured non-tensor overhead, and explains why it can OOM below nominal device capacity.

## Primary references

- MLCommons, [MLPerf Inference: Datacenter benchmark](https://mlcommons.org/benchmarks/inference-datacenter/), version-sensitive; accessed 2026-09-19.
- Kwon et al., [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://arxiv.org/abs/2309.06180), 2023.
- vLLM, [official documentation](https://docs.vllm.ai/en/latest/), version-sensitive; accessed 2026-09-19. Pin engine commit and configuration, model revision, hardware clocks and power, workload, tokenizer, and measurement boundary.
