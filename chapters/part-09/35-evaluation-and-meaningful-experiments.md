# 35. Evaluation and Meaningful Experiments

Status: **Drafted.**

Part 9: Data, Scaling and Evaluation

## Learning outcome

Report a paired baseline comparison with defined metrics, controlled inference, slice analysis, and uncertainty.

## Prerequisites

CH-28, CH-33, and CH-34.

<a id="t-35-01"></a>
## Evaluation

Evaluation estimates behavior under a stated distribution and protocol. Begin with the decision the result supports. Model selection needs sensitivity; a release gate needs thresholds tied to risk; research needs a falsifiable hypothesis.

Pin checkpoint, tokenizer, prompt template, decoding settings, tool environment, dataset revision, scoring code, and hardware/software versions when measuring performance. Report quality, latency, throughput, memory, reliability, and relevant safety properties. A single average hides regressions.

<a id="t-35-02"></a>
## Perplexity

For $M$ evaluated tokens with average negative log-likelihood

$$L=-\frac{1}{M}\sum_{t=1}^{M}\log p(x_t\mid x_{<t}),$$

perplexity is $\operatorname{PPL}=e^L$. If $L=2$, perplexity is about 7.39. It is the geometric mean inverse probability assigned to the observed next token. Compare it only under the same tokenizer, token rules, and corpus. Lower perplexity can coexist with worse instruction following.

<a id="t-35-03"></a>
## Downstream tasks

Task evaluations test code, retrieval, summarization, or domain QA. Exact match fits objective short answers, not every semantic task. Execute code against hidden tests; separate retrieval recall from answer generation; check summary factuality.

Choose slices before seeing results: language, difficulty, context length, domain, and request type. Macro averaging gives slices equal weight; micro averaging weights examples. Report which one you use.

<a id="t-35-04"></a>
## Reasoning benchmarks

Reasoning benchmarks mix reasoning, knowledge, parsing, and format compliance. Verifiable final answers are useful, but generated rationales do not prove hidden computation followed that prose. Test alternate forms, distractors, and out-of-distribution compositions. Hold inference budget fixed: 64 samples versus one sample compares different systems.

Benchmark saturation and exposure make claims time-sensitive. As of September 2026, check the exact benchmark and model revisions plus contamination evidence.

<a id="t-35-05"></a>
## Human evaluation

For contextual outputs, write a rubric with observable criteria, randomize order, blind model identity, and permit ties. Use multiple raters on a subset and report agreement. Pairwise comparison is easier than absolute scoring but remains vulnerable to position, verbosity, and style biases. Preference is not truth: raters can prefer confident errors, so add factual checks and domain experts.

<a id="t-35-06"></a>
## Experimental design

Write the hypothesis and primary metric first. Choose a baseline differing only in the mechanism studied. Hold data, training budget, inference settings, and scoring constant. Run multiple seeds when variance can change the result. Use paired comparisons on identical items. Record attempted variants; selecting the best among many and calling it one test is multiple-comparison bias.

<a id="t-35-07"></a>
## Uncertainty introduction

A point estimate without uncertainty invites false precision. For accuracy on $n$ independent items, rough standard error is $\sqrt{\hat p(1-\hat p)/n}$. For paired systems, bootstrap items and recompute the difference; cluster-bootstrap when examples share a repository or conversation.

If A scores 73% and B 74% on 200 items, the gap may be noise. Report an interval for $B-A$. Statistical significance also need not imply practical value; predefine the smallest useful effect.

## Four recurring perspectives

- **Follow the Token:** scoring must identify conditioned tokens and tokens included in loss.
- **Follow the Gradient:** evaluation disables gradients, but using tests to choose updates transfers information into selection.
- **Follow the Byte:** retained logits dwarf scalar metrics; stream statistics unless diagnostics require them.
- **Follow the Request:** include prompts, tools, retries, queueing, and stop conditions when evaluating the system.

## Lab and exit check

Compare two fixed models on 300 examples. Pin decoding, report paired accuracy difference with a bootstrap 95% interval, break results into predetermined slices, inspect disagreements, and measure latency with warmups. State one supported conclusion and one unsupported conclusion.

## Exercises

1. Compute perplexity for average NLL 1.5 nats. **Check:** $e^{1.5}\approx4.48$.
2. Model A and B are evaluated on the same 500 prompts. Explain why bootstrapping paired item-level differences is preferable to treating their aggregate scores as independent. **Check:** pairing retains covariance from shared item difficulty and estimates uncertainty in the actual per-item comparison.

## References

- Liang et al., [Holistic Evaluation of Language Models](https://arxiv.org/abs/2211.09110), 2022.
- Dror et al., [Testing Statistical Significance in NLP](https://aclanthology.org/P18-1128/), 2018.
- Mitchell et al., [Model Cards for Model Reporting](https://arxiv.org/abs/1810.03993), 2018.
