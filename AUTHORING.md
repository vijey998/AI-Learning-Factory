# Authoring and evidence policy

1. Preserve every source requirement and stable topic ID. Merges change destinations, not obligations.
2. Select authoritative references before writing a technical deep dive. Pin software versions, model revisions, dataset versions and hardware. Do not treat a previously suggested reading list as a verified citation.
3. Teach each mechanism in order: concrete problem, intuition, worked example, formal definition, implementation, failure case, exercise and connection to the four perspectives.
4. State dimensions and conventions next to equations. Define B, T, D, H, Hkv and head dimension before use. Distinguish MACs from FLOPs and decimal GB from binary GiB.
5. Keep runnable code in code/. Chapters show the relevant excerpt and point to the exact implementation. Do not claim GPU results from CPU tests or simulated schedules.
6. Compare optimization results at matched quality and workload. Report warmup, compilation, transfer, synchronization, context lengths, concurrency and uncertainty.
7. Introduce sampling sufficiently early to run tiny GPT; reserve its full derivation for Chapter 51. Introduce basic held-out evaluation during tiny-model training; reserve rigorous evaluation for Part IX. Advanced chapter order must not prevent a basic working milestone.
8. Avoid anthropomorphic conclusions from attention plots or probe accuracy. Mark causal evidence, correlational evidence and speculation separately.
9. A chapter moves from planned to drafted only after substantive teaching content exists. Every non-planned topic needs an evidence path and section anchor.
10. Technically reviewed requires a dated review record identifying the reviewer or review process, references, derivation checks, executable checks, known limits and unresolved findings. A model's own second pass is not independent human review.
11. Integrated requires cross-chapter notation, prerequisites, links and examples to be reconciled. Complete requires passing review, exercises/answers, lab validation where applicable and resolved findings. Never auto-promote based on word count or heading existence.
12. Final release also requires original V1 reconciliation, source citation audit, completed labs and visual verification of HTML/PDF exports. The automated checker is a structural safeguard; editorial review establishes semantic coverage.

## Research claims

Neural handoff, silent expert intervention and dead-call elimination are candidate research programs. A proposal must name a falsifiable hypothesis, competitive baselines, a fixed budget, a quality metric, transfer/routing overhead, ablations, uncertainty and a negative-result criterion. Novelty requires a current literature search.
