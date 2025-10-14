# 18. Queries, Keys, Values and Scaling

Status: **Draft — not yet independently reviewed.**

Attention separates *what a position seeks*, *what each source advertises*, and *what each source contributes*. Those roles are queries, keys, and values.

<a id="t-18-01"></a>
## Query

A query is the destination position's search representation. It is not an English question; it is a learned vector whose dot products with keys drive routing. Different layers can learn different matching rules.

<a id="t-18-02"></a>
## Key

A key is a source position's address-like representation. A large query-key dot product indicates compatibility under the learned projections. Similar content vectors can have dissimilar keys if the layer learns to route them differently.

<a id="t-18-03"></a>
## Value

A value is the information mixed when its key is selected. Keys decide *where* to read; values decide *what* is returned. Keeping them separate lets a source advertise one property while contributing another representation.

<a id="t-18-04"></a>
## QKV projections

Given hidden states $X[B,T,D]$, learned matrices produce $Q=XW_Q$, $K=XW_K$, and $V=XW_V$. In one head, $W_Q,W_K\in\mathbb{R}^{D\times d_k}$ and $W_V\in\mathbb{R}^{D\times d_v}$. Implementations often fuse the three matrix multiplications into one projection and split the result; the mathematical roles remain distinct.

<a id="t-18-05"></a>
## Scaled dot-product attention

For one sequence and head,

$$A=\operatorname{softmax}\left(\frac{QK^T}{\sqrt{d_k}}+M\right),\qquad O=AV,$$

where softmax acts across source positions and $M$ is an optional mask or bias. Let $q=[1,0]$, keys $k_1=[1,0],k_2=[0,1]$, and values $v_1=[2,0],v_2=[0,4]$. Unscaled scores are `[1,0]`; after division by $\sqrt2$, softmax is approximately `[0.670,0.330]`, giving output `[1.340,1.320]`.

<a id="t-18-06"></a>
## Square-root scaling

If query and key coordinates are independent with mean zero and variance one, their dot product has variance approximately $d_k$. Dividing by $\sqrt{d_k}$ keeps score variance near one. Without scaling, large dimensions push softmax toward saturation, producing tiny derivatives for most entries. Learned distributions violate the simple assumptions, but the variance argument explains the design.

<a id="t-18-07"></a>
## Attention weights

Each row of $A$ is nonnegative and sums to one over allowed sources. The output is therefore a convex combination of value rows for that head. Masked entries should receive zero probability. Numerically stable softmax subtracts the row maximum before exponentiating; using a finite mask value that is insufficiently negative in a low-precision dtype can leak probability. A row in which every source is masked has no valid normalized attention distribution and must be handled explicitly; naively applying softmax to all $-\infty$ inputs produces an undefined $0/0$ normalization and typically NaNs.

Weights depend on both query and keys. Changing the value vectors leaves weights unchanged but changes the output; changing a key can reroute every query that compares with it. Gradients flow through both routing and content paths.

## Four perspectives

**Follow the Token:** each destination constructs a query, compares with source keys, then mixes values. **Follow the Gradient:** loss changes query/key projections through weights and value projections through the mixture. **Follow the Byte:** $Q,K,V$ are linear in $T$, while the dense score matrix is quadratic. **Follow the Request:** prefill builds all positions together; decode creates one new query and compares it with cached keys.

## Exit check

Recompute the worked example with values swapped, then with keys swapped. Which changes routing and which changes only retrieved content? Derive the score variance under independent unit-variance coordinates. Verify every tensor shape for $T=4,d_k=2,d_v=3$.

## References

- Vaswani et al., [Attention Is All You Need](https://arxiv.org/abs/1706.03762), 2017.
