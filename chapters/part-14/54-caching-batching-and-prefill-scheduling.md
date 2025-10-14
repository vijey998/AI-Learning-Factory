# 54. Caching, Batching and Prefill Scheduling

Status: **Drafted**

## The scheduler is part of model performance

Requests arrive at different times with different prompt and output lengths. Static batching waits for a cohort and wastes slots when shorter members finish. Modern serving continuously changes the active batch while protecting memory and latency targets.

<a id="t-54-01"></a>
## Prefix caching

Many requests share exact token prefixes: a system prompt, tool schema, or document. Prefix caching retains the corresponding per-layer KV blocks, so a later request begins after the cached prefix. The key must cover everything that affects K/V: model and adapter revision, exact token IDs, position treatment, relevant attention configuration, KV dtype, and often multimodal inputs or prompt metadata.

<a id="t-54-02"></a>
## Prefix reuse

Reuse can be full or block-aligned partial matching. Radix trees or hashes locate the longest reusable prefix; reference counts protect shared blocks. Savings scale with reused prefill work, but lookup, hashing, metadata, and cache residency cost resources. Private prompt content creates isolation and eviction requirements. Text equality is insufficient if tokenization or model state differs.

<a id="t-54-03"></a>
## Continuous batching

At each scheduling iteration, finished sequences leave and waiting sequences enter. Active decode rows execute together, raising weight reuse and throughput. The scheduler tracks per-request state, stop conditions, KV blocks, and fairness. Large batches improve throughput until memory, queue delay, or kernel scaling becomes limiting. Throughput-optimal scheduling can violate an interactive latency SLO.

Consider A and B starting together, with A finishing after two tokens and B after eight. Static batching leaves A's row idle for six steps. Continuous batching admits C into available capacity. The exact implementation may rebuild metadata rather than literally reuse a row, but the utilization effect is the same.

<a id="t-54-04"></a>
## Chunked prefill

A long prompt can monopolize the device and delay decode tokens. Chunked prefill divides its tokens across iterations, interleaving chunks with latency-sensitive decode. It also caps temporary activation size. Smaller chunks improve fairness but can reduce prefill efficiency and add scheduling overhead. Chunk size should be chosen from measured TTFT, TPOT, throughput, and memory, not folklore.

A token-budget scheduler might allow 2,048 scheduled tokens per iteration: 32 active decode sequences consume one token each, leaving at most 2,016 prefill tokens. If two prompts each request a 1,024-token chunk, the second must be shortened to 992 tokens or deferred. Admission must ensure KV capacity for all scheduled tokens and a policy for predicted output growth; a token budget is not itself a memory budget.

<a id="t-54-05"></a>
## Cache correctness

Cache hits are correctness claims. Validate by comparing logits with and without reuse on exact token sequences. Include model/adapter changes, differing positions, block-boundary prefixes, cancellation, eviction, concurrent references, and hash collision handling. Hashes locate candidates; exact identity or collision-safe verification establishes equality.

Eviction policies can use recency, frequency, size, recomputation cost, tenant quota, or combinations. Evict only unreferenced blocks. A high hit rate can still lose if it retains cheap short prefixes while evicting costly long ones; saved prefill tokens or time is a better value measure.

## Simulation and four perspectives

Simulate arrivals with timestamp, prompt length, target output, shared-prefix ID, and cancellation. Compare static and continuous batching with and without chunked prefill under the identical arrival trace. Report p50/p95 TTFT and TPOT, completion latency, output tokens/s, queue depth, cache hit value in saved prefill tokens, and peak physical blocks. Include one overload interval so fairness and admission behavior are observable.

- **Follow the Token:** a prompt token is computed, reused, or scheduled in a chunk.
- **Follow the Gradient:** serving caches contain no training graph and must not mutate weights.
- **Follow the Byte:** shared pages save physical KV; active sequences compete for block capacity.
- **Follow the Request:** admission, fairness, and preemption determine user-visible latency.

Failures include tenant data leakage, stale adapter cache, hash-only equality, starvation of long prompts, over-admission, head-of-line blocking, and metrics averaged across unlike requests. Exit when a deterministic simulation explains both a throughput win and a tail-latency regression.

## Primary references

- Yu et al., [Orca: A Distributed Serving System for Transformer-Based Generative Models](https://www.usenix.org/conference/osdi22/presentation/yu), 2022.
- Kwon et al., [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://arxiv.org/abs/2309.06180), 2023.
- Agrawal et al., [Taming Throughput-Latency Tradeoff in LLM Inference with Sarathi-Serve](https://arxiv.org/abs/2403.02310), 2024.
- vLLM, [Automatic Prefix Caching](https://docs.vllm.ai/en/latest/features/automatic_prefix_caching.html), version-sensitive; accessed 2026-09-19. Pin engine commit and configuration, block size, arrival trace, model revision, and SLO.
