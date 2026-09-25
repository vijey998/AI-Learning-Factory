# Exercise and Exit-Check Solutions

These concise solutions are keyed to the numbered chapters. Numerical answers use the assumptions stated in the chapter; empirical labs instead give acceptance criteria, because benchmark values depend on the recorded environment. A result that does not include its boundary, units, configuration, and limitations is incomplete.

## Part I — Orientation

### 01. The LLM in One Picture

Token IDs are categorical indices, not magnitudes. `[B,T,D]` becomes `[B,T,V]` at the vocabulary projection (LM head). Sampling can change output without changing weights. `[1024,4096]` BF16 uses `1024×4096×2 = 8,388,608` bytes = 8 MiB. Appending a token extends request state; it does not retrain the model.

### 02. Training vs Inference

For one request, weights are persistent and unchanged; prompt IDs, hidden activations, and KV entries are request-local. Gradients and Adam moments are absent from ordinary inference; optimizer moments are persistent training state. RNG state advances only when the chosen decoding path consumes randomness.

### 03. Anatomy of the Modern LLM Stack

A defensible diagnosis maps the symptom to the narrowest layer: malformed roles belong to application/template logic; queue delay to serving; a graph break to compiler/runtime; a slow GEMM to the kernel; OOM to live allocations and memory policy. Confirm with boundary traces before changing a lower layer.

### 04. Building Our Tiny Laboratory

A passing artifact records the exact command, hypothesis, expected and actual result, seed, dependency/hardware versions, and one limitation. Tests must pass and `build/environment.json` must be sufficient for another reader to identify what ran; a notebook with hidden state alone is not reproducible.

## Part II — Mathematical Foundations

### 05. Tensors and Resource Accounting

`X:[4,512,1024]`, `W:[1024,4096]`, and `Y:[4,512,4096]`. Their BF16 payloads are 4, 8, and 16 MiB. The projection costs approximately `2BTD·4096 = 17,179,869,184` FLOPs, excluding bias, backward work, workspaces, padding, and allocator overhead.

### 06. Geometry and Number Formats

For `q=[1,0]`, dot products with `a=[2,0]`, `b=[1,1]`, and `c=[100,100]` are 2, 1, and 100; cosines are 1, `1/√2`, and `1/√2`. Stable softmax subtracts the maximum because the common exponential factor cancels. Packed INT4 also needs scales, zero points, grouping metadata, padding, and sometimes dequantization buffers.

### 07. Probability, Logits and Loss

`softmax(z_i+c)=e^{z_i}e^c/(e^cΣ_j e^{z_j})=softmax(z_i)`. For one-hot target `y`, cross-entropy is `−Σ_i y_i log p_i = −log p_target`. Entropy describes one distribution, cross-entropy scores a target against a prediction, and `KL(P||Q)` compares normalized distributions asymmetrically.

### 08. Gradients, Graphs and Autodiff

For `L=a²+ab`, both paths into `a` accumulate, so `∂L/∂a=2a+b`; `∂L/∂b=a`. Centered finite differences should converge toward these values until rounding error dominates. This tests only the implemented scalar primitives, not broadcasting, tensor views, or nondifferentiable operators.

## Part III — Neural Networks

### 09. Linear Layers and Nonlinearities

Three affine maps collapse to `W=W3W2W1` and `b=W3W2b1+W3b2+b3`. A tent is `ReLU(x+1)−2ReLU(x)+ReLU(x−1)`. A wrongly shaped bias can broadcast without an exception, sharing or varying offsets along the wrong axis and therefore defining a different model.

### 10. A Tiny Network, Forward and Backward

With `b1=−2`, `z1=−1`, the first ReLU derivative is zero, so gradients through that hidden unit to its incoming weight and bias are zero. Centered differences validate the original analytic derivatives away from the ReLU kink. Summing a batch loss multiplies gradients by batch size relative to averaging.

### 11. Optimization and State

For `P` parameters: BF16 parameters use `2P`, FP32 gradients `4P`, and two FP32 Adam moments `8P`, totaling `14P` bytes; add `4P` if FP32 master weights are retained. `zero_grad` prevents unintended accumulation. Coupled L2 adds `λθ` to the gradient before Adam normalization; AdamW applies a separate `−ηλθ` decay.

### 12. Initialization and Training Stability

Norms `[0.9,0.8,0.02,0.0001]` justify locating where signal collapses, then checking activations, gradients, initialization, masks, and precision at that boundary—not naming a cause from norms alone. `[6,8]` has norm 10, so clipping at 5 yields `[3,4]`. Raising epsilon may suppress numerical symptoms while materially changing normalization or optimizer dynamics.

## Part IV — Tokens and Representations

### 13. Tokenization Algorithms

One valid BPE answer must state corpus frequencies and a deterministic tie rule, then show the pair counts and vocabulary after each of three merges. Round trips must preserve bytes or normalized text for whitespace, emoji, both accent forms, and unseen scripts. Round-trip correctness says nothing about compression, sequence length, fairness, or model compatibility.

### 14. Vocabulary and Token IDs

If IDs 1 and 2 are permuted but embedding rows are not, both input meanings and output labels silently swap. Permuting IDs, embedding rows, and tied/output rows together preserves the function. Hash tokenizer model/config, vocabulary and merges, special-token map, model config, weight shards/index, templates, and relevant code revision.

### 15. Embedding Matrices and Geometry

For IDs `[1,1,3]` with upstream vectors `g1,g2,g3`, only rows 1 and 3 are nonzero: `∇E[1]=g1+g2`, `∇E[3]=g3`. Scaling one vector by ten leaves its cosine direction unchanged but changes Euclidean distances. A probe can exploit correlated information without proving the representation causally drives behavior.

### 16. Position and Sequence Order

Without position information, permuting token rows permutes Q/K/V and therefore permutes attention outputs: the operation is equivariant. For a 2-D RoPE pair, rotations compose as `R(p)^T R(q)=R(q−p)`, so the dot product depends on relative offset. Extrapolation may fail from unseen rotation frequencies and from learned attention/content behavior outside the training distribution.

## Part V — Attention

### 17. Sequence Modeling and the Attention Idea

For recurrence `h_t=0.25h_{t−1}+x_t`, `h0=0` and inputs `[1,2,3]` give `1`, `2.25`, and `3.5625`. Attention instead forms an explicit weighted sum `Σ_i α_i v_i`, with nonnegative weights summing to one. Recurrence has compact sequential state; full attention offers direct access to all positions but quadratic score work/storage in the naive form.

### 18. Queries, Keys, Values and Scaling

Swapping values changes retrieved content under unchanged weights; swapping keys changes routing weights. For independent unit-variance Q/K coordinates, the dot-product variance is `d_k`, hence division by `√d_k`. With `T=4,d_k=2,d_v=3`, Q/K are `[4,2]`, scores and weights `[4,4]`, V `[4,3]`, and output `[4,3]` per head.

### 19. Causal and Multi-Head Attention

The permitted 4×4 mask is lower triangular: rows allow columns `{0}`, `{0,1}`, `{0,1,2}`, `{0,1,2,3}`; forbidden entries receive `−∞` before softmax. For `B=3,T=7,D=12,H=3`, `d_h=4`, Q/K/V are `[3,3,7,4]`, concatenation returns `[3,7,12]`. Mutating future tokens must not change earlier logits.

### 20. Attention Shapes and Compute Cost

For `B=4,T=1024,D=2048,H=16`, `d_h=128`; each Q/K/V tensor is `[4,16,1024,128]` and 16 MiB in BF16, or 48 MiB total. Scores are `[4,16,1024,1024]` and 128 MiB in BF16. Four D×D projections cost about `8BTD² = 137.44` GFLOPs; QKᵀ plus AV costs about `4BT²D = 34.36` GFLOPs. Doubling T doubles projections/QKV bytes but quadruples scores and attention matmuls.

## Part VI — The Transformer

### 21. Residual Streams and Normalization

Pre-norm computes `x+F(norm(x))`; post-norm computes `norm(x+F(x))`, so identical sublayer weights do not make their inputs or gradient paths equal. A correct normalization computes statistics over the feature dimension independently for every batch/time position. Report stream RMS, update RMS, and gradient norms by layer for both variants.

### 22. Feed-Forward Networks and Complete Blocks

For `(B,T,D,H,M)=(2,16,128,4,352)`, every residual boundary is `[2,16,128]`; per-head width is 32. A SwiGLU MLP needs two D→M projections (gate and value) and one M→D projection, hence three matrices. Its M is often smaller than the 4D width of a two-matrix GELU MLP to match parameter/compute budgets.

### 23. Stacking, Vocabulary Projection and Tying

IDs `[B,T]` look up embeddings `[B,T,D]`, blocks preserve that shape, and the LM head produces `[B,T,V]`; logits at position `t` predict label `t+1` after shifting. In a tied model, input embedding and output projection reference the same parameter object and receive the sum of gradients from both uses, reducing the parameter count by `V·D` relative to untied weights.

### 24. Build Our GPT From Scratch

A pass requires finite `[B,T,V]` logits, a reconciled hand/framework parameter count, true tied storage, and causal isolation. Removing the causal mask should make an earlier logit change when only a future token changes. Shape tests alone cannot detect leakage, wrong normalization, bad positions, or numerically incorrect attention.

## Part VII — Training Systems

### 25. Sequences, Batches and Pretraining

A correct packed collator returns token IDs, position IDs that reset per example when required, an attention mask that blocks cross-example attention, and a loss mask excluding separators/padding. Changing example A must leave B’s logits unchanged. The loss denominator is the count (or weight sum) of valid target tokens, not padded sequence length.

### 26. The Training Step and Schedule

With dropout off, identical examples/order, and loss weighted by valid tokens, four microbatches of two should match one batch of eight within floating-point tolerance. Dropout consumes different masks and changes arithmetic order, so exact equality is not expected. Account separately for parameters, gradients, master weights if any, and optimizer buffers.

### 27. Mixed Precision and Checkpoint Anatomy

A complete step-two checkpoint restores model, optimizer, scheduler/scaler, data position, and every RNG state. Repeating step three should reproduce the sampled batch, dropout masks, loss, parameters, optimizer buffers, and scheduler count under deterministic kernels. Any hardware/library nondeterminism must be named rather than hidden behind a loose tolerance.

### 28. Debugging and Training Our Tiny Model

At initialization, vocabulary cross-entropy should be near `ln V`; one batch should overfit; held-out metrics must use evaluation behavior; resume must reproduce the next step. A one-token label shift can leave loss plausible while teaching the wrong alignment; an excessive learning rate typically causes spikes/non-finite values or divergence. Record seeds, versions, and dataset hash.

## Part VIII — Architectures

### 29. Transformer Families

Encoder self-attention permits all 4×4 source pairs; three-token decoder self-attention uses a 3×3 lower triangle; cross-attention permits all 3×4 target-to-source pairs. Encoder K/V can be cached during decoder generation because the source is fixed; decoder self K/V grows. BERT predicts masked positions, GPT predicts shifted next tokens, and T5 predicts sentinel-delimited removed spans.

### 30. Modern Positions, Heads and MLPs

For `D=2048,H=16`, `d_h=128`. Q always has `D²` parameters; K and V together have `2D(Hkv·d_h)`, and output projection has `D²`. BF16 KV per token-layer is `2·Hkv·128·2` bytes: 8192 bytes for `Hkv=16`, 2048 for 4, and 512 for 1. Each query head maps to exactly one K/V group.

### 31. Mixture of Experts

For `N=1000,E=8,k=2`, there are 2000 assignments; nominal per-expert capacity is `ceil(capacity_factor·2000/8)`: 250 at factor 1.0 and 313 at 1.25. Report histogram, coefficient of variation, routing entropy, and assignments beyond capacity. Dropping loses routed computation; rerouting changes which expert computes the token. Small decode batches commonly underutilize experts.

### 32. Alternative Architectures and Real Configs

A passing answer pins an official config revision and derives `d_h`, attention/MLP tensor counts, dtype weight bytes, and KV bytes at `B=1,T=4096`; every mismatch with loaded tensors must be attributed to biases, norms, embeddings, tying, padding, or architecture-specific weights. A sparse/local/state-space alternative cannot directly access every earlier token with an arbitrary content-based edge in one layer as full attention can.

## Part IX — Data and Evaluation

### 33. Data Sources and Cleaning

A reproducible shard is derivable from a manifest of permitted immutable inputs plus pinned cleaning/dedup code. The report must show document and byte counts after acquisition, filtering, exact dedup, and near-dedup, with reason codes and manual samples from accepted/rejected sets. Unrecorded source drift fails the exit check.

### 34. Mixtures, Tokens and Synthetic Data

If allocation amounts are `a_i`, expected epochs are `a_i/u_i` for unique-token counts `u_i`; allocations must sum to 12B. Exact hashes should catch planted exact leaks but not paraphrases; shingles may catch overlap while creating topical false positives and missing semantic rewrites. Report both false positives and false negatives rather than one recall number.

### 35. Evaluation and Meaningful Experiments

Use paired per-example differences for the 300 shared examples and bootstrap those pairs for a 95% interval. A supported claim is restricted to the pinned prompts, decoding, slices, and measured latency boundary. An unsupported claim extrapolates to all tasks, users, or deployment loads from this sample.

### 36. Scaling Laws

Fit the stated power law to all nine size/budget runs, inspect residual structure, bootstrap runs or appropriate units, and evaluate the untouched held-out run. Report point error and interval coverage. Adding inference cost can change the selected model even when predicted training loss ordering is unchanged.

## Part X — Adaptation and Reasoning

### 37. Pretraining, Continued Pretraining and SFT

For each rendered conversation, labels equal token IDs only on intended assistant spans and are ignored elsewhere, including after truncation and packing. Attention must prevent cross-example leakage. A continued-pretraining mixture should retain a stated general-data replay fraction and predefine domain and general-retention gates.

### 38. Parameter-Efficient Adaptation

LoRA for one `d_out×d_in` weight adds `r(d_in+d_out)` parameters through factors `A` and `B`. Before merge, `y=(W+sBA)x`; after setting `W′=W+sBA`, outputs should match within numeric tolerance. Adapter identity belongs in cache keys; changing it invalidates prefix states computed with old weights.

### 39. Preferences and Reinforcement Learning

Reward-model pair loss is `−log σ(r_chosen−r_rejected)`. DPO applies the same logistic form to the policy-vs-reference log-ratio margin scaled by β. PPO’s path is rollout → rewards/advantages → clipped policy updates, typically with frozen reference and reward models and a trainable policy/value path. Summed sequence log-probabilities introduce a length effect that averaging changes.

### 40. Reasoning, Test-Time Compute and Distillation

All three strategies must receive the same total generation-token budget. Compare correctness, wall latency, consumed tokens, and selection failures; majority vote can waste correlated samples, while checker ranking inherits checker errors. Distillation is supported only if verified-example training beats an equal-data SFT control on held-out tasks.

## Part XI — Hardware Performance

### 41. Why GPUs and How They Execute

For one million elements, block counts are `ceil(1,000,000/t)`: 7813 for 128 threads, 3907 for 256, and 1954 for 512. The final blocks contain 64, 64, and 64 valid lanes respectively; masking is required. Occupancy is only a resource constraint—memory access, registers, and instruction efficiency determine the winner.

### 42. Memory Hierarchy and Movement

For P parameters at b bytes each, weights use `Pb`; the ideal transfer lower bound is bytes/bandwidth at each SSD→RAM, RAM→GPU, and HBM scan boundary. Real time is higher due to protocol, contention, page faults, and incomplete overlap. Contiguous/coalesced reads require fewer transactions than strided reads for the same useful payload.

### 43. Throughput, Intensity and Rooflines

Arithmetic intensity is FLOPs divided by bytes moved at the boundary being modeled. The roofline ceiling is `min(peak FLOP/s, intensity×measured bandwidth)`. Prefill or larger decode batches reuse weights and raise ideal intensity. Actual points lie below the roof because of launch gaps, imperfect tiling, occupancy limits, non-GEMM work, synchronization, and unmodeled traffic.

### 44. Profiling Transformer Bottlenecks

Warm up, synchronize only outside measured intervals, use CPU wall time for end-to-end and GPU events for device spans, and sweep batches. The largest interval is a candidate bottleneck, not proof; falsification requires an intervention predicted to shrink that span without shifting the boundary or workload. Publish a systems timeline and kernel-level evidence when CUDA is available.

## Part XII — Kernels and Runtime

### 45. Kernels, GEMM and Tiling

GEMM work is `2MNK` FLOPs. A 128×128 tile can lose to 64×64 through register/shared-memory pressure, fewer resident blocks, poor edge utilization, or bank/layout effects. Fusing activation with its producer/consumer can avoid writing and rereading the intermediate activation, but only a byte trace establishes the saving.

### 46. CUDA, Triton and CUTLASS

Fused BF16 add-plus-activation logically reads two inputs and writes one output: 6 bytes/element. For 16 million elements this is 96,000,000 bytes ≈ 91.6 MiB; at 0.20 ms, logical bandwidth is about 447 GiB/s. A passing report covers irregular shapes, NaN contract, cold compile time, warm median/p95, environment, and the best matched framework baseline.

### 47. Graphs, Compilers and Runtimes

A passing two-shape-family experiment reports the exported/compiled graph, guards, graph breaks, generated kernel count, cold compile time, and warmed time. Fusion is valuable when it removes actual allocations/HBM traffic. A speedup claim fails if compilation is included only for one path, semantics differ, or unseen shapes trigger unreported recompilation/fallback.

### 48. CUDA Graphs and Execution Overhead

Eighty 4 µs kernels plus eighty 3 µs host gaps take 560 µs, of which 240/560 ≈ 43% is orchestration. Break-even reuse is `N>C/(E−R)`; 2 s setup and 0.5 ms saving reaches equality at 4000 hits. Power-of-two batch buckets `{1,2,4,8,16,32}` bound variants; batch 11 masks five slots and wastes 5/16 capacity.

## Part XIII — Inference

### 49. Load Weights and Trace a Forward Pass

The required trace is IDs `[B,T]` → residual `[B,T,D]` → Q `[B,H,T,d_h]`, K/V `[B,Hkv,T,d_h]` → attention `[B,H,T,d_h]` → MLP `[B,T,F]` → logits `[B,T,V]`. For `B=2,T=128,D=4096` BF16, one residual is 2 MiB; `V=128,000` full logits are 62.5 MiB. Compare final logits with uninstrumented eager execution.

### 50. Prefill, Decode and KV Cache

KV bytes are `2LBHkvSd_hb`. With `L=32,Hkv=8,d_h=128,b=2`, one token/sequence uses 131,072 bytes = 128 KiB, and 8192 tokens use 1 GiB. Historical K/V are needed for new-query routing and retrieval; historical Q is not. Cached and full-prefix logits must match before sampling.

### 51. Sampling and Decoding Policies

For logits `[2,1,0]`, greedy chooses the first token; at `τ=0.5`, probabilities are about `[0.867,0.117,0.016]`. Top-2 at τ=1 renormalizes to `[0.731,0.269,0]`; top-p 0.8 keeps the first two under the include-crossing convention. Seeded frequencies should fall within a stated sampling interval. Filtering transforms a distribution; beam search compares sequences.

### 52. Inference Memory and Latency Accounting

Separate weights, KV, active tensors/workspaces, runtime pools, and reserve; KV token bytes are `2LHkv d_h b`. TTFT includes the declared admission-to-first-emission components; TPOT states whether the first token is excluded. OOM below nominal capacity can arise from fragmentation, peak temporaries, allocator reservation, concurrent requests, or non-model processes.

## Part XIV — Efficient Inference

### 53. FlashAttention and Paged KV Memory

A BF16 score tensor `[1,32,8192,8192]` uses `1×32×8192²×2 = 4 GiB`. Online-softmax block merges track row maximum `m`, normalizer `l`, and weighted accumulator, rescaling old and new terms by `exp(m_old−m_new)`. Page waste for length S and page size P is `ceil(S/P)P−S` slots. FlashAttention remains exact attention and still has quadratic arithmetic.

### 54. Caching, Batching and Prefill Scheduling

Use the same arrival trace for every policy and report TTFT, TPOT, completion, throughput, queue depth, cache reuse, and peak pages. Continuous batching can raise throughput yet worsen tail latency when long prefills or admission pressure delay decode. Prefix equality must include tokens, model/adapter, positions, and relevant execution semantics—not a hash alone.

### 55. Speculative Decoding and Dynamic Execution

Exact speculative sampling must match direct target-model output frequencies statistically; greedy mode must match token-for-token. Report accepted tokens per verification pass plus end-to-end latency and added draft weight/KV memory. A valid negative conclusion is no speedup at matched quality and production concurrency, even when acceptance rate looks high.

### 56. Quantization Across the Inference Path

Per-row quantization typically lowers error for rows with different ranges but spends more scale metadata than per-tensor quantization. Physical bytes include packed values, scales, zeros, padding, and temporary buffers. A passing comparison pins group size, calibration data, kernels, prompts, and evaluates perplexity, task quality, long context, latency, and residency.

## Part XV — Distributed Execution

### 57. Parallel Training Strategies

Let parameter, gradient, and optimizer-state bytes be `P_b,G_b,O_b`. DDP stores all three per rank. Ideal ZeRO stages shard optimizer only, then optimizer+gradients, then optimizer+gradients+parameters by N; add unsharded activations and a 15% runtime reserve. Gather windows can still OOM because peak live parameters overlap activations, workspaces, and communication buffers.

### 58. Partitioning Model Computation

A valid placement uses two 16-layer pipeline stages and four tensor-parallel ranks per stage, consuming eight devices. A BF16 boundary `[B,T,D]=[4,1024,4096]` is 32 MiB. A residual-sized collective moves the same logical 32 MiB tensor (algorithmic traffic differs). Tensor collectives recur per sharded layer; the pipeline transfer occurs at the stage boundary per microbatch/direction.

### 59. Collectives and Interconnects

For a ring all-reduce of message M on N ranks, the common ideal model is `2(N−1)α + 2(N−1)M/(N·BW)`. Substitute 16 MiB, 256 MiB, and 1 GiB with explicitly stated α and effective bandwidth for intra- and inter-node links. Datasheet bandwidth overpredicts performance because protocol, topology, contention, chunking, and synchronization reduce usable bandwidth.

### 60. Distributed Execution and Failure Recovery

With two ranks holding scalars 1 and 2, an all-reduce sum must yield 3 on both. Killing a rank before the next collective should produce a bounded timeout/error rather than an indefinite hang. The GPU gate separately checks NCCL topology, numerical parity, peak memory, overlap, throughput, and recovery; a CPU Gloo pass does not validate those properties.

## Part XVI — Serving

### 61. Anatomy of an Inference Server

The simulator must model arrivals, token budgets, paged KV allocation/reference counts, cancellation, and bounded output queues. Its strongest invariant is zero leaked pages after all requests finish or cancel. Compare FIFO and continuous batching on identical traces; report both TTFT and completion because throughput improvements can redistribute waiting time.

### 62. Tenants, Models and Residency

Two 14 GiB models plus 2 GiB workspace each already consume 32 GiB; adding 6 GiB KV cannot fit a 24 GiB GPU. Keep at most one resident and budget workspace/KV explicitly, or reduce/offload those demands. Cold transition lower bounds are bytes divided by PCIe/SSD bandwidth; alternating-model arrivals reveal eviction thrash and SLO misses.

### 63. Disaggregation and Runtime Comparisons

Pin exact runtime releases and compare supported hardware, artifacts, scheduler, KV layout, quantization, compilation, and fallbacks. KV transfer bytes use `2LBHkvTd_hb`; transfer time is bytes/effective bandwidth plus latency. Disaggregation wins only when saved prefill/decode time and scheduling benefit exceed transfer and coordination overhead at the measured context/concurrency.

### 64. Production Serving and GPU Clusters

An open-loop ramp should show queueing rise once arrival rate exceeds sustainable service. Report queue delay, TTFT, TPOT, completion, token throughput, RPS, percentiles, errors, and cancellations without dropping failed requests. A worker-kill test passes only if detection, routing removal, capacity loss, recovery, and user-visible failures/latency are timestamped.

## Part XVII — Local Inference

### 65. CPU and Edge Inference

Sweep pinned thread counts after warmup and report prompt/decode rates, p95 token latency, memory, bandwidth counters, power/temperature, and host responsiveness. Saturation is where more threads no longer improve useful bytes/s or tokens/s because memory bandwidth, cache capacity, thermals, or scheduling becomes limiting.

### 66. Hybrid Memory and Local Loading

On 8 GiB VRAM, a 15% reserve leaves 6.8 GiB before accounting for other processes. A 6 GiB model leaves only 0.8 GiB for workspace and KV, so placement must offload layers or shrink context/workspace unless their measured sum fits. Cold-vs-warm readiness differences primarily expose storage/page-cache transfer; first-token time additionally includes tokenization, transfer, and prefill.

### 67. Local Runtimes and Accelerators

A passing operation-placement table covers one prefill and five decode steps, naming each accelerator kernel and every host-device copy or CPU fallback. The deliberately unsupported case must record explicit error or fallback behavior. Numerical output must match a trusted reference within a dtype-appropriate tolerance; fast but silently different output fails.

### 68. Packaging, Power and Thermal Limits

The offline package includes hashes, config, licenses, diagnostics, rollback, clean uninstall, and recovery tests for corruption and interrupted installation. A 30-minute run must report startup, first token, steady decode, peak memory, package power, temperature, clocks, and latency. Compare power modes only after thermal steady state; initial boost is not sustained performance.

## Part XVIII — Retrieval and Agents

### 69. Embeddings, Contrastive Learning and Vector Indexes

Compare approximate results against exact top-10 neighbors to compute recall@10, alongside p50/p95 latency, index memory, and build time over search breadth. For unit-normalized vectors, `||x−y||²=2−2x·y`, so cosine and Euclidean rankings agree; without normalization, vector norms can reorder results.

### 70. RAG and Retrieval Quality

Evaluate at least 30 answerable and 10 unanswerable queries. Retrieval recall, answer correctness, citation entailment/support, abstention, and latency are distinct metrics. Diagnose failures at ingestion, retrieval, context packing, or generation; specificity and presence of a citation do not establish grounding.

### 71. Memory, Tools and Structured Output

Constrained decoding improves syntax, schema validation checks structure/types, authorization checks permission, and execution enforces real-world semantics—none substitutes for the others. The write tool needs an idempotency key; persistent facts need provenance and expiry. Malformed JSON, unauthorized args, duplicate writes, poisoned tool output, failures, and corrections must all have tested outcomes.

### 72. Agents and Multi-Model Economics

Compare the router against strong-model-only under matched workload and quality, reporting task success, cost, latency percentiles, calls, escalation, and recovery. Bounded retry and abstention prevent unbounded cost. A planner or critic is justified only when its removal reduces marginal value beyond uncertainty while its added latency/cost is included.

## Part XIX — Interpretability and Composition

### 73. Hidden States, Layers and Attention Heads

Record exact hook points and shapes at three layers. A logit lens maps states to vocabulary space; a probe predicts labels from states; ablation intervenes. If a probe is accurate but ablating/patching the signal does not selectively change behavior, the evidence is correlational. Attention weights alone omit value content and downstream computation.

### 74. Features, Probes and Mechanisms

Use disjoint clean/corrupted pairs, held-out evaluation, shuffled-label control, and a non-target behavior. A probe establishes decodability; activation patching or selective ablation can support causal involvement. If an intervention degrades all outputs, it shows nonspecific damage rather than a mechanism for the target behavior.

### 75. Steering, Editing and Representation Engineering

Build the contrastive direction only on discovery data, select strength on validation, and report final effects on test data. Random and reversed directions test specificity; at least two side-effect metrics bound collateral change. A weight edit must be checked on exact, paraphrased, neighboring, and unrelated prompts before making a locality or generalization claim.

### 76. Merging, Stitching and Representation Compatibility

Compare frozen same-model and cross-model stitches with linear, low-rank, and nonlinear bridges on held-out reconstruction and task accuracy, plus parameters, FLOPs, transfer bytes, and latency. Success only with a large nonlinear connector shows that the connector learned a translation; it does not establish that the original spaces were naturally aligned.

## Part XX — Research Frontier

### 77. Efficient Memory and Adaptive Computation

Compare recent-window and score-based KV eviction with no eviction across context lengths on perplexity, needle retrieval, latency, and measured cache bytes. Evaluate fixed and dynamic layer skipping separately and include batching divergence. A policy passes only at matched quality on ordinary and adversarial long-context cases, not merely lower memory.

### 78. Routable Intelligence and Neural Handoffs

The preregistration fixes hypothesis, baselines, budget, metrics, uncertainty, stopping/negative criteria, and artifact plan before the pilot. A dead-call ablation determines whether the handoff itself adds value beyond orchestration. If text exchange or whole-request routing wins, that is the correct result, not a failed experiment.

### 79. Research Design and Reproduction

A complete package contains a dated search log, prior-art matrix, claim-evidence links, pinned reproduction plan, preregistration, and negative-result criterion. Reproduce one central result with uncertainty, or document the precise blocker and attempted resolutions. “Runs on the author’s machine” fails until a clean environment can execute it.

### 80. Evidence, Ablations and Publication

The submission gate requires a claim-evidence table, ablation grid, paired uncertainty analysis, full resource profile, limitations, source-type tags, and a reproducibility manifest. The supported paragraph must stay within observed tasks, budgets, and intervals; the stronger rejected paragraph should expose the prohibited extrapolation. A clean environment must regenerate the main table.
