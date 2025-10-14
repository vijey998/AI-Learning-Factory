# 33. Data Sources and Cleaning

Status: **Drafted.**

Part 9: Data, Scaling and Evaluation

## Learning outcome

Create a small corpus with reproducible filtering and exact/near-duplicate checks, while retaining enough provenance to explain why every document is present.

## Prerequisites

CH-25 and CH-28. Sequence construction and split leakage are developed there; this chapter moves upstream to the corpus pipeline.

<a id="t-33-01"></a>
## Training data sources

An LLM learns from token sequences, but those sequences begin as artifacts made for other purposes: web pages, books, source code, papers, conversations, manuals, and licensed or commissioned datasets. A source is more than a topic label. It has an acquisition method, timestamp, rights basis, language distribution, document boundaries, and selection process. Those properties shape the model. Web crawls offer breadth but contain spam and duplication; books offer sustained prose but a narrower distribution; code has executable structure but licenses and generated copies require care; instruction data teaches interaction patterns but may be small and stylistically repetitive.

Build a source manifest before processing content. A useful row contains `source_id`, URI or collection name, retrieval date, content hash, rights basis, parser version, language hint, and raw byte count. Keep raw and derived datasets logically distinct. A later parser fix must not silently redefine the old dataset. The central engineering rule is lineage: a training token should be traceable to a source record and transformation version.

<a id="t-33-02"></a>
## Cleaning

Cleaning converts an artifact into a faithful document. For HTML, that may mean decoding bytes, removing navigation and scripts, extracting visible text, preserving headings and code blocks, normalizing Unicode, and recording extraction failures. Cleaning should remove representation noise without rewriting the author's meaning.

Order matters. Decode before Unicode normalization; parse markup before collapsing whitespace; preserve document and paragraph boundaries before tokenization. Keep counters for every transformation. If 18% of a domain becomes empty after extraction, that is a pipeline incident. Aggressive cleaning can be destructive: lowercasing harms case-sensitive code, ASCII-only rules delete most languages, and flattening tables can scramble relationships. Inspect before/after samples for every rule.

<a id="t-33-03"></a>
## Filtering

Filtering decides whether a document or span belongs in the training distribution. Deterministic filters may use length, repeated-character ratio, language identification, parser confidence, boilerplate fraction, or secrets and personal-data detectors. Learned classifiers can rank quality, but their own training distribution imports preferences and blind spots.

Treat a filter as a versioned decision function that emits a reason, not merely a Boolean. Measure acceptance rates by source, language, topic, and time. A global 60% acceptance rate can hide a filter that keeps 90% of English and 5% of Tamil. Quality filtering is optimization under coverage constraints, not a universal scalar.

<a id="t-33-04"></a>
## Deduplication

Exact deduplication hashes a canonical representation. Near deduplication finds substantial overlap. A common pipeline tokenizes shingles, computes MinHash signatures, and uses locality-sensitive hashing to produce candidate pairs; exact similarity is checked only for candidates.

For token-shingle sets $A$ and $B$, Jaccard similarity is

$$J(A,B)=\frac{|A\cap B|}{|A\cup B|}.$$

If two pages have 90 shared 5-grams and 10 unique 5-grams each, their union has 110 and $J=90/110\approx0.818$. A threshold of 0.8 marks them as near duplicates. The threshold and shingle size are part of the dataset definition.

Cluster duplicates before assigning splits. Otherwise a paraphrased training item can leak into evaluation. Distinguish unwanted repetition from legitimate recurrence: identical license headers should not force unrelated code files into one giant cluster.

<a id="t-33-05"></a>
## Dataset provenance

Publish a dataset card or internal equivalent containing sources, versions, transformations, removal rules, known limitations, composition statistics, and hashes of produced shards. Pin code and configuration. Record random seeds for probabilistic sampling. One design is immutable raw objects plus an append-only ledger:

```text
raw_hash -> parse:v3 -> language_filter:v2 -> pii_filter:v5
         -> dedup_cluster:8f31 -> shard:train-0042
```

If a source must later be removed, lineage identifies affected shards and checkpoints. Without it, “we removed the data” is difficult to demonstrate.

## Four recurring perspectives

- **Follow the Token:** raw bytes become decoded text, normalized spans, tokenizer IDs, and packed sequences.
- **Follow the Gradient:** preprocessing has no gradient, but inclusion determines which token losses later contribute gradients.
- **Follow the Byte:** raw copies, parsed text, signatures, and tokenized shards can multiply storage.
- **Follow the Request:** provenance connects an observed response back to candidate training sources and transformations.

## Lab and exit check

Collect 100 documents from two permitted sources. Produce a manifest, clean them, emit filter reason codes, remove exact duplicates, and cluster near duplicates. Report document and byte counts after each stage and inspect ten accepted and ten rejected items. Exit check: can another person reproduce the final shard from the manifest and pinned code?

## Exercises

1. Two documents have 75 shared shingles and 25 unique shingles each. Compute Jaccard similarity. **Check:** the union has 125 shingles, so $J=0.60$.
2. Explain why deduplicating separately inside train and validation is insufficient. **Check:** cross-split duplicates survive; clustering must precede assignment if the cluster is the unit of independence.

## References

- Lee et al., [Deduplicating Training Data Makes Language Models Better](https://arxiv.org/abs/2107.06499), 2021.
- Dodge et al., [Documenting Large Webtext Corpora](https://arxiv.org/abs/2104.08758), 2021.
- Penedo et al., [The RefinedWeb Dataset for Falcon LLM](https://arxiv.org/abs/2306.01116), 2023.
