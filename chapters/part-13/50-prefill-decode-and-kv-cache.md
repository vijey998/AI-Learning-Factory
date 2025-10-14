# 50. Prefill, Decode and KV Cache

Status: **Drafted**

## Two phases of one computation

A causal model repeatedly predicts one next token, but serving divides work into a parallel prompt phase and a serial generation phase.

<a id="t-50-01"></a>
## Prefill

Prefill processes all T prompt tokens together. It computes Q, K, and V for each layer, performs causal attention over the prompt, and stores K/V for later. Large GEMMs across T rows often have enough arithmetic intensity to use the GPU well. Time to first token includes queueing, tokenization/transfer, prefill, final sampling, and streaming overhead—not merely a forward pass.

<a id="t-50-02"></a>
## Autoregressive decode

After sampling token T+1, decode feeds that one ID back. Each layer forms one new query, key, and value. The query attends to all cached keys and combines cached values. One token is emitted, then the process repeats until a stop condition. Decode has a sequential dependency across tokens; batching many requests is the primary way to expose parallel work.

<a id="t-50-03"></a>
## KV cache

For each layer, store K and V with conceptual shape [B,Hkv,S,Dh], where S grows with sequence length. Ignoring padding and metadata, bytes are

\[
2L B H_{kv} S D_h b,
\]

where the leading 2 is K plus V and b is bytes per element. For L=32, Hkv=8, Dh=128, BF16, one token per sequence consumes 128 KiB. At 8,192 tokens that is 1 GiB per sequence. MHA with Hkv=32 would require four times as much.

The arithmetic is $2\times32\times8\times128\times2=131{,}072$ bytes per token. Multiplying by 8,192 gives 1,073,741,824 bytes exactly. This is logical payload only: paged allocators round to blocks and add tables, alignment, and partially filled-block waste.

Cache layout matters: layer-first, token blocks, head grouping, alignment, and page tables influence coalescing and fragmentation. Store post-position-encoding keys when the architecture requires it, and ensure cache positions match position IDs.

<a id="t-50-04"></a>
## Why K and V, but not historical Q?

At a new step, only the **new query** asks what prior information matters. Historical queries were used to compute historical outputs, which do not change in a causal model. Historical keys must remain because the new query scores against them; historical values must remain because those scores form a weighted sum. Caching old queries provides no input to the next attention result.

Without a cache, recomputing the length-S prefix each step repeats projections and attention for unchanged tokens. With a cache, projections run only for the new token, although attention still reads K/V across S. That is why long-context decode becomes memory-intensive.

<a id="t-50-05"></a>
## Context length

The maximum context includes prompt plus generated tokens unless the runtime supports an explicit sliding window or eviction policy. Longer S grows cache linearly and per-token attention work roughly linearly. RoPE scaling or a config advertising a longer window does not guarantee preserved model quality. Capacity, supported positions, and evaluated quality are different claims.

## Correctness lab

Implement two paths on a tiny deterministic model: (1) recompute the full prefix after every sampled token; (2) prefill once and append K/V. At each step compare logits before sampling with strict FP32 tolerance or a justified reduced-precision tolerance. Use greedy decoding so randomness cannot hide a mismatch. Test T=1, multiple batches, grouped-query attention, a left-padded batch, and an irregular stop length. Assert that cache length advances by exactly one for each live sequence and does not advance for a finished row.

## Four perspectives and failures

- **Follow the Token:** prompt tokens enter together; generated tokens enter one at a time.
- **Follow the Gradient:** inference caches are detached state, not training activations.
- **Follow the Byte:** each new token appends 2*L*Hkv*Dh elements and rereads historical state.
- **Follow the Request:** the scheduler alternates prefill work and decode iterations for active sequences.

Typical defects are off-by-one masks, wrong cache position, RoPE applied twice, cache aliasing across requests, padding contamination, and logits compared after sampling. The exit check is equality of cached and uncached logits plus a derived bytes-per-token budget.

## Primary references

- Vaswani et al., [Attention Is All You Need](https://arxiv.org/abs/1706.03762), 2017.
- Ainslie et al., [GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints](https://arxiv.org/abs/2305.13245), 2023.
- Hugging Face, [Caching](https://huggingface.co/docs/transformers/main/en/cache_explanation), version-sensitive; accessed 2026-09-19. Pin model code and revision because cache structure and position handling are architecture-specific.
