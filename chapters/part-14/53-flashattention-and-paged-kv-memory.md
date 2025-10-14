# 53. FlashAttention and Paged KV Memory

Status: **Drafted**

## Two different memory problems

FlashAttention changes how attention arithmetic moves data. PagedAttention changes how a serving system allocates persistent KV state. They solve different problems and can coexist.

<a id="t-53-01"></a>
## Why naive inference is slow

Naive attention may materialize the score matrix S=QK^T and probability matrix P=softmax(S), each [B,H,T,T] during full attention. At B=1,H=32,T=8192 in BF16, one such matrix is 4 GiB. Even when enough memory exists, writing and rereading these intermediates through HBM is expensive. During decode, the matrix is only [B,H,1,S], but every step rereads a growing cache; small GEMMs also use compute units poorly.

<a id="t-53-02"></a>
## FlashAttention

FlashAttention is an **exact, IO-aware** attention algorithm up to normal floating-point rounding. It tiles Q, K, and V so score blocks are produced on chip, incorporated into a running softmax and output, and discarded rather than stored in HBM. It changes the schedule, not the attention definition.

<a id="t-53-03"></a>
## Online softmax and IO scheduling

Softmax appears to require all scores because its denominator spans a row. Online softmax makes blocks composable. For a processed prefix, keep running maximum m, normalizer l, and weighted output accumulator o. For a new block with maximum m_b and exponent sum l_b, set m_new=max(m,m_b), rescale old and new contributions by exp(m-m_new) and exp(m_b-m_new), then combine. The final o/l equals full softmax attention.

Tiling reduces HBM traffic but introduces constraints from head width, masks, dropout, causal structure, and hardware. It does not make the quadratic arithmetic of full prefill disappear. A fallback kernel can beat it on small or unusual shapes.

<a id="t-53-04"></a>
## KV cache layout

Decode needs efficient append of one K/V row and efficient reads across all prior positions. Layout choices order layer, block, token, KV head, and head dimension differently. A contiguous per-request allocation makes reads simple but requires predicting maximum length or reallocating/copying. Variable completion lengths create internal waste and fragmented free regions.

<a id="t-53-05"></a>
## Paged KV memory

Paged allocation divides KV into fixed-size token blocks. Each sequence owns a logical list of blocks mapped to noncontiguous physical blocks. Growth allocates another free block; completion returns blocks; shared prefixes can reference the same physical blocks with copy-on-write semantics. Waste is bounded mostly by the final partially filled block rather than reserved maximum context.

If each block holds 16 tokens and a sequence has 129 tokens, it needs nine blocks: capacity 144, internal waste 15 tokens. Metadata and indirect addressing are the price.

That final-block waste is 15/144 = 10.4% of allocated token slots for this sequence. At exactly 128 tokens it is zero; at 129 it jumps to the maximum of 15 slots for a 16-token block. Report physical blocks and logical tokens rather than an average “bytes per token” that hides this boundary effect.

<a id="t-53-06"></a>
## PagedAttention

PagedAttention kernels follow block tables while computing attention, much as virtual memory translates logical pages. They must preserve causal order despite noncontiguous physical storage and support different sequence lengths in one batch. The original vLLM work connected this mechanism to higher serving utilization by reducing KV fragmentation and enabling sharing, but performance depends on workload and implementation.

## Four perspectives and exit check

- **Follow the Token:** FlashAttention computes its exact weighted value blockwise; paging maps its historical K/V to physical blocks.
- **Follow the Gradient:** FlashAttention training uses backward kernels/recomputation; serving pages are inference state.
- **Follow the Byte:** one optimization removes T-by-T intermediates; the other reduces reserved and fragmented KV.
- **Follow the Request:** block tables grow, share, and free as requests arrive and finish.

Failures include treating FlashAttention as approximate, claiming it removes quadratic compute, confusing paging with OS swapping, stale block-table entries, reference-count bugs, and comparing unmatched attention features. Derive the 4 GiB score example, perform an online-softmax merge for two blocks and compare it numerically with a full softmax, then calculate page waste for lengths 128, 129, and 143.

## Primary references

- Dao et al., [FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness](https://arxiv.org/abs/2205.14135), 2022.
- Dao, [FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning](https://arxiv.org/abs/2307.08691), 2023.
- Kwon et al., [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://arxiv.org/abs/2309.06180), 2023.
- vLLM, [official documentation](https://docs.vllm.ai/), version-sensitive; accessed 2026-09-19. Pin kernel version, attention backend, dtype, mask, model, block size, GPU, and workload.
