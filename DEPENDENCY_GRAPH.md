# Prerequisites and reading paths

The default path is sequential, with explicit cross-part prerequisites listed below. This conservative order is deliberate for a novice-to-research curriculum. Experienced readers may use the paths below, but should verify each chapter outcome before skipping it.

| Path | Chapters | Purpose |
| --- | --- | --- |
| Model construction | 1–28 | Implement and train a tiny decoder |
| Systems | 1–8, 17–24, 29–36, 41–68 | Explain execution, memory and service behavior |
| Adaptation and applications | 1–40, 49–52, 69–72 | Understand post-training and agent workflows |
| Research | Core foundations plus 73–80 | Design controlled representation and efficiency experiments |

An overview can name a mechanism before its formal treatment. It must not require unexplained mathematics. Examples: basic sampling appears in Chapter 1; the full policy treatment is Chapter 51. Basic held-out evaluation appears before Part IX.

| Chapter | Prerequisites |
| --- | --- |
| [CH-01: The LLM in One Picture](chapters/part-01/01-the-llm-in-one-picture.md) |  |
| [CH-02: Training vs Inference](chapters/part-01/02-training-vs-inference.md) | CH-01 |
| [CH-03: Anatomy of the Modern LLM Stack](chapters/part-01/03-anatomy-of-the-modern-llm-stack.md) | CH-02 |
| [CH-04: Building Our Tiny Laboratory](chapters/part-01/04-building-our-tiny-laboratory.md) | CH-03 |
| [CH-05: Tensors and Resource Accounting](chapters/part-02/05-tensors-and-resource-accounting.md) | CH-04 |
| [CH-06: Geometry and Number Formats](chapters/part-02/06-geometry-and-number-formats.md) | CH-05 |
| [CH-07: Probability, Logits and Loss](chapters/part-02/07-probability-logits-and-loss.md) | CH-06 |
| [CH-08: Gradients, Graphs and Autodiff](chapters/part-02/08-gradients-graphs-and-autodiff.md) | CH-07 |
| [CH-09: Linear Layers and Nonlinearities](chapters/part-03/09-linear-layers-and-nonlinearities.md) | CH-08 |
| [CH-10: A Tiny Network, Forward and Backward](chapters/part-03/10-a-tiny-network-forward-and-backward.md) | CH-09 |
| [CH-11: Optimization and State](chapters/part-03/11-optimization-and-state.md) | CH-10 |
| [CH-12: Initialization and Training Stability](chapters/part-03/12-initialization-and-training-stability.md) | CH-11 |
| [CH-13: Tokenization Algorithms](chapters/part-04/13-tokenization-algorithms.md) | CH-12 |
| [CH-14: Vocabulary and Token IDs](chapters/part-04/14-vocabulary-and-token-ids.md) | CH-13 |
| [CH-15: Embedding Matrices and Geometry](chapters/part-04/15-embedding-matrices-and-geometry.md) | CH-14 |
| [CH-16: Position and Sequence Order](chapters/part-04/16-position-and-sequence-order.md) | CH-15 |
| [CH-17: Sequence Modeling and the Attention Idea](chapters/part-05/17-sequence-modeling-and-the-attention-idea.md) | CH-16 |
| [CH-18: Queries, Keys, Values and Scaling](chapters/part-05/18-queries-keys-values-and-scaling.md) | CH-05, CH-07, CH-15, CH-17 |
| [CH-19: Causal and Multi-Head Attention](chapters/part-05/19-causal-and-multi-head-attention.md) | CH-18 |
| [CH-20: Attention Shapes and Compute Cost](chapters/part-05/20-attention-shapes-and-compute-cost.md) | CH-05, CH-18, CH-19 |
| [CH-21: Residual Streams and Normalization](chapters/part-06/21-residual-streams-and-normalization.md) | CH-20 |
| [CH-22: Feed-Forward Networks and Complete Blocks](chapters/part-06/22-feed-forward-networks-and-complete-blocks.md) | CH-21 |
| [CH-23: Stacking, Vocabulary Projection and Tying](chapters/part-06/23-stacking-vocabulary-projection-and-tying.md) | CH-22 |
| [CH-24: Build Our GPT From Scratch](chapters/part-06/24-build-our-gpt-from-scratch.md) | CH-23 |
| [CH-25: Sequences, Batches and Pretraining](chapters/part-07/25-sequences-batches-and-pretraining.md) | CH-24 |
| [CH-26: The Training Step and Schedule](chapters/part-07/26-the-training-step-and-schedule.md) | CH-08, CH-11, CH-24, CH-25 |
| [CH-27: Mixed Precision and Checkpoint Anatomy](chapters/part-07/27-mixed-precision-and-checkpoint-anatomy.md) | CH-26 |
| [CH-28: Debugging and Training Our Tiny Model](chapters/part-07/28-debugging-and-training-our-tiny-model.md) | CH-27 |
| [CH-29: Transformer Families](chapters/part-08/29-transformer-families.md) | CH-28 |
| [CH-30: Modern Positions, Heads and MLPs](chapters/part-08/30-modern-positions-heads-and-mlps.md) | CH-16, CH-19, CH-29 |
| [CH-31: Mixture of Experts](chapters/part-08/31-mixture-of-experts.md) | CH-30 |
| [CH-32: Alternative Architectures and Real Configs](chapters/part-08/32-alternative-architectures-and-real-configs.md) | CH-31 |
| [CH-33: Data Sources and Cleaning](chapters/part-09/33-data-sources-and-cleaning.md) | CH-32 |
| [CH-34: Mixtures, Tokens and Synthetic Data](chapters/part-09/34-mixtures-tokens-and-synthetic-data.md) | CH-33 |
| [CH-35: Evaluation and Meaningful Experiments](chapters/part-09/35-evaluation-and-meaningful-experiments.md) | CH-34 |
| [CH-36: Scaling Laws](chapters/part-09/36-scaling-laws.md) | CH-05, CH-35 |
| [CH-37: Pretraining, Continued Pretraining and SFT](chapters/part-10/37-pretraining-continued-pretraining-and-sft.md) | CH-36 |
| [CH-38: Parameter-Efficient Adaptation](chapters/part-10/38-parameter-efficient-adaptation.md) | CH-37 |
| [CH-39: Preferences and Reinforcement Learning](chapters/part-10/39-preferences-and-reinforcement-learning.md) | CH-07, CH-37, CH-38 |
| [CH-40: Reasoning, Test-Time Compute and Distillation](chapters/part-10/40-reasoning-test-time-compute-and-distillation.md) | CH-39 |
| [CH-41: Why GPUs and How They Execute](chapters/part-11/41-why-gpus-and-how-they-execute.md) | CH-40 |
| [CH-42: Memory Hierarchy and Movement](chapters/part-11/42-memory-hierarchy-and-movement.md) | CH-41 |
| [CH-43: Throughput, Intensity and Rooflines](chapters/part-11/43-throughput-intensity-and-rooflines.md) | CH-05, CH-42 |
| [CH-44: Profiling Transformer Bottlenecks](chapters/part-11/44-profiling-transformer-bottlenecks.md) | CH-43 |
| [CH-45: Kernels, GEMM and Tiling](chapters/part-12/45-kernels-gemm-and-tiling.md) | CH-44 |
| [CH-46: CUDA, Triton and CUTLASS](chapters/part-12/46-cuda-triton-and-cutlass.md) | CH-45 |
| [CH-47: Graphs, Compilers and Runtimes](chapters/part-12/47-graphs-compilers-and-runtimes.md) | CH-08, CH-24, CH-46 |
| [CH-48: CUDA Graphs and Execution Overhead](chapters/part-12/48-cuda-graphs-and-execution-overhead.md) | CH-47 |
| [CH-49: Load Weights and Trace a Forward Pass](chapters/part-13/49-load-weights-and-trace-a-forward-pass.md) | CH-48 |
| [CH-50: Prefill, Decode and KV Cache](chapters/part-13/50-prefill-decode-and-kv-cache.md) | CH-19, CH-24, CH-49 |
| [CH-51: Sampling and Decoding Policies](chapters/part-13/51-sampling-and-decoding-policies.md) | CH-50 |
| [CH-52: Inference Memory and Latency Accounting](chapters/part-13/52-inference-memory-and-latency-accounting.md) | CH-05, CH-30, CH-50, CH-51 |
| [CH-53: FlashAttention and Paged KV Memory](chapters/part-14/53-flashattention-and-paged-kv-memory.md) | CH-20, CH-42, CH-50, CH-52 |
| [CH-54: Caching, Batching and Prefill Scheduling](chapters/part-14/54-caching-batching-and-prefill-scheduling.md) | CH-53 |
| [CH-55: Speculative Decoding and Dynamic Execution](chapters/part-14/55-speculative-decoding-and-dynamic-execution.md) | CH-54 |
| [CH-56: Quantization Across the Inference Path](chapters/part-14/56-quantization-across-the-inference-path.md) | CH-06, CH-35, CH-55 |
| [CH-57: Parallel Training Strategies](chapters/part-15/57-parallel-training-strategies.md) | CH-56 |
| [CH-58: Partitioning Model Computation](chapters/part-15/58-partitioning-model-computation.md) | CH-20, CH-41, CH-57 |
| [CH-59: Collectives and Interconnects](chapters/part-15/59-collectives-and-interconnects.md) | CH-58 |
| [CH-60: Distributed Execution and Failure Recovery](chapters/part-15/60-distributed-execution-and-failure-recovery.md) | CH-59 |
| [CH-61: Anatomy of an Inference Server](chapters/part-16/61-anatomy-of-an-inference-server.md) | CH-60 |
| [CH-62: Tenants, Models and Residency](chapters/part-16/62-tenants-models-and-residency.md) | CH-61 |
| [CH-63: Disaggregation and Runtime Comparisons](chapters/part-16/63-disaggregation-and-runtime-comparisons.md) | CH-50, CH-52, CH-59, CH-62 |
| [CH-64: Production Serving and GPU Clusters](chapters/part-16/64-production-serving-and-gpu-clusters.md) | CH-63 |
| [CH-65: CPU and Edge Inference](chapters/part-17/65-cpu-and-edge-inference.md) | CH-64 |
| [CH-66: Hybrid Memory and Local Loading](chapters/part-17/66-hybrid-memory-and-local-loading.md) | CH-65 |
| [CH-67: Local Runtimes and Accelerators](chapters/part-17/67-local-runtimes-and-accelerators.md) | CH-66 |
| [CH-68: Packaging, Power and Thermal Limits](chapters/part-17/68-packaging-power-and-thermal-limits.md) | CH-67 |
| [CH-69: Embeddings, Contrastive Learning and Vector Indexes](chapters/part-18/69-embeddings-contrastive-learning-and-vector-indexes.md) | CH-06, CH-15, CH-35, CH-68 |
| [CH-70: RAG and Retrieval Quality](chapters/part-18/70-rag-and-retrieval-quality.md) | CH-69 |
| [CH-71: Memory, Tools and Structured Output](chapters/part-18/71-memory-tools-and-structured-output.md) | CH-70 |
| [CH-72: Agents and Multi-Model Economics](chapters/part-18/72-agents-and-multi-model-economics.md) | CH-71 |
| [CH-73: Hidden States, Layers and Attention Heads](chapters/part-19/73-hidden-states-layers-and-attention-heads.md) | CH-72 |
| [CH-74: Features, Probes and Mechanisms](chapters/part-19/74-features-probes-and-mechanisms.md) | CH-07, CH-35, CH-73 |
| [CH-75: Steering, Editing and Representation Engineering](chapters/part-19/75-steering-editing-and-representation-engineering.md) | CH-74 |
| [CH-76: Merging, Stitching and Representation Compatibility](chapters/part-19/76-merging-stitching-and-representation-compatibility.md) | CH-21, CH-73, CH-75 |
| [CH-77: Efficient Memory and Adaptive Computation](chapters/part-20/77-efficient-memory-and-adaptive-computation.md) | CH-76 |
| [CH-78: Routable Intelligence and Neural Handoffs](chapters/part-20/78-routable-intelligence-and-neural-handoffs.md) | CH-52, CH-59, CH-72, CH-76, CH-77 |
| [CH-79: Research Design and Reproduction](chapters/part-20/79-research-design-and-reproduction.md) | CH-35, CH-36, CH-78 |
| [CH-80: Evidence, Ablations and Publication](chapters/part-20/80-evidence-ablations-and-publication.md) | CH-35, CH-79 |
