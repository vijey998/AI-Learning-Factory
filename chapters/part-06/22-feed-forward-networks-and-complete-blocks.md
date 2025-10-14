# 22. Feed-Forward Networks and Complete Blocks

Status: **Drafted — technical and editorial review pending.**

Part 6: Build a Transformer

## Learning outcome

Build a block with explicit shapes and a parameter-count breakdown.

## Prerequisites

CH-21.

Attention moves information between positions. The feed-forward sublayer transforms each position independently. This division—communication, then computation—is the repeating structure of a decoder Transformer.

<a id="t-22-01"></a>
### Feed-forward networks

Coverage ID: `T-22-01`.

For $X\in\mathbb{R}^{B\times T\times D}$, a conventional position-wise FFN is

$$
\mathrm{FFN}(X)=\phi(XW_1+b_1)W_2+b_2,
$$

where $W_1\in\mathbb{R}^{D\times M}$, $W_2\in\mathbb{R}^{M\times D}$, and $M$ is the intermediate width. The same weights are applied to all $BT$ token vectors. With $D=512,M=2048$, weights contribute $2DM=2{,}097{,}152$ parameters; biases add 2,560. The two matrix multiplies cost roughly $4BTDM$ FLOPs if one multiply-add counts as two FLOPs.

Calling the FFN “position-wise” does not mean it ignores context: its input already contains context mixed by attention. It simply performs no new cross-position communication.

<a id="t-22-02"></a>
### GELU vs SwiGLU

Coverage ID: `T-22-02`.

GELU smoothly gates by input magnitude:

$$
\mathrm{GELU}(z)=z\Phi(z),
$$

usually approximated in code. A gated unit uses two input projections. SwiGLU is commonly written

$$
\mathrm{SwiGLU}(X)=\left(\mathrm{SiLU}(XW_g)\odot XW_u\right)W_d,
\qquad \mathrm{SiLU}(z)=z\sigma(z).
$$

The gate projection $W_g$ decides how much of the “up” projection $W_u$ passes elementwise. Shapes are $W_g,W_u\in\mathbb{R}^{D\times M}$ and $W_d\in\mathbb{R}^{M\times D}$. A common implementation error is swapping conventions from a checkpoint; multiplication is commutative, but applying SiLU to the wrong branch is not.

<a id="t-22-03"></a>
### MLP expansion

Coverage ID: `T-22-03`.

The intermediate width creates a larger feature workspace. A GELU FFN near $M=4D$ has about $8D^2$ weights. A SwiGLU FFN has $3DM$, so choosing $M\approx(8/3)D$ approximately matches that parameter count. Hardware-friendly widths are often rounded to a multiple such as 256.

For $D=4096$: a $4D$ GELU FFN has $2\cdot4096\cdot16384\approx134.2$ million weights. A SwiGLU with $M=11008$ has $3\cdot4096\cdot11008\approx135.3$ million. “Smaller expansion” therefore does not imply fewer parameters once the third matrix is included.

<a id="t-22-04"></a>
### Complete Transformer block

Coverage ID: `T-22-04`.

A pre-norm decoder block is:

$$
A=X+\mathrm{MHA}(N_1(X);\text{causal mask}),
$$
$$
Y=A+\mathrm{MLP}(N_2(A)).
$$

Every boundary has shape $[B,T,D]$. For standard MHA, four $D\times D$ projections contribute about $4D^2$ weights. Add a SwiGLU MLP with $3DM$, plus small normalization vectors. At $D=768,M=2048$, the block has roughly $4(768)^2+3(768)(2048)=7.08$ million main weights.

```python
class Block(nn.Module):
    def forward(self, x):
        assert x.ndim == 3 and x.shape[-1] == self.width
        x = x + self.attn(self.norm1(x), causal=True)
        x = x + self.mlp(self.norm2(x))
        return x
```

Dropout, biases, positional method, norm type, and attention variant belong in the configuration because they change behavior or checkpoint compatibility.

## Failure cases

Wrong causal masks leak labels. A missing output projection prevents heads from being recombined. Applying a single normalization to both residual branches changes the architecture. Materializing unnecessary intermediate tensors can dominate runtime even though the formula is correct.

## Four recurring perspectives

- **Follow the Token:** attention gathers context; the MLP transforms the resulting token vector independently.
- **Follow the Gradient:** each residual branch receives gradients through both its update and identity paths.
- **Follow the Byte:** MLP weights often exceed attention weights; decode repeatedly streams them from accelerator memory.
- **Follow the Request:** each generated token traverses every block, making block-level inefficiency multiply by depth and output length.

## Lab and exit check

Implement one block, print every parameter shape, and reconcile the framework total with a hand calculation. For (B=2,T=16,D=128,H=4,M=352), assert every residual boundary remains `[2,16,128]`. Explain why SwiGLU needs three matrices and why its expansion ratio differs from a two-matrix GELU FFN.

## Exercises

1. For a bias-free block with $D=128$, $M=352$, standard MHA, and SwiGLU, calculate the main weight count. **Check:** $4D^2+3DM=200{,}704$.
2. Give a concrete input shape that a tensor library could broadcast against `[2,16,128]` but that must be rejected at a residual boundary. Explain why successful broadcasting is not evidence of architectural correctness.

## References

- Vaswani et al., [Attention Is All You Need](https://arxiv.org/abs/1706.03762), 2017.
- Hendrycks and Gimpel, [Gaussian Error Linear Units](https://arxiv.org/abs/1606.08415), 2016.
- Shazeer, [GLU Variants Improve Transformer](https://arxiv.org/abs/2002.05202), 2020.
