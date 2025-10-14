# 28. Debugging and Training Our Tiny Model

Status: **Drafted — technical and editorial review pending.**

Part 7: Train the Thing

## Learning outcome

Overfit a tiny batch, then train with a held-out split and document failures.

## Prerequisites

CH-27.

Training combines data, masks, numerics, optimization, and mutable state. Debug it as a pipeline of falsifiable invariants rather than staring at one loss curve.

<a id="t-28-01"></a>
### Debugging training

Coverage ID: `T-28-01`.

Begin with the smallest deterministic case. Print decoded inputs and shifted labels. Assert IDs, shapes, masks, dtypes, devices, and finite values. Establish a random-loss baseline: with $V$ roughly uniform classes, cross-entropy begins near $\log V$. Overfit one tiny batch before scaling; if the model cannot memorize it, more data and GPUs only make the bug expensive.

Log valid tokens, learning rate, loss, gradient norm, parameter/update norm, tokens per second, and memory. Save the exact config and seed. Change one variable per experiment.

<a id="t-28-02"></a>
### NaNs

Coverage ID: `T-28-02`.

NaNs can originate in data, logits, normalization, softmax, loss, gradients, or optimizer state. Locate the **first** nonfinite tensor with hooks or anomaly detection. Frequent causes include excessive learning rate, FP16 overflow, division by tiny values, all-masked attention rows, and invalid labels. Once a NaN enters Adam moments, restoring finite weights alone may not recover the run.

<a id="t-28-03"></a>
### Exploding gradients

Coverage ID: `T-28-03`.

Plot global and per-layer gradient norms before clipping. A sudden rise can reflect bad batches, unstable residual scale, excessive learning rate, or incorrect loss normalization. Clipping avoids one destructive step but can conceal repeated instability. Compare update norm to parameter norm to learn whether nominal learning rate translates into extreme movement.

<a id="t-28-04"></a>
### Bad initialization

Coverage ID: `T-28-04`.

Initialization that is too large produces saturated logits and growing residuals; too small can make updates or signals negligible. Inspect activation mean/RMS and gradient RMS by depth on the first batch. Output/head and residual projection initialization conventions can be architecture-specific. Never assume a generic initializer reproduces a published model.

<a id="t-28-05"></a>
### Overfitting

Coverage ID: `T-28-05`.

Memorizing one batch is a debugging success. Memorizing the training split while held-out loss rises is a generalization failure. Track both under `eval()` with fixed data. Data leakage may make validation look artificially good; split before overlapping chunks and audit duplicates.

<a id="t-28-06"></a>
### Train a tiny language model

Coverage ID: `T-28-06`.

Use a small corpus with a documented train/validation split. Fit tokenizer only on allowed training data if the experiment requires strict isolation. First overfit one batch until loss falls sharply. Then reset from initialization, train on the full training split, evaluate at fixed token intervals, and save the best and latest checkpoints. Generate samples from a fixed prompt and fixed seed as a qualitative smoke test; samples do not replace held-out loss.

A minimal loop is:

```python
for step, batch in enumerate(loader):
    optimizer.zero_grad(set_to_none=True)
    logits = model(batch.ids)
    loss = token_cross_entropy(logits[:, :-1], batch.ids[:, 1:], batch.mask)
    loss.backward()
    grad_norm = clip_grad_norm_(model.parameters(), limit)
    optimizer.step(); scheduler.step()
```

## Failure ledger

Record symptom, first failing invariant, evidence, hypothesis, intervention, and outcome. “Lowered LR and it worked” is weaker than showing the first nonfinite tensor was an FP16 attention score and that a precision change eliminated it under the same batch.

## Four recurring perspectives

- **Follow the Token:** decode inputs and targets; many apparent model bugs are corrupt examples or shifts.
- **Follow the Gradient:** trace finiteness and scale from loss back through layers before the optimizer mutates state.
- **Follow the Byte:** leaks often come from retained graphs, saved activations, or unbounded logging—not model weights.
- **Follow the Request:** training correctness is tested with batches; generation tests causal execution and decoding as a user would observe it.

## Lab and exit check

Pass four gates: uniform-loss sanity, one-batch overfit, held-out evaluation, and checkpoint resume. Intentionally inject a shifted-label bug and an excessive learning rate; document how each appears in metrics. Report seeds, versions, dataset hash, and limits of reproducibility.

## Exercises

1. For vocabulary size 256, compute the uniform-prediction loss in nats. **Check:** $\log 256\approx5.545$.
2. Training loss falls while validation loss rises. Name two distinct hypotheses and one discriminating test for each. **Check:** examples include ordinary overfitting versus split leakage; regularization/data scaling tests the first, while cross-split duplicate auditing tests the second.

## References

- Goodfellow, Bengio, and Courville, [*Deep Learning*](https://www.deeplearningbook.org/), optimization chapters, 2016.
- PyTorch autograd anomaly detection and reproducibility documentation, version pinned for execution.
