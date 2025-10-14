# 12. Initialization and Training Stability

Status: **Draft — not yet independently reviewed.**

A valid training program can still fail because signals shrink, explode, overflow, or change too abruptly. Stability is observed through measurements, not inferred from the absence of an exception.

<a id="t-12-01"></a>
## Initialization

If units in the same layer start with identical incoming and outgoing parameters, the architecture and data treat them symmetrically: they receive identical gradients and remain redundant. Random weight initialization breaks that symmetry, while its scale aims to preserve activation and gradient variance. Xavier-style scaling suits roughly symmetric activations; He scaling uses weight variance near $2/fan_{in}$ for ReLU. Biases may still be initialized identically because randomized weights already distinguish the units. These rules are approximations based on independence and distribution assumptions, not universal guarantees.

<a id="t-12-02"></a>
## Gradient norms

The global L2 norm is $\|g\|_2=\sqrt{\sum_i g_i^2}$. Log global and per-layer norms alongside parameter norms and update-to-weight ratios. A single global number can hide one broken layer; per-layer traces reveal where failure begins.

<a id="t-12-03"></a>
## Clipping

Global norm clipping with threshold $c$ rescales $g\leftarrow g\min(1,c/\|g\|_2)$. For $g=[3,4]$ and $c=2$, the norm falls from 5 to 2 and the gradient becomes $[1.2,1.6]$. Clipping limits a damaging step; chronic clipping usually signals a deeper problem such as scale, data, precision, or learning rate.

<a id="t-12-04"></a>
## Warmup

Warmup raises the learning rate gradually during early steps while activations and optimizer moments are poorly calibrated. Linear warmup to $\eta_{max}$ over $N$ optimizer steps uses $\eta_t=\eta_{max}t/N$. Count optimizer steps consistently when gradient accumulation is active.

<a id="t-12-05"></a>
## Vanishing gradients

Backprop multiplies local Jacobians. Repeated factors below one can shrink sensitivity exponentially, leaving early layers nearly unchanged. Saturating sigmoid or tanh units amplify this risk. Residual connections, normalization, suitable initialization, and gated recurrence create shorter or better-conditioned paths.

<a id="t-12-06"></a>
## Exploding gradients

Repeated factors above one can create enormous norms, overflow, NaNs, and destructive updates. Check the first nonfinite tensor rather than only the eventual loss. Lowering the learning rate cannot repair an overflow that already occurred in the forward pass.

<a id="t-12-07"></a>
## Stability diagnostics

Track loss, learning rate, gradient norms before clipping, clipping fraction, activation mean/variance, parameter norms, update ratios, nonfinite counts, and throughput. Reproduce with a fixed small batch; overfit that batch; then add scale and mixed precision one change at a time. Data corruption can mimic optimizer instability, so inspect tokens and targets too.

## Four perspectives

**Follow the Token:** malformed or extreme inputs can poison activation statistics. **Follow the Gradient:** identify the earliest layer where norms collapse or spike. **Follow the Byte:** lower precision narrows numerical range and loss scaling changes how gradients occupy it. **Follow the Request:** the training loop should fail fast on nonfinite values and checkpoint enough state for reproduction.

## Exit check

Given per-layer norms `[0.9, 0.8, 0.02, 0.0001]`, propose a diagnostic sequence without claiming the cause from norms alone. Calculate the clipped version of `[6,8]` at threshold 5. Explain why increasing epsilon may mask symptoms while altering optimization.

## References

- Glorot and Bengio, [Understanding the difficulty of training deep feedforward neural networks](https://proceedings.mlr.press/v9/glorot10a.html), 2010.
- He et al., [Delving Deep into Rectifiers](https://arxiv.org/abs/1502.01852), 2015.
- [PyTorch gradient clipping](https://docs.pytorch.org/docs/stable/generated/torch.nn.utils.clip_grad_norm_.html). Accessed 2026-09-19.
