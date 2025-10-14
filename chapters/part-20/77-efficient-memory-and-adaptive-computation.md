# 77. Efficient Memory and Adaptive Computation

Status: **Draft — not yet independently reviewed.**

A conventional decoder stores every layer’s keys and values and executes every layer for every generated token. Those choices are simple and robust, not laws of nature. Changing them trades memory or compute for approximation risk and control overhead.

<a id="t-77-01"></a>
## Efficient KV memory

For $L$ layers, $H_{kv}$ key-value heads, head width $d_h$, context $T$, batch $B$, and $s$ bytes per element, a basic KV cache occupies

$$M_{KV}=2LBTH_{kv}d_hs.$$

The factor two is keys plus values. GQA and MQA reduce $H_{kv}$; lower precision reduces $s$; paging reduces allocation waste but not logical KV content. Before inventing an eviction policy, calculate which factor dominates the intended workload.

<a id="t-77-02"></a>
## KV-cache compression

Compression can quantize values, store low-rank or clustered approximations, share structure, or retain full precision for sensitive tokens and layers. Evaluate perplexity or task quality across context lengths and decode positions, not just reconstruction error. Quantization metadata and dequantization kernels consume memory and time. A nominal four-bit cache may not produce a clean 4x system reduction after scales, alignment, fragmentation, and uncompressed regions.

<a id="t-77-03"></a>
## KV-cache eviction

Eviction retains a token subset under a memory budget. Sliding windows keep recent tokens; attention-sink approaches preserve initial tokens plus a recent window; score-based methods keep tokens judged important from past attention. Past attention is an imperfect predictor of future need, especially when a late question refers to an early detail. Policies must operate per layer or coordinate across layers, and compaction itself moves bytes. Test adversarial retrieval, long-range dependencies, and changing topics.

Eviction changes which keys and values are available, not the historical position of retained tokens. Preserve the model's position semantics—especially rotary position indices—when compacting physical storage. Renumbering retained entries as if they were a shorter fresh sequence is a different approximation and can corrupt attention even when the selected tokens were correct.

<a id="t-77-04"></a>
## Activation compression

Training stores activations for backward; distributed inference may transmit activations between stages or machines. Quantization, sparsification, low-rank coding, and checkpoint recomputation reduce storage or traffic. The relevant objective is end-to-end step time or request latency at matched quality. Compression can be slower when encode/decode kernels or synchronization exceed bytes saved. Error can compound across repeatedly compressed boundaries.

<a id="t-77-05"></a>
## Dynamic computation

Dynamic computation chooses work from the input or intermediate state. Examples include early exits, conditional experts, speculative paths, token pruning, and layer skipping. A controller must estimate difficulty early enough for savings to matter. Its false-easy errors harm quality; false-hard errors lose savings. Evaluate expected compute and the worst cohorts, because average savings can conceal systematic undercomputation.

<a id="t-77-06"></a>
## Conditional layer execution

A skip controller can bypass a transformer block or reuse a previous state. Skipping preserves tensor shape but changes the state distribution expected by later layers. Static layer pruning chooses one smaller architecture for all requests; dynamic skipping chooses per request or token and adds branching, batching fragmentation, and compilation challenges. Grouping requests by execution path can recover throughput while increasing queue delay.

<a id="t-77-07"></a>
## Adaptive computation

Adaptive Computation Time introduced learned halting for recurrent networks; transformer variants use exit heads or confidence criteria. Confidence is not automatically calibrated, and early logits can be confidently wrong. Train or calibrate the halting policy under an explicit compute penalty, then plot quality versus actual FLOPs, bytes, and wall time. Compare with a uniformly smaller model, quantization, distillation, and fixed layer pruning.

## Worked budget

Assume a 32-layer model with eight KV heads, $d_h=128$, BF16, batch one, and 32,768 cached tokens. The basic cache is $2\cdot32\cdot32768\cdot8\cdot128\cdot2\approx4.29$ GB decimal. Halving context halves it; moving from eight to one KV head divides it by eight; 8-bit storage approximately halves element bytes before metadata. This arithmetic identifies the largest lever before benchmarking implementation details.

## Four perspectives

- **Follow the Token:** each policy decides which past tokens remain addressable and how many future layers process the current token.
- **Follow the Gradient:** learned compressors and routers receive task and compute-cost gradients; heuristic eviction at inference receives none.
- **Follow the Byte:** count payload, metadata, fragmentation, compaction, and encode/decode movement rather than quoting nominal bit width.
- **Follow the Request:** scheduling must handle different cache sizes and execution paths while preserving latency SLOs and isolation.

## Lab and exit check

Implement recent-window and score-based eviction on a small KV-cached decoder, plus a no-eviction baseline. Test perplexity, needle retrieval, latency, and measured cache bytes across context lengths. Separately simulate fixed and dynamic layer skipping and report batching effects. A policy passes only at matched quality on both ordinary and adversarial long-context cases.

Add a position-integrity test: compact the cache without eviction and confirm logits match the uncompacted baseline within the declared numerical tolerance. Only then attribute quality changes to the eviction policy.

## References

- Graves, [Adaptive Computation Time for Recurrent Neural Networks](https://arxiv.org/abs/1603.08983), 2016.
- Xin et al., [DeeBERT](https://aclanthology.org/2020.acl-main.204/), ACL 2020.
- Xiao et al., [Efficient Streaming Language Models with Attention Sinks](https://openreview.net/forum?id=NG7sS51zVF), ICLR 2024.
- Zhang et al., [H2O: Heavy-Hitter Oracle for Efficient Generative Inference](https://proceedings.neurips.cc/paper_files/paper/2023/hash/6ceefa7b15572587b78ecfcebb2827f8-Abstract-Conference.html), NeurIPS 2023.
