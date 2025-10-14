# 80. Evidence, Ablations and Publication

Status: **Draft — not yet independently reviewed.**

The final task is to make claims no larger than the evidence. Strong work connects a controlled comparison, uncertainty, resource measurement, and a reproducible artifact to one precise conclusion.

<a id="t-80-01"></a>
## Ablations

An ablation removes or replaces a component to estimate its marginal contribution. Compare full method, component removed, reasonable alternative, and interactions between components. Retraining after removal answers whether the architecture needs the component; removing it only at inference answers whether the trained system currently relies on it. Those are different questions. Keep tuning budgets equal, and avoid interpreting a broken implementation as evidence for the full design.

For a neural handoff, ablate the router, bridge, latent transfer, and expert intervention separately. Include a shuffled bridge and same-model stitch. If only the complete stack works, factorial ablations can reveal synergy; if nothing changes when a component disappears, its call may be dead.

<a id="t-80-02"></a>
## Statistical significance

A statistical test quantifies incompatibility between observed data and a null model under assumptions. It does not measure practical value or probability that the hypothesis is true. Define the unit of independence: tokens from one sequence are not thousands of independent experiments, and repeated benchmark prompts may share templates. Use paired tests when methods run on the same items. Correct or constrain multiple comparisons rather than fishing among many metrics.

Report the effect estimate and uncertainty beside any test. Predeclare one primary outcome or use a justified hierarchical or multiplicity procedure; testing 20 slices and highlighting the smallest unadjusted value changes the false-positive rate. If prompts are nested in documents or users, a cluster bootstrap or hierarchical model is often more defensible than treating prompts as independent.

<a id="t-80-03"></a>
## Confidence intervals

A confidence interval describes an estimator’s sampling uncertainty under a procedure. Bootstrap paired per-example differences when analytic assumptions are unsuitable; resample at the independent unit, such as document, user, or run. For training variance, report results across independently trained seeds, not merely repeated evaluation of one checkpoint. An interval excluding zero may still describe a uselessly small improvement.

For bounded or highly skewed metrics, state the interval method; a normal interval can extend beyond the valid range. With only a few training seeds, neither a narrow standard-error bar nor a bootstrap over benchmark examples captures optimization variance reliably. Show individual seed results and treat broad generalization claims as provisional.

<a id="t-80-04"></a>
## Uncertainty

Separate aleatoric variation in data, epistemic uncertainty from limited knowledge, optimization variance across seeds, measurement noise, and distribution uncertainty. Report sensitivity to prompts, checkpoints, workloads, and hardware where relevant. Error bars do not cover untested populations. Use calibration metrics when probabilities drive routing, but remember that calibration can degrade after distribution shift.

<a id="t-80-05"></a>
## Profiling research claims

Profile the complete workload after warmup and synchronize accelerators around timed regions. Separate compilation, model load, prefill, decode, transfer, bridge, queue, and sampling time. Use traces and hardware counters to explain a result, then validate with end-to-end latency. Profilers perturb execution; state their settings. Throughput measured at saturation and single-request latency answer different questions.

<a id="t-80-06"></a>
## FLOPs-memory-latency measurement

Analytic FLOPs expose scaling; profiler FLOPs expose executed kernels; wall time exposes the system. Report counting convention, shapes, batch, sequence lengths, precision, hardware, software versions, concurrency, and quality. Measure peak allocated and resident memory where possible, plus KV and weight calculations. Include host-device and network bytes. A lower-FLOP method can be slower because it launches more kernels, moves more memory, or fragments batches.

<a id="t-80-07"></a>
## Writing papers

Write the contribution as a verifiable claim: problem, gap, method, evidence, and limits. Methods should be reproducible; results should connect every headline claim to a table or figure; related work should explain differences rather than list citations. Put limitations beside conclusions, not buried as ceremonial text. Release negative findings when they constrain a promising direction: discovering that bridge transfer costs erase neural-handoff savings is useful systems knowledge.

<a id="t-80-08"></a>
## arXiv

arXiv is a public preprint repository, not peer review. A posting establishes a dated, citable manuscript and can accelerate feedback. Check category, endorsement, license, anonymization policy of intended venues, and artifact redaction before submission. Version updates transparently; do not imply that a preprint has conference acceptance.

<a id="t-80-09"></a>
## Workshops

Workshops often welcome emerging ideas, focused communities, and preliminary results. Standards and archival status vary. They are useful for refining a research program, especially when the contribution is a careful negative result or benchmark. Read the exact call, review model, page limit, proceedings policy, and dual-submission rule.

<a id="t-80-10"></a>
## Conferences

A conference submission targets a community’s contribution and evidence norms. Choose venue from the work, rather than reshaping claims after results to chase prestige. Check current deadlines, formatting, anonymity, ethics review, artifact tracks, and concurrent-submission rules on the official site. Acceptance is a selective review outcome, not proof that every claim is correct.

<a id="t-80-11"></a>
## Peer review

Review tests novelty, validity, clarity, significance, and reproducibility through fallible human judgement. Respond to critiques with evidence and precise revisions. Separate fixable presentation gaps from experiments that change the conclusion. As a reviewer, disclose conflicts, protect confidentiality, and avoid demanding citations for self-promotion. Open reviews and rebuttals can improve transparency but do not remove bias or variance.

<a id="t-80-12"></a>
## Finding unanswered questions

Unanswered questions appear where assumptions remain untested, methods fail on a slice, systems costs invalidate an algorithmic gain, or two literatures use different abstractions. Keep a discrepancy log while reproducing work. Ask which result would change a design decision, then seek the smallest decisive experiment. “Nobody used this exact acronym” is not novelty. A useful question has plausible value, measurable outcomes, feasible resources, and a result worth knowing even when negative.

## Claim-evidence table

| Claim | Required evidence | Common overclaim |
|---|---|---|
| Higher quality | Matched data/budget, strong baselines, uncertainty | Best single seed |
| Faster inference | End-to-end workload at matched quality | Kernel microbenchmark only |
| Lower memory | Measured peak plus accounting | Nominal datatype ratio |
| Causal mechanism | Controlled interventions and specificity | Probe or attention plot |
| General method | Multiple models, tasks, and shifts | One checkpoint and dataset |
| Novel research | Current prior-art search | New label for known method |

## Four perspectives

- **Follow the Token:** publish prompts, tokenization, context lengths, truncation, decoding, and scoring so evaluation inputs are reconstructible.
- **Follow the Gradient:** disclose seeds, training curves, selection rules, failed runs, and compute spent on tuning each method.
- **Follow the Byte:** reconcile theoretical memory/FLOPs with profiler counters, transfers, synchronization, and wall-clock behavior.
- **Follow the Request:** preserve the full request trace and configuration needed to reproduce both quality and service-level claims.

## Lab and exit check

Produce a paper-sized evidence package: claim-evidence table, ablation grid, paired uncertainty analysis, full resource profile, limitations, and reproducibility manifest. Write one paragraph that the data supports and one stronger paragraph it does not support. Tag every source as peer-reviewed paper, preprint, technical report, documentation, or code artifact. The project is ready for submission only when a clean environment can regenerate the main table.

Before release, trace every abstract and conclusion claim to a result cell and every result cell to a command, configuration, raw artifact, and analysis step. Any broken link becomes either a repaired artifact or a narrower claim.

## References

- Dodge et al., [Show Your Work: Improved Reporting of Experimental Results](https://aclanthology.org/D19-1224/), EMNLP-IJCNLP 2019.
- Dror et al., [The Hitchhiker’s Guide to Testing Statistical Significance in NLP](https://aclanthology.org/P18-1128/), ACL 2018.
- Agarwal et al., [Deep Reinforcement Learning at the Edge of the Statistical Precipice](https://proceedings.neurips.cc/paper/2021/hash/f514cec81cb148559cf475e7426eed5e-Abstract.html), NeurIPS 2021.
- Wasserstein, Schirm, and Lazar, [Moving to a World Beyond “p < 0.05”](https://doi.org/10.1080/00031305.2019.1583913), The American Statistician 2019.
- [arXiv submission help](https://info.arxiv.org/help/submit/index.html), accessed 2026-09-19.
- [NeurIPS Paper Checklist](https://neurips.cc/public/guides/PaperChecklist), accessed 2026-09-19.
