# 20. Attention Shapes and Compute Cost

Status: **Draft — not yet independently reviewed.**

The formula for attention is short; its tensors can be enormous. Shape and resource accounting turn “quadratic” from a slogan into an engineering estimate.

<a id="t-20-01"></a>
## Attention tensor shapes

Define batch $B$, sequence length $T$, model width $D$, heads $H$, and head width $d_h=D/H$. Standard multi-head Q, K, V have shape $[B,H,T,d_h]$. Scores and probabilities have shape $[B,H,T,T]$. Multiplying probabilities by V returns $[B,H,T,d_h]$, then concatenation returns $[B,T,D]$.

Write these shapes beside code. Most attention bugs are axis, mask-broadcast, or reshape errors that may preserve the total element count and avoid a runtime exception.

<a id="t-20-02"></a>
## Attention compute cost

QKV projections cost roughly $6BTD^2$ FLOPs and output projection about $2BTD^2$, using two FLOPs per multiply-add. Score formation $QK^T$ costs about $2BHT^2d_h=2BT^2D$; multiplying weights by V costs another $2BT^2D$. Thus the main dense-attention matrix products cost about $4BT^2D$, excluding softmax and masking.

For $B=1,T=2048,D=4096$, the two attention matrix multiplications require roughly $4(2048^2)(4096)=68.7$ billion FLOPs per layer. The four projections require about $8(2048)(4096^2)=274.9$ billion FLOPs. Under these assumptions the two terms are equal when $T=2D$; at this context and width, projections still exceed attention matmuls. This comparison omits biases, softmax, normalization, and feed-forward work.

<a id="t-20-03"></a>
## Quadratic sequence cost

Doubling $T$ doubles projection work but quadruples pairwise attention work. Dense attention creates $T^2$ query-key relations per head. “Attention is $O(T^2D)$” omits constants, projections, batch, heads, and the distinction between training/prefill and single-token decode, so use it as scaling guidance rather than a complete performance model.

During cached decode for one new token, the query compares with $T$ cached keys, so per-step attention is linear in current context. Generating many tokens still repeats that growing linear work. Hardware utilization, memory traffic, and kernel launch overhead determine elapsed time; FLOPs alone do not.

<a id="t-20-04"></a>
## Attention memory accounting

A materialized score tensor uses $BH T^2$ elements. With $B=2,H=32,T=4096$, that is 1,073,741,824 elements: about 2.15 GB decimal in BF16 for one tensor. Probabilities, dropout masks, saved activations, and gradients can multiply this during training. Q, K, and V together use $3BTD$ elements, linear in $T$.

FlashAttention changes the IO schedule and avoids writing the full score/probability matrix to HBM, while computing exact attention up to normal floating-point differences. It does not change the dense pairwise arithmetic's asymptotic $T^2$ nature. This distinction—stored intermediates versus operations—is crucial.

## Four perspectives

**Follow the Token:** every destination relates to every allowed source. **Follow the Gradient:** training may need Q, K, V and normalization statistics or recomputation for backward. **Follow the Byte:** materialized scores can dominate activation memory, and memory-efficient kernels tile them on-chip. **Follow the Request:** prefill exposes a $T\times T$ workload, while one decode step exposes $1\times T$ attention plus weight reads and KV-cache traffic.

## Exit check

For $B=4,T=1024,D=2048,H=16$, derive every tensor shape, BF16 QKV bytes, score bytes, projection FLOPs, and attention-matmul FLOPs. Repeat after doubling $T$. State whether each quantity doubles or quadruples, and state what your calculation omits.

## References

- Vaswani et al., [Attention Is All You Need](https://arxiv.org/abs/1706.03762), 2017.
- Dao et al., [FlashAttention](https://arxiv.org/abs/2205.14135), 2022.
