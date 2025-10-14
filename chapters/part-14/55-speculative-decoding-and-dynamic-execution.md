# 55. Speculative Decoding and Dynamic Execution

Status: **Drafted**

## Spend less target-model time per accepted token

Autoregressive decode normally invokes the large target once per token. Dynamic methods try to accept several tokens per expensive step or avoid unneeded computation. Every speedup claim must include quality, acceptance, batching, and overhead.

<a id="t-55-01"></a>
## Speculative decoding

A cheaper process proposes gamma tokens. The target scores those positions in one verification pass. In exact sampling variants, an acceptance/rejection rule and correction distribution preserve the target distribution; greedy variants accept the matching prefix. Accepted tokens advance generation, then a target token resolves the first rejection or follows a fully accepted block.

Speed depends on accepted tokens per target pass, draft cost, verification efficiency, and batch effects. A high acceptance rate can still lose if the draft is slow or verification kernels are inefficient.

For an accounting example, suppose a verification pass advances by an average of 3.2 tokens and costs 8 ms, while drafting costs 3 ms per attempted block. The combined 11 ms / 3.2 = 3.44 ms per advanced token is faster than a 5 ms target-only baseline. If batching makes verification cost 14 ms, the same acceptance statistics yield 5.31 ms and lose. Accepted length is therefore an input to a latency calculation, not a speedup by itself.

<a id="t-55-02"></a>
## Draft-verifier design

Draft and target must share compatible tokenization and conditioning. Choose gamma by measuring: too small leaves parallelism unused; too large wastes rejected work. Track accepted length distribution by prompt type and output position, target passes, end-to-end TPOT, and exact-distribution tests—not only acceptance percentage.

<a id="t-55-03"></a>
## Speculative-model architectures

The proposer may be a smaller separate model, early-exit head, multiple-token prediction head, n-gram lookup, or tree of candidates. Self-speculative designs reuse part of the target but create cache/control complexity. Tree verification can test branches in parallel at greater temporary-memory cost. These are architectural choices beyond the generic decoding algorithm.

<a id="t-55-04"></a>
## Sparsity

Sparse execution skips known zero or inactive work. Unstructured zeros rarely speed a dense GPU kernel without compatible storage and kernels. Structured N:M sparsity, block sparsity, and MoE routing align work into executable units, but metadata, load imbalance, and hardware support determine realized gains.

<a id="t-55-05"></a>
## Pruning

Pruning creates sparsity by removing weights, heads, channels, layers, or experts using magnitude, sensitivity, or learned criteria. One-shot pruning is cheap but can damage quality; retraining may recover it. Report remaining parameters, actual executed operations and bytes, and downstream quality. A smaller checkpoint with dense-shaped kernels is not necessarily faster.

<a id="t-55-06"></a>
## Early exit

Early-exit models attach prediction heads before the final layer and stop when a confidence rule fires. Calibration is difficult: entropy or margin can look confident and still be wrong. Thresholds shift compute distributions and tail behavior. Evaluate per-domain worst cases and compare against a smaller dense model at equal quality and compute.

<a id="t-55-07"></a>
## Layer skipping

Layer skipping routes individual tokens or requests around blocks. Static removal yields a smaller model; dynamic skipping needs a router and variable execution. GPUs prefer regular batches, so divergent layer paths may erase theoretical savings unless requests are regrouped. Cache semantics also change if later layers expect missing states.

<a id="t-55-08"></a>
## CUDA Graph optimization

Dynamic decisions conflict with fixed graph topology. Practical systems capture common verification sizes, draft lengths, batch buckets, or routing patterns and fall back elsewhere. A huge graph cache raises warmup and memory. Include cache hit rate and compilation amortization when attributing a speedup to graph replay.

## Exactness, perspectives, and exit check

Test exact speculative sampling on a tiny vocabulary by enumerating or drawing enough samples to compare output frequencies with direct target sampling and confidence intervals. Include a case where the draft assigns zero probability to a token that the target can emit, exercising the correction path. For greedy mode, compare token-for-token. Then report attempted draft length, accepted-length distribution, advanced tokens per target pass, draft time, verification time, and end-to-end latency.

- **Follow the Token:** candidates remain provisional until verified.
- **Follow the Gradient:** routers, exit heads, or pruned models require training/calibration; decoding itself is inference.
- **Follow the Byte:** drafting adds weights/KV; accepting multiple tokens amortizes target weight reads.
- **Follow the Request:** scheduler and batch size determine whether verification parallelism becomes wall-time savings.

Failures include calling approximate methods exact, ignoring draft memory, measuring batch one only, using acceptance rate without accepted length, sparse formats without kernels, and routing divergence. Exit when you can state a negative-result criterion: no speedup at matched quality and production concurrency.

## Primary references

- Leviathan, Kalman, and Matias, [Fast Inference from Transformers via Speculative Decoding](https://arxiv.org/abs/2211.17192), 2023.
- Chen et al., [Accelerating Large Language Model Decoding with Speculative Sampling](https://arxiv.org/abs/2302.01318), 2023.
- NVIDIA, [CUDA C++ Programming Guide: CUDA Graphs](https://docs.nvidia.com/cuda/cuda-c-programming-guide/#cuda-graphs), version-sensitive; accessed 2026-09-19. Pin algorithm variant, draft and target revisions, engine commit, draft length, batch and concurrency, prompts, precision, and graph policy.
