# 19. Causal and Multi-Head Attention

Status: **Draft — not yet independently reviewed.**

Language-model training exposes an entire sequence for efficiency while enforcing the information boundary of left-to-right generation. Causal masks provide that boundary; multiple heads provide several learned routing spaces in parallel.

<a id="t-19-01"></a>
## Causal attention

At position $i$, a decoder-only language model may attend only to positions $j\le i$. Thus the representation used to predict token $i+1$ cannot inspect that target or later tokens. Training can still compute every position simultaneously because the mask constrains information flow within the matrix operation.

<a id="t-19-02"></a>
## Causal masks

The additive mask has $M_{ij}=0$ when $j\le i$ and $-\infty$ otherwise. It is added before softmax, making forbidden probabilities zero. For $T=3$, allowed rows are `[1,0,0]`, `[1,1,0]`, and `[1,1,1]` conceptually. A mask with the wrong diagonal can prevent self-attention; a transposed inequality can expose the future.

A decisive test changes future token embeddings while holding the prefix fixed. Outputs at earlier positions must remain unchanged within numerical tolerance. Merely inspecting a triangular matrix is weaker because broadcasting and axis mistakes can apply it incorrectly.

<a id="t-19-03"></a>
## Multi-head attention

With $H$ heads and head width $d_h$, projections reshape $Q,K,V$ from $[B,T,Hd_h]$ to $[B,H,T,d_h]$. Each head computes its own $[T,T]$ routing matrix. Heads can specialize in different patterns, though specialization should be measured rather than assumed and individual heads can be redundant.

When $D=Hd_h$, the combined projection width matches the residual width. Grouped-query and multi-query variants later change the number of KV heads, but ordinary multi-head attention uses the same head count for Q, K, and V.

<a id="t-19-04"></a>
## Head concatenation

Per-head outputs $O_h[B,T,d_h]$ are concatenated along the feature axis to $O_{cat}[B,T,Hd_h]$. Concatenation preserves every coordinate; it does not average heads. A reshape must transpose axes correctly—reinterpreting `[B,H,T,d_h]` directly as `[B,T,Hd_h]` can interleave positions and heads.

<a id="t-19-05"></a>
## Output projection

The matrix $W_O[Hd_h,D]$ mixes concatenated head features back into the residual width. Without it, heads occupy fixed disjoint coordinate blocks. The projection lets downstream computation combine their contributions and is part of attention's parameter and FLOP cost.

## Worked shape trace

For $B=2,T=5,D=8,H=2,d_h=4$: projected Q, K, V each reshape to `[2,2,5,4]`; scores and weights are `[2,2,5,5]`; head outputs are `[2,2,5,4]`; transpose and concatenate to `[2,5,8]`; output projection preserves `[2,5,8]`.

## Four perspectives

**Follow the Token:** each token retrieves several mixtures, one per head. **Follow the Gradient:** the causal mask blocks computational paths from future tokens, so their gradients cannot influence earlier states through attention. **Follow the Byte:** every head contributes a score matrix; fused kernels may avoid storing it in full. **Follow the Request:** during decode, a single new query attends to cached prefix keys and values and needs no future mask entries.

## Exit check

Write the $4\times4$ causal mask. Design the future-token mutation test. Trace shapes for $B=3,T=7,D=12,H=3$. Explain why attention visualizations alone cannot establish what each head causally contributes.

## References

- Vaswani et al., [Attention Is All You Need](https://arxiv.org/abs/1706.03762), 2017.
- [PyTorch scaled dot-product attention](https://docs.pytorch.org/docs/stable/generated/torch.nn.functional.scaled_dot_product_attention.html). Accessed 2026-09-19.
