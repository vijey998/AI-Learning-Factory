# 06. Geometry and Number Formats

Status: **Draft — not yet independently reviewed.**

Geometry explains how representations interact. Number formats explain how approximately a machine can store and compute those interactions.

<a id="t-06-01"></a>
## Dot products

For vectors $a,b\in\mathbb{R}^D$, $a\cdot b=\sum_i a_i b_i$. It combines alignment and magnitude. Attention uses dot products between queries and keys; linear layers compute many dot products at once.

<a id="t-06-02"></a>
## Cosine similarity

Cosine similarity divides the dot product by both magnitudes: $\cos(a,b)=a\cdot b/(\|a\|\|b\|)$. It compares direction and is undefined for a zero vector. Normalizing vectors makes cosine equal their dot product.

<a id="t-06-03"></a>
## Magnitude

The Euclidean norm is $\|a\|_2=\sqrt{\sum_i a_i^2}$. If `a=[1,0]`, `b=[10,1]`, and `c=[1,1]`, dot-product ranking may favor `b` because it is large, while cosine asks which direction is closer. Neither metric is universally correct; training and retrieval design decide what magnitude should mean.

<a id="t-06-04"></a>
## Basis

A basis is a set of independent vectors that can express every vector in a space. Coordinates depend on the chosen basis. Rotating a representation and compensating in the next linear map can preserve behavior, which is why reading individual hidden coordinates as fixed concepts is risky.

<a id="t-06-05"></a>
## Subspaces

A subspace is closed under vector addition and scalar multiplication. The columns of a matrix span its column space. A low-rank adapter restricts an update to a lower-dimensional factorization, connecting a practical fine-tuning method to subspace structure.

<a id="t-06-06"></a>
## Orthogonality

Vectors are orthogonal when their dot product is zero. Orthogonality expresses perpendicular directions under the chosen inner product; it does not automatically mean statistical independence or semantic unrelatedness.

<a id="t-06-07"></a>
## Projections

The projection of $x$ onto nonzero $u$ is $(x\cdot u)/(u\cdot u)\,u$. Probes and steering methods often identify a direction and project activations onto or away from it. A measured direction can correlate with a feature without being its unique causal representation.

<a id="t-06-08"></a>
## Linear transformations

A matrix maps vectors while preserving addition and scalar multiplication. Rank describes the dimension of the output subspace reachable through the map. Transformer projections learn different coordinate systems for queries, keys, values, and feed-forward features.

<a id="t-06-09"></a>
## FP32

IEEE 754 binary32 allocates one sign bit, eight exponent bits, and 23 explicitly stored fraction bits (24 bits of precision for normal values because of the implicit leading bit). It offers much wider range and finer precision than 16-bit formats at twice their payload size. A workload labeled “FP32” can still use fused operations, reduced-precision hardware modes, or library-specific accumulation behavior; inspect operations rather than relying on the label.

<a id="t-06-10"></a>
## FP16

FP16 saves memory and can use fast matrix hardware, but its exponent range is much narrower than FP32 or BF16. Small gradients can underflow and large values can overflow. Loss scaling shifts gradients into a representable range; it cannot repair every unstable computation.

<a id="t-06-11"></a>
## BF16

BF16 keeps an exponent width comparable to FP32 with fewer fraction bits. It trades precision for range, which often makes training easier than FP16 while retaining two-byte storage. Accumulation may still occur in FP32.

<a id="t-06-12"></a>
## FP8

FP8 denotes families of eight-bit floating formats with different exponent/fraction tradeoffs. Scaling and hardware support are part of the method. Saying “FP8” without naming the format and scaling policy is incomplete.

<a id="t-06-13"></a>
## INT8

Integer quantization maps real values to an integer grid using scale and possibly zero point. Per-tensor scaling is cheap but sensitive to outliers; per-channel or grouped scaling can reduce error at metadata and kernel complexity cost.

<a id="t-06-14"></a>
## INT4

Four-bit weights can roughly halve packed payload relative to INT8, but scales, zeros, group metadata, padding, and unpacking remain. A nominal 4-bit model is not exactly `parameter_count/2` bytes on disk or in memory.

<a id="t-06-15"></a>
## Overflow

Overflow occurs when magnitude exceeds the representable range, often producing infinity. `exp(large_logit)` is a familiar trigger. Subtracting the maximum logit before exponentiation prevents this without changing softmax.

<a id="t-06-16"></a>
## Underflow

Underflow maps very small magnitudes to subnormal values or zero. Multiplying many probabilities underflows quickly, motivating sums of log-probabilities. A zeroed gradient cannot guide an update.

<a id="t-06-17"></a>
## Numerical stability

Stable algorithms compute the intended mathematical quantity while avoiding avoidable range and cancellation problems. Associativity fails in floating point: `(a+b)+c` may differ from `a+(b+c)`. Parallel reductions therefore need tolerances, not blind bitwise equality.

## Exit problem

Compare query `q=[1,0]` with `a=[2,0]` and `b=[1,1]`. Dot products are 2 and 1; cosines are 1 and about 0.707. Both rank `a` first, but for `c=[100,100]`, dot product favors `c` while cosine still favors `a`. Then explain why stable softmax subtracts the maximum and why packed INT4 memory includes more than weight nibbles.

## References

- IEEE, [IEEE Standard for Floating-Point Arithmetic (IEEE 754-2019)](https://doi.org/10.1109/IEEESTD.2019.8766229), 2019.
- Micikevicius et al., [Mixed Precision Training](https://arxiv.org/abs/1710.03740), 2017.
