# 30. Modern Positions, Heads and MLPs

Status: **Drafted — technical and editorial review pending.**

Part 8: Modern LLM Architecture

## Learning outcome

Derive KV dimensions and parameter counts for three head-sharing configurations.

## Prerequisites

CH-16, CH-19, CH-29.

Modern decoder models often keep the overall block while changing how position enters attention, how K/V are shared, and how the MLP gates features. These changes target quality, training behavior, and especially decode memory traffic.

<a id="t-30-01"></a>
### RoPE deep dive

Coverage ID: `T-30-01`.

Rotary position embeddings rotate pairs of Q and K coordinates by a position-dependent angle. For one pair and position (p),

\[
R(p\theta)\begin{bmatrix}x_0\\x_1\end{bmatrix}=
\begin{bmatrix}\cos p\theta&-\sin p\theta\\\sin p\theta&\cos p\theta\end{bmatrix}
\begin{bmatrix}x_0\\x_1\end{bmatrix}.
\]

Because $R(p\theta)^{\top}R(q\theta)=R((q-p)\theta)$, the dot product between rotated Q at $p$ and K at $q$ depends on relative displacement. Values are not normally rotated. Frequencies span coordinate pairs; model-specific base, scaling, and partial rotary dimensions are checkpoint contracts. Extending context by changing them is an intervention requiring evaluation, not a free extrapolation.

<a id="t-30-02"></a>
### MHA

Coverage ID: `T-30-02`.

With $H$ query heads and $d_h=D/H$, multi-head attention produces Q, K, and V each with $H$ heads. Per cached token per layer, K and V store $2Hd_h=2D$ elements. Projection weights for Q/K/V total $3D^2$ when all project from $D$ to $D$.

<a id="t-30-03"></a>
### MQA

Coverage ID: `T-30-03`.

Multi-query attention retains $H$ query heads but uses one shared K head and one shared V head. Q has shape `[B,H,T,d_h]`; K/V have `[B,1,T,d_h]` and broadcast logically across query heads. Cache per token per layer falls to $2d_h$ elements, a factor $H$ below MHA. Sharing can affect quality or capacity; it is not simply lossless compression.

<a id="t-30-04"></a>
### GQA

Coverage ID: `T-30-04`.

Grouped-query attention uses $H_{kv}$ K/V heads, where $1<H_{kv}<H$ and normally $H\bmod H_{kv}=0$. Each K/V group serves $H/H_{kv}$ query heads. Cache storage is $2H_{kv}d_h$ elements per token per layer. MHA is the special case $H_{kv}=H$; MQA is $H_{kv}=1$.

Example: $D=4096,H=32,d_h=128$. MHA caches 8,192 K/V elements per token-layer; GQA with $H_{kv}=8$ caches 2,048; MQA caches 256. At BF16 those are 16,384, 4,096, and 512 bytes respectively.

Projection parameters also change: Q remains $D\times D$, while K and V each become $D\times(H_{kv}d_h)$. The output projection remains $D\times D$.

<a id="t-30-05"></a>
### Modern MLPs

Coverage ID: `T-30-05`.

Many current decoders use bias-free SwiGLU-like MLPs with an “up,” “gate,” and “down” projection. RMSNorm and pre-norm frequently accompany them, but these choices are independent. Fused kernels may compute two input projections together; the mathematical parameter count remains three matrices.

<a id="t-30-06"></a>
### SwiGLU parameter accounting

Coverage ID: `T-30-06`.

For width $D$ and intermediate $M$, SwiGLU weights total $3DM$. Compare a two-matrix GELU FFN at $M_g=4D$: $2D(4D)=8D^2$. Equal parameter count gives $3DM_s\approx8D^2$, so $M_s\approx(8/3)D$, before rounding and biases. At $D=4096,M_s=11008$, the total is 135,266,304 weights.

## Four recurring perspectives

- **Follow the Token:** RoPE changes Q/K phase; GQA changes which K/V representation each query head reads.
- **Follow the Gradient:** shared K/V heads aggregate learning signals from multiple query heads.
- **Follow the Byte:** GQA/MQA chiefly shrink persistent KV cache and K/V projection sizes; decode benefits strongly.
- **Follow the Request:** long-context, high-concurrency serving amplifies KV savings, while prefill still performs substantial attention compute.

## Lab and exit check

For (D=2048,H=16), calculate projection parameters and BF16 KV bytes per token-layer for (H_{kv}=16,4,1). Verify that (D/H) is integral and each query head maps to exactly one K/V group. Implement a two-dimensional RoPE rotation and numerically show its dot product depends on position difference.

## Exercises

1. For $D=2048,H=16,d_h=128$, compute Q/K/V projection weights for $H_{kv}=4$. **Check:** Q has 4,194,304 weights; K and V each have 1,048,576.
2. Compute BF16 KV bytes per token-layer for $H_{kv}=16,4,1$. **Check:** 8192, 2048, and 512 bytes.

## References

- Su et al., [RoFormer: Enhanced Transformer with Rotary Position Embedding](https://arxiv.org/abs/2104.09864), 2021.
- Shazeer, [Fast Transformer Decoding: One Write-Head is All You Need](https://arxiv.org/abs/1911.02150), 2019.
- Ainslie et al., [GQA: Training Generalized Multi-Query Transformer Models](https://arxiv.org/abs/2305.13245), 2023.
