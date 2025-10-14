# 25. Sequences, Batches and Pretraining

Status: **Drafted — technical and editorial review pending.**

Part 7: Train the Thing

## Learning outcome

Construct shifted labels and packed sequences without unintended cross-example attention.

## Prerequisites

CH-24.

A model becomes a language model through the examples and objective presented to it. Data preparation determines which predictions are rewarded, which tokens can see one another, and how efficiently the training budget is used.

<a id="t-25-01"></a>
### Preparing training sequences

Coverage ID: `T-25-01`.

Tokenize documents, insert explicitly defined boundary tokens, concatenate or pack according to policy, and cut windows no longer than context $C$. Given tokens `[BOS, the, cat, sat, EOS]`, the input is `[BOS, the, cat, sat]` and labels are `[the, cat, sat, EOS]`. Padding labels normally use an ignore index so they contribute neither loss nor gradient.

Splitting data after making overlapping windows can leak almost identical text into train and validation. Split at the document or source level before window construction and deduplicate across splits.

<a id="t-25-02"></a>
### Sequence packing

Coverage ID: `T-25-02`.

Packing fills a fixed-length row with multiple short examples to reduce padding. Suppose capacity is 8 and examples are `[A1,A2,A3]` and `[B1,B2]`. The packed tokens may occupy one row, but ordinary causal attention would let B tokens attend to A tokens. If examples are meant to be independent, use a block-diagonal causal mask and reset or consistently define position IDs. Also mask the loss transition `A3 → B1`; otherwise the model learns an artificial boundary.

Packing policy depends on the training goal. Continuous pretraining corpora may intentionally treat document separators as part of one stream. Instruction tuning usually isolates examples. “Packed” therefore describes storage, not semantics.

<a id="t-25-03"></a>
### Batches

Coverage ID: `T-25-03`.

A batch tensor has shape $[B,T]$, and the model returns $[B,T,V]$. All examples in the batch are processed before an optimizer step, but they remain logically independent unless the attention mask says otherwise. Token count $B\times T$ is often a better workload measure than sequence count.

<a id="t-25-04"></a>
### Mini-batches

Coverage ID: `T-25-04`.

Full-corpus gradients are impractical, so training estimates them from mini-batches. Sampling introduces gradient noise. Shuffling should be reproducible yet different each epoch; distributed samplers must avoid unintended duplication. Bucketing by length can reduce padding but may correlate neighboring batches with content or source, so shuffle at an appropriate level.

<a id="t-25-05"></a>
### Next-token prediction

Coverage ID: `T-25-05`.

For valid label positions $\mathcal{M}$, the objective is

$$
L=-\frac{1}{|\mathcal M|}\sum_{(b,t)\in\mathcal M}
\log p_\theta(x_{b,t+1}\mid x_{b,\le t}).
$$

A length-$T$ row yields at most $T-1$ internal predictions. Verify the shift using readable tokens before training; an off-by-one label bug can still produce a decreasing loss on repetitive data.

<a id="t-25-06"></a>
### Full pretraining

Coverage ID: `T-25-06`.

Pretraining repeatedly samples token batches from a large mixture, computes next-token loss, updates parameters, evaluates held-out data, and checkpoints state. “One epoch” may be meaningless when the corpus is streamed or sampled by mixture weights; token budget and optimizer steps are clearer. The learned model reflects the dataset, tokenizer, mixture, ordering, objective, and optimization procedure—not architecture alone.

<a id="t-25-07"></a>
### Batch size and sequence length dynamics

Coverage ID: `T-25-07`.

Increasing $B$ increases independent sequences; increasing $T$ increases context and causal dependencies. Both raise tokens per step, but attention compute grows approximately with $BT^2D$, while token-wise layers scale near $BTD^2$. Doubling $T$ can therefore more than double cost. Larger batches reduce gradient noise and the number of optimizer steps per token budget; learning-rate behavior may need retuning. Longer sequences also change the distribution of positional distances, so matching total tokens does not make two runs equivalent.

## Four recurring perspectives

- **Follow the Token:** each token becomes both an input and, shifted by one position, a supervision target.
- **Follow the Gradient:** only unmasked label positions contribute; batching averages their signals.
- **Follow the Byte:** padding wastes activation and attention storage; packing improves utilization but needs correct masks.
- **Follow the Request:** pretraining uses full sequence batches, while production prompts have variable lengths and different scheduling constraints.

## Lab and exit check

Write a collator that packs two examples, returns IDs, positions, attention mask, and loss mask, and visually print all four. Assert that changing A cannot change logits for B under independent-example packing. Reconcile the count of valid labels with the loss denominator.

## Exercises

1. Pack examples of lengths 3 and 2 into capacity 8. Count valid next-token labels when cross-example transitions and padding are masked. **Check:** $(3-1)+(2-1)=3$.
2. At fixed $B$ and $D$, double $T$ from 512 to 1024. By what factor do token-wise work and the quadratic attention-score term grow? **Check:** approximately $2\times$ and $4\times$, respectively.

## References

- Vaswani et al., [Attention Is All You Need](https://arxiv.org/abs/1706.03762), 2017.
- Brown et al., [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165), 2020.
