# Parts 06–10 internal review

Date: 2026-09-19  
Scope: Chapters 21–40  
Review type: **AI-assisted internal review; not independent human review**

## Review process

The review read the twenty chapter sources in Parts 06–10 and checked their explanations, equations, tensor shapes, parameter and memory arithmetic, worked examples, cross-chapter prerequisites, exercises, and source lists. Stable topic anchors and all chapter status lines were preserved. No curriculum, generated output, central project metadata, scripts, labs, code, figures, or bibliography database were edited.

## Material changes

- Corrected the residual-branch gradient statement by fixing the Jacobian convention and explicitly showing the transpose for column-vector gradients.
- Standardized ambiguous parenthetical notation in core derivations, including batching, accumulation, RoPE, MHA/MQA/GQA, MoE capacity, and real-configuration accounting.
- Replaced the overloaded distillation temperature symbol with $\tau$ and defined the softened distribution and conventional $\tau^2$ scaling.
- Added explicit prerequisite continuity to Chapters 33–40.
- Added two answer-checkable exercises to every chapter in scope. The exercises cover derivations, tensor shapes, parameter counts, memory units, masking, uncertainty, routing overflow, preference objectives, and verifier error rates.
- Converted the unlinked references in Chapters 21–32 to direct primary-paper or official-publication links. Chapters 33–40 already used direct links; version-sensitive framework documentation remains clearly labeled as such.

## Derivation and arithmetic checks

The review independently recalculated representative values used by the text and exercises:

- LayerNorm and RMSNorm examples; residual Jacobian $I+J_F$.
- SwiGLU/MHA block counts and tied-embedding savings.
- Q/K/V, score, and logit tensor shapes for the tiny GPT.
- Token-weighted accumulation, clipping, loss scaling, and optimizer-state bytes.
- MHA/GQA/MQA projection sizes and KV-cache bytes.
- MoE capacity ceilings and overflow counts.
- Llama 2 7B-style per-token KV storage, including the 2 GiB result at 4,096 tokens under the stated MHA/BF16 assumptions.
- Jaccard similarity, mixture epochs, perplexity, $6ND$ planning FLOPs, LoRA counts, Bradley–Terry loss, PPO clipping, pass@k, and verifier error rates.

## Executable and structural checks

`python scripts/check_manuscript.py` was run after the edits and returned `PASS` for all 80 chapters, with no missing or reordered anchors, no status-line failures, and no math-delimiter errors.

## Known limits and unresolved findings

- This review is not an independent human technical or editorial review and must not be used to promote chapter status on that basis.
- The chapter labs and full training experiments were not executed in this review; executable validation remains a separate release requirement.
- External links were selected as direct primary or official sources but were not exhaustively checked for future availability, redirects, or post-2026 revisions.
- Fast-moving claims about reasoning training, synthetic data, benchmark contamination, and current model conventions remain revision-sensitive and should be rechecked against pinned sources before publication.
- The chapters now contain compact answer checks, not a separately typeset instructor solution manual.
- Visual teaching assets and final rendered PDF/HTML inspection were outside this scoped review.

## Disposition

Parts 06–10 are materially stronger and structurally valid, but remain drafted pending independent human review, lab validation where applicable, citation/link verification at release time, and publication-layout inspection.
