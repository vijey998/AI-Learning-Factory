# 21. Residual Streams and Normalization

Status: **Drafted — technical and editorial review pending.**

Part 6: Build a Transformer

## Learning outcome

Implement both normalization placements and inspect residual scales.

## Prerequisites

CH-20.

Let $X\in\mathbb{R}^{B\times T\times D}$ denote the current hidden state. A Transformer block must transform it without erasing the information already present, while keeping numerical scales trainable through many layers. Residual addition preserves a direct path; normalization controls scale. Those two mechanisms are simple enough to fit on one line and consequential enough to decide whether a deep model trains.

<a id="t-21-01"></a>
### Residual connections

Coverage ID: `T-21-01`.

A residual sublayer computes

$$
Y=X+F(X;\theta).
$$

The shapes of $X$ and $F(X)$ must match exactly. For $B=2,T=4,D=8$, both contain 64 elements. The addition has no learned parameters. It lets a sublayer learn a correction rather than reconstruct the entire representation. Using column-vector gradients and $J_F=\partial F/\partial X$, backpropagation gives

$$
\nabla_X L=(I+J_F)^{\top}\nabla_Y L,
$$

so the identity term provides a short gradient path. This does not guarantee healthy gradients—the other branch can still destabilize them—but it makes exact information and gradient preservation possible when $F$ is initially small.

A common bug is adding tensors with accidentally broadcast dimensions. Assert equality rather than accepting broadcasting at residual boundaries.

<a id="t-21-02"></a>
### Residual streams

Coverage ID: `T-21-02`.

The **residual stream** is the $D$-dimensional state carried through the stack. Attention writes a context-dependent update into it; the MLP writes a token-local update. For pre-normalized blocks:

$$
X' = X + \mathrm{Attention}(\mathrm{Norm}(X)),\qquad
X''=X'+\mathrm{MLP}(\mathrm{Norm}(X')).
$$

Calling the stream a shared workspace is useful, provided we do not imply that individual coordinates have stable human meanings. Rotating the basis can preserve the computation while changing every coordinate. The stream is also where later probes and activation interventions operate, which is why scale and normalization placement matter.

<a id="t-21-03"></a>
### LayerNorm

Coverage ID: `T-21-03`.

LayerNorm normalizes each token independently across its $D$ features. For token vector $x\in\mathbb{R}^D$,

$$
\mu=\frac1D\sum_i x_i,\quad
\sigma^2=\frac1D\sum_i(x_i-\mu)^2,
$$
$$
\mathrm{LN}(x)=\gamma\odot\frac{x-\mu}{\sqrt{\sigma^2+\epsilon}}+\beta.
$$

With $x=[1,2,3]$, $\mu=2$, variance $=2/3$, and the unscaled output is approximately $[-1.225,0,1.225]$. $\gamma,\beta\in\mathbb{R}^D$ contribute $2D$ parameters. Normalizing across batch or time is a different operation and leaks dependence between examples or positions.

Compute mean and variance in adequate precision. A small `epsilon` prevents division by zero; changing it can affect low-precision behavior.

<a id="t-21-04"></a>
### RMSNorm

Coverage ID: `T-21-04`.

RMSNorm removes mean subtraction:

$$
\mathrm{RMSNorm}(x)=\gamma\odot\frac{x}{\sqrt{D^{-1}\sum_i x_i^2+\epsilon}}.
$$

It usually has $D$ learned scale parameters and no bias. For `[1,2,3]`, RMS is $\sqrt{14/3}\approx2.160$, giving `[0.463,0.926,1.389]` before $\gamma$. RMSNorm fixes root-mean-square scale but does not center the vector. It is therefore not interchangeable with LayerNorm after training.

<a id="t-21-05"></a>
### Pre-norm

Coverage ID: `T-21-05`.

Pre-norm applies normalization before the sublayer: $Y=X+F(N(X))$. The residual path from $Y$ to $X$ is an exact identity, which generally makes deep optimization easier. The stream itself is not normalized after every addition, so its magnitude may grow with depth; a final normalization before the LM head is common.

<a id="t-21-06"></a>
### Post-norm

Coverage ID: `T-21-06`.

Post-norm computes $Y=N(X+F(X))$. Every forward state is normalized immediately, but the direct backward route now passes through the normalization Jacobian. The original Transformer used post-norm; many decoder LLMs use pre-norm or related variants for stable deep training. Loading weights into the wrong layout changes the function even when all tensor shapes match.

## Worked implementation

```python
class PreNormBlock(nn.Module):
    def forward(self, x):
        x = x + self.attn(self.norm1(x))
        x = x + self.mlp(self.norm2(x))
        return x

class PostNormBlock(nn.Module):
    def forward(self, x):
        x = self.norm1(x + self.attn(x))
        x = self.norm2(x + self.mlp(x))
        return x
```

Log the RMS of the stream and both updates per layer. A useful diagnostic is `update_rms / stream_rms`; abrupt spikes often precede divergence.

## Four recurring perspectives

- **Follow the Token:** one token remains a $D$-vector while attention and the MLP add different updates.
- **Follow the Gradient:** residual identities shorten the backward route; norm placement changes its Jacobian.
- **Follow the Byte:** normalization reads and writes $BTD$ elements and reduction statistics; unfused kernels add memory traffic.
- **Follow the Request:** inference applies the same block layout encoded by the checkpoint; a layout mismatch corrupts every generated token.

## Lab and exit check

Implement both variants with identical sublayers. Track stream RMS, update RMS, and gradient norm for 24 layers on the same batch. Explain why identical weights do not make the two layouts equivalent. Verify that each normalization treats batch and time positions independently.

## Exercises

1. Compute LayerNorm and RMSNorm for $x=[-1,1]$ with unit scale, zero bias, and $\epsilon=0$. **Check:** both return $[-1,1]$. Then repeat for $x=[1,3]$ and explain why only LayerNorm is invariant to adding the same constant to every coordinate.
2. Let $F(x)=Ax$ for a two-dimensional vector. Derive the residual Jacobian and identify a matrix $A$ for which the residual path still has a zero singular value. **Check:** the Jacobian is $I+A$; $A=-I$ is the simplest counterexample to the claim that residual connections guarantee nonvanishing gradients.

## References

- He et al., [Deep Residual Learning for Image Recognition](https://arxiv.org/abs/1512.03385), 2015.
- Ba, Kiros, and Hinton, [Layer Normalization](https://arxiv.org/abs/1607.06450), 2016.
- Zhang and Sennrich, [Root Mean Square Layer Normalization](https://arxiv.org/abs/1910.07467), 2019.
- Vaswani et al., [Attention Is All You Need](https://arxiv.org/abs/1706.03762), 2017.
