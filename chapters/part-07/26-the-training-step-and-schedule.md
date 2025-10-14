# 26. The Training Step and Schedule

Status: **Drafted — technical and editorial review pending.**

Part 7: Train the Thing

## Learning outcome

Show equivalence of accumulated and full-batch gradients under matched conditions.

## Prerequisites

CH-08, CH-11, CH-24, CH-25.

A training step is a state transition. Parameters, optimizer buffers, scheduler counters, and random-number generators may all change. Separating the phases makes bugs observable.

<a id="t-26-01"></a>
### Training forward pass

Coverage ID: `T-26-01`.

Given IDs and masks, the model produces logits $Z\in\mathbb{R}^{B\times T\times V}$. Training mode may activate dropout. Autograd records operations and saves selected tensors needed backward. Labels are data, not model inputs, even when a convenience API accepts them in the same call.

<a id="t-26-02"></a>
### Training loss

Coverage ID: `T-26-02`.

Flatten valid logits to `[N,V]` and labels to `[N]`, where $N$ is the number of supervised tokens. Cross-entropy should be computed with log-sum-exp stabilization. Track both mean loss and token count: averaging per microbatch and then averaging microbatches is biased when their valid-token counts differ.

<a id="t-26-03"></a>
### Training backward pass

Coverage ID: `T-26-03`.

`loss.backward()` accumulates gradients into parameter `.grad` buffers. It does not update parameters. Clear gradients intentionally—usually before the accumulation window—and inspect norms before the optimizer step. Retaining the graph without need grows memory; detaching the loss before backward removes the graph entirely.

<a id="t-26-04"></a>
### Optimizer state updates in memory

Coverage ID: `T-26-04`.

AdamW stores first and second moment tensors $m,v$ for each parameter $w$:

$$
m_t=\beta_1m_{t-1}+(1-\beta_1)g_t,
\quad v_t=\beta_2v_{t-1}+(1-\beta_2)g_t^2.
$$

After bias correction, the optimizer updates $w$, while decoupled weight decay applies separately. With FP32 parameters, gradients, $m$, and $v$, persistent training state can approach 16 bytes per parameter before mixed-precision copies or distributed sharding. `optimizer.step()` mutates parameters and buffers; `zero_grad()` releases or zeroes gradient storage.

<a id="t-26-05"></a>
### Learning rates

Coverage ID: `T-26-05`.

The learning rate controls update scale, not loss scale. Too large diverges; too small wastes compute or settles poorly. Schedules may be step-based or token-based. Record which, because variable batch sizes make those clocks disagree.

<a id="t-26-06"></a>
### Warmup

Coverage ID: `T-26-06`.

Warmup increases the learning rate from a small value over early steps or tokens. Early moment estimates and representations are poorly calibrated, making full-size updates risky. A linear warmup to $\eta_{\max}$ over $W$ steps is $\eta_s=\eta_{\max}(s+1)/W$ for $s<W$. Off-by-one errors can begin at zero or overshoot the intended peak.

<a id="t-26-07"></a>
### Gradient accumulation

Coverage ID: `T-26-07`.

To emulate one batch using $K$ equal-size microbatches, backpropagate `loss / K` for each, then step once. More generally, accumulate **summed token losses** and divide by total valid tokens. Exact equivalence requires the same examples, stochastic masks, batch-dependent operations, precision, and reduction order. Dropout and floating-point associativity can prevent bitwise equality even when the estimator is correct.

<a id="t-26-08"></a>
### Gradient clipping

Coverage ID: `T-26-08`.

Global-norm clipping rescales all gradients when

$$
\|g\|_2=\sqrt{\sum_p\|g_p\|_2^2}>c,
\qquad g\leftarrow g\frac{c}{\|g\|_2+\epsilon}.
$$

Clip after unscaling mixed-precision gradients and after completing accumulation, before `optimizer.step()`. Frequent clipping signals an unstable regime; it is a guardrail, not a cure.

## Canonical step order

```text
zero gradients → K × (forward → token-summed loss → scaled backward)
→ unscale → inspect/clip → optimizer step → scheduler step → log
```

## Four recurring perspectives

- **Follow the Token:** valid target tokens determine the denominator and effective batch.
- **Follow the Gradient:** backward accumulates; clipping transforms; the optimizer consumes and clears nothing automatically.
- **Follow the Byte:** gradients and Adam moments rival or exceed weight memory.
- **Follow the Request:** training schedules optimize corpus throughput; inference has no optimizer state or backward graph.

## Lab and exit check

Compare one batch of eight examples against four microbatches of two using dropout disabled. Weight both by valid token counts. Assert parameter gradients are numerically close, then enable dropout and explain any difference. Print parameter, gradient, and optimizer-buffer bytes.

## Exercises

1. Two microbatches contain 80 and 20 valid tokens with mean losses 2.0 and 4.0. Compute the correct combined mean. **Check:** $(80\cdot2+20\cdot4)/100=2.4$, not 3.0.
2. A gradient has norm 12 and the clipping threshold is 3. Ignoring $\epsilon$, compute the multiplier. **Check:** $3/12=0.25$.

## References

- Kingma and Ba, [Adam: A Method for Stochastic Optimization](https://arxiv.org/abs/1412.6980), 2014.
- Loshchilov and Hutter, [Decoupled Weight Decay Regularization](https://arxiv.org/abs/1711.05101), 2017.
- Pascanu, Mikolov, and Bengio, [On the Difficulty of Training Recurrent Neural Networks](https://proceedings.mlr.press/v28/pascanu13.html), 2013.
