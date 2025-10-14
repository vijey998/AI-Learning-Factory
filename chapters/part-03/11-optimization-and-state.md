# 11. Optimization and State

Status: **Draft — not yet independently reviewed.**

Backpropagation supplies a direction. An optimizer decides how parameter state changes over time.

<a id="t-11-01"></a>
## SGD

Plain stochastic gradient descent applies $\theta_{t+1}=\theta_t-\eta g_t$. If $\theta=3$, $g=4$, and $\eta=0.1$, the new value is $2.6$. “Stochastic” refers to estimating the full-data gradient from a sample or minibatch. A learning rate that is too small wastes steps; one that is too large can jump across a basin and diverge.

<a id="t-11-02"></a>
## Momentum

Momentum filters noisy gradients: $v_t=\beta v_{t-1}+g_t$ and $\theta_{t+1}=\theta_t-\eta v_t$ under one common convention. Definitions differ by scaling and sign, so compare equations rather than optimizer names. Momentum accelerates persistent directions but can overshoot when the useful direction changes.

<a id="t-11-03"></a>
## AdamW

Adam tracks exponential averages $m_t=\beta_1m_{t-1}+(1-\beta_1)g_t$ and $v_t=\beta_2v_{t-1}+(1-\beta_2)g_t^2$. Bias-corrected $\hat m_t$ and $\hat v_t$ compensate for zero initialization, and the adaptive update divides by $\sqrt{\hat v_t}+\epsilon$. AdamW then applies decoupled weight decay separately. Adaptive scaling helps coordinates with different gradient scales, but it does not remove schedule tuning.

<a id="t-11-04"></a>
## Optimizer states

SGD needs no persistent tensor beyond parameters unless momentum is enabled. Momentum adds one parameter-sized buffer. AdamW usually adds two, often stored in FP32 even when model weights use BF16. Training memory may also include parameters, gradients, master weights, activations, and communication buffers. “A 7B model needs 14 GB” describes BF16 weights only, not a training job.

<a id="t-11-05"></a>
## Learning-rate schedules

A schedule makes $\eta$ depend on step. Constant, step, cosine, and linear decay encode different assumptions. Cosine decay from peak $\eta_{max}$ to $\eta_{min}$ over progress $p\in[0,1]$ uses $\eta=\eta_{min}+\tfrac12(\eta_{max}-\eta_{min})(1+\cos \pi p)$. Schedulers must step at the intended unit—optimizer step, not every microbatch when using accumulation.

<a id="t-11-06"></a>
## Weight decay

Decoupled decay applies $\theta\leftarrow(1-\eta\lambda)\theta$ separately from the gradient update. L2 regularization adds $\lambda\theta$ to the gradient; the two coincide for plain SGD but generally differ for adaptive methods. Biases and normalization scales are often excluded by policy; the policy should be explicit.

## Four perspectives

**Follow the Token:** a batch produces the loss estimate that drives one update. **Follow the Gradient:** gradients are transient measurements; optimizer moments are persistent history. **Follow the Byte:** Adam's two FP32 moments can outweigh low-precision weights. **Follow the Request:** training systems coordinate accumulation, clipping, optimizer step, scheduler step, and zeroing in a strict order.

## Exit check

For two parameters in BF16 with FP32 gradients and Adam moments, write a byte formula and state whether master FP32 weights are assumed. Explain why `zero_grad` is necessary when a framework accumulates gradients. Compare coupled L2 and AdamW on one symbolic step.

## Ordering one training step

With gradient accumulation, divide or otherwise normalize the loss consistently across microbatches, accumulate gradients, unscale them if mixed precision is active, detect nonfinite values, clip if configured, call the optimizer, advance the schedule, and clear gradients. Changing this order changes behavior. Clipping scaled gradients uses the wrong threshold; advancing the schedule per microbatch shortens the schedule; clearing between microbatches defeats accumulation. A skipped optimizer step after overflow should also skip scheduler advancement under the usual step-based interpretation.

To compare optimizers, hold model, data order, token budget, schedule budget, precision, and evaluation fixed. Reporting only the lowest training loss rewards overfitting and extra compute. Optimizer choice is part of a full experimental configuration, including epsilon, betas, decay exclusions, batch size, and gradient normalization.

## References

- Kingma and Ba, [Adam](https://arxiv.org/abs/1412.6980), 2014.
- Loshchilov and Hutter, [Decoupled Weight Decay Regularization](https://arxiv.org/abs/1711.05101), 2017.
- [PyTorch optimizer documentation](https://docs.pytorch.org/docs/stable/optim.html). Accessed 2026-09-19.
