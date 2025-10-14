# 13. Tokenization Algorithms

Status: **Draft — not yet independently reviewed.**

Models consume integers from a finite vocabulary. Tokenization defines the reversible contract between text and those integers, and its choices affect sequence length, multilingual coverage, code handling, cost, and compatibility.

<a id="t-13-01"></a>
## Why machines need tokens

Text arrives as encoded bytes, while a model predicts among a fixed number of categories. A tokenizer segments text and maps each segment to an ID. The decoder reverses IDs into segments and reconstructs text. Token boundaries need not match linguistic words: `unbelievable` might become `un`, `believ`, `able`.

<a id="t-13-02"></a>
## Characters

A character vocabulary is compact and handles unseen words, but sequences grow long. “Transformers” has 12 ASCII characters and potentially more Unicode code points or bytes under other scripts. Unicode normalization matters: visually identical strings can have different code-point sequences.

<a id="t-13-03"></a>
## Words

Word tokens shorten common prose and offer intuitive boundaries, but vocabularies explode across inflections, spelling, identifiers, and languages. An out-of-vocabulary word must collapse to an unknown token or be decomposed by another scheme. Punctuation and whitespace rules become part of the model contract.

<a id="t-13-04"></a>
## Subwords

Subwords trade vocabulary size against sequence length. Frequent strings become single tokens; rare strings decompose into smaller known units. The learned inventory reflects corpus frequencies, so a tokenizer trained mostly on English may represent another language inefficiently. Token count is therefore a property of both text and tokenizer.

<a id="t-13-05"></a>
## BPE from scratch

Byte Pair Encoding begins with small symbols and repeatedly merges the most frequent adjacent pair. For a corpus containing `low`, `lower`, and `lowest`, an early merge might join `l`+`o`, then `lo`+`w`. Encoding applies learned merges in rank order. Training and encoding require deterministic tie-breaking; otherwise two implementations may produce incompatible vocabularies.

A minimal trainer counts adjacent pairs weighted by word frequency, selects one pair, replaces non-overlapping occurrences, and repeats until the vocabulary budget is reached. Naive rescanning is educational but slow. Production trainers maintain efficient pair statistics and carefully specify pre-tokenization, normalization, byte fallback, and merge order.

<a id="t-13-06"></a>
## WordPiece

WordPiece also builds subwords but historically chooses additions using a likelihood-related criterion rather than raw pair frequency. Common implementations mark continuation pieces, such as `play` + `##ing`. The exact training algorithm is implementation-specific; the vocabulary plus segmentation procedure determines compatibility.

<a id="t-13-07"></a>
## SentencePiece

SentencePiece trains directly from raw sentences and treats whitespace as an ordinary symbol, commonly rendered `▁`. It supports BPE and unigram language-model tokenization. The unigram method begins with candidates and removes pieces while minimizing likelihood damage, enabling alternative segmentations during training.

<a id="t-13-08"></a>
## Byte-level tokenization

Starting from 256 byte values guarantees coverage of arbitrary UTF-8 input. Learned merges recover compact common strings. Coverage does not guarantee efficiency: rare scripts or binary-like data may expand heavily, and a Unicode character can span several byte tokens. Decode must concatenate bytes before UTF-8 interpretation; decoding each token independently can create invalid fragments.

## Four perspectives

**Follow the Token:** raw bytes become segments and IDs. **Follow the Gradient:** discrete segmentation is fixed during ordinary model training; gradients update embeddings, not merge choices. **Follow the Byte:** tokenization changes $T$, which changes activation, attention, and KV-cache cost. **Follow the Request:** the server must use the exact normalization, special-token policy, vocabulary, and merge model expected by the weights.

## Exit check

Perform three BPE merges on `low lower lowest` with stated frequencies and tie-breaking. Verify `decode(encode(text)) == text` for whitespace, emoji, composed/decomposed accents, and an unseen script. Explain why round-trip success alone does not establish efficient tokenization.

## References

- Sennrich, Haddow, and Birch, [Neural Machine Translation of Rare Words with Subword Units](https://aclanthology.org/P16-1162/), 2016.
- Kudo and Richardson, [SentencePiece](https://aclanthology.org/D18-2012/), 2018.
- Schuster and Nakajima, [Japanese and Korean Voice Search](https://research.google/pubs/japanese-and-korean-voice-search/), 2012.
