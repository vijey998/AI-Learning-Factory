# 27. Mixed Precision and Checkpoint Anatomy

Status: **Drafted — technical and editorial review pending.**

Part 7: Train the Thing

## Learning outcome

Resume a run with matching next-step behavior and explain memory tradeoffs.

## Prerequisites

CH-26.

Training must fit in memory and survive interruption. Mixed precision reduces cost; activation checkpointing trades compute for memory; durable checkpoints preserve the entire state transition, not merely model weights.

<a id="t-27-01"></a>
### Mixed-precision training

Coverage ID: `T-27-01`.

Mixed precision uses lower-precision formats for selected matrix operations and activations while retaining sensitive reductions or master state in higher precision. FP16 has limited exponent range; BF16 retains FP32-like exponent width with fewer fraction bits. The exact autocast policy is framework and hardware dependent, so record versions and device. “BF16 training” does not mean every tensor is BF16.

<a id="t-27-02"></a>
### Loss scaling

Coverage ID: `T-27-02`.

Small FP16 gradients can underflow to zero. Multiply loss by scale $S$, backpropagate scaled gradients, then divide gradients by $S$ before clipping and stepping. Dynamic scaling lowers $S$ when Inf/NaN gradients occur and may raise it after stable steps. BF16 often needs no loss scaling due to its wider exponent range. Clipping before unscale uses the wrong norm.

<a id="t-27-03"></a>
### Activation checkpointing

Coverage ID: `T-27-03`.

Ordinary backward stores intermediates from each layer. Activation checkpointing stores selected boundary states and recomputes missing forward operations during backward. Memory falls; FLOPs and wall time rise. Random operations require preserved RNG behavior, otherwise recomputation uses different dropout masks and yields an invalid gradient. This mechanism is unrelated to saving a durable checkpoint despite the shared name.

<a id="t-27-04"></a>
### Checkpoints

Coverage ID: `T-27-04`.

A resumable training checkpoint is a versioned bundle written atomically. Save to a temporary path, flush, then rename; incomplete writes should never appear valid. Include step/token counters, data position or sampler state, software/config identifiers, and integrity metadata in addition to the components below.

<a id="t-27-05"></a>
### Weights

Coverage ID: `T-27-05`.

Model parameters reproduce the learned function in evaluation mode when paired with the architecture. They do not reproduce the next training step alone. Shared weights should remain shared after loading, and dtype conversion must be explicit.

<a id="t-27-06"></a>
### Config

Coverage ID: `T-27-06`.

Store all shape- and behavior-defining fields: (V,C,D,L,H,M), normalization, positions, biases, dropout, tying, and special-token IDs. Code defaults drift. A checkpoint without its config is an archaeological artifact.

<a id="t-27-07"></a>
### Tokenizer state

Coverage ID: `T-27-07`.

Save vocabulary, merge/model rules, normalization and pre-tokenization rules, added tokens, and special-token mappings. The same text under a different tokenizer produces different IDs; matching vocabulary size is insufficient.

<a id="t-27-08"></a>
### Optimizer state

Coverage ID: `T-27-08`.

Adam moments and per-parameter step counters determine the next update. Omitting them restarts optimization dynamics even if weights match. Parameter ordering or names must map buffers to the correct tensors.

<a id="t-27-09"></a>
### Scheduler state

Coverage ID: `T-27-09`.

Save the scheduler’s current step/token counter, phase, and any best-metric state. Reconstructing from filename can be wrong after skipped steps, accumulation changes, or partial epochs.

<a id="t-27-10"></a>
### RNG state

Coverage ID: `T-27-10`.

Save Python, NumPy, CPU framework, and each accelerator RNG state as applicable. Also preserve distributed sampler epoch/state. Exact replay can still be prevented by nondeterministic kernels or different hardware, but missing RNG state guarantees dropout and sampling divergence.

## Memory example

One billion BF16 parameters occupy about 2 GB (decimal). FP32 master weights add 4 GB, FP32 gradients 4 GB, and two FP32 Adam moments 8 GB: roughly 18 GB before activations and allocator overhead. Implementations and sharding strategies vary, so measure the actual process.

## Four recurring perspectives

- **Follow the Token:** autocast changes arithmetic representation, not token meaning or labels.
- **Follow the Gradient:** scaling protects small gradients; recomputation recreates the graph; optimizer buffers shape updates.
- **Follow the Byte:** low-precision activations save memory; optimizer state often dominates persistent training storage.
- **Follow the Request:** inference checkpoints may need only weights/config/tokenizer, while exact training resume needs the whole state bundle.

## Lab and exit check

Train two steps, save, run a third step and record loss and parameters. Reload after step two and repeat the third step. With deterministic settings, compare loss, sampled batch, dropout behavior, parameters, optimizer buffers, and scheduler count. List any platform limitation preventing exact equality.

## Exercises

1. A scaled backward pass uses $S=1024$ and produces a stored gradient value 51.2. What value should clipping inspect after unscale? **Check:** 0.05.
2. List the minimum additional state needed to reproduce the next AdamW step beyond model weights. **Check:** optimizer moments and counters, scheduler state, batch/sampler position, applicable RNG states, and the exact configuration/software behavior.

## References

- Micikevicius et al., [Mixed Precision Training](https://arxiv.org/abs/1710.03740), 2017.
- Chen et al., [Training Deep Nets with Sublinear Memory Cost](https://arxiv.org/abs/1604.06174), 2016.
- PyTorch reproducibility and automatic mixed precision documentation, version pinned for execution.
