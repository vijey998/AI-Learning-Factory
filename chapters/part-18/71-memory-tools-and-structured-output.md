# 71. Memory, Tools and Structured Output

Status: **Draft — not yet independently reviewed.**

An application’s memory is stored state selected for a future request. A model’s weights and KV cache are also forms of state, but they solve different problems. Conflating them produces systems that remember the wrong facts forever and forget the right ones at session boundaries.

<a id="t-71-01"></a>
## Short-term memory

Short-term memory is the active conversation state: recent messages, tool results, and a working summary. Sending the entire transcript increases cost and can bury the current instruction. Sliding windows discard old details; summarization compresses them with possible loss; structured state extracts fields such as goal, constraints, and unresolved decisions. Keep provenance so a summary can distinguish user statements from model inference.

<a id="t-71-02"></a>
## Persistent memory

Persistent memory survives sessions. It may contain explicit preferences, approved project facts, or task checkpoints. Persistence requires a schema, authorization, retention policy, and user-visible correction path. Store confidence, source, created time, last-confirmed time, and scope. “User prefers Python” should not silently become a permanent global rule because one task used Python.

<a id="t-71-03"></a>
## Long-term memory

Long-term retrieval selects a small subset of persistent records for the current query. Similarity alone is insufficient: recency, importance, entity, project, validity interval, and access control matter. Episodic records describe events; semantic records describe consolidated facts; procedural records describe approved workflows. Consolidation can merge repetition but must preserve disagreements rather than average them into fiction.

<a id="t-71-04"></a>
## Tool calling

A tool call is a typed request from the model to external code. A safe loop exposes names, descriptions, and argument schemas; validates proposed arguments; checks authorization; executes; returns a structured result; and lets the model continue. The model proposes actions but the application owns policy. Tool outputs are untrusted data and may contain instructions that should not override the system. Use idempotency keys for retried mutations and distinguish read operations from writes.

Idempotency needs a stable operation identity and stored outcome, not just a random key on each retry. If the connection drops after a charge succeeds, replay with the same key and arguments must return the original result or a conflict; creating a fresh key can charge twice. Exactly-once effects generally require cooperation from the external system, so document whether the application provides at-most-once attempts, idempotent replay, or reconciliation.

<a id="t-71-05"></a>
## Structured outputs

Structured output asks the model to produce data matching a schema, such as `{query, filters, top_k}`. Schema validation catches missing fields, invalid enums, and type errors; it cannot establish that values are factually correct. Version schemas and prefer semantic field names. Optional fields need defined defaults, while unions need a discriminating tag. Parse failures should produce bounded repair or a clear error, not an infinite “please fix JSON” loop.

Validate semantic and security constraints after schema validation: `top_k` can be an integer yet exceed the service limit, and a syntactically valid path can escape an allowed directory. Bind identity and authorization from trusted application state rather than accepting model-produced tenant or user IDs.

<a id="t-71-06"></a>
## Constrained decoding

Constrained decoders mask tokens that would make the output impossible under a grammar or schema. At each step, valid next tokens depend on the parser state; logits for invalid continuations are excluded before sampling. This can guarantee syntactic validity under supported tokenization and grammar semantics. It does not guarantee business validity: a date may be well formed but nonexistent, and an account ID may belong to another user. Validate after decoding too.

<a id="t-71-07"></a>
## Memory invalidation

Memory becomes dangerous when facts change. Use explicit expiry for volatile data, tombstones for deletion, version or entity keys for supersession, and contradiction detection for new evidence. Retrieval should prefer current authoritative records while retaining audit history where policy permits. When a user corrects a fact, invalidate derived summaries that depended on it. Embedding deletion must propagate through replicas, caches, backups, and indexes according to the product’s retention contract.

## Four perspectives

- **Follow the Token:** messages are compressed into summaries or records, selected records return as context, and constrained tokens form typed output.
- **Follow the Gradient:** ordinary memory and tool execution do not change weights; fine-tuning on memories would create a harder-to-delete channel.
- **Follow the Byte:** raw transcripts, vector copies, indexes, and tool payloads have separate storage and retention costs.
- **Follow the Request:** retrieve scoped state, construct prompt, validate tool proposal, authorize, execute, record result, and update only approved memory.

## Lab and exit check

Implement a three-tool loop with JSON Schema validation, one read tool, one idempotent write tool, and one intentionally failing tool. Add persistent records with provenance and expiry. Test malformed JSON, unauthorized arguments, duplicate writes, prompt injection in a tool result, and correction of a stored fact. Explain which guarantees come from decoding, validation, authorization, and execution.

Simulate a lost response after the write commits, then retry. The test passes only if the effect occurs once and the client receives a deterministic prior result or a reconcilable status.

## References

- Schick et al., [Toolformer](https://proceedings.neurips.cc/paper_files/paper/2023/hash/d842425e4bf79ba039352da0f658a906-Abstract-Conference.html), NeurIPS 2023.
- Poesia et al., [Synchromesh](https://openreview.net/forum?id=KmtVD97J43e), ICLR 2022.
- [JSON Schema 2020-12 specification](https://json-schema.org/specification-links#2020-12), accessed 2026-09-19.
