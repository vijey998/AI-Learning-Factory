# 05. Tensors and Resource Accounting

Status: **Draft — not yet independently reviewed.**

A tensor is an array plus a contract: shape, numeric type, layout, device, and meaning. Most LLM bugs become easier once those facts are written beside every operation.

<a id="t-05-01"></a>
## Scalars

A scalar has one value: a loss, learning rate, or temperature. A framework may store it as a zero-dimensional tensor with shape `[]`. Scalar does not mean unimportant: one loss value can summarize millions of token predictions.

<a id="t-05-02"></a>
## Vectors

A vector is a one-dimensional array. A token representation of width $D$ has shape `[D]`; a vocabulary-logit vector has shape `[V]`. Its coordinates only gain meaning from the space and operation using them.

<a id="t-05-03"></a>
## Matrices

A matrix has two axes. A weight $W\in\mathbb{R}^{D_{in}\times D_{out}}$ maps an input row vector from width $D_{in}$ to $D_{out}$. An embedding table `[V,D]` is also a matrix, but lookup selects rows instead of multiplying by the integer token ID.

<a id="t-05-04"></a>
## Tensors

Tensor is the general term for an array with any number of axes. A batch of hidden states commonly has `[B,T,D]`: batch, token position, hidden width. Names matter more than rank. Both an image and attention scores may be rank four while representing completely different things.

<a id="t-05-05"></a>
## Shapes

Shape records the length of each axis. For `X[B,T,D]` and `W[D,F]`, `X @ W` produces `[B,T,F]`. Write this before code. Shape agreement catches wrong transposes and accidental mixing of heads or batches.

<a id="t-05-06"></a>
## Dimensions

*Dimension* can mean the number of axes or an axis length. This book uses **rank** for the number of axes and names such as hidden width for axis lengths. A `[2,8,64]` tensor has rank three and 1,024 elements.

<a id="t-05-07"></a>
## Indexing

`X[b,t,d]` chooses one scalar. `X[b,t,:]` chooses the hidden vector at one token. Slicing may produce a view sharing storage rather than a copy; mutating a view can therefore alter its base. We avoid in-place mutation until ownership is explicit.

<a id="t-05-08"></a>
## Transpose

Transposing swaps axes without changing element values. Attention uses $QK^T$: `[T,Dh] @ [Dh,T] -> [T,T]`. A transpose may change strides instead of physically rearranging bytes. Some kernels need contiguous layouts and may trigger a copy later.

<a id="t-05-09"></a>
## Batch dimensions

Batch axes describe independent examples or requests processed together. Batched matrix multiplication applies the compatible operation across leading axes. A batch increases parallel work, but training batches, prefill batches, and continuously changing decode batches have different scheduling behavior.

<a id="t-05-10"></a>
## Broadcasting

Broadcasting aligns shapes from the trailing axes. Dimensions are compatible when equal or when one is 1. Adding bias `[F]` to output `[B,T,F]` reuses the same bias across batch and token axes. Broadcasting is conceptually expanded; a good implementation need not materialize copies. An accidental `[T,1] + [T]` yields `[T,T]`, a classic silent memory bug.

<a id="t-05-11"></a>
## Dtypes

A dtype specifies representation and nominal bits per element. It affects range, precision, supported hardware paths, and storage. Never infer dtype from a model name or file extension. Mixed-precision systems may store weights in one format, accumulate in another, and quantize caches separately.

<a id="t-05-12"></a>
## Element counts

For dense shape $(n_1,\ldots,n_k)$, element count is $N=\prod_i n_i$. `[1024,4096]` contains 4,194,304 elements. Zero-length axes make the product zero; sparse tensors require a different accounting model.

<a id="t-05-13"></a>
## Bytes

Ideal dense payload bytes equal `elements × bits/8`. BF16 uses 2 bytes, so the preceding tensor needs 8,388,608 bytes, or 8 MiB. Actual memory can include headers, padding, allocator rounding, alignment, packed-format metadata, workspaces, copies, gradients, and cached blocks. State whether GB means $10^9$ bytes or GiB means $2^{30}$.

<a id="t-05-14"></a>
## FLOPs

For multiplying `[M,K] @ [K,N]` by the textbook algorithm, there are $MKN$ multiplications and $MN(K-1)$ additions. We approximate this as $2MKN$ FLOPs, dropping the lower-order $MN$ term. Some sources count one fused multiply-add as one operation rather than two; always state the convention. FLOPs estimate arithmetic, not time.

<a id="t-05-15"></a>
## Matrix multiplication

For `X[B,T,D] @ W[D,F]`, flattening the leading axes gives $M=BT$, so output is `[B,T,F]` and cost is approximately $2B T D F$ FLOPs. With `B=1,T=128,D=256,F=1024`, the estimate is 67,108,864 FLOPs. Input, weights, and output must also move through memory; later roofline analysis asks which resource limits execution.

## Resource ledger

For every important tensor, record: semantic axes, shape, dtype, elements, ideal bytes, lifetime, owner, and operation count. Apply it to attention score `[B,H,T,T]`: its quadratic $T^2$ term is immediately visible. FlashAttention later changes the materialization schedule; it does not change the mathematical attention result.

## Exit problem

Let `X` be BF16 `[4,512,1024]` and `W` be BF16 `[1024,4096]`. The output is `[4,512,4096]`. Ideal payloads are 4 MiB, 8 MiB, and 16 MiB. The projection costs about $2(4)(512)(1024)(4096)=17,179,869,184$ FLOPs. These figures exclude bias, allocator overhead, accumulation details, and backward work.

## References

- [NumPy documentation](https://numpy.org/) — multidimensional arrays, indexing, vectorization, and broadcasting. Accessed 2026-09-18.
