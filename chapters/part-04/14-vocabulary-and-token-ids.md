# 14. Vocabulary and Token IDs

Status: **Draft — not yet independently reviewed.**

A vocabulary is an ordered mapping, not merely a bag of strings. Its row numbers connect tokenizer output to embedding and output-projection rows.

<a id="t-14-01"></a>
## Vocabulary

Suppose the vocabulary is `{0:"<pad>", 1:"cat", 2:"dog", 3:"s"}`. Its size $V=4$ sets the embedding table's first dimension and the number of language-model logits. Adding a token creates a new category; removing or reordering one changes the semantics of an existing row. The tokenizer model, normalization rules, pre-tokenizer, merge ranks, and special-token configuration together form the full artifact.

<a id="t-14-02"></a>
## Token IDs

An ID is an index, not a magnitude. ID 100 is not semantically “greater” than ID 5. Feeding raw IDs as continuous scalar features would invent an ordering; embedding lookup uses the ID to select a row. For a batch of IDs $I[B,T]$, lookup into $E[V,D]$ produces $X[B,T,D]$.

Two tokenizers may emit different IDs for the same visible token. Even when both contain `cat`, its row can differ. Human-readable token strings therefore cannot establish model compatibility.

<a id="t-14-03"></a>
## Special tokens

Special tokens encode protocol events such as beginning/end of text, padding, unknown input, separators, roles, or tool boundaries. Some are allowed only when inserted by a chat template. Treating user text that resembles a control token as the control token can create injection or parsing errors. Tokenizers distinguish ordinary encoding from explicit special-token recognition.

Padding is usually masked so it does not affect attention or loss. End-of-sequence often terminates generation, but the runtime's stopping policy decides behavior. A token's name alone does not enforce semantics.

<a id="t-14-04"></a>
## Unknown tokens

Word-level and some subword tokenizers use `<unk>` when no decomposition exists. Multiple distinct strings then become the same ID, irreversibly losing information. Byte fallback avoids unknown text by representing its encoded bytes, though at potentially high token cost. An unknown token appearing frequently in production is a monitoring signal for data or configuration drift.

<a id="t-14-05"></a>
## Tokenizer-model compatibility

Imagine swapping IDs 1 and 2 above while leaving weights unchanged. Text `cat` now retrieves the row learned for `dog`, and the logit formerly decoded as `cat` becomes `dog`. Tensor shapes still match; outputs become wrong without a clean exception. Compatibility requires the exact token-to-ID map, special IDs, added tokens, normalization, chat template, and vocabulary size used for training or adaptation.

Vocabulary expansion is possible: resize input embeddings and output head, initialize new rows, and train them. It is a model change, not a harmless tokenizer edit. With tied input/output weights, both interfaces change together. Shrinking a vocabulary requires remapping or discarding rows and can invalidate checkpoints and adapters.

## Four perspectives

**Follow the Token:** a string segment becomes one stable integer and selects one row. **Follow the Gradient:** only rows referenced by a batch receive gradients *through the lookup operation*, though a tied or separate output softmax can touch all vocabulary rows; optimizer weight decay can also change a row with zero data gradient. **Follow the Byte:** embeddings and LM head scale as $V\times D$, so vocabulary expansion has a measurable memory cost. **Follow the Request:** client templates and server tokenizers must agree on control tokens and stop IDs.

## Exit check

Construct a four-token vocabulary and embedding table. Permute two IDs without moving rows and describe the failure. Then permute both IDs and rows consistently. List the artifacts you would hash in a production model package to detect mismatch.

## References

- [Hugging Face tokenizer summary](https://huggingface.co/docs/transformers/tokenizer_summary) and [special tokens](https://huggingface.co/docs/tokenizers/api/added-tokens). Accessed 2026-09-19.
