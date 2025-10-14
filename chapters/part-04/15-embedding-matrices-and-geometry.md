# 15. Embedding Matrices and Geometry

Status: **Draft — not yet independently reviewed.**

An embedding layer turns a category index into a learned vector. That vector is an initial state, not a permanent dictionary definition.

<a id="t-15-01"></a>
## Embedding matrices

An embedding table $E\in\mathbb{R}^{V\times D}$ contains one $D$-dimensional row for each vocabulary item. IDs `[2,5,2]` return rows `[E_2,E_5,E_2]`, producing shape $[3,D]`. Mathematically, lookup equals multiplying a one-hot vector by $E$, but gathering rows avoids materializing enormous sparse one-hot tensors.

Initialization is usually random. Meaningful structure emerges because gradient updates make rows useful for prediction. Rows can encode many entangled regularities; assigning a single human meaning to a coordinate is rarely justified.

<a id="t-15-02"></a>
## Static embeddings

A static token embedding returns the same table row for the same ID before context processing. In a simple word-vector model, `bank` might have one vector even in “river bank” and “bank loan.” Static geometry can capture distributional similarity, but polysemy is compressed into one point.

<a id="t-15-03"></a>
## Contextual embeddings

After Transformer layers, each occurrence has a hidden state conditioned on surrounding tokens. The two occurrences of `bank` begin with the same token row but diverge as attention and MLPs mix context. Calling every hidden state an “embedding” is common but ambiguous; specify whether you mean input-table rows, layer activations, pooled sequence vectors, or a separately trained retrieval model.

<a id="t-15-04"></a>
## Representation geometry

Cosine similarity compares direction: $\cos(a,b)=a\cdot b/(\|a\|\|b\|)$. Euclidean distance also depends on magnitude. Nearest neighbors can expose useful structure, but similarity is evidence about geometry under a metric, not proof that the model “understands” a concept. An invertible rotation changes coordinates while preserving dot products, showing why individual dimensions have no stable universal semantics.

Anisotropy, frequency effects, and normalization can distort neighbor searches. Always state the layer, pooling method, normalization, metric, corpus, and model revision when reporting embedding results.

<a id="t-15-05"></a>
## Embedding lookup and gradients

If IDs `[2,5,2]` yield upstream gradients $g_1,g_2,g_3$, then row 2 receives $g_1+g_3$, row 5 receives $g_2$, and unused rows receive zero from this lookup. Repeated-token accumulation is the sparse analogue of shared-parameter gradient accumulation. Dense output heads may still generate gradients for every vocabulary row when weights are tied.

For $V=50{,}000$, $D=4096$, a BF16 table stores 409.6 MB decimal. Lookup performs little arithmetic relative to bytes moved, so it is memory-oriented. During distributed training, sharding or sparse access patterns complicate the simple local picture.

## Four perspectives

**Follow the Token:** ID $i$ selects $E_i$, then context transforms that state layer by layer. **Follow the Gradient:** repeated IDs accumulate into shared rows. **Follow the Byte:** table size is $V D$ elements and lookup is a gather with irregular access. **Follow the Request:** tokenization and checkpoint revision determine which semantic row a request retrieves.

## Exit check

Given IDs `[1,1,3]` and three upstream vectors, write the nonzero row gradients. Compare cosine and Euclidean neighbors before and after scaling one vector by ten. Explain why a high probe score from one layer would be correlational rather than automatically causal.

## References

- [PyTorch `Embedding`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Embedding.html). Accessed 2026-09-19.
- Mikolov et al., [Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/abs/1301.3781), 2013.
- Peters et al., [Deep contextualized word representations](https://aclanthology.org/N18-1202/), 2018.
