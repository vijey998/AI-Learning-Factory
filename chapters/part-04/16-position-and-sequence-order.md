# 16. Position and Sequence Order

Status: **Draft — not yet independently reviewed.**

Self-attention based only on token content is permutation equivariant: rearranging input rows rearranges outputs in the same way. Language needs order, so the model must receive positional information.

<a id="t-16-01"></a>
## Position and sequence order

“Dog bites person” and “person bites dog” contain the same token multiset but express different relationships. If input states are only token embeddings and attention has no positional signal, the mechanism cannot distinguish the permutations beyond corresponding row order. Position can enter by addition, attention-score bias, or transformations of queries and keys.

<a id="t-16-02"></a>
## Sinusoidal positions

The original Transformer adds fixed sinusoids: $PE(pos,2i)=\sin(pos/10000^{2i/D})$ and $PE(pos,2i+1)=\cos(pos/10000^{2i/D})$. Different frequencies provide a structured code for each position. Because phase differences express offsets, relative positions can be derived through linear relationships. No positional parameters are learned, though extrapolation beyond training length is not automatically reliable.

<a id="t-16-03"></a>
## Learned positions

A learned table $P[T_{max},D]$ adds row $P_t$ to the token at position $t$. It is flexible and simple, but adds parameters and has no trained rows beyond $T_{max}$. Extending the table by random initialization does not teach the model to use longer contexts; interpolation and continued training are model changes requiring evaluation.

<a id="t-16-04"></a>
## Relative-position methods

Relative methods modify attention using distance $i-j$ rather than only absolute $i$ and $j$. A learned or fixed bias can favor nearby or direction-specific positions. T5-style relative biases bucket distances so many far offsets share parameters. ALiBi adds head-specific linear penalties based on distance. These schemes change attention scores directly and often avoid a full $T\times D$ position table.

<a id="t-16-05"></a>
## RoPE introduction

Rotary Position Embedding rotates pairs of query and key coordinates by a position-dependent angle. The dot product between a query at $i$ and key at $j$ then depends on their relative phase $i-j$. Values are not rotated in the standard construction. For one 2-D pair, $R(\theta p)[x_1,x_2]^T$ uses the familiar rotation matrix; multiple coordinate pairs use different frequencies.

RoPE consumes little persistent memory, but context extension depends on frequency behavior and training. Scaling recipes modify positions or frequencies and must be validated for quality across both short and long contexts.

## Worked invariance check

Take content vectors $a,b$ and swap their rows. Without positions, their pairwise score matrix swaps rows and columns consistently. Add distinct $P_0,P_1$ before projections and the states are no longer simply the same multiset. This demonstrates the missing information rather than claiming any one positional method is universally best.

## Four perspectives

**Follow the Token:** the same token gets a different state or attention relation at each position. **Follow the Gradient:** learned tables and biases receive gradients; fixed sinusoids and fixed rotations do not. **Follow the Byte:** learned positions store $T_{max}D$ parameters, while score biases may materialize or generate $T^2$ relations. **Follow the Request:** cached decode must assign monotonically correct position indices, including after prefix reuse or batching.

## Exit check

Show why content-only self-attention is permutation equivariant. Calculate one 2-D rotation at positions 1 and 3 and relate its dot product to their offset. List two reasons a model can fail beyond its training context even when its positional formula is defined there.

## References

- Vaswani et al., [Attention Is All You Need](https://arxiv.org/abs/1706.03762), 2017.
- Shaw, Uszkoreit, and Vaswani, [Self-Attention with Relative Position Representations](https://aclanthology.org/N18-2074/), 2018.
- Su et al., [RoFormer](https://arxiv.org/abs/2104.09864), 2021.
