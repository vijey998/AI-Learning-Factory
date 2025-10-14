# 69. Embeddings, Contrastive Learning and Vector Indexes

Status: **Draft — not yet independently reviewed.**

An embedding system turns a search problem into geometry. Its success depends on three contracts: the encoder must place useful items near one another, the index must retrieve those neighbors efficiently, and the application must know what “near” means for its users.

<a id="t-69-01"></a>
## Embeddings revisited

Given an encoder $f$, an item $x$ becomes a vector $z=f(x)\in\mathbb{R}^D$. Similarity is commonly dot product $z_q^Tz_d$, cosine similarity, or negative Euclidean distance. If vectors are unit-normalized, ranking by cosine and squared Euclidean distance is equivalent because $\lVert q-d\rVert^2=2-2q^Td$. That algebra does not make the representation semantic by decree: the training data and objective decide which distinctions the space preserves.

<a id="t-69-02"></a>
## Sentence embeddings

A sentence encoder returns one fixed-width vector for a variable-length sentence. Mean pooling contextual token states is a strong, transparent baseline; a learned pooling token is another choice. A bi-encoder embeds queries and candidates separately, enabling offline candidate indexing. Its speed comes from compressing each text before the pair is known, so it can miss fine token-to-token interactions. A cross-encoder reads the pair jointly and is usually slower but more expressive.

For “reset the pump controller” and “restart pump control,” a domain encoder may produce nearby vectors. “Reset the account password” shares a verb but should remain farther away. Test such hard negatives rather than admiring a two-dimensional projection.

<a id="t-69-03"></a>
## Document embeddings

Long documents rarely fit cleanly into one vector. Truncation discards evidence; pooling thousands of tokens can dilute a decisive paragraph. Common designs embed chunks, store several vectors per document, or build hierarchical document and passage vectors. Retrieval should preserve the document ID, section path, timestamps, permissions, and character offsets so the original evidence can be reconstructed. A document embedding is one record in a retrieval data model, not a replacement for the document.

<a id="t-69-04"></a>
## Contrastive embedding training

For a batch of matched query-document pairs $(q_i,d_i)$, a standard in-batch contrastive loss is

$$
L_i=-\log\frac{\exp(s(q_i,d_i)/\tau)}{\sum_j\exp(s(q_i,d_j)/\tau)},
$$

where $s$ is similarity and $\tau$ is temperature. Gradients pull the positive pair together and push batch negatives away. This works only when negatives are meaningful. False negatives teach the model to separate valid matches; trivial negatives produce little learning. Hard-negative mining improves discrimination but can amplify annotation errors. Sentence-BERT demonstrated efficient sentence retrieval with siamese encoders; DPR showed the same basic pattern for open-domain passage retrieval.

The denominator shown uses documents in the batch as negatives for each query. A symmetric objective also predicts queries from documents, but it is a different loss and should be stated. Deduplicate near-identical items before batch construction and keep documents from one source entity in one data split; otherwise near-duplicate passages can become false negatives during training and leakage during evaluation.

<a id="t-69-05"></a>
## Vector search

Exact search computes similarity to all $N$ vectors, costing roughly $O(ND)$ operations per query. For one million 768-dimensional FP32 vectors, the raw matrix is about 3.07 GB decimal, before IDs and index overhead. A matrix multiplication can make exact search surprisingly competitive at modest scale and high batch size. Always measure it as the quality reference.

<a id="t-69-06"></a>
## Approximate nearest neighbors

Approximate nearest-neighbor (ANN) methods visit or decode only part of the collection. They trade recall for latency, memory, construction time, and update behavior. Report recall@$k$ against exact neighbors, queries per second at stated concurrency, p50/p95 latency, index size, build time, and filtering conditions. “Fast ANN” without the achieved recall is an incomplete claim.

<a id="t-69-07"></a>
## HNSW

Hierarchical Navigable Small World indexes organize vectors in a multi-layer proximity graph. Search begins in sparse upper layers, greedily approaches the query, then explores a candidate set in denser lower layers. Larger construction and search breadth parameters generally improve recall while consuming time and memory. HNSW supports incremental inserts well, but graph links and per-node metadata can be expensive. Deletes, filters, and changing embedding distributions require operational testing; the elegant graph sketch does not settle those costs.

<a id="t-69-08"></a>
## IVF

An inverted-file index first assigns each vector to a coarse centroid. At query time it probes the nearest `nprobe` lists and searches only their members. More lists reduce candidates per list; more probes recover recall at added cost. Coarse quantizer training must represent production data. Distribution shift can create overloaded or poorly placed cells, so list-size histograms and recall by cohort matter.

<a id="t-69-09"></a>
## Product quantization

Product quantization splits a $D$-dimensional vector into $m$ subvectors and replaces each with a codebook ID. With 256 centroids per subspace, each ID takes one byte, so a vector becomes roughly $m$ bytes plus codebooks. Distance tables let search compare compressed codes cheaply. Compression introduces distortion; IVF-PQ often retrieves a candidate set using compressed distances and reranks a smaller set with full vectors. Measure end-task quality because nearest-neighbor recall alone may hide losses on the evidence the generator needs.

<a id="t-69-10"></a>
## Vector databases

A vector database combines an index with persistence, metadata filtering, updates, replication, access control, and query APIs. Those system properties can dominate algorithm choice. Filtering after ANN may return too few authorized results; filtering before search may fragment the index. Store the encoder name and revision with every vector, because vectors from incompatible embedding spaces are not safely comparable. Re-embedding is a data migration with dual-write, backfill, validation, and rollback concerns.

## Four perspectives

- **Follow the Token:** token states are pooled into one or more vectors; ANN returns IDs that lead back to original token spans.
- **Follow the Gradient:** contrastive gradients shape neighborhoods; index construction and query execution themselves use no gradient.
- **Follow the Byte:** exact FP32 storage is $4ND$ bytes; graph edges, codes, metadata, and replicas add overhead.
- **Follow the Request:** encode query, apply authorization filters, search, optionally rerank, fetch source spans, and record retrieval telemetry.

## Lab and exit check

Embed a labelled corpus and compare exact search with HNSW or IVF at several search breadths. Record recall@10, p50/p95 latency, memory, build time, and one semantic failure. Explain why cosine and Euclidean rankings agree only after normalization. A successful demo does not establish robustness under new domains, deletions, or permission filters.

Repeat the comparison with metadata filtering and with 10% of the corpus replaced by newly embedded documents. Report whether recall, latency, and index size remain stable after updates; a static index benchmark does not establish operational update quality.

## References

- Reimers and Gurevych, [Sentence-BERT](https://aclanthology.org/D19-1410/), EMNLP-IJCNLP 2019.
- Karpukhin et al., [Dense Passage Retrieval](https://aclanthology.org/2020.emnlp-main.550/), EMNLP 2020.
- Malkov and Yashunin, [Efficient and Robust Approximate Nearest Neighbor Search Using HNSW](https://doi.org/10.1109/TPAMI.2018.2889473), IEEE TPAMI 2020.
- Jégou, Douze, and Schmid, [Product Quantization for Nearest Neighbor Search](https://doi.org/10.1109/TPAMI.2010.57), IEEE TPAMI 2011.
- Johnson, Douze, and Jégou, [Billion-scale similarity search with GPUs](https://doi.org/10.1109/TBDATA.2019.2921572), IEEE Transactions on Big Data 2021.
