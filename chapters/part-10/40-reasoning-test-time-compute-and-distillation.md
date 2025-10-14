# 40. Reasoning, Test-Time Compute and Distillation

Status: **Drafted.**

Part 10: Post-Training and Reasoning

## Learning outcome

Compare sampling and search budgets at fixed cost, explain verifiable-reward training, and evaluate a distilled student without anthropomorphic claims.

## Prerequisites

CH-35 and CH-37 through CH-39.

<a id="t-40-01"></a>
## RL with verifiable rewards

Some tasks provide an external checker: unit tests, a symbolic answer, proof verifier, or simulator outcome. Reinforcement learning with verifiable rewards (RLVR) generates candidate trajectories, computes a reproducible reward, and increases probability of successful behavior. It avoids some subjective reward-model errors, but correctness of the checker becomes the specification.

Sparse success rewards give weak credit assignment. Curriculum design, multiple samples, outcome baselines, and process signals can help. A model may exploit bugs, formatting shortcuts, or weak tests, so hold out checkers and adversarial cases. Research moved quickly through 2024–2026; implementation claims here should always name the paper, model, and revision date.

<a id="t-40-02"></a>
## Reasoning models

“Reasoning model” is a behavioral label for systems trained or configured to spend more computation on multi-step tasks. It does not establish consciousness, symbolic internals, or faithful introspection. Relevant mechanisms include curated derivations, RLVR, search, self-consistency, verifiers, and longer generated scratchpads.

Measure final correctness, robustness to perturbation, compute used, and failure modes. Long output is not automatically good reasoning. Models can produce fluent rationalizations after arriving at an answer through other internal computation.

<a id="t-40-03"></a>
## Why generation can produce reasoning-like behavior

Autoregressive generation turns one difficult mapping into a sequence of conditional steps. Each emitted token becomes additional context, functioning as writable external state. Training data contains algorithms, worked examples, arguments, and code, so next-token learning can acquire patterns that decompose problems. Attention and nonlinear layers transform internal representations at every step.

This explanation needs no claim that the model “thinks like a person.” The visible chain can support computation, but it can also be redundant, copied, or unfaithful. Causal tests—forcing intermediate values, perturbing steps, or using hidden scratchpads—are stronger than reading prose as a trace of internal causation.

<a id="t-40-04"></a>
## Test-time compute

Inference can spend extra compute through longer trajectories, multiple samples, tree search, iterative revision, tools, or verifier ranking. Compare systems at fixed FLOPs, latency, energy, or monetary cost. Pass@k increases the chance that at least one of $k$ samples succeeds; it does not solve selection unless an oracle or verifier identifies the answer.

If independent samples succeed with probability $p$, oracle pass@k is $1-(1-p)^k$. With $p=0.3$ and $k=4$, it is about 0.760, but independence is usually false and a real selector is imperfect. Parallel sampling improves wall time only when hardware capacity exists.

<a id="t-40-05"></a>
## Distillation

Distillation trains a student from teacher outputs, probabilities, features, or selected trajectories. With logits, a temperature-softened loss can match distributions. Let $\tau>0$ be the distillation temperature and $p_\tau=\operatorname{softmax}(z/\tau)$:

$$\mathcal L_{KD}=\tau^2\,D_{KL}(p_\tau^{\mathrm{teacher}}\|p_\tau^{\mathrm{student}}).$$

The $\tau^2$ factor is the conventional compensation for the gradient-scale change caused by softening; implementations may combine this term with hard-label cross-entropy using an explicit mixing coefficient.

Sequence distillation instead trains on teacher-generated text. Reasoning distillation may select verified trajectories and then apply SFT or preference learning. It transfers demonstrated behavior, bounded by student capacity and data coverage; it does not copy an internal algorithm wholesale.

Evaluate the student against ground truth, not only teacher agreement. Track compression, latency, and calibration alongside accuracy. A teacher's systematic errors can be amplified by large synthetic datasets.

<a id="t-40-06"></a>
## Verifier limits

A verifier can rank outputs only on properties it observes. Outcome verifiers miss invalid intermediate logic that happens to land on the answer. Learned process verifiers inherit annotation and distribution errors. Executable tests are incomplete specifications. Repeated selection against one verifier creates pressure to exploit it.

Use independent tests, hidden cases, verifier ensembles where justified, and periodic human audits. Report verifier false-positive and false-negative rates. When comparing search methods, account for verifier compute and selection bias.

## Four recurring perspectives

- **Follow the Token:** generated intermediate tokens become new context and may act as an external work tape.
- **Follow the Gradient:** RLVR reinforces verified sequences; distillation moves student probabilities toward teacher-derived targets.
- **Follow the Byte:** longer contexts and multiple candidates multiply KV-cache and activation traffic.
- **Follow the Request:** a scheduler must budget samples, tools, verifier calls, deadlines, and stopping rules.

## Lab and exit check

Run one task under equal total generation-token budgets using a single long sample, four shorter samples with majority vote, and candidates ranked by a checker. Report correctness, latency, tokens, and selection errors. Distill verified examples into a smaller model and compare it with equal-data SFT on human answers.

## Exercises

1. Under the independence assumption, compute oracle pass@8 when single-sample success is $p=0.2$. **Check:** $1-0.8^8\approx0.832$; a deployable selector generally achieves less.
2. A verifier accepts 90 correct and 15 incorrect candidates and rejects 10 correct and 85 incorrect candidates. Compute its false-positive and false-negative rates. **Check:** FPR $=15/100=15\%$ and FNR $=10/100=10\%$.

## References

- Wang et al., [Self-Consistency Improves Chain of Thought Reasoning](https://arxiv.org/abs/2203.11171), 2022.
- Hinton et al., [Distilling the Knowledge in a Neural Network](https://arxiv.org/abs/1503.02531), 2015.
- Cobbe et al., [Training Verifiers to Solve Math Word Problems](https://arxiv.org/abs/2110.14168), 2021.
- Gao et al., [On Designing Effective RL Reward at Training Time for LLM Reasoning](https://arxiv.org/abs/2410.15115), 2024.
