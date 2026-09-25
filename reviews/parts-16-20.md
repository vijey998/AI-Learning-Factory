# Internal review: Parts 16–20

Date: 2026-09-19  
Scope: Chapters 61–80  
Review type: AI-assisted internal technical and editorial review; not an independent expert review.

## Review standard

This pass checked factual precision, systems accounting, claim strength, worked examples, exercises, and the use of primary papers, specifications, and official project documentation. It preserved all curriculum anchors and status lines. The review did not execute the proposed labs, reproduce paper results, benchmark runtimes, or independently verify every external URL. Those remain release-gate work.

## Changes made

| Part | Focus of review | Material strengthening |
|---|---|---|
| 16, serving | Admission, queues, tenancy, residency, disaggregation, tail metrics | Added stability and Little's-law checks, cache-isolation tests, residency-thrash scenarios, typed KV handoff requirements, corrected KV notation, workload-matching rules, percentile uncertainty, and request-accounting identities. |
| 17, local inference | Bandwidth ceilings, cold/warm loading, accelerator correctness, energy | Marked roofline calculations as bounds, added NUMA controls, operational cold-start definitions, maximum-context failure tests, teacher-forced numerical comparison, silent-fallback classification, and explicit energy accounting. |
| 18, RAG and agents | Retrieval metrics, state safety, tool semantics, orchestration economics | Added contrastive-data leakage controls, dynamic-index tests, success-versus-recall distinctions, stale and unauthorized evidence cases, retry/idempotency semantics, semantic authorization checks, a cascade-cost example, and state-reset requirements. |
| 19, interpretability | Measurement validity, causal claims, intervention controls | Clarified final-normalization use in logit lenses, split leakage, SAE non-identifiability, normalized patching metrics, exact steering hook semantics, selection bias, merge compatibility, and rollout evaluation. |
| 20, research agenda | Approximation correctness, neural-handoff feasibility, research design, inference | Added position-integrity checks for KV eviction, destination-KV requirements for handoffs, sample-size and stopping-rule guidance, explicit reproducibility terminology, multiple-comparison controls, interval caveats, and claim-to-artifact traceability. |

## Evidence-level findings

- Chapters 61–77 mostly state established mechanisms or bounded engineering guidance. Performance claims are now framed as measurements or upper bounds rather than universal constants.
- Chapter 78 appropriately labels cross-model neural handoffs and independent expert intervention as hypotheses. The added destination-KV analysis identifies a necessary condition that a cached autoregressive implementation must solve.
- Chapters 73–76 now more consistently distinguish decodability, association, necessity, sufficiency, and mechanism. Probes, attention maps, reconstruction, and representational similarity are not treated as causal proof.
- Chapters 79–80 distinguish engineering measurements from broader scientific claims and now require explicit independent units, stopping rules, uncertainty methods, and artifact traceability.

## Primary-source posture

The reviewed chapters preferentially cite original conference or journal papers, standards, specifications, and official runtime documentation. Added primary sources cover GPU similarity search, TREC retrieval evaluation, reproducibility terminology, and statistical reporting. Fast-moving runtime documentation is date-labelled; readers must still pin release or commit revisions when reproducing results.

## Residual risks and required independent work

1. Run every chapter exercise and milestone lab on pinned hardware and software, retain raw outputs, and reconcile observed numbers with the prose.
2. Have serving and runtime specialists independently review Chapters 61–68, especially version-specific runtime behavior and security boundaries.
3. Have retrieval and security specialists threat-model Chapters 69–72 with real authorization, deletion, injection, and retry tests.
4. Have interpretability researchers independently review Chapters 73–78 and attempt the proposed negative controls and handoff baselines.
5. Have a statistician or experienced empirical researcher review the proposed analyses in Chapters 79–80 before publication.
6. Perform a link and bibliographic metadata check as a separate release task; this review intentionally did not edit the central bibliography.

## Internal disposition

The scoped chapters are stronger and suitable for the next implementation and independent-review stage. This document does not promote any chapter status and must not be represented as external peer review or validation of the book's experimental claims.
