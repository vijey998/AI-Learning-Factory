# 79. Research Design and Reproduction

Status: **Draft — not yet independently reviewed.**

Research begins when a plausible idea becomes a question that could lose. A proposal that counts every outcome as success is a product pitch, not an experiment.

<a id="t-79-01"></a>
## Forming research questions

A useful question specifies population, intervention, comparison, outcome, and constraint. Replace “Can neural handoff work?” with: “On datasets X and Y, can a rank-$r$ bridge from model A layer $i$ to model B layer $j$ match B within one accuracy point while reducing p95 latency by at least 20% on hardware H?” Name a negative result in advance. Separate mechanism questions (“why?”), empirical questions (“does it?”), and systems questions (“at what measured cost?”).

<a id="t-79-02"></a>
## Literature search

Search by mechanism, synonyms, older terminology, and neighboring fields. Use scholarly indexes and citation graphs, then follow references backward and citing papers forward. Record queries, dates, databases, inclusion criteria, and exclusions. Search recent conference proceedings and preprints because terminology shifts quickly, while treating non-peer-reviewed work at its actual evidence level. Stop when new searches mostly repeat known clusters, not when the first supportive paper appears.

<a id="t-79-03"></a>
## Prior-art search

Prior-art search asks whether the claimed contribution already exists, including under another name or outside LLM research. Search papers, patents, code, technical reports, theses, and product documentation. Decompose the idea into claims: architecture, objective, training method, deployment pattern, and demonstrated result. Novel combinations can still be obvious combinations; novelty is a legal and scholarly question requiring current expert review. A literature review in this book cannot certify patentability.

<a id="t-79-04"></a>
## Reading papers critically

Read the abstract for the claimed result, methods for what was actually done, tables and figures for evidence, and appendices for missing details. Build a claim-evidence table: exact claim, experiment, baseline, metric, uncertainty, and threat. Check data leakage, hyperparameter fairness, compute mismatch, cherry-picked tasks, and whether the metric measures the stated goal. Distinguish comparisons made in one controlled implementation from numbers copied across papers.

<a id="t-79-05"></a>
## Designing a research experiment

Change the smallest set of variables that tests the hypothesis. Define independent variables, outcomes, controls, unit of analysis, randomization, stopping rule, and analysis before looking at results. Pilot to debug instrumentation, then freeze the protocol. Avoid tuning the proposed method on the test set while leaving baselines at defaults. If compute limits the sweep, state that constraint and choose a fair allocation.

Plan sample size from the smallest effect that would change the decision, expected variance, and intended analysis—not from a conventional round number. If formal power analysis is infeasible, simulate plausible effect and variance ranges and publish the sensitivity. Sequentially checking results and stopping when $p<0.05$ inflates false positives unless the stopping rule and analysis explicitly support sequential testing.

<a id="t-79-06"></a>
## Choosing baselines

Include a trivial baseline, current standard, strongest feasible competitor, and an oracle or upper bound where useful. For efficiency research, compare with smaller models, quantization, caching, batching, and hardware-aware tuning—not only an intentionally naive implementation. Match quality, data, compute budget, and optimization effort. A baseline that receives less tuning is a weak foundation for a superiority claim.

<a id="t-79-07"></a>
## Benchmark selection

Select benchmarks that exercise the claimed mechanism and represent deployment conditions. Report contamination risk, licenses, languages, domains, prompt templates, scoring, and known limitations. One aggregate score can hide regressions; define slices and worst-case metrics. Add task-specific cases that can falsify the mechanism, such as long-range references for KV eviction. Keep a final untouched test set.

<a id="t-79-08"></a>
## Reproducing papers

Begin with the authors’ exact commit, environment, data version, checkpoint, and command when available. Reproduce one reported table cell before extending the method. Record deviations and classify outcomes: exact reproduction, approximate reproduction within uncertainty, failure due to missing artifacts, or contradiction under matched conditions. Contacting authors can resolve ambiguity, but undocumented private knowledge is itself a reproducibility limitation.

<a id="t-79-09"></a>
## Reproducibility

A reproducibility package includes code, dependency lock, seeds, hardware and software versions, data acquisition and checksums, preprocessing, configurations, commands, raw results, and analysis scripts. Deterministic kernels may reduce variance but can alter performance. Containers capture user space, not every driver, firmware, accelerator, or external API dependency. Preserve intermediate artifacts and a machine-readable manifest.

Use terminology explicitly. Following the ACM artifact vocabulary, repeatability concerns the same team and setup, reproducibility involves a different team using the authors' artifacts, and replicability seeks the result independently. Communities use these words differently, so define the adopted convention instead of assuming it.

<a id="t-79-10"></a>
## Scientific vs engineering claims

A scientific claim concerns general relationships, such as a routing signal predicting task difficulty across specified distributions. An engineering claim concerns an artifact under conditions, such as 18% lower p95 latency on an H100 with a named serving stack. Both matter, but evidence does not transfer automatically. A faster kernel on one shape is not a general architectural law; a statistically reliable accuracy gain may be commercially irrelevant if it doubles cost.

## Worked preregistration

For KV eviction, predeclare contexts, token budgets, policies, quality metrics, three seeds, hardware, warmup, and maximum tuning trials. Primary outcome might be retrieval accuracy at a fixed 2 GB cache; secondary outcomes are p95 latency and perplexity. The negative criterion is failure to match the recent-window baseline’s worst-slice accuracy. Publish the protocol before inspecting the final test results, then label exploratory analyses separately.

## Four perspectives

- **Follow the Token:** datasets, tokenizers, templates, truncation, and scoring must be versioned because they define the experimental input.
- **Follow the Gradient:** training seeds, schedules, data order, checkpoint selection, and tuning budget can dominate apparent improvements.
- **Follow the Byte:** resource claims require measured memory, transfers, artifacts, and hardware counters under a reproducible workload.
- **Follow the Request:** an experiment is a replayable request pipeline with configuration, trace, outcome, and immutable provenance.

## Lab and exit check

Select one paper relevant to Chapter 77 or 78. Produce a search log, prior-art matrix, claim-evidence table, reproduction plan, and preregistration with a negative-result criterion. Reproduce one central result or document precisely why it cannot be reproduced. A repository that runs only on the author’s machine is an unresolved result.

## References

- Pineau et al., [Improving Reproducibility in Machine Learning Research](https://jmlr.org/papers/v22/20-303.html), JMLR 2021.
- Gundersen and Kjensmo, [State of the Art: Reproducibility in Artificial Intelligence](https://ojs.aaai.org/index.php/AAAI/article/view/11503), AAAI 2018.
- [NeurIPS Paper Checklist](https://neurips.cc/public/guides/PaperChecklist), current author guidance, accessed 2026-09-19.
- [ACM Artifact Review and Badging](https://www.acm.org/publications/policies/artifact-review-and-badging-current), accessed 2026-09-19.
- National Academies, [Reproducibility and Replicability in Science](https://doi.org/10.17226/25303), 2019.
