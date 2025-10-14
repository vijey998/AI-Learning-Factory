# 36. Scaling Laws

Status: **Drafted.**

Part 9: Data, Scaling and Evaluation

## Learning outcome

Fit a small scaling experiment, allocate a compute budget, and disclose extrapolation uncertainty.

## Prerequisites

CH-34 and CH-35.

<a id="t-36-01"></a>
## Scaling laws

Scaling laws are empirical regularities connecting loss to model size, data, and compute. A common form is

$$L(N)=L_\infty + A N^{-\alpha}.$$

Taking logs linearizes the reducible part only if $L_\infty$ is known. Fit the original objective or jointly estimate the floor; subtracting an arbitrary floor can manufacture a straight line. Scaling laws summarize a measured regime, not a physical guarantee.

Kaplan et al. (2020) found smooth power laws over their range. Hoffmann et al. (2022) revisited compute-optimal allocation with more runs and concluded model size and token count should grow roughly together under their assumptions. Different recommendations reflect data, fits, and optimization; a “Chinchilla ratio” is not universal.

<a id="t-36-02"></a>
## Parameters vs data vs compute

More parameters increase capacity and per-token cost. More unique appropriate data supplies evidence. More compute can buy either. Under fixed compute, an oversized model trained on too few tokens may be undertrained; a small model may see many epochs but hit capacity.

For dense Transformer planning, $C\approx6ND$ FLOPs is useful. With $N=1$B and $D=20$B, this gives $1.2\times10^{20}$ FLOPs. It excludes system inefficiency. Wall time is $C/(uP)$, where $P$ is peak FLOP/s and $u$ achieved utilization; measure $u$.

<a id="t-36-03"></a>
## Compute budgets

Budget pilot runs, search, failures, evaluation, checkpointing, and inference after training. A training-optimal model can be deployment-poor if latency or memory is unacceptable. Use proxy runs to calibrate tokens/second, utilization, loss curves, and input bottlenecks. Maintain rerun reserve and predeclare stopping limits.

<a id="t-36-04"></a>
## Scaling fits

Train a grid varying $N$ and $D$ enough to identify both effects. Keep data, tokenizer, optimizer quality, and evaluation consistent. Fit held-out loss, inspect residuals, and bootstrap across runs. Report estimates, intervals, observed range, and fit error.

For sizes 10M, 30M, 100M, and 300M at several budgets, changing architecture and data only for the largest model destroys the scale-only comparison. Curved residuals indicate misspecification.

<a id="t-36-05"></a>
## Extrapolation limits

Predictions beyond the measured range compound uncertainty. Data-regime changes, architecture transitions, optimizer instability, precision limits, and capability thresholds can break a fit. Show observations and extrapolations separately, offer plausible ranges, and refit after each step. As of September 2026, results from one architecture and corpus remain evidence about that setup rather than a timeless recipe.

## Four recurring perspectives

- **Follow the Token:** $D$ counts processed tokens, including repeats; composition can change while the scalar stays fixed.
- **Follow the Gradient:** batch size and scale change optimization noise; a poor optimizer can resemble a scaling limit.
- **Follow the Byte:** parameters, optimizer states, activations, and checkpoints constrain feasible scale.
- **Follow the Request:** serving volume can make a smaller, more-trained model economically superior.

## Lab and exit check

Train three sizes at three budgets on one corpus. Fit a power law, visualize residuals, bootstrap parameters, and predict a held-out run. Report prediction error and interval. Add an inference-cost term and see whether model selection changes.

## Exercises

1. Estimate training FLOPs for $N=3\times10^9$ parameters and $D=60\times10^9$ tokens using $6ND$. **Check:** $1.08\times10^{21}$ FLOPs.
2. At sustained throughput $uP=2\times10^{17}$ FLOP/s, convert that estimate to idealized wall time. **Check:** 5,400 seconds, or 1.5 hours; this deliberately simplified result excludes failures, evaluation, and pipeline stalls.

## References

- Kaplan et al., [Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361), 2020.
- Hoffmann et al., [Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556), 2022.
- Bian et al., [Scaling Inference-Efficient Language Models](https://arxiv.org/abs/2501.18107), 2025.
