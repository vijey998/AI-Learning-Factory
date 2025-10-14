# 70. RAG and Retrieval Quality

Status: **Draft — not yet independently reviewed.**

Retrieval-augmented generation (RAG) gives a model evidence at request time. It does not guarantee that the evidence is relevant, that the model will use it correctly, or that the resulting answer is true. Treat retrieval and generation as separately measurable stages.

<a id="t-70-01"></a>
## RAG

A basic pipeline transforms query $q$ into retrieval query $q'$, retrieves candidates $D_k$, constructs prompt $p(q,D_k)$, and generates answer $y$. Lewis et al. introduced RAG as a learned combination of parametric and retrieved non-parametric memory; production systems also use simpler frozen retrievers and prompt assembly. The practical gain is updateability and source visibility. The price is another failure surface: ingestion, indexing, query formulation, retrieval, context packing, and generation can each fail.

<a id="t-70-02"></a>
## Chunking strategies

Fixed token windows are reproducible but can split tables or procedures. Overlap protects boundary evidence but duplicates tokens and can crowd the context. Structure-aware chunking follows headings, paragraphs, code symbols, or document sections. Semantic segmentation attempts to split on topic shifts but adds model cost and instability. Preserve parent relationships so a matched paragraph can be expanded with its heading or neighboring steps. Choose chunk size through evaluation, not a universal folklore number.

Suppose an answer requires a warning in one paragraph and a limit in the next. Independent 200-token chunks may retrieve only one. Parent-child retrieval can search small passages, then supply the containing section. The added context helps only if it does not displace more valuable evidence.

<a id="t-70-03"></a>
## Retrieval strategies

Sparse retrieval such as BM25 rewards exact lexical overlap and handles identifiers well. Dense retrieval can match paraphrases. Hybrid retrieval combines their scores or rankings, often with reciprocal-rank fusion. Query rewriting, multi-query retrieval, hypothetical-document queries, and decomposition can expand recall, but each adds latency and may drift from intent. For domain systems, metadata constraints—product version, date, asset, language, permission—often improve relevance more reliably than another LLM call.

<a id="t-70-04"></a>
## Reranking

A two-stage design retrieves perhaps 50–200 candidates cheaply, then applies a cross-encoder or late-interaction model to a smaller set. Reranking improves fine-grained relevance because it evaluates query and passage together. It cannot recover an omitted candidate. Measure first-stage recall at the reranker cutoff, reranker quality, and total latency. ColBERT’s late interaction retains token-level vectors and uses maximum-similarity aggregation, occupying a middle ground between single-vector search and a full cross-encoder.

<a id="t-70-05"></a>
## Retrieval evaluation

Build a judgement set of queries with relevant passages and explicit “no answer” cases. Useful retrieval metrics include recall@$k$, precision@$k$, mean reciprocal rank, and nDCG. Evaluate slices: exact identifiers, paraphrases, temporal questions, multi-hop questions, and permission-filtered queries. Then evaluate the complete answer with evidence attribution, correctness, completeness, abstention, and latency. A generator can answer from memorized parameters even when retrieval failed, masking a broken retriever.

Define relevance and denominators before computing metrics. Recall@$k$ is the fraction of judged relevant items retrieved in the first $k$; success@$k$ merely asks whether at least one relevant item appeared. For questions requiring two independent passages, success@$k$ can look perfect while evidence recall is only one half. Pool judgements beyond one system's results so unjudged candidates are not automatically treated as irrelevant.

An intervention test makes attribution clearer: remove the decisive passage, replace it with a conflicting passage, or shuffle irrelevant passages. If the answer never changes, claimed grounding is doubtful. If it follows malicious text blindly, instruction hierarchy is weak.

<a id="t-70-06"></a>
## Grounding

Grounding means the response’s externally checkable claims are supported by supplied evidence. Citation presence is insufficient; the cited span must entail the claim. Require stable source IDs and offsets, distinguish quotation from inference, and make abstention valid when evidence is missing. Retrieved documents are untrusted input: they can contain obsolete content, prompt injection, or data the user may not access. Enforce access before retrieval output reaches the model and separate document text from system instructions.

## Four perspectives

- **Follow the Token:** source text becomes chunks, retrieved chunks become prompt tokens, and citations map generated claims back to spans.
- **Follow the Gradient:** a frozen RAG pipeline has none at request time; retriever or generator fine-tuning changes which evidence is selected or used.
- **Follow the Byte:** overlap enlarges indexes and prompts; reranking adds activation and model-weight traffic.
- **Follow the Request:** trace ingestion version, rewritten query, candidates, scores, filters, packed context, answer, and citations as one observable record.

## Lab and exit check

Create at least 30 answerable and 10 unanswerable queries over a small corpus. Compare lexical, dense, and hybrid retrieval; then add reranking. Report retrieval recall, answer correctness, citation support, abstention, and latency. Diagnose one failure as ingestion, retrieval, packing, or generation. Do not label an answer grounded merely because it sounds specific.

Add one stale-document case and one unauthorized-but-highly-relevant document. The expected result is use of the current authorized source, not merely retrieval of the semantically closest passage.

## References

- Lewis et al., [Retrieval-Augmented Generation](https://proceedings.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html), NeurIPS 2020.
- Robertson and Zaragoza, [The Probabilistic Relevance Framework: BM25 and Beyond](https://doi.org/10.1561/1500000019), 2009.
- Khattab and Zaharia, [ColBERT](https://doi.org/10.1145/3397271.3401075), SIGIR 2020.
- Thakur et al., [BEIR](https://openreview.net/forum?id=wCu6T5xFjeJ), ICLR 2021.
- Craswell et al., [Overview of the TREC 2020 Deep Learning Track](https://trec.nist.gov/pubs/trec29/papers/OVERVIEW.DL.pdf), TREC 2020.
