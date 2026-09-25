# Parts 01–05 technical and editorial review

Date: 2026-09-19  
Review type: **AI-assisted internal review; not an independent human review**  
Scope: Chapters 1–20 only, covering Parts 01–05.

## Method

The pass checked the prose against the equations and tensor shapes, recomputed the numerical examples, inspected terminology and transitions, checked that each curriculum topic anchor and chapter status line remained present, and assessed citations for proximity and preference for primary papers or authoritative documentation. Numerical spot checks covered softmax values, tensor payloads, matrix-multiplication FLOPs, the scalar forward/backward example, attention mixtures, and attention memory. The repository manuscript checker was run after editing.

This record reports internal defect detection, not approval for publication. It does not replace review by a subject-matter expert, copy editor, accessibility reviewer, or counsel.

## Chapter checks

| Chapter | Checks and disposition | Remaining limitations |
| --- | --- | --- |
| 01 — The LLM in One Picture | Checked end-to-end token path, shapes, softmax table, BF16 byte answer, and train/inference distinction. Recast the autoregressive equation with explicit indices and clarified chain rule versus model parameterization. Added primary architecture and sequence-model references. | The token IDs and logits are intentionally synthetic. No trained-model trace or tokenizer fixture is included in this chapter. |
| 02 — Training vs Inference | Checked loss/update equations, parameter-versus-activation taxonomy, teacher forcing, PyTorch mode distinctions, and lifecycle lists. Corrected the table so freezing some parameters does not imply that the entire training computation lacks a backward graph. | Exact training memory depends on optimizer, sharding, rematerialization, and precision; the chapter appropriately avoids a universal multiplier. |
| 03 — Anatomy of the Modern LLM Stack | Checked system-layer boundaries, request trace, prefill/decode distinctions, and diagnostic table. Added primary references for PagedAttention, PyTorch graph compilation, and roofline analysis. | Runtime products evolve quickly; named implementations and operational behavior require version-pinned verification before release. |
| 04 — Building Our Tiny Laboratory | Checked setup commands, environment-record claims, grad/eval controls, measurement protocol, and reproducibility language. No factual correction was required. | Later dependency pins and accelerator-specific protocols are outside this chapter and must be supplied by their labs. |
| 05 — Tensors and Resource Accounting | Recomputed element counts, byte conversions, projection shapes, and FLOPs. Replaced the approximate operation-count explanation with the exact textbook multiplication/addition counts before the $2MKN$ approximation. | The ledger remains an idealized dense accounting model; sparse, packed, allocator, and backward costs are explicitly excluded. |
| 06 — Geometry and Number Formats | Checked vector formulas, projection definition, format tradeoffs, overflow/underflow claims, and quantization caveats. Specified binary32 fields and normal-value precision; added IEEE 754 and mixed-precision sources. | Exact FP8/INT8/INT4 behavior is format-, scale-, and hardware-specific and is intentionally deferred. |
| 07 — Probability, Logits and Loss | Recomputed softmax probabilities and NLL; checked entropy, KL, odds, cross-entropy derivative, and masking language. Clarified that the chain rule is an identity while the model approximates its conditional factors; added foundational references. | Log base and reduction denominator must still be declared by each experiment; the prose warns about both but provides no executable loss fixture here. |
| 08 — Gradients, Graphs and Autodiff | Checked hand derivatives, graph accumulation, reverse-mode description, finite-difference advice, and code-facing exercise. Clarified that autodiff uses analytic primitive rules but remains subject to floating-point error and nondifferentiability conventions. | The bundled scalar engine does not validate tensor broadcasting, mutation/version semantics, or higher-order gradients. |
| 09 — Linear Layers and Nonlinearities | Recomputed affine/ReLU example, parameter bytes, gradient shapes, and affine-collapse identity. Checked GELU definition and XOR qualification. No correction was required. | The proposed XOR experiment is not implemented in the allowed scope, and the “tent” exercise has no supplied solution. |
| 10 — A Tiny Network, Forward and Backward | Recomputed every forward value, derivative, SGD update, and post-update loss. Checked mutation and accumulation warnings. No correction was required. | The example demonstrates one smooth-side ReLU case; batching and nondifferentiable points remain intentionally unvalidated. |
| 11 — Optimization and State | Checked SGD, momentum convention warning, Adam moments and bias correction, AdamW/L2 distinction, cosine schedule, and mixed-precision step ordering. No correction was required. | Framework-specific optimizer defaults, foreach/fused implementations, and state dtypes require version-pinned tests. |
| 12 — Initialization and Training Stability | Checked clipping arithmetic, warmup units, stability diagnostics, and initialization scaling. Qualified the symmetry argument to cover both incoming and outgoing parameters and noted that identical biases can be safe when weights already break symmetry. | Modern Transformer-specific residual scaling and normalization placement are deferred to later architecture chapters. |
| 13 — Tokenization Algorithms | Checked character/word/subword tradeoffs, BPE procedure, WordPiece qualification, SentencePiece description, byte fallback, and round-trip exercise. No correction was required. | Exact BPE and WordPiece training behavior remains implementation-specific; a concrete tokenizer artifact is not built here. |
| 14 — Vocabulary and Token IDs | Checked ID/row compatibility, special-token semantics, unknown handling, resizing, and tied weights. Clarified that lookup sparsity describes that operation only: output heads and optimizer decay can affect other rows. | Security implications of chat-template parsing need adversarial tests at the application boundary. |
| 15 — Embedding Matrices and Geometry | Checked lookup equivalence, repeated-row gradient accumulation, cosine claims, rotation invariance, and BF16 table bytes. No correction was required. | The chapter does not empirically demonstrate anisotropy or frequency effects; those claims need a pinned model/corpus experiment. |
| 16 — Position and Sequence Order | Checked permutation equivariance, sinusoidal equations, learned tables, relative biases, RoPE query/key rotation, and context-extension caveats. No correction was required. | The exit exercise does not provide numerical vectors or a solution; specific RoPE scaling methods are deliberately deferred. |
| 17 — Sequence Modeling and the Attention Idea | Recomputed the scalar RNN and attention mixture; checked recurrence, LSTM gradient-path qualification, parallelism, and interpretability warning. No correction was required. | Complexity comparisons are conceptual; wall-clock claims require matched kernels and hardware. |
| 18 — Queries, Keys, Values and Scaling | Recomputed scaled scores, softmax weights, output vector, and shape contracts. Added the all-masked-row edge case and its undefined normalization/NaN failure mode. | Cross-attention, dropout, and grouped-query shapes are outside this chapter’s stated scope. |
| 19 — Causal and Multi-Head Attention | Checked mask orientation, future-token mutation test, head reshaping/concatenation, output projection, and shape trace. No correction was required. | Kernel-specific causal-mask alignment for unequal query/key lengths requires runtime-specific tests. |
| 20 — Attention Shapes and Compute Cost | Recomputed projection and pairwise FLOPs, BF16 score bytes, and scaling laws. Added the $T=2D$ crossover under the chapter’s assumptions and made omitted work explicit. | FLOP estimates are not latency predictions; backward, recomputation, communication, and kernel workspace remain workload-specific. |

## Cross-chapter findings

- Notation is internally consistent in the reviewed scope: $B$ is batch, $T$ sequence length, $D$ residual width, $V$ vocabulary size, and $H$ attention heads; $d_h$ or $d_k$ names per-head widths where needed.
- The “Follow the Token / Gradient / Byte / Request” device is used consistently and does not substitute for the mathematical derivations.
- Topic anchors and draft status lines were preserved. The status lines correctly avoid implying independent review.
- Citations are strongest where primary architecture or algorithm claims appear. Some foundational mathematics is supported by standards or canonical references; rapidly changing framework behavior is linked to authoritative documentation where appropriate.
- Exercises are generally diagnostic rather than repetitive, but most do not yet have worked solutions. A solutions appendix remains a publication task.

## Verification result

`python scripts/check_manuscript.py` returned `PASS` for all 80 chapters with no reported errors at the end of this review. Corpus-wide word totals can continue to change while other scoped review passes edit their chapters, so this record does not freeze that aggregate as a review result.

## Review limitations

No external web verification, plagiarism scan, legal review, sensitivity review, or independent reproduction was performed in this pass. Links and bibliographic metadata should be checked in the final citation pipeline. Only Chapters 1–20 were substantively reviewed. Executable artifacts were read only as needed to assess prose references; code, labs, figures, central curriculum data, generated outputs, and bibliography files were outside the authorized edit scope.
