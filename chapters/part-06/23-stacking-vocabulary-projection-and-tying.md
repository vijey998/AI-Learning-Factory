# 23. Stacking, Vocabulary Projection and Tying

Status: **Drafted — technical and editorial review pending.**

Part 6: Build a Transformer

## Learning outcome

Trace hidden states to vocabulary logits and verify shared-weight gradients.

## Prerequisites

CH-22.

A single block refines representations once. A language model stacks blocks, normalizes the final residual state, and converts each position into scores over the vocabulary.

<a id="t-23-01"></a>
### Stack the blocks

Coverage ID: `T-23-01`.

Let $X_0=E[token]+P[position]$ and $X_{\ell+1}=\mathrm{Block}_\ell(X_\ell)$ for $\ell=0\ldots L-1$. Every $X_\ell\in\mathbb{R}^{B\times T\times D}$, but layers do not share parameters unless explicitly designed to. A final normalization produces $H=N_f(X_L)$.

Depth increases sequential computation: block $\ell+1$ cannot start until block $\ell$ produces its state for that microbatch. Activation memory during training also scales roughly with $LBTD$ before checkpointing. Do not reuse one Python module $L$ times accidentally; that creates weight sharing rather than a stack of independent blocks.

<a id="t-23-02"></a>
### Vocabulary projection

Coverage ID: `T-23-02`.

The vocabulary projection maps $H\in\mathbb{R}^{B\times T\times D}$ to logits $Z\in\mathbb{R}^{B\times T\times V}$:

$$
Z=HW_{vocab}^{\top}+b,\qquad W_{vocab}\in\mathbb{R}^{V\times D}.
$$

For (B=2,T=128,D=768,V=50{,}000), logits contain 12.8 million values: about 25.6 MB in BF16 (decimal units). Training need not retain every full-precision softmax probability if a fused cross-entropy kernel is used.

<a id="t-23-03"></a>
### LM head

Coverage ID: `T-23-03`.

The projection module is called the **language-modeling head**. Logits are unnormalized scores, not probabilities. For next-token training, logit vector (Z_{b,t,:}) is compared with target token (x_{b,t+1}). During generation, only the last needed position is sampled after prefill, avoiding vocabulary projection for unused positions where the runtime permits.

A bias is optional. Checkpoint loaders must match whether it exists. Temperature and top-p belong to decoding after logits; they are not part of the trained head.

<a id="t-23-04"></a>
### Weight tying

Coverage ID: `T-23-04`.

Input embeddings use $E\in\mathbb{R}^{V\times D}$. Weight tying sets $W_{vocab}=E$, so token lookup and output scoring share one parameter tensor. This saves $VD$ parameters and couples the geometry used to read and predict tokens. For $V=50{,}000,D=768$, that saves 38.4 million parameters, or 76.8 MB of BF16 weights.

The shared tensor receives two gradient contributions:

\[
\nabla_E L=\nabla_E^{input}L+\nabla_E^{output}L.
\]

In PyTorch, use the same `Parameter` object, not copied values:

```python
self.token_embedding = nn.Embedding(V, D)
self.lm_head = nn.Linear(D, V, bias=False)
self.lm_head.weight = self.token_embedding.weight
assert self.lm_head.weight is self.token_embedding.weight
```

Calling `.clone()` creates a different tensor and breaks tying. Optimizer parameter lists must not update a shared parameter twice.

## Worked trace

With token IDs `[4, 1, 9]`, embedding lookup produces `[1,3,D]`. After $L$ blocks the shape remains `[1,3,D]`; the head returns `[1,3,V]`. The final vector at position 1 predicts token 9. The logit for vocabulary item $j$ is the dot product between hidden state $h$ and embedding row $E_j$ when weights are tied.

## Four recurring perspectives

- **Follow the Token:** an ID becomes an embedding, is repeatedly refined, then is compared with every vocabulary embedding.
- **Follow the Gradient:** tied embeddings accumulate input-path and output-path signals into one parameter.
- **Follow the Byte:** the $V\times D$ table is large; tying removes a full duplicate but logits can still be large.
- **Follow the Request:** prefill may compute logits selectively; decode requires the head once per generated step.

## Lab and exit check

Build tied and untied versions. Verify object identity, parameter counts, and that one backward pass gives the shared weight a gradient reflecting both uses. Trace shapes from `[B,T]` IDs to `[B,T,V]` logits and identify which slice predicts each label.

## Exercises

1. For $V=32{,}000$ and $D=4096$, calculate the parameters and BF16 bytes saved by tying. **Check:** 131,072,000 parameters and 262,144,000 bytes (262.144 MB decimal).
2. With IDs `[4,1,9]`, list the two next-token training pairs and identify the logit positions used. **Check:** position 0 predicts ID 1 and position 1 predicts ID 9; no internal target follows position 2.

## References

- Press and Wolf, [Using the Output Embedding to Improve Language Models](https://arxiv.org/abs/1608.05859), 2016.
- Inan, Khosravi, and Socher, [Tying Word Vectors and Word Classifiers](https://arxiv.org/abs/1611.01462), 2016.
