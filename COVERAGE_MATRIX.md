# Coverage matrix

Generated from `curriculum/*.json`. A destination means planned coverage, not substantive completion.

- 80 chapters; 544 atomic teaching requirements.
- 441 source obligations: 161 original V1 topics, 206 V2 headings, 54 audit correction groups, and 20 framework/milestone obligations.
- 544 drafted topics; 0 complete topics.
- The original 161-topic V1 outline is reconciled item by item in the source inventory.

## Source reconciliation

| Source ID | Obligation | Destination | Chapter status |
| --- | --- | --- | --- |
| V1-001 | What Actually Is an LLM? | [CH-01](chapters/part-01/01-the-llm-in-one-picture.md) | drafted |
| V1-002 | Training vs Inference | [CH-02](chapters/part-01/02-training-vs-inference.md) | drafted |
| V1-003 | The Entire LLM Technology Stack | [CH-03](chapters/part-01/03-anatomy-of-the-modern-llm-stack.md) | drafted |
| V1-004 | Scalars, Vectors, Matrices and Tensors | [CH-05](chapters/part-02/05-tensors-and-resource-accounting.md) | drafted |
| V1-005 | Geometry of Vectors | [CH-06](chapters/part-02/06-geometry-and-number-formats.md) | drafted |
| V1-006 | Probability for Language Models | [CH-07](chapters/part-02/07-probability-logits-and-loss.md) | drafted |
| V1-007 | Softmax | [CH-07](chapters/part-02/07-probability-logits-and-loss.md) | drafted |
| V1-008 | Calculus Without Pain | [CH-08](chapters/part-02/08-gradients-graphs-and-autodiff.md) | drafted |
| V1-009 | Backpropagation | [CH-08](chapters/part-02/08-gradients-graphs-and-autodiff.md) | drafted |
| V1-010 | Optimization | [CH-11](chapters/part-03/11-optimization-and-state.md) | drafted |
| V1-011 | Numerical Representation | [CH-06](chapters/part-02/06-geometry-and-number-formats.md) | drafted |
| V1-012 | Tokenization | [CH-13](chapters/part-04/13-tokenization-algorithms.md) | drafted |
| V1-013 | Embeddings | [CH-15](chapters/part-04/15-embedding-matrices-and-geometry.md) | drafted |
| V1-014 | Positional Information | [CH-16](chapters/part-04/16-position-and-sequence-order.md) | drafted |
| V1-015 | Contextual vs Static Representations | [CH-15](chapters/part-04/15-embedding-matrices-and-geometry.md) | drafted |
| V1-016 | Before Transformers | [CH-17](chapters/part-05/17-sequence-modeling-and-the-attention-idea.md) | drafted |
| V1-017 | Attention Intuition | [CH-17](chapters/part-05/17-sequence-modeling-and-the-attention-idea.md) | drafted |
| V1-018 | Queries, Keys and Values | [CH-18](chapters/part-05/18-queries-keys-values-and-scaling.md) | drafted |
| V1-019 | Scaled Dot-Product Attention | [CH-18](chapters/part-05/18-queries-keys-values-and-scaling.md) | drafted |
| V1-020 | Causal Attention | [CH-19](chapters/part-05/19-causal-and-multi-head-attention.md) | drafted |
| V1-021 | Multi-Head Attention | [CH-19](chapters/part-05/19-causal-and-multi-head-attention.md) | drafted |
| V1-022 | The MLP / Feed-Forward Network | [CH-22](chapters/part-06/22-feed-forward-networks-and-complete-blocks.md) | drafted |
| V1-023 | Residual Connections | [CH-21](chapters/part-06/21-residual-streams-and-normalization.md) | drafted |
| V1-024 | Normalization | [CH-21](chapters/part-06/21-residual-streams-and-normalization.md) | drafted |
| V1-025 | One Complete Transformer Block | [CH-22](chapters/part-06/22-feed-forward-networks-and-complete-blocks.md) | drafted |
| V1-026 | Build a Tiny GPT | [CH-24](chapters/part-06/24-build-our-gpt-from-scratch.md) | drafted |
| V1-027 | Decoder-Only Models | [CH-29](chapters/part-08/29-transformer-families.md) | drafted |
| V1-028 | Encoder Models | [CH-29](chapters/part-08/29-transformer-families.md) | drafted |
| V1-029 | Encoder-Decoder Models | [CH-29](chapters/part-08/29-transformer-families.md) | drafted |
| V1-030 | Modern Architectural Improvements | [CH-30](chapters/part-08/30-modern-positions-heads-and-mlps.md) | drafted |
| V1-031 | Mixture of Experts | [CH-31](chapters/part-08/31-mixture-of-experts.md) | drafted |
| V1-032 | Other Sequence Architectures | [CH-32](chapters/part-08/32-alternative-architectures-and-real-configs.md) | drafted |
| V1-033 | Creating Training Data | [CH-33](chapters/part-09/33-data-sources-and-cleaning.md) | drafted |
| V1-034 | Next-Token Prediction | [CH-25](chapters/part-07/25-sequences-batches-and-pretraining.md) | drafted |
| V1-035 | Forward Pass | [CH-26](chapters/part-07/26-the-training-step-and-schedule.md) | drafted |
| V1-036 | Loss | [CH-26](chapters/part-07/26-the-training-step-and-schedule.md) | drafted |
| V1-037 | Backward Pass | [CH-26](chapters/part-07/26-the-training-step-and-schedule.md) | drafted |
| V1-038 | Optimizer Step | [CH-26](chapters/part-07/26-the-training-step-and-schedule.md) | drafted |
| V1-039 | Batch Size, Sequence Length and Training Dynamics | [CH-25](chapters/part-07/25-sequences-batches-and-pretraining.md) | drafted |
| V1-040 | Checkpoints | [CH-27](chapters/part-07/27-mixed-precision-and-checkpoint-anatomy.md) | drafted |
| V1-041 | Pretraining | [CH-25](chapters/part-07/25-sequences-batches-and-pretraining.md) | drafted |
| V1-042 | Continued Pretraining | [CH-37](chapters/part-10/37-pretraining-continued-pretraining-and-sft.md) | drafted |
| V1-043 | Supervised Fine-Tuning | [CH-37](chapters/part-10/37-pretraining-continued-pretraining-and-sft.md) | drafted |
| V1-044 | PEFT | [CH-38](chapters/part-10/38-parameter-efficient-adaptation.md) | drafted |
| V1-045 | Alignment / Preference Training | [CH-39](chapters/part-10/39-preferences-and-reinforcement-learning.md) | drafted |
| V1-046 | Distillation | [CH-40](chapters/part-10/40-reasoning-test-time-compute-and-distillation.md) | drafted |
| V1-047 | CPU vs GPU | [CH-41](chapters/part-11/41-why-gpus-and-how-they-execute.md) | drafted |
| V1-048 | GPU Architecture | [CH-41](chapters/part-11/41-why-gpus-and-how-they-execute.md) | drafted |
| V1-049 | GPU Memory Hierarchy | [CH-42](chapters/part-11/42-memory-hierarchy-and-movement.md) | drafted |
| V1-050 | Compute vs Memory Bandwidth | [CH-43](chapters/part-11/43-throughput-intensity-and-rooflines.md) | drafted |
| V1-051 | Matrix Multiplication on GPUs | [CH-45](chapters/part-12/45-kernels-gemm-and-tiling.md) | drafted |
| V1-052 | Kernels | [CH-45](chapters/part-12/45-kernels-gemm-and-tiling.md) | drafted |
| V1-053 | Kernel Launches and Fusion | [CH-45](chapters/part-12/45-kernels-gemm-and-tiling.md) | drafted |
| V1-054 | CUDA, Triton and Higher-Level Frameworks | [CH-46](chapters/part-12/46-cuda-triton-and-cutlass.md) | drafted |
| V1-055 | The Roofline Model | [CH-43](chapters/part-11/43-throughput-intensity-and-rooflines.md) | drafted |
| V1-056 | One Forward Pass Through a Real LLM | [CH-49](chapters/part-13/49-load-weights-and-trace-a-forward-pass.md) | drafted |
| V1-057 | Prefill | [CH-50](chapters/part-13/50-prefill-decode-and-kv-cache.md) | drafted |
| V1-058 | Decode | [CH-50](chapters/part-13/50-prefill-decode-and-kv-cache.md) | drafted |
| V1-059 | KV Cache | [CH-50](chapters/part-13/50-prefill-decode-and-kv-cache.md) | drafted |
| V1-060 | Sampling | [CH-51](chapters/part-13/51-sampling-and-decoding-policies.md) | drafted |
| V1-061 | Context Windows | [CH-50](chapters/part-13/50-prefill-decode-and-kv-cache.md) | drafted |
| V1-062 | Memory Accounting | [CH-52](chapters/part-13/52-inference-memory-and-latency-accounting.md) | drafted |
| V1-063 | Quantization | [CH-56](chapters/part-14/56-quantization-across-the-inference-path.md) | drafted |
| V1-064 | FlashAttention | [CH-53](chapters/part-14/53-flashattention-and-paged-kv-memory.md) | drafted |
| V1-065 | PagedAttention | [CH-53](chapters/part-14/53-flashattention-and-paged-kv-memory.md) | drafted |
| V1-066 | Continuous Batching | [CH-54](chapters/part-14/54-caching-batching-and-prefill-scheduling.md) | drafted |
| V1-067 | Prefix Caching | [CH-54](chapters/part-14/54-caching-batching-and-prefill-scheduling.md) | drafted |
| V1-068 | Chunked Prefill | [CH-54](chapters/part-14/54-caching-batching-and-prefill-scheduling.md) | drafted |
| V1-069 | Speculative Decoding | [CH-55](chapters/part-14/55-speculative-decoding-and-dynamic-execution.md) | drafted |
| V1-070 | Model Offloading | [CH-62](chapters/part-16/62-tenants-models-and-residency.md) | drafted |
| V1-071 | CPU Inference | [CH-65](chapters/part-17/65-cpu-and-edge-inference.md) | drafted |
| V1-072 | GPU Inference | [CH-49](chapters/part-13/49-load-weights-and-trace-a-forward-pass.md) | drafted |
| V1-073 | NPU / Accelerator Inference | [CH-67](chapters/part-17/67-local-runtimes-and-accelerators.md) | drafted |
| V1-074 | Why One GPU Stops Being Enough | [CH-57](chapters/part-15/57-parallel-training-strategies.md) | drafted |
| V1-075 | Data Parallelism | [CH-57](chapters/part-15/57-parallel-training-strategies.md) | drafted |
| V1-076 | Tensor Parallelism | [CH-58](chapters/part-15/58-partitioning-model-computation.md) | drafted |
| V1-077 | Pipeline Parallelism | [CH-58](chapters/part-15/58-partitioning-model-computation.md) | drafted |
| V1-078 | Sequence Parallelism | [CH-58](chapters/part-15/58-partitioning-model-computation.md) | drafted |
| V1-079 | Expert Parallelism | [CH-58](chapters/part-15/58-partitioning-model-computation.md) | drafted |
| V1-080 | Sharded Training | [CH-57](chapters/part-15/57-parallel-training-strategies.md) | drafted |
| V1-081 | Interconnects | [CH-59](chapters/part-15/59-collectives-and-interconnects.md) | drafted |
| V1-082 | Collective Communications | [CH-59](chapters/part-15/59-collectives-and-interconnects.md) | drafted |
| V1-083 | What an Inference Server Actually Does | [CH-61](chapters/part-16/61-anatomy-of-an-inference-server.md) | drafted |
| V1-084 | Request Scheduling | [CH-61](chapters/part-16/61-anatomy-of-an-inference-server.md) | drafted |
| V1-085 | Throughput vs Latency | [CH-64](chapters/part-16/64-production-serving-and-gpu-clusters.md) | drafted |
| V1-086 | Batching and Scheduling Policies | [CH-61](chapters/part-16/61-anatomy-of-an-inference-server.md) | drafted |
| V1-087 | KV-Cache Management | [CH-61](chapters/part-16/61-anatomy-of-an-inference-server.md) | drafted |
| V1-088 | Multi-Tenant Serving | [CH-62](chapters/part-16/62-tenants-models-and-residency.md) | drafted |
| V1-089 | Model Loading and Residency | [CH-62](chapters/part-16/62-tenants-models-and-residency.md) | drafted |
| V1-090 | Multi-Model Serving | [CH-62](chapters/part-16/62-tenants-models-and-residency.md) | drafted |
| V1-091 | Disaggregated Prefill and Decode | [CH-63](chapters/part-16/63-disaggregation-and-runtime-comparisons.md) | drafted |
| V1-092 | Failure Handling and Observability | [CH-64](chapters/part-16/64-production-serving-and-gpu-clusters.md) | drafted |
| V1-093 | vLLM / TensorRT-LLM / llama.cpp-Type Architectures | [CH-63](chapters/part-16/63-disaggregation-and-runtime-comparisons.md) | drafted |
| V1-094 | Why Edge Inference Is Different | [CH-65](chapters/part-17/65-cpu-and-edge-inference.md) | drafted |
| V1-095 | CPU + GPU Hybrid Execution | [CH-66](chapters/part-17/66-hybrid-memory-and-local-loading.md) | drafted |
| V1-096 | Unified Memory | [CH-66](chapters/part-17/66-hybrid-memory-and-local-loading.md) | drafted |
| V1-097 | Quantized Local Models | [CH-66](chapters/part-17/66-hybrid-memory-and-local-loading.md) | drafted |
| V1-098 | llama.cpp and GGUF Internals | [CH-66](chapters/part-17/66-hybrid-memory-and-local-loading.md) | drafted |
| V1-099 | OpenVINO / NPUs / Hardware-Specific Runtimes | [CH-67](chapters/part-17/67-local-runtimes-and-accelerators.md) | drafted |
| V1-100 | Model Loading and Memory Mapping | [CH-66](chapters/part-17/66-hybrid-memory-and-local-loading.md) | drafted |
| V1-101 | Pruning | [CH-55](chapters/part-14/55-speculative-decoding-and-dynamic-execution.md) | drafted |
| V1-102 | Distillation | [CH-40](chapters/part-10/40-reasoning-test-time-compute-and-distillation.md) | drafted |
| V1-103 | Dynamic Computation | [CH-68](chapters/part-17/68-packaging-power-and-thermal-limits.md) | drafted |
| V1-104 | Sentence and Document Embeddings | [CH-69](chapters/part-18/69-embeddings-contrastive-learning-and-vector-indexes.md) | drafted |
| V1-105 | Contrastive Learning | [CH-69](chapters/part-18/69-embeddings-contrastive-learning-and-vector-indexes.md) | drafted |
| V1-106 | Vector Search | [CH-69](chapters/part-18/69-embeddings-contrastive-learning-and-vector-indexes.md) | drafted |
| V1-107 | Approximate Nearest Neighbors | [CH-69](chapters/part-18/69-embeddings-contrastive-learning-and-vector-indexes.md) | drafted |
| V1-108 | Vector Databases | [CH-69](chapters/part-18/69-embeddings-contrastive-learning-and-vector-indexes.md) | drafted |
| V1-109 | RAG | [CH-70](chapters/part-18/70-rag-and-retrieval-quality.md) | drafted |
| V1-110 | Chunking and Retrieval | [CH-70](chapters/part-18/70-rag-and-retrieval-quality.md) | drafted |
| V1-111 | Reranking | [CH-70](chapters/part-18/70-rag-and-retrieval-quality.md) | drafted |
| V1-112 | Memory Systems | [CH-71](chapters/part-18/71-memory-tools-and-structured-output.md) | drafted |
| V1-113 | Why Generation Can Behave Like Reasoning | [CH-40](chapters/part-10/40-reasoning-test-time-compute-and-distillation.md) | drafted |
| V1-114 | Test-Time Compute | [CH-40](chapters/part-10/40-reasoning-test-time-compute-and-distillation.md) | drafted |
| V1-115 | Tool Calling | [CH-71](chapters/part-18/71-memory-tools-and-structured-output.md) | drafted |
| V1-116 | Structured Outputs | [CH-71](chapters/part-18/71-memory-tools-and-structured-output.md) | drafted |
| V1-117 | Agents | [CH-72](chapters/part-18/72-agents-and-multi-model-economics.md) | drafted |
| V1-118 | Planning | [CH-72](chapters/part-18/72-agents-and-multi-model-economics.md) | drafted |
| V1-119 | Multi-Agent Systems | [CH-72](chapters/part-18/72-agents-and-multi-model-economics.md) | drafted |
| V1-120 | Multi-LLM Systems | [CH-72](chapters/part-18/72-agents-and-multi-model-economics.md) | drafted |
| V1-121 | Cost of Agentic Systems | [CH-72](chapters/part-18/72-agents-and-multi-model-economics.md) | drafted |
| V1-122 | Hidden States | [CH-73](chapters/part-19/73-hidden-states-layers-and-attention-heads.md) | drafted |
| V1-123 | The Residual Stream | [CH-73](chapters/part-19/73-hidden-states-layers-and-attention-heads.md) | drafted |
| V1-124 | What Individual Layers Learn | [CH-73](chapters/part-19/73-hidden-states-layers-and-attention-heads.md) | drafted |
| V1-125 | Attention-Head Analysis | [CH-73](chapters/part-19/73-hidden-states-layers-and-attention-heads.md) | drafted |
| V1-126 | Probing | [CH-74](chapters/part-19/74-features-probes-and-mechanisms.md) | drafted |
| V1-127 | Activation Steering | [CH-75](chapters/part-19/75-steering-editing-and-representation-engineering.md) | drafted |
| V1-128 | Representation Engineering | [CH-75](chapters/part-19/75-steering-editing-and-representation-engineering.md) | drafted |
| V1-129 | Mechanistic Interpretability | [CH-74](chapters/part-19/74-features-probes-and-mechanisms.md) | drafted |
| V1-130 | Model Editing | [CH-75](chapters/part-19/75-steering-editing-and-representation-engineering.md) | drafted |
| V1-131 | Model Merging | [CH-76](chapters/part-19/76-merging-stitching-and-representation-compatibility.md) | drafted |
| V1-132 | Layer Stitching | [CH-76](chapters/part-19/76-merging-stitching-and-representation-compatibility.md) | drafted |
| V1-133 | KV-Cache Compression | [CH-77](chapters/part-20/77-efficient-memory-and-adaptive-computation.md) | drafted |
| V1-134 | KV Eviction | [CH-77](chapters/part-20/77-efficient-memory-and-adaptive-computation.md) | drafted |
| V1-135 | Prefix Reuse | [CH-77](chapters/part-20/77-efficient-memory-and-adaptive-computation.md) | drafted |
| V1-136 | Activation Compression | [CH-77](chapters/part-20/77-efficient-memory-and-adaptive-computation.md) | drafted |
| V1-137 | Early Exit | [CH-55](chapters/part-14/55-speculative-decoding-and-dynamic-execution.md) | drafted |
| V1-138 | Adaptive Computation | [CH-77](chapters/part-20/77-efficient-memory-and-adaptive-computation.md) | drafted |
| V1-139 | Dynamic Layer Skipping | [CH-77](chapters/part-20/77-efficient-memory-and-adaptive-computation.md) | drafted |
| V1-140 | Model Cascades | [CH-78](chapters/part-20/78-routable-intelligence-and-neural-handoffs.md) | drafted |
| V1-141 | Speculative Models | [CH-55](chapters/part-14/55-speculative-decoding-and-dynamic-execution.md) | drafted |
| V1-142 | Neural Handoffs | [CH-78](chapters/part-20/78-routable-intelligence-and-neural-handoffs.md) | drafted |
| V1-143 | Latent Model-to-Model Communication | [CH-78](chapters/part-20/78-routable-intelligence-and-neural-handoffs.md) | drafted |
| V1-144 | Cross-Model Representation Translation | [CH-78](chapters/part-20/78-routable-intelligence-and-neural-handoffs.md) | drafted |
| V1-145 | Sparse Expert Intervention | [CH-78](chapters/part-20/78-routable-intelligence-and-neural-handoffs.md) | drafted |
| V1-146 | LLM Call Elimination | [CH-78](chapters/part-20/78-routable-intelligence-and-neural-handoffs.md) | drafted |
| V1-147 | Computation as a Routable Resource | [CH-78](chapters/part-20/78-routable-intelligence-and-neural-handoffs.md) | drafted |
| V1-148 | Forming a Research Question | [CH-79](chapters/part-20/79-research-design-and-reproduction.md) | drafted |
| V1-149 | Literature Search | [CH-79](chapters/part-20/79-research-design-and-reproduction.md) | drafted |
| V1-150 | Baselines | [CH-79](chapters/part-20/79-research-design-and-reproduction.md) | drafted |
| V1-151 | Designing Experiments | [CH-79](chapters/part-20/79-research-design-and-reproduction.md) | drafted |
| V1-152 | Ablations | [CH-80](chapters/part-20/80-evidence-ablations-and-publication.md) | drafted |
| V1-153 | Benchmark Selection | [CH-79](chapters/part-20/79-research-design-and-reproduction.md) | drafted |
| V1-154 | Statistical Significance | [CH-80](chapters/part-20/80-evidence-ablations-and-publication.md) | drafted |
| V1-155 | Profiling Compute | [CH-80](chapters/part-20/80-evidence-ablations-and-publication.md) | drafted |
| V1-156 | Measuring FLOPs, Memory and Latency | [CH-80](chapters/part-20/80-evidence-ablations-and-publication.md) | drafted |
| V1-157 | Reproducibility | [CH-79](chapters/part-20/79-research-design-and-reproduction.md) | drafted |
| V1-158 | Reading Papers Critically | [CH-79](chapters/part-20/79-research-design-and-reproduction.md) | drafted |
| V1-159 | Writing a Research Paper | [CH-80](chapters/part-20/80-evidence-ablations-and-publication.md) | drafted |
| V1-160 | arXiv, Conferences and Peer Review | [CH-80](chapters/part-20/80-evidence-ablations-and-publication.md) | drafted |
| V1-161 | Finding Unanswered Questions | [CH-80](chapters/part-20/80-evidence-ablations-and-publication.md) | drafted |
| V2-001 | The LLM in One Picture | [CH-01](chapters/part-01/01-the-llm-in-one-picture.md) | drafted |
| V2-002 | Training vs Inference | [CH-02](chapters/part-01/02-training-vs-inference.md) | drafted |
| V2-003 | Anatomy of the Modern LLM Stack | [CH-03](chapters/part-01/03-anatomy-of-the-modern-llm-stack.md) | drafted |
| V2-004 | Building Our Tiny Laboratory | [CH-04](chapters/part-01/04-building-our-tiny-laboratory.md) | drafted |
| V2-005 | Scalars → Vectors → Matrices → Tensors | [CH-05](chapters/part-02/05-tensors-and-resource-accounting.md) | drafted |
| V2-006 | Shapes, Dimensions and Broadcasting | [CH-05](chapters/part-02/05-tensors-and-resource-accounting.md) | drafted |
| V2-007 | Matrix Multiplication | [CH-05](chapters/part-02/05-tensors-and-resource-accounting.md) | drafted |
| V2-008 | Vector Geometry | [CH-06](chapters/part-02/06-geometry-and-number-formats.md) | drafted |
| V2-009 | Probability for Language Models | [CH-07](chapters/part-02/07-probability-logits-and-loss.md) | drafted |
| V2-010 | Softmax, Logits and Cross-Entropy | [CH-07](chapters/part-02/07-probability-logits-and-loss.md) | drafted |
| V2-011 | Derivatives, Gradients and the Chain Rule | [CH-08](chapters/part-02/08-gradients-graphs-and-autodiff.md) | drafted |
| V2-012 | Computational Graphs | [CH-08](chapters/part-02/08-gradients-graphs-and-autodiff.md) | drafted |
| V2-013 | Automatic Differentiation | [CH-08](chapters/part-02/08-gradients-graphs-and-autodiff.md) | drafted |
| V2-014 | Linear Layers | [CH-09](chapters/part-03/09-linear-layers-and-nonlinearities.md) | drafted |
| V2-015 | Nonlinearities | [CH-09](chapters/part-03/09-linear-layers-and-nonlinearities.md) | drafted |
| V2-016 | Building a Tiny Neural Network | [CH-10](chapters/part-03/10-a-tiny-network-forward-and-backward.md) | drafted |
| V2-017 | Forward Propagation | [CH-10](chapters/part-03/10-a-tiny-network-forward-and-backward.md) | drafted |
| V2-018 | Backpropagation by Hand | [CH-10](chapters/part-03/10-a-tiny-network-forward-and-backward.md) | drafted |
| V2-019 | Optimizers: SGD → AdamW | [CH-11](chapters/part-03/11-optimization-and-state.md) | drafted |
| V2-020 | Initialization and Training Stability | [CH-12](chapters/part-03/12-initialization-and-training-stability.md) | drafted |
| V2-021 | Why Machines Need Tokens | [CH-13](chapters/part-04/13-tokenization-algorithms.md) | drafted |
| V2-022 | Characters, Words and Subwords | [CH-13](chapters/part-04/13-tokenization-algorithms.md) | drafted |
| V2-023 | BPE From Scratch | [CH-13](chapters/part-04/13-tokenization-algorithms.md) | drafted |
| V2-024 | Vocabulary and Token IDs | [CH-14](chapters/part-04/14-vocabulary-and-token-ids.md) | drafted |
| V2-025 | Embedding Matrices | [CH-15](chapters/part-04/15-embedding-matrices-and-geometry.md) | drafted |
| V2-026 | Representation Geometry | [CH-15](chapters/part-04/15-embedding-matrices-and-geometry.md) | drafted |
| V2-027 | Position and Sequence Order | [CH-16](chapters/part-04/16-position-and-sequence-order.md) | drafted |
| V2-028 | Why Sequence Modeling Is Hard | [CH-17](chapters/part-05/17-sequence-modeling-and-the-attention-idea.md) | drafted |
| V2-029 | The Attention Idea | [CH-17](chapters/part-05/17-sequence-modeling-and-the-attention-idea.md) | drafted |
| V2-030 | Query, Key and Value | [CH-18](chapters/part-05/18-queries-keys-values-and-scaling.md) | drafted |
| V2-031 | Scaled Dot-Product Attention | [CH-18](chapters/part-05/18-queries-keys-values-and-scaling.md) | drafted |
| V2-032 | Causal Attention | [CH-19](chapters/part-05/19-causal-and-multi-head-attention.md) | drafted |
| V2-033 | Multi-Head Attention | [CH-19](chapters/part-05/19-causal-and-multi-head-attention.md) | drafted |
| V2-034 | Attention Tensor Shapes and Compute Cost | [CH-20](chapters/part-05/20-attention-shapes-and-compute-cost.md) | drafted |
| V2-035 | Residual Streams | [CH-21](chapters/part-06/21-residual-streams-and-normalization.md) | drafted |
| V2-036 | Normalization: LayerNorm and RMSNorm | [CH-21](chapters/part-06/21-residual-streams-and-normalization.md) | drafted |
| V2-037 | Feed-Forward Networks | [CH-22](chapters/part-06/22-feed-forward-networks-and-complete-blocks.md) | drafted |
| V2-038 | Complete Transformer Block | [CH-22](chapters/part-06/22-feed-forward-networks-and-complete-blocks.md) | drafted |
| V2-039 | Stack the Blocks | [CH-23](chapters/part-06/23-stacking-vocabulary-projection-and-tying.md) | drafted |
| V2-040 | Vocabulary Projection / LM Head | [CH-23](chapters/part-06/23-stacking-vocabulary-projection-and-tying.md) | drafted |
| V2-041 | Weight Tying | [CH-23](chapters/part-06/23-stacking-vocabulary-projection-and-tying.md) | drafted |
| V2-042 | Build Our GPT From Scratch | [CH-24](chapters/part-06/24-build-our-gpt-from-scratch.md) | drafted |
| V2-043 | Preparing Training Sequences | [CH-25](chapters/part-07/25-sequences-batches-and-pretraining.md) | drafted |
| V2-044 | Batches and Mini-Batches | [CH-25](chapters/part-07/25-sequences-batches-and-pretraining.md) | drafted |
| V2-045 | Next-Token Prediction | [CH-25](chapters/part-07/25-sequences-batches-and-pretraining.md) | drafted |
| V2-046 | The Forward Pass | [CH-26](chapters/part-07/26-the-training-step-and-schedule.md) | drafted |
| V2-047 | Loss | [CH-26](chapters/part-07/26-the-training-step-and-schedule.md) | drafted |
| V2-048 | Backward Pass | [CH-26](chapters/part-07/26-the-training-step-and-schedule.md) | drafted |
| V2-049 | Optimizer State | [CH-26](chapters/part-07/26-the-training-step-and-schedule.md) | drafted |
| V2-050 | Learning Rates and Warmup | [CH-26](chapters/part-07/26-the-training-step-and-schedule.md) | drafted |
| V2-051 | Gradient Accumulation and Clipping | [CH-26](chapters/part-07/26-the-training-step-and-schedule.md) | drafted |
| V2-052 | Mixed-Precision Training | [CH-27](chapters/part-07/27-mixed-precision-and-checkpoint-anatomy.md) | drafted |
| V2-053 | Checkpoints | [CH-27](chapters/part-07/27-mixed-precision-and-checkpoint-anatomy.md) | drafted |
| V2-054 | Debugging Training | [CH-28](chapters/part-07/28-debugging-and-training-our-tiny-model.md) | drafted |
| V2-055 | GPT → Llama-Type Architectures | [CH-29](chapters/part-08/29-transformer-families.md) | drafted |
| V2-056 | RoPE Deep Dive | [CH-30](chapters/part-08/30-modern-positions-heads-and-mlps.md) | drafted |
| V2-057 | MHA → MQA → GQA | [CH-30](chapters/part-08/30-modern-positions-heads-and-mlps.md) | drafted |
| V2-058 | Modern MLPs | [CH-30](chapters/part-08/30-modern-positions-heads-and-mlps.md) | drafted |
| V2-059 | Mixture of Experts | [CH-31](chapters/part-08/31-mixture-of-experts.md) | drafted |
| V2-060 | Sparse and Alternative Attention | [CH-32](chapters/part-08/32-alternative-architectures-and-real-configs.md) | drafted |
| V2-061 | State-Space and Hybrid Models | [CH-32](chapters/part-08/32-alternative-architectures-and-real-configs.md) | drafted |
| V2-062 | Reading a Real Model Config | [CH-32](chapters/part-08/32-alternative-architectures-and-real-configs.md) | drafted |
| V2-063 | Where Training Data Comes From | [CH-33](chapters/part-09/33-data-sources-and-cleaning.md) | drafted |
| V2-064 | Cleaning and Filtering | [CH-33](chapters/part-09/33-data-sources-and-cleaning.md) | drafted |
| V2-065 | Deduplication | [CH-33](chapters/part-09/33-data-sources-and-cleaning.md) | drafted |
| V2-066 | Dataset Mixtures | [CH-34](chapters/part-09/34-mixtures-tokens-and-synthetic-data.md) | drafted |
| V2-067 | Token Budgets | [CH-34](chapters/part-09/34-mixtures-tokens-and-synthetic-data.md) | drafted |
| V2-068 | Synthetic Data | [CH-34](chapters/part-09/34-mixtures-tokens-and-synthetic-data.md) | drafted |
| V2-069 | Contamination | [CH-34](chapters/part-09/34-mixtures-tokens-and-synthetic-data.md) | drafted |
| V2-070 | Evaluation | [CH-35](chapters/part-09/35-evaluation-and-meaningful-experiments.md) | drafted |
| V2-071 | Scaling Laws | [CH-36](chapters/part-09/36-scaling-laws.md) | drafted |
| V2-072 | Experimental Design | [CH-35](chapters/part-09/35-evaluation-and-meaningful-experiments.md) | drafted |
| V2-073 | Pretraining vs Post-Training | [CH-37](chapters/part-10/37-pretraining-continued-pretraining-and-sft.md) | drafted |
| V2-074 | Supervised Fine-Tuning | [CH-37](chapters/part-10/37-pretraining-continued-pretraining-and-sft.md) | drafted |
| V2-075 | LoRA and QLoRA | [CH-38](chapters/part-10/38-parameter-efficient-adaptation.md) | drafted |
| V2-076 | Preference Data | [CH-39](chapters/part-10/39-preferences-and-reinforcement-learning.md) | drafted |
| V2-077 | Reward Models | [CH-39](chapters/part-10/39-preferences-and-reinforcement-learning.md) | drafted |
| V2-078 | RLHF | [CH-39](chapters/part-10/39-preferences-and-reinforcement-learning.md) | drafted |
| V2-079 | DPO-Type Objectives | [CH-39](chapters/part-10/39-preferences-and-reinforcement-learning.md) | drafted |
| V2-080 | RL With Verifiable Rewards | [CH-40](chapters/part-10/40-reasoning-test-time-compute-and-distillation.md) | drafted |
| V2-081 | Reasoning Models | [CH-40](chapters/part-10/40-reasoning-test-time-compute-and-distillation.md) | drafted |
| V2-082 | Test-Time Compute | [CH-40](chapters/part-10/40-reasoning-test-time-compute-and-distillation.md) | drafted |
| V2-083 | Distillation | [CH-40](chapters/part-10/40-reasoning-test-time-compute-and-distillation.md) | drafted |
| V2-084 | Why GPUs | [CH-41](chapters/part-11/41-why-gpus-and-how-they-execute.md) | drafted |
| V2-085 | GPU Anatomy | [CH-41](chapters/part-11/41-why-gpus-and-how-they-execute.md) | drafted |
| V2-086 | Threads, Warps and Blocks | [CH-41](chapters/part-11/41-why-gpus-and-how-they-execute.md) | drafted |
| V2-087 | Memory Hierarchy | [CH-42](chapters/part-11/42-memory-hierarchy-and-movement.md) | drafted |
| V2-088 | HBM Bandwidth | [CH-42](chapters/part-11/42-memory-hierarchy-and-movement.md) | drafted |
| V2-089 | Compute Throughput | [CH-43](chapters/part-11/43-throughput-intensity-and-rooflines.md) | drafted |
| V2-090 | Arithmetic Intensity | [CH-43](chapters/part-11/43-throughput-intensity-and-rooflines.md) | drafted |
| V2-091 | Compute-Bound vs Memory-Bound | [CH-43](chapters/part-11/43-throughput-intensity-and-rooflines.md) | drafted |
| V2-092 | Roofline Model | [CH-43](chapters/part-11/43-throughput-intensity-and-rooflines.md) | drafted |
| V2-093 | What a GPU Kernel Is | [CH-45](chapters/part-12/45-kernels-gemm-and-tiling.md) | drafted |
| V2-094 | GEMM | [CH-45](chapters/part-12/45-kernels-gemm-and-tiling.md) | drafted |
| V2-095 | Tiling | [CH-45](chapters/part-12/45-kernels-gemm-and-tiling.md) | drafted |
| V2-096 | Tensor Cores | [CH-45](chapters/part-12/45-kernels-gemm-and-tiling.md) | drafted |
| V2-097 | Kernel Launch Overhead | [CH-45](chapters/part-12/45-kernels-gemm-and-tiling.md) | drafted |
| V2-098 | Kernel Fusion | [CH-45](chapters/part-12/45-kernels-gemm-and-tiling.md) | drafted |
| V2-099 | CUDA | [CH-46](chapters/part-12/46-cuda-triton-and-cutlass.md) | drafted |
| V2-100 | Triton | [CH-46](chapters/part-12/46-cuda-triton-and-cutlass.md) | drafted |
| V2-101 | CUTLASS-Level Concepts | [CH-46](chapters/part-12/46-cuda-triton-and-cutlass.md) | drafted |
| V2-102 | Profiling | [CH-46](chapters/part-12/46-cuda-triton-and-cutlass.md) | drafted |
| V2-103 | PyTorch Eager Execution | [CH-47](chapters/part-12/47-graphs-compilers-and-runtimes.md) | drafted |
| V2-104 | Computational Graph Capture | [CH-47](chapters/part-12/47-graphs-compilers-and-runtimes.md) | drafted |
| V2-105 | torch.compile / Dynamo / Inductor | [CH-47](chapters/part-12/47-graphs-compilers-and-runtimes.md) | drafted |
| V2-106 | CUDA Graphs | [CH-48](chapters/part-12/48-cuda-graphs-and-execution-overhead.md) | drafted |
| V2-107 | Loading Model Weights | [CH-49](chapters/part-13/49-load-weights-and-trace-a-forward-pass.md) | drafted |
| V2-108 | Prompt Processing | [CH-49](chapters/part-13/49-load-weights-and-trace-a-forward-pass.md) | drafted |
| V2-109 | Prefill | [CH-50](chapters/part-13/50-prefill-decode-and-kv-cache.md) | drafted |
| V2-110 | Autoregressive Decode | [CH-50](chapters/part-13/50-prefill-decode-and-kv-cache.md) | drafted |
| V2-111 | KV Cache | [CH-50](chapters/part-13/50-prefill-decode-and-kv-cache.md) | drafted |
| V2-112 | Sampling | [CH-51](chapters/part-13/51-sampling-and-decoding-policies.md) | drafted |
| V2-113 | Context Length | [CH-50](chapters/part-13/50-prefill-decode-and-kv-cache.md) | drafted |
| V2-114 | Latency Accounting | [CH-52](chapters/part-13/52-inference-memory-and-latency-accounting.md) | drafted |
| V2-115 | Why Naïve Inference Is Slow | [CH-53](chapters/part-14/53-flashattention-and-paged-kv-memory.md) | drafted |
| V2-116 | FlashAttention | [CH-53](chapters/part-14/53-flashattention-and-paged-kv-memory.md) | drafted |
| V2-117 | KV Cache Layout | [CH-53](chapters/part-14/53-flashattention-and-paged-kv-memory.md) | drafted |
| V2-118 | Paged KV Memory | [CH-53](chapters/part-14/53-flashattention-and-paged-kv-memory.md) | drafted |
| V2-119 | Prefix Caching | [CH-54](chapters/part-14/54-caching-batching-and-prefill-scheduling.md) | drafted |
| V2-120 | Continuous Batching | [CH-54](chapters/part-14/54-caching-batching-and-prefill-scheduling.md) | drafted |
| V2-121 | Chunked Prefill | [CH-54](chapters/part-14/54-caching-batching-and-prefill-scheduling.md) | drafted |
| V2-122 | Speculative Decoding | [CH-55](chapters/part-14/55-speculative-decoding-and-dynamic-execution.md) | drafted |
| V2-123 | Quantization | [CH-56](chapters/part-14/56-quantization-across-the-inference-path.md) | drafted |
| V2-124 | Sparsity | [CH-55](chapters/part-14/55-speculative-decoding-and-dynamic-execution.md) | drafted |
| V2-125 | Early Exit / Layer Skipping | [CH-55](chapters/part-14/55-speculative-decoding-and-dynamic-execution.md) | drafted |
| V2-126 | CUDA Graph Optimization | [CH-55](chapters/part-14/55-speculative-decoding-and-dynamic-execution.md) | drafted |
| V2-127 | Why One Accelerator Stops Being Enough | [CH-57](chapters/part-15/57-parallel-training-strategies.md) | drafted |
| V2-128 | Data Parallelism | [CH-57](chapters/part-15/57-parallel-training-strategies.md) | drafted |
| V2-129 | Tensor Parallelism | [CH-58](chapters/part-15/58-partitioning-model-computation.md) | drafted |
| V2-130 | Pipeline Parallelism | [CH-58](chapters/part-15/58-partitioning-model-computation.md) | drafted |
| V2-131 | Sequence/Context Parallelism | [CH-58](chapters/part-15/58-partitioning-model-computation.md) | drafted |
| V2-132 | Expert Parallelism | [CH-58](chapters/part-15/58-partitioning-model-computation.md) | drafted |
| V2-133 | ZeRO / FSDP Concepts | [CH-57](chapters/part-15/57-parallel-training-strategies.md) | drafted |
| V2-134 | Collectives | [CH-59](chapters/part-15/59-collectives-and-interconnects.md) | drafted |
| V2-135 | NCCL | [CH-59](chapters/part-15/59-collectives-and-interconnects.md) | drafted |
| V2-136 | PCIe, NVLink, NVSwitch, InfiniBand | [CH-59](chapters/part-15/59-collectives-and-interconnects.md) | drafted |
| V2-137 | Distributed Training Failures | [CH-60](chapters/part-15/60-distributed-execution-and-failure-recovery.md) | drafted |
| V2-138 | Distributed Inference | [CH-60](chapters/part-15/60-distributed-execution-and-failure-recovery.md) | drafted |
| V2-139 | Anatomy of an Inference Server | [CH-61](chapters/part-16/61-anatomy-of-an-inference-server.md) | drafted |
| V2-140 | Request Queues | [CH-61](chapters/part-16/61-anatomy-of-an-inference-server.md) | drafted |
| V2-141 | Scheduling | [CH-61](chapters/part-16/61-anatomy-of-an-inference-server.md) | drafted |
| V2-142 | Dynamic/Continuous Batching | [CH-61](chapters/part-16/61-anatomy-of-an-inference-server.md) | drafted |
| V2-143 | KV-Cache Allocation | [CH-61](chapters/part-16/61-anatomy-of-an-inference-server.md) | drafted |
| V2-144 | Multi-Tenant Serving | [CH-62](chapters/part-16/62-tenants-models-and-residency.md) | drafted |
| V2-145 | Multi-Model Serving | [CH-62](chapters/part-16/62-tenants-models-and-residency.md) | drafted |
| V2-146 | Prefill/Decode Disaggregation | [CH-63](chapters/part-16/63-disaggregation-and-runtime-comparisons.md) | drafted |
| V2-147 | Memory Residency and Model Loading | [CH-62](chapters/part-16/62-tenants-models-and-residency.md) | drafted |
| V2-148 | Throughput vs Latency | [CH-64](chapters/part-16/64-production-serving-and-gpu-clusters.md) | drafted |
| V2-149 | Observability | [CH-64](chapters/part-16/64-production-serving-and-gpu-clusters.md) | drafted |
| V2-150 | Autoscaling | [CH-64](chapters/part-16/64-production-serving-and-gpu-clusters.md) | drafted |
| V2-151 | Failure Recovery | [CH-64](chapters/part-16/64-production-serving-and-gpu-clusters.md) | drafted |
| V2-152 | GPU Cluster Scheduling | [CH-64](chapters/part-16/64-production-serving-and-gpu-clusters.md) | drafted |
| V2-153 | Edge Constraints | [CH-65](chapters/part-17/65-cpu-and-edge-inference.md) | drafted |
| V2-154 | CPU Inference | [CH-65](chapters/part-17/65-cpu-and-edge-inference.md) | drafted |
| V2-155 | SIMD / CPU Vectorization | [CH-65](chapters/part-17/65-cpu-and-edge-inference.md) | drafted |
| V2-156 | GPU Offloading | [CH-66](chapters/part-17/66-hybrid-memory-and-local-loading.md) | drafted |
| V2-157 | Unified/Shared Memory | [CH-66](chapters/part-17/66-hybrid-memory-and-local-loading.md) | drafted |
| V2-158 | Quantized Formats | [CH-66](chapters/part-17/66-hybrid-memory-and-local-loading.md) | drafted |
| V2-159 | Memory Mapping | [CH-66](chapters/part-17/66-hybrid-memory-and-local-loading.md) | drafted |
| V2-160 | llama.cpp Internals | [CH-67](chapters/part-17/67-local-runtimes-and-accelerators.md) | drafted |
| V2-161 | OpenVINO / NPUs | [CH-67](chapters/part-17/67-local-runtimes-and-accelerators.md) | drafted |
| V2-162 | Power and Thermal Limits | [CH-68](chapters/part-17/68-packaging-power-and-thermal-limits.md) | drafted |
| V2-163 | Startup and Model Loading | [CH-66](chapters/part-17/66-hybrid-memory-and-local-loading.md) | drafted |
| V2-164 | Model Packaging | [CH-68](chapters/part-17/68-packaging-power-and-thermal-limits.md) | drafted |
| V2-165 | Embeddings Revisited | [CH-69](chapters/part-18/69-embeddings-contrastive-learning-and-vector-indexes.md) | drafted |
| V2-166 | Contrastive Embedding Training | [CH-69](chapters/part-18/69-embeddings-contrastive-learning-and-vector-indexes.md) | drafted |
| V2-167 | Vector Search | [CH-69](chapters/part-18/69-embeddings-contrastive-learning-and-vector-indexes.md) | drafted |
| V2-168 | Approximate Nearest Neighbors | [CH-69](chapters/part-18/69-embeddings-contrastive-learning-and-vector-indexes.md) | drafted |
| V2-169 | RAG | [CH-70](chapters/part-18/70-rag-and-retrieval-quality.md) | drafted |
| V2-170 | Reranking | [CH-70](chapters/part-18/70-rag-and-retrieval-quality.md) | drafted |
| V2-171 | Long-Term Memory | [CH-71](chapters/part-18/71-memory-tools-and-structured-output.md) | drafted |
| V2-172 | Tool Calling | [CH-71](chapters/part-18/71-memory-tools-and-structured-output.md) | drafted |
| V2-173 | Agents | [CH-72](chapters/part-18/72-agents-and-multi-model-economics.md) | drafted |
| V2-174 | Planning | [CH-72](chapters/part-18/72-agents-and-multi-model-economics.md) | drafted |
| V2-175 | Multi-Agent Systems | [CH-72](chapters/part-18/72-agents-and-multi-model-economics.md) | drafted |
| V2-176 | Multi-LLM Systems | [CH-72](chapters/part-18/72-agents-and-multi-model-economics.md) | drafted |
| V2-177 | Agent Compute Economics | [CH-72](chapters/part-18/72-agents-and-multi-model-economics.md) | drafted |
| V2-178 | Hidden States | [CH-73](chapters/part-19/73-hidden-states-layers-and-attention-heads.md) | drafted |
| V2-179 | Residual Stream | [CH-73](chapters/part-19/73-hidden-states-layers-and-attention-heads.md) | drafted |
| V2-180 | Representation Geometry | [CH-73](chapters/part-19/73-hidden-states-layers-and-attention-heads.md) | drafted |
| V2-181 | Attention Heads | [CH-73](chapters/part-19/73-hidden-states-layers-and-attention-heads.md) | drafted |
| V2-182 | Neurons and Features | [CH-74](chapters/part-19/74-features-probes-and-mechanisms.md) | drafted |
| V2-183 | Probing | [CH-74](chapters/part-19/74-features-probes-and-mechanisms.md) | drafted |
| V2-184 | Sparse Autoencoders | [CH-74](chapters/part-19/74-features-probes-and-mechanisms.md) | drafted |
| V2-185 | Activation Steering | [CH-75](chapters/part-19/75-steering-editing-and-representation-engineering.md) | drafted |
| V2-186 | Mechanistic Interpretability | [CH-74](chapters/part-19/74-features-probes-and-mechanisms.md) | drafted |
| V2-187 | Model Editing | [CH-75](chapters/part-19/75-steering-editing-and-representation-engineering.md) | drafted |
| V2-188 | Model Merging | [CH-76](chapters/part-19/76-merging-stitching-and-representation-compatibility.md) | drafted |
| V2-189 | Layer Stitching | [CH-76](chapters/part-19/76-merging-stitching-and-representation-compatibility.md) | drafted |
| V2-190 | Efficient KV Memory | [CH-77](chapters/part-20/77-efficient-memory-and-adaptive-computation.md) | drafted |
| V2-191 | Dynamic Computation | [CH-77](chapters/part-20/77-efficient-memory-and-adaptive-computation.md) | drafted |
| V2-192 | Conditional Layer Execution | [CH-77](chapters/part-20/77-efficient-memory-and-adaptive-computation.md) | drafted |
| V2-193 | Neural Routing | [CH-78](chapters/part-20/78-routable-intelligence-and-neural-handoffs.md) | drafted |
| V2-194 | Model Cascades | [CH-78](chapters/part-20/78-routable-intelligence-and-neural-handoffs.md) | drafted |
| V2-195 | Latent Communication | [CH-78](chapters/part-20/78-routable-intelligence-and-neural-handoffs.md) | drafted |
| V2-196 | Cross-Model Representations | [CH-78](chapters/part-20/78-routable-intelligence-and-neural-handoffs.md) | drafted |
| V2-197 | Neural Handoffs | [CH-78](chapters/part-20/78-routable-intelligence-and-neural-handoffs.md) | drafted |
| V2-198 | Sparse Expert Intervention | [CH-78](chapters/part-20/78-routable-intelligence-and-neural-handoffs.md) | drafted |
| V2-199 | LLM Dead-Call Elimination | [CH-78](chapters/part-20/78-routable-intelligence-and-neural-handoffs.md) | drafted |
| V2-200 | Computation as a Routable Resource | [CH-78](chapters/part-20/78-routable-intelligence-and-neural-handoffs.md) | drafted |
| V2-201 | Designing a Research Experiment | [CH-79](chapters/part-20/79-research-design-and-reproduction.md) | drafted |
| V2-202 | Reproducing Papers | [CH-79](chapters/part-20/79-research-design-and-reproduction.md) | drafted |
| V2-203 | Ablations | [CH-80](chapters/part-20/80-evidence-ablations-and-publication.md) | drafted |
| V2-204 | Profiling Research Claims | [CH-80](chapters/part-20/80-evidence-ablations-and-publication.md) | drafted |
| V2-205 | Writing Papers | [CH-80](chapters/part-20/80-evidence-ablations-and-publication.md) | drafted |
| V2-206 | Finding Questions Nobody Has Answered Yet | [CH-80](chapters/part-20/80-evidence-ablations-and-publication.md) | drafted |
| AUDIT-001 | Indexing, transpose and batch dimensions | [CH-05](chapters/part-02/05-tensors-and-resource-accounting.md) | drafted |
| AUDIT-002 | Magnitude, basis, subspaces, orthogonality and linear transformations | [CH-06](chapters/part-02/06-geometry-and-number-formats.md) | drafted |
| AUDIT-003 | Conditional probability, likelihood, log-probability, entropy and KL divergence | [CH-07](chapters/part-02/07-probability-logits-and-loss.md) | drafted |
| AUDIT-004 | Momentum and learning-rate schedules | [CH-11](chapters/part-03/11-optimization-and-state.md) | drafted |
| AUDIT-005 | FP32, FP16, BF16, FP8, INT8, INT4, overflow, underflow and numerical stability | [CH-06](chapters/part-02/06-geometry-and-number-formats.md) | drafted |
| AUDIT-006 | WordPiece, SentencePiece, byte-level tokenization and special tokens | [CH-13](chapters/part-04/13-tokenization-algorithms.md) | drafted |
| AUDIT-007 | Relative positional representations | [CH-16](chapters/part-04/16-position-and-sequence-order.md) | drafted |
| AUDIT-008 | Static vs contextual embeddings | [CH-15](chapters/part-04/15-embedding-matrices-and-geometry.md) | drafted |
| AUDIT-009 | RNNs, LSTMs and sequence bottlenecks | [CH-17](chapters/part-05/17-sequence-modeling-and-the-attention-idea.md) | drafted |
| AUDIT-010 | Pre-norm vs post-norm | [CH-21](chapters/part-06/21-residual-streams-and-normalization.md) | drafted |
| AUDIT-011 | Encoder-only/BERT and encoder-decoder/T5 | [CH-29](chapters/part-08/29-transformer-families.md) | drafted |
| AUDIT-012 | Sliding-window, local and global attention | [CH-32](chapters/part-08/32-alternative-architectures-and-real-configs.md) | drafted |
| AUDIT-013 | MoE sparse activation, routing, capacity and load balancing | [CH-31](chapters/part-08/31-mixture-of-experts.md) | drafted |
| AUDIT-014 | State-space and recurrent hybrid models | [CH-32](chapters/part-08/32-alternative-architectures-and-real-configs.md) | drafted |
| AUDIT-015 | Sequence packing | [CH-25](chapters/part-07/25-sequences-batches-and-pretraining.md) | drafted |
| AUDIT-016 | Optimizer updates: exactly which tensors and states change | [CH-26](chapters/part-07/26-the-training-step-and-schedule.md) | drafted |
| AUDIT-017 | Batch size, sequence length and training dynamics | [CH-25](chapters/part-07/25-sequences-batches-and-pretraining.md) | drafted |
| AUDIT-018 | Checkpoint weights, config, tokenizer, optimizer and scheduler state | [CH-27](chapters/part-07/27-mixed-precision-and-checkpoint-anatomy.md) | drafted |
| AUDIT-019 | Explicit full pretraining | [CH-25](chapters/part-07/25-sequences-batches-and-pretraining.md) | drafted |
| AUDIT-020 | Continued pretraining | [CH-37](chapters/part-10/37-pretraining-continued-pretraining-and-sft.md) | drafted |
| AUDIT-021 | PEFT adapters, prefix tuning and prompt tuning | [CH-38](chapters/part-10/38-parameter-efficient-adaptation.md) | drafted |
| AUDIT-022 | PPO | [CH-39](chapters/part-10/39-preferences-and-reinforcement-learning.md) | drafted |
| AUDIT-023 | Memory hierarchy through registers, shared/SRAM, caches, HBM, RAM and SSD | [CH-42](chapters/part-11/42-memory-hierarchy-and-movement.md) | drafted |
| AUDIT-024 | Dedicated end-to-end real-model forward-pass trace | [CH-49](chapters/part-13/49-load-weights-and-trace-a-forward-pass.md) | drafted |
| AUDIT-025 | Greedy, temperature, top-k, top-p and beam search | [CH-51](chapters/part-13/51-sampling-and-decoding-policies.md) | drafted |
| AUDIT-026 | Worked inference weights, KV, activations and overhead memory calculations | [CH-52](chapters/part-13/52-inference-memory-and-latency-accounting.md) | drafted |
| AUDIT-027 | PTQ, QAT, GPTQ, AWQ, GGUF and separate weight/activation/KV quantization | [CH-56](chapters/part-14/56-quantization-across-the-inference-path.md) | drafted |
| AUDIT-028 | Generic GPU-RAM-SSD model offloading | [CH-62](chapters/part-16/62-tenants-models-and-residency.md) | drafted |
| AUDIT-029 | Explicit GPU inference system treatment | [CH-49](chapters/part-13/49-load-weights-and-trace-a-forward-pass.md) | drafted |
| AUDIT-030 | DDP to ZeRO to FSDP progression | [CH-57](chapters/part-15/57-parallel-training-strategies.md) | drafted |
| AUDIT-031 | Broadcast collective | [CH-59](chapters/part-15/59-collectives-and-interconnects.md) | drafted |
| AUDIT-032 | TTFT, TPOT, tokens/s, req/s and p95/p99 serving metrics | [CH-64](chapters/part-16/64-production-serving-and-gpu-clusters.md) | drafted |
| AUDIT-033 | vLLM, TensorRT-LLM and llama.cpp architecture comparison | [CH-63](chapters/part-16/63-disaggregation-and-runtime-comparisons.md) | drafted |
| AUDIT-034 | CPU-GPU hybrid and unified/shared memory | [CH-66](chapters/part-17/66-hybrid-memory-and-local-loading.md) | drafted |
| AUDIT-035 | Pruning explicitly | [CH-55](chapters/part-14/55-speculative-decoding-and-dynamic-execution.md) | drafted |
| AUDIT-036 | Edge distillation and dynamic edge computation | [CH-68](chapters/part-17/68-packaging-power-and-thermal-limits.md) | drafted |
| AUDIT-037 | Sentence vs document embeddings | [CH-69](chapters/part-18/69-embeddings-contrastive-learning-and-vector-indexes.md) | drafted |
| AUDIT-038 | HNSW, IVF, product quantization and vector databases | [CH-69](chapters/part-18/69-embeddings-contrastive-learning-and-vector-indexes.md) | drafted |
| AUDIT-039 | Chunking, retrieval strategies and retrieval evaluation | [CH-70](chapters/part-18/70-rag-and-retrieval-quality.md) | drafted |
| AUDIT-040 | Short-term vs persistent memory | [CH-71](chapters/part-18/71-memory-tools-and-structured-output.md) | drafted |
| AUDIT-041 | Why generation can produce reasoning-like behavior | [CH-40](chapters/part-10/40-reasoning-test-time-compute-and-distillation.md) | drafted |
| AUDIT-042 | Structured output and constrained decoding | [CH-71](chapters/part-18/71-memory-tools-and-structured-output.md) | drafted |
| AUDIT-043 | What individual layers learn and layer specialization | [CH-73](chapters/part-19/73-hidden-states-layers-and-attention-heads.md) | drafted |
| AUDIT-044 | Representation engineering | [CH-75](chapters/part-19/75-steering-editing-and-representation-engineering.md) | drafted |
| AUDIT-045 | KV-cache compression and eviction | [CH-77](chapters/part-20/77-efficient-memory-and-adaptive-computation.md) | drafted |
| AUDIT-046 | Activation compression | [CH-77](chapters/part-20/77-efficient-memory-and-adaptive-computation.md) | drafted |
| AUDIT-047 | Explicit early exit | [CH-55](chapters/part-14/55-speculative-decoding-and-dynamic-execution.md) | drafted |
| AUDIT-048 | Draft/verifier speculative-model architectures | [CH-55](chapters/part-14/55-speculative-decoding-and-dynamic-execution.md) | drafted |
| AUDIT-049 | Forming research questions, literature review and prior-art search | [CH-79](chapters/part-20/79-research-design-and-reproduction.md) | drafted |
| AUDIT-050 | Baseline and benchmark selection | [CH-79](chapters/part-20/79-research-design-and-reproduction.md) | drafted |
| AUDIT-051 | Statistical significance, uncertainty and confidence intervals | [CH-80](chapters/part-20/80-evidence-ablations-and-publication.md) | drafted |
| AUDIT-052 | Reproducibility and critical paper reading | [CH-79](chapters/part-20/79-research-design-and-reproduction.md) | drafted |
| AUDIT-053 | Scientific claims vs engineering claims | [CH-79](chapters/part-20/79-research-design-and-reproduction.md) | drafted |
| AUDIT-054 | arXiv, workshops, conferences and peer review | [CH-80](chapters/part-20/80-evidence-ablations-and-publication.md) | drafted |
| FRAME-001 | Resource accounting from the mathematical foundations onward | [CH-05](chapters/part-02/05-tensors-and-resource-accounting.md) | drafted |
| FRAME-002 | Follow the Token throughout the curriculum | [CH-01](chapters/part-01/01-the-llm-in-one-picture.md) | drafted |
| FRAME-003 | Follow the Gradient throughout the curriculum | [CH-02](chapters/part-01/02-training-vs-inference.md) | drafted |
| FRAME-004 | Follow the Byte throughout the curriculum | [CH-05](chapters/part-02/05-tensors-and-resource-accounting.md) | drafted |
| FRAME-005 | Follow the Request throughout the curriculum | [CH-61](chapters/part-16/61-anatomy-of-an-inference-server.md) | drafted |
| FRAME-006 | Tokenizer from scratch milestone | [CH-13](chapters/part-04/13-tokenization-algorithms.md) | drafted |
| FRAME-007 | Micro autograd engine milestone | [CH-08](chapters/part-02/08-gradients-graphs-and-autodiff.md) | drafted |
| FRAME-008 | Self-attention from scratch milestone | [CH-19](chapters/part-05/19-causal-and-multi-head-attention.md) | drafted |
| FRAME-009 | GPT from scratch milestone | [CH-24](chapters/part-06/24-build-our-gpt-from-scratch.md) | drafted |
| FRAME-010 | Train a tiny language model milestone | [CH-28](chapters/part-07/28-debugging-and-training-our-tiny-model.md) | drafted |
| FRAME-011 | Profile its FLOPs and memory milestone | [CH-44](chapters/part-11/44-profiling-transformer-bottlenecks.md) | drafted |
| FRAME-012 | Simple Triton kernel milestone | [CH-46](chapters/part-12/46-cuda-triton-and-cutlass.md) | drafted |
| FRAME-013 | KV-cached inference milestone | [CH-50](chapters/part-13/50-prefill-decode-and-kv-cache.md) | drafted |
| FRAME-014 | Quantize the model milestone | [CH-56](chapters/part-14/56-quantization-across-the-inference-path.md) | drafted |
| FRAME-015 | Tiny continuous-batching server milestone | [CH-61](chapters/part-16/61-anatomy-of-an-inference-server.md) | drafted |
| FRAME-016 | Multiple-GPU execution milestone | [CH-60](chapters/part-15/60-distributed-execution-and-failure-recovery.md) | drafted |
| FRAME-017 | Deploy a quantized version locally milestone | [CH-68](chapters/part-17/68-packaging-power-and-thermal-limits.md) | drafted |
| FRAME-018 | Probe hidden representations milestone | [CH-74](chapters/part-19/74-features-probes-and-mechanisms.md) | drafted |
| FRAME-019 | Reproduce a research paper milestone | [CH-79](chapters/part-20/79-research-design-and-reproduction.md) | drafted |
| FRAME-020 | Design an original experiment milestone | [CH-80](chapters/part-20/80-evidence-ablations-and-publication.md) | drafted |

## Atomic topic requirements

| Topic ID | Topic | Destination | Status | Evidence |
| --- | --- | --- | --- | --- |
| T-01-01 | Prompt | [CH-01](chapters/part-01/01-the-llm-in-one-picture.md#t-01-01) | drafted | [section](chapters/part-01/01-the-llm-in-one-picture.md#t-01-01) |
| T-01-02 | Tokenizer | [CH-01](chapters/part-01/01-the-llm-in-one-picture.md#t-01-02) | drafted | [section](chapters/part-01/01-the-llm-in-one-picture.md#t-01-02) |
| T-01-03 | Embeddings | [CH-01](chapters/part-01/01-the-llm-in-one-picture.md#t-01-03) | drafted | [section](chapters/part-01/01-the-llm-in-one-picture.md#t-01-03) |
| T-01-04 | Transformer | [CH-01](chapters/part-01/01-the-llm-in-one-picture.md#t-01-04) | drafted | [section](chapters/part-01/01-the-llm-in-one-picture.md#t-01-04) |
| T-01-05 | Logits | [CH-01](chapters/part-01/01-the-llm-in-one-picture.md#t-01-05) | drafted | [section](chapters/part-01/01-the-llm-in-one-picture.md#t-01-05) |
| T-01-06 | Sampling | [CH-01](chapters/part-01/01-the-llm-in-one-picture.md#t-01-06) | drafted | [section](chapters/part-01/01-the-llm-in-one-picture.md#t-01-06) |
| T-01-07 | Output tokens | [CH-01](chapters/part-01/01-the-llm-in-one-picture.md#t-01-07) | drafted | [section](chapters/part-01/01-the-llm-in-one-picture.md#t-01-07) |
| T-01-08 | Next-token conditional distribution | [CH-01](chapters/part-01/01-the-llm-in-one-picture.md#t-01-08) | drafted | [section](chapters/part-01/01-the-llm-in-one-picture.md#t-01-08) |
| T-02-01 | Training vs inference | [CH-02](chapters/part-01/02-training-vs-inference.md#t-02-01) | drafted | [section](chapters/part-01/02-training-vs-inference.md#t-02-01) |
| T-02-02 | Parameters vs activations | [CH-02](chapters/part-01/02-training-vs-inference.md#t-02-02) | drafted | [section](chapters/part-01/02-training-vs-inference.md#t-02-02) |
| T-02-03 | Loss vs generated text | [CH-02](chapters/part-01/02-training-vs-inference.md#t-02-03) | drafted | [section](chapters/part-01/02-training-vs-inference.md#t-02-03) |
| T-02-04 | Learning vs execution | [CH-02](chapters/part-01/02-training-vs-inference.md#t-02-04) | drafted | [section](chapters/part-01/02-training-vs-inference.md#t-02-04) |
| T-03-01 | Applications | [CH-03](chapters/part-01/03-anatomy-of-the-modern-llm-stack.md#t-03-01) | drafted | [section](chapters/part-01/03-anatomy-of-the-modern-llm-stack.md#t-03-01) |
| T-03-02 | Agents and RAG in the stack | [CH-03](chapters/part-01/03-anatomy-of-the-modern-llm-stack.md#t-03-02) | drafted | [section](chapters/part-01/03-anatomy-of-the-modern-llm-stack.md#t-03-02) |
| T-03-03 | Inference server | [CH-03](chapters/part-01/03-anatomy-of-the-modern-llm-stack.md#t-03-03) | drafted | [section](chapters/part-01/03-anatomy-of-the-modern-llm-stack.md#t-03-03) |
| T-03-04 | Model runtime | [CH-03](chapters/part-01/03-anatomy-of-the-modern-llm-stack.md#t-03-04) | drafted | [section](chapters/part-01/03-anatomy-of-the-modern-llm-stack.md#t-03-04) |
| T-03-05 | PyTorch and compiler | [CH-03](chapters/part-01/03-anatomy-of-the-modern-llm-stack.md#t-03-05) | drafted | [section](chapters/part-01/03-anatomy-of-the-modern-llm-stack.md#t-03-05) |
| T-03-06 | Tensor operations | [CH-03](chapters/part-01/03-anatomy-of-the-modern-llm-stack.md#t-03-06) | drafted | [section](chapters/part-01/03-anatomy-of-the-modern-llm-stack.md#t-03-06) |
| T-03-07 | GPU kernels | [CH-03](chapters/part-01/03-anatomy-of-the-modern-llm-stack.md#t-03-07) | drafted | [section](chapters/part-01/03-anatomy-of-the-modern-llm-stack.md#t-03-07) |
| T-03-08 | GPU hardware | [CH-03](chapters/part-01/03-anatomy-of-the-modern-llm-stack.md#t-03-08) | drafted | [section](chapters/part-01/03-anatomy-of-the-modern-llm-stack.md#t-03-08) |
| T-03-09 | Memory | [CH-03](chapters/part-01/03-anatomy-of-the-modern-llm-stack.md#t-03-09) | drafted | [section](chapters/part-01/03-anatomy-of-the-modern-llm-stack.md#t-03-09) |
| T-03-10 | Silicon | [CH-03](chapters/part-01/03-anatomy-of-the-modern-llm-stack.md#t-03-10) | drafted | [section](chapters/part-01/03-anatomy-of-the-modern-llm-stack.md#t-03-10) |
| T-04-01 | Python | [CH-04](chapters/part-01/04-building-our-tiny-laboratory.md#t-04-01) | drafted | [section](chapters/part-01/04-building-our-tiny-laboratory.md#t-04-01) |
| T-04-02 | NumPy | [CH-04](chapters/part-01/04-building-our-tiny-laboratory.md#t-04-02) | drafted | [section](chapters/part-01/04-building-our-tiny-laboratory.md#t-04-02) |
| T-04-03 | PyTorch | [CH-04](chapters/part-01/04-building-our-tiny-laboratory.md#t-04-03) | drafted | [section](chapters/part-01/04-building-our-tiny-laboratory.md#t-04-03) |
| T-04-04 | Notebooks | [CH-04](chapters/part-01/04-building-our-tiny-laboratory.md#t-04-04) | drafted | [section](chapters/part-01/04-building-our-tiny-laboratory.md#t-04-04) |
| T-04-05 | Profiling tools | [CH-04](chapters/part-01/04-building-our-tiny-laboratory.md#t-04-05) | drafted | [section](chapters/part-01/04-building-our-tiny-laboratory.md#t-04-05) |
| T-04-06 | CPU baseline | [CH-04](chapters/part-01/04-building-our-tiny-laboratory.md#t-04-06) | drafted | [section](chapters/part-01/04-building-our-tiny-laboratory.md#t-04-06) |
| T-04-07 | Seeds and environment records | [CH-04](chapters/part-01/04-building-our-tiny-laboratory.md#t-04-07) | drafted | [section](chapters/part-01/04-building-our-tiny-laboratory.md#t-04-07) |
| T-05-01 | Scalars | [CH-05](chapters/part-02/05-tensors-and-resource-accounting.md#t-05-01) | drafted | [section](chapters/part-02/05-tensors-and-resource-accounting.md#t-05-01) |
| T-05-02 | Vectors | [CH-05](chapters/part-02/05-tensors-and-resource-accounting.md#t-05-02) | drafted | [section](chapters/part-02/05-tensors-and-resource-accounting.md#t-05-02) |
| T-05-03 | Matrices | [CH-05](chapters/part-02/05-tensors-and-resource-accounting.md#t-05-03) | drafted | [section](chapters/part-02/05-tensors-and-resource-accounting.md#t-05-03) |
| T-05-04 | Tensors | [CH-05](chapters/part-02/05-tensors-and-resource-accounting.md#t-05-04) | drafted | [section](chapters/part-02/05-tensors-and-resource-accounting.md#t-05-04) |
| T-05-05 | Shapes | [CH-05](chapters/part-02/05-tensors-and-resource-accounting.md#t-05-05) | drafted | [section](chapters/part-02/05-tensors-and-resource-accounting.md#t-05-05) |
| T-05-06 | Dimensions | [CH-05](chapters/part-02/05-tensors-and-resource-accounting.md#t-05-06) | drafted | [section](chapters/part-02/05-tensors-and-resource-accounting.md#t-05-06) |
| T-05-07 | Indexing | [CH-05](chapters/part-02/05-tensors-and-resource-accounting.md#t-05-07) | drafted | [section](chapters/part-02/05-tensors-and-resource-accounting.md#t-05-07) |
| T-05-08 | Transpose | [CH-05](chapters/part-02/05-tensors-and-resource-accounting.md#t-05-08) | drafted | [section](chapters/part-02/05-tensors-and-resource-accounting.md#t-05-08) |
| T-05-09 | Batch dimensions | [CH-05](chapters/part-02/05-tensors-and-resource-accounting.md#t-05-09) | drafted | [section](chapters/part-02/05-tensors-and-resource-accounting.md#t-05-09) |
| T-05-10 | Broadcasting | [CH-05](chapters/part-02/05-tensors-and-resource-accounting.md#t-05-10) | drafted | [section](chapters/part-02/05-tensors-and-resource-accounting.md#t-05-10) |
| T-05-11 | Dtypes | [CH-05](chapters/part-02/05-tensors-and-resource-accounting.md#t-05-11) | drafted | [section](chapters/part-02/05-tensors-and-resource-accounting.md#t-05-11) |
| T-05-12 | Element counts | [CH-05](chapters/part-02/05-tensors-and-resource-accounting.md#t-05-12) | drafted | [section](chapters/part-02/05-tensors-and-resource-accounting.md#t-05-12) |
| T-05-13 | Bytes | [CH-05](chapters/part-02/05-tensors-and-resource-accounting.md#t-05-13) | drafted | [section](chapters/part-02/05-tensors-and-resource-accounting.md#t-05-13) |
| T-05-14 | FLOPs | [CH-05](chapters/part-02/05-tensors-and-resource-accounting.md#t-05-14) | drafted | [section](chapters/part-02/05-tensors-and-resource-accounting.md#t-05-14) |
| T-05-15 | Matrix multiplication | [CH-05](chapters/part-02/05-tensors-and-resource-accounting.md#t-05-15) | drafted | [section](chapters/part-02/05-tensors-and-resource-accounting.md#t-05-15) |
| T-06-01 | Dot products | [CH-06](chapters/part-02/06-geometry-and-number-formats.md#t-06-01) | drafted | [section](chapters/part-02/06-geometry-and-number-formats.md#t-06-01) |
| T-06-02 | Cosine similarity | [CH-06](chapters/part-02/06-geometry-and-number-formats.md#t-06-02) | drafted | [section](chapters/part-02/06-geometry-and-number-formats.md#t-06-02) |
| T-06-03 | Magnitude | [CH-06](chapters/part-02/06-geometry-and-number-formats.md#t-06-03) | drafted | [section](chapters/part-02/06-geometry-and-number-formats.md#t-06-03) |
| T-06-04 | Basis | [CH-06](chapters/part-02/06-geometry-and-number-formats.md#t-06-04) | drafted | [section](chapters/part-02/06-geometry-and-number-formats.md#t-06-04) |
| T-06-05 | Subspaces | [CH-06](chapters/part-02/06-geometry-and-number-formats.md#t-06-05) | drafted | [section](chapters/part-02/06-geometry-and-number-formats.md#t-06-05) |
| T-06-06 | Orthogonality | [CH-06](chapters/part-02/06-geometry-and-number-formats.md#t-06-06) | drafted | [section](chapters/part-02/06-geometry-and-number-formats.md#t-06-06) |
| T-06-07 | Projections | [CH-06](chapters/part-02/06-geometry-and-number-formats.md#t-06-07) | drafted | [section](chapters/part-02/06-geometry-and-number-formats.md#t-06-07) |
| T-06-08 | Linear transformations | [CH-06](chapters/part-02/06-geometry-and-number-formats.md#t-06-08) | drafted | [section](chapters/part-02/06-geometry-and-number-formats.md#t-06-08) |
| T-06-09 | FP32 | [CH-06](chapters/part-02/06-geometry-and-number-formats.md#t-06-09) | drafted | [section](chapters/part-02/06-geometry-and-number-formats.md#t-06-09) |
| T-06-10 | FP16 | [CH-06](chapters/part-02/06-geometry-and-number-formats.md#t-06-10) | drafted | [section](chapters/part-02/06-geometry-and-number-formats.md#t-06-10) |
| T-06-11 | BF16 | [CH-06](chapters/part-02/06-geometry-and-number-formats.md#t-06-11) | drafted | [section](chapters/part-02/06-geometry-and-number-formats.md#t-06-11) |
| T-06-12 | FP8 | [CH-06](chapters/part-02/06-geometry-and-number-formats.md#t-06-12) | drafted | [section](chapters/part-02/06-geometry-and-number-formats.md#t-06-12) |
| T-06-13 | INT8 | [CH-06](chapters/part-02/06-geometry-and-number-formats.md#t-06-13) | drafted | [section](chapters/part-02/06-geometry-and-number-formats.md#t-06-13) |
| T-06-14 | INT4 | [CH-06](chapters/part-02/06-geometry-and-number-formats.md#t-06-14) | drafted | [section](chapters/part-02/06-geometry-and-number-formats.md#t-06-14) |
| T-06-15 | Overflow | [CH-06](chapters/part-02/06-geometry-and-number-formats.md#t-06-15) | drafted | [section](chapters/part-02/06-geometry-and-number-formats.md#t-06-15) |
| T-06-16 | Underflow | [CH-06](chapters/part-02/06-geometry-and-number-formats.md#t-06-16) | drafted | [section](chapters/part-02/06-geometry-and-number-formats.md#t-06-16) |
| T-06-17 | Numerical stability | [CH-06](chapters/part-02/06-geometry-and-number-formats.md#t-06-17) | drafted | [section](chapters/part-02/06-geometry-and-number-formats.md#t-06-17) |
| T-07-01 | Conditional probability | [CH-07](chapters/part-02/07-probability-logits-and-loss.md#t-07-01) | drafted | [section](chapters/part-02/07-probability-logits-and-loss.md#t-07-01) |
| T-07-02 | Likelihood | [CH-07](chapters/part-02/07-probability-logits-and-loss.md#t-07-02) | drafted | [section](chapters/part-02/07-probability-logits-and-loss.md#t-07-02) |
| T-07-03 | Log-probability | [CH-07](chapters/part-02/07-probability-logits-and-loss.md#t-07-03) | drafted | [section](chapters/part-02/07-probability-logits-and-loss.md#t-07-03) |
| T-07-04 | Entropy | [CH-07](chapters/part-02/07-probability-logits-and-loss.md#t-07-04) | drafted | [section](chapters/part-02/07-probability-logits-and-loss.md#t-07-04) |
| T-07-05 | KL divergence | [CH-07](chapters/part-02/07-probability-logits-and-loss.md#t-07-05) | drafted | [section](chapters/part-02/07-probability-logits-and-loss.md#t-07-05) |
| T-07-06 | Softmax | [CH-07](chapters/part-02/07-probability-logits-and-loss.md#t-07-06) | drafted | [section](chapters/part-02/07-probability-logits-and-loss.md#t-07-06) |
| T-07-07 | Logits | [CH-07](chapters/part-02/07-probability-logits-and-loss.md#t-07-07) | drafted | [section](chapters/part-02/07-probability-logits-and-loss.md#t-07-07) |
| T-07-08 | Cross-entropy | [CH-07](chapters/part-02/07-probability-logits-and-loss.md#t-07-08) | drafted | [section](chapters/part-02/07-probability-logits-and-loss.md#t-07-08) |
| T-07-09 | Log-sum-exp | [CH-07](chapters/part-02/07-probability-logits-and-loss.md#t-07-09) | drafted | [section](chapters/part-02/07-probability-logits-and-loss.md#t-07-09) |
| T-08-01 | Derivatives | [CH-08](chapters/part-02/08-gradients-graphs-and-autodiff.md#t-08-01) | drafted | [section](chapters/part-02/08-gradients-graphs-and-autodiff.md#t-08-01) |
| T-08-02 | Gradients | [CH-08](chapters/part-02/08-gradients-graphs-and-autodiff.md#t-08-02) | drafted | [section](chapters/part-02/08-gradients-graphs-and-autodiff.md#t-08-02) |
| T-08-03 | Chain rule | [CH-08](chapters/part-02/08-gradients-graphs-and-autodiff.md#t-08-03) | drafted | [section](chapters/part-02/08-gradients-graphs-and-autodiff.md#t-08-03) |
| T-08-04 | Computational graphs | [CH-08](chapters/part-02/08-gradients-graphs-and-autodiff.md#t-08-04) | drafted | [section](chapters/part-02/08-gradients-graphs-and-autodiff.md#t-08-04) |
| T-08-05 | Automatic differentiation | [CH-08](chapters/part-02/08-gradients-graphs-and-autodiff.md#t-08-05) | drafted | [section](chapters/part-02/08-gradients-graphs-and-autodiff.md#t-08-05) |
| T-08-06 | Reverse-mode autodiff | [CH-08](chapters/part-02/08-gradients-graphs-and-autodiff.md#t-08-06) | drafted | [section](chapters/part-02/08-gradients-graphs-and-autodiff.md#t-08-06) |
| T-08-07 | Finite-difference checks | [CH-08](chapters/part-02/08-gradients-graphs-and-autodiff.md#t-08-07) | drafted | [section](chapters/part-02/08-gradients-graphs-and-autodiff.md#t-08-07) |
| T-09-01 | Linear layers | [CH-09](chapters/part-03/09-linear-layers-and-nonlinearities.md#t-09-01) | drafted | [section](chapters/part-03/09-linear-layers-and-nonlinearities.md#t-09-01) |
| T-09-02 | Biases | [CH-09](chapters/part-03/09-linear-layers-and-nonlinearities.md#t-09-02) | drafted | [section](chapters/part-03/09-linear-layers-and-nonlinearities.md#t-09-02) |
| T-09-03 | Nonlinearities | [CH-09](chapters/part-03/09-linear-layers-and-nonlinearities.md#t-09-03) | drafted | [section](chapters/part-03/09-linear-layers-and-nonlinearities.md#t-09-03) |
| T-09-04 | ReLU | [CH-09](chapters/part-03/09-linear-layers-and-nonlinearities.md#t-09-04) | drafted | [section](chapters/part-03/09-linear-layers-and-nonlinearities.md#t-09-04) |
| T-09-05 | GELU | [CH-09](chapters/part-03/09-linear-layers-and-nonlinearities.md#t-09-05) | drafted | [section](chapters/part-03/09-linear-layers-and-nonlinearities.md#t-09-05) |
| T-09-06 | Parameter shapes | [CH-09](chapters/part-03/09-linear-layers-and-nonlinearities.md#t-09-06) | drafted | [section](chapters/part-03/09-linear-layers-and-nonlinearities.md#t-09-06) |
| T-10-01 | Building a tiny neural network | [CH-10](chapters/part-03/10-a-tiny-network-forward-and-backward.md#t-10-01) | drafted | [section](chapters/part-03/10-a-tiny-network-forward-and-backward.md#t-10-01) |
| T-10-02 | Forward propagation | [CH-10](chapters/part-03/10-a-tiny-network-forward-and-backward.md#t-10-02) | drafted | [section](chapters/part-03/10-a-tiny-network-forward-and-backward.md#t-10-02) |
| T-10-03 | Backpropagation by hand | [CH-10](chapters/part-03/10-a-tiny-network-forward-and-backward.md#t-10-03) | drafted | [section](chapters/part-03/10-a-tiny-network-forward-and-backward.md#t-10-03) |
| T-10-04 | Gradient shapes | [CH-10](chapters/part-03/10-a-tiny-network-forward-and-backward.md#t-10-04) | drafted | [section](chapters/part-03/10-a-tiny-network-forward-and-backward.md#t-10-04) |
| T-11-01 | SGD | [CH-11](chapters/part-03/11-optimization-and-state.md#t-11-01) | drafted | [section](chapters/part-03/11-optimization-and-state.md#t-11-01) |
| T-11-02 | Momentum | [CH-11](chapters/part-03/11-optimization-and-state.md#t-11-02) | drafted | [section](chapters/part-03/11-optimization-and-state.md#t-11-02) |
| T-11-03 | AdamW | [CH-11](chapters/part-03/11-optimization-and-state.md#t-11-03) | drafted | [section](chapters/part-03/11-optimization-and-state.md#t-11-03) |
| T-11-04 | Optimizer states | [CH-11](chapters/part-03/11-optimization-and-state.md#t-11-04) | drafted | [section](chapters/part-03/11-optimization-and-state.md#t-11-04) |
| T-11-05 | Learning-rate schedules | [CH-11](chapters/part-03/11-optimization-and-state.md#t-11-05) | drafted | [section](chapters/part-03/11-optimization-and-state.md#t-11-05) |
| T-11-06 | Weight decay | [CH-11](chapters/part-03/11-optimization-and-state.md#t-11-06) | drafted | [section](chapters/part-03/11-optimization-and-state.md#t-11-06) |
| T-12-01 | Initialization | [CH-12](chapters/part-03/12-initialization-and-training-stability.md#t-12-01) | drafted | [section](chapters/part-03/12-initialization-and-training-stability.md#t-12-01) |
| T-12-02 | Gradient norms | [CH-12](chapters/part-03/12-initialization-and-training-stability.md#t-12-02) | drafted | [section](chapters/part-03/12-initialization-and-training-stability.md#t-12-02) |
| T-12-03 | Clipping | [CH-12](chapters/part-03/12-initialization-and-training-stability.md#t-12-03) | drafted | [section](chapters/part-03/12-initialization-and-training-stability.md#t-12-03) |
| T-12-04 | Warmup | [CH-12](chapters/part-03/12-initialization-and-training-stability.md#t-12-04) | drafted | [section](chapters/part-03/12-initialization-and-training-stability.md#t-12-04) |
| T-12-05 | Vanishing gradients | [CH-12](chapters/part-03/12-initialization-and-training-stability.md#t-12-05) | drafted | [section](chapters/part-03/12-initialization-and-training-stability.md#t-12-05) |
| T-12-06 | Exploding gradients | [CH-12](chapters/part-03/12-initialization-and-training-stability.md#t-12-06) | drafted | [section](chapters/part-03/12-initialization-and-training-stability.md#t-12-06) |
| T-12-07 | Stability diagnostics | [CH-12](chapters/part-03/12-initialization-and-training-stability.md#t-12-07) | drafted | [section](chapters/part-03/12-initialization-and-training-stability.md#t-12-07) |
| T-13-01 | Why machines need tokens | [CH-13](chapters/part-04/13-tokenization-algorithms.md#t-13-01) | drafted | [section](chapters/part-04/13-tokenization-algorithms.md#t-13-01) |
| T-13-02 | Characters | [CH-13](chapters/part-04/13-tokenization-algorithms.md#t-13-02) | drafted | [section](chapters/part-04/13-tokenization-algorithms.md#t-13-02) |
| T-13-03 | Words | [CH-13](chapters/part-04/13-tokenization-algorithms.md#t-13-03) | drafted | [section](chapters/part-04/13-tokenization-algorithms.md#t-13-03) |
| T-13-04 | Subwords | [CH-13](chapters/part-04/13-tokenization-algorithms.md#t-13-04) | drafted | [section](chapters/part-04/13-tokenization-algorithms.md#t-13-04) |
| T-13-05 | BPE from scratch | [CH-13](chapters/part-04/13-tokenization-algorithms.md#t-13-05) | drafted | [section](chapters/part-04/13-tokenization-algorithms.md#t-13-05) |
| T-13-06 | WordPiece | [CH-13](chapters/part-04/13-tokenization-algorithms.md#t-13-06) | drafted | [section](chapters/part-04/13-tokenization-algorithms.md#t-13-06) |
| T-13-07 | SentencePiece | [CH-13](chapters/part-04/13-tokenization-algorithms.md#t-13-07) | drafted | [section](chapters/part-04/13-tokenization-algorithms.md#t-13-07) |
| T-13-08 | Byte-level tokenization | [CH-13](chapters/part-04/13-tokenization-algorithms.md#t-13-08) | drafted | [section](chapters/part-04/13-tokenization-algorithms.md#t-13-08) |
| T-14-01 | Vocabulary | [CH-14](chapters/part-04/14-vocabulary-and-token-ids.md#t-14-01) | drafted | [section](chapters/part-04/14-vocabulary-and-token-ids.md#t-14-01) |
| T-14-02 | Token IDs | [CH-14](chapters/part-04/14-vocabulary-and-token-ids.md#t-14-02) | drafted | [section](chapters/part-04/14-vocabulary-and-token-ids.md#t-14-02) |
| T-14-03 | Special tokens | [CH-14](chapters/part-04/14-vocabulary-and-token-ids.md#t-14-03) | drafted | [section](chapters/part-04/14-vocabulary-and-token-ids.md#t-14-03) |
| T-14-04 | Unknown tokens | [CH-14](chapters/part-04/14-vocabulary-and-token-ids.md#t-14-04) | drafted | [section](chapters/part-04/14-vocabulary-and-token-ids.md#t-14-04) |
| T-14-05 | Tokenizer-model compatibility | [CH-14](chapters/part-04/14-vocabulary-and-token-ids.md#t-14-05) | drafted | [section](chapters/part-04/14-vocabulary-and-token-ids.md#t-14-05) |
| T-15-01 | Embedding matrices | [CH-15](chapters/part-04/15-embedding-matrices-and-geometry.md#t-15-01) | drafted | [section](chapters/part-04/15-embedding-matrices-and-geometry.md#t-15-01) |
| T-15-02 | Static embeddings | [CH-15](chapters/part-04/15-embedding-matrices-and-geometry.md#t-15-02) | drafted | [section](chapters/part-04/15-embedding-matrices-and-geometry.md#t-15-02) |
| T-15-03 | Contextual embeddings | [CH-15](chapters/part-04/15-embedding-matrices-and-geometry.md#t-15-03) | drafted | [section](chapters/part-04/15-embedding-matrices-and-geometry.md#t-15-03) |
| T-15-04 | Representation geometry | [CH-15](chapters/part-04/15-embedding-matrices-and-geometry.md#t-15-04) | drafted | [section](chapters/part-04/15-embedding-matrices-and-geometry.md#t-15-04) |
| T-15-05 | Embedding lookup | [CH-15](chapters/part-04/15-embedding-matrices-and-geometry.md#t-15-05) | drafted | [section](chapters/part-04/15-embedding-matrices-and-geometry.md#t-15-05) |
| T-16-01 | Position and sequence order | [CH-16](chapters/part-04/16-position-and-sequence-order.md#t-16-01) | drafted | [section](chapters/part-04/16-position-and-sequence-order.md#t-16-01) |
| T-16-02 | Sinusoidal positions | [CH-16](chapters/part-04/16-position-and-sequence-order.md#t-16-02) | drafted | [section](chapters/part-04/16-position-and-sequence-order.md#t-16-02) |
| T-16-03 | Learned positions | [CH-16](chapters/part-04/16-position-and-sequence-order.md#t-16-03) | drafted | [section](chapters/part-04/16-position-and-sequence-order.md#t-16-03) |
| T-16-04 | Relative-position methods | [CH-16](chapters/part-04/16-position-and-sequence-order.md#t-16-04) | drafted | [section](chapters/part-04/16-position-and-sequence-order.md#t-16-04) |
| T-16-05 | RoPE introduction | [CH-16](chapters/part-04/16-position-and-sequence-order.md#t-16-05) | drafted | [section](chapters/part-04/16-position-and-sequence-order.md#t-16-05) |
| T-17-01 | Sequence modeling bottlenecks | [CH-17](chapters/part-05/17-sequence-modeling-and-the-attention-idea.md#t-17-01) | drafted | [section](chapters/part-05/17-sequence-modeling-and-the-attention-idea.md#t-17-01) |
| T-17-02 | RNNs | [CH-17](chapters/part-05/17-sequence-modeling-and-the-attention-idea.md#t-17-02) | drafted | [section](chapters/part-05/17-sequence-modeling-and-the-attention-idea.md#t-17-02) |
| T-17-03 | LSTMs | [CH-17](chapters/part-05/17-sequence-modeling-and-the-attention-idea.md#t-17-03) | drafted | [section](chapters/part-05/17-sequence-modeling-and-the-attention-idea.md#t-17-03) |
| T-17-04 | The attention idea | [CH-17](chapters/part-05/17-sequence-modeling-and-the-attention-idea.md#t-17-04) | drafted | [section](chapters/part-05/17-sequence-modeling-and-the-attention-idea.md#t-17-04) |
| T-17-05 | Content-based retrieval | [CH-17](chapters/part-05/17-sequence-modeling-and-the-attention-idea.md#t-17-05) | drafted | [section](chapters/part-05/17-sequence-modeling-and-the-attention-idea.md#t-17-05) |
| T-18-01 | Query | [CH-18](chapters/part-05/18-queries-keys-values-and-scaling.md#t-18-01) | drafted | [section](chapters/part-05/18-queries-keys-values-and-scaling.md#t-18-01) |
| T-18-02 | Key | [CH-18](chapters/part-05/18-queries-keys-values-and-scaling.md#t-18-02) | drafted | [section](chapters/part-05/18-queries-keys-values-and-scaling.md#t-18-02) |
| T-18-03 | Value | [CH-18](chapters/part-05/18-queries-keys-values-and-scaling.md#t-18-03) | drafted | [section](chapters/part-05/18-queries-keys-values-and-scaling.md#t-18-03) |
| T-18-04 | QKV projections | [CH-18](chapters/part-05/18-queries-keys-values-and-scaling.md#t-18-04) | drafted | [section](chapters/part-05/18-queries-keys-values-and-scaling.md#t-18-04) |
| T-18-05 | Scaled dot-product attention | [CH-18](chapters/part-05/18-queries-keys-values-and-scaling.md#t-18-05) | drafted | [section](chapters/part-05/18-queries-keys-values-and-scaling.md#t-18-05) |
| T-18-06 | Square-root scaling | [CH-18](chapters/part-05/18-queries-keys-values-and-scaling.md#t-18-06) | drafted | [section](chapters/part-05/18-queries-keys-values-and-scaling.md#t-18-06) |
| T-18-07 | Attention weights | [CH-18](chapters/part-05/18-queries-keys-values-and-scaling.md#t-18-07) | drafted | [section](chapters/part-05/18-queries-keys-values-and-scaling.md#t-18-07) |
| T-19-01 | Causal attention | [CH-19](chapters/part-05/19-causal-and-multi-head-attention.md#t-19-01) | drafted | [section](chapters/part-05/19-causal-and-multi-head-attention.md#t-19-01) |
| T-19-02 | Causal masks | [CH-19](chapters/part-05/19-causal-and-multi-head-attention.md#t-19-02) | drafted | [section](chapters/part-05/19-causal-and-multi-head-attention.md#t-19-02) |
| T-19-03 | Multi-head attention | [CH-19](chapters/part-05/19-causal-and-multi-head-attention.md#t-19-03) | drafted | [section](chapters/part-05/19-causal-and-multi-head-attention.md#t-19-03) |
| T-19-04 | Head concatenation | [CH-19](chapters/part-05/19-causal-and-multi-head-attention.md#t-19-04) | drafted | [section](chapters/part-05/19-causal-and-multi-head-attention.md#t-19-04) |
| T-19-05 | Output projection | [CH-19](chapters/part-05/19-causal-and-multi-head-attention.md#t-19-05) | drafted | [section](chapters/part-05/19-causal-and-multi-head-attention.md#t-19-05) |
| T-20-01 | Attention tensor shapes | [CH-20](chapters/part-05/20-attention-shapes-and-compute-cost.md#t-20-01) | drafted | [section](chapters/part-05/20-attention-shapes-and-compute-cost.md#t-20-01) |
| T-20-02 | Attention compute cost | [CH-20](chapters/part-05/20-attention-shapes-and-compute-cost.md#t-20-02) | drafted | [section](chapters/part-05/20-attention-shapes-and-compute-cost.md#t-20-02) |
| T-20-03 | Quadratic sequence cost | [CH-20](chapters/part-05/20-attention-shapes-and-compute-cost.md#t-20-03) | drafted | [section](chapters/part-05/20-attention-shapes-and-compute-cost.md#t-20-03) |
| T-20-04 | Attention memory accounting | [CH-20](chapters/part-05/20-attention-shapes-and-compute-cost.md#t-20-04) | drafted | [section](chapters/part-05/20-attention-shapes-and-compute-cost.md#t-20-04) |
| T-21-01 | Residual connections | [CH-21](chapters/part-06/21-residual-streams-and-normalization.md#t-21-01) | drafted | [section](chapters/part-06/21-residual-streams-and-normalization.md#t-21-01) |
| T-21-02 | Residual streams | [CH-21](chapters/part-06/21-residual-streams-and-normalization.md#t-21-02) | drafted | [section](chapters/part-06/21-residual-streams-and-normalization.md#t-21-02) |
| T-21-03 | LayerNorm | [CH-21](chapters/part-06/21-residual-streams-and-normalization.md#t-21-03) | drafted | [section](chapters/part-06/21-residual-streams-and-normalization.md#t-21-03) |
| T-21-04 | RMSNorm | [CH-21](chapters/part-06/21-residual-streams-and-normalization.md#t-21-04) | drafted | [section](chapters/part-06/21-residual-streams-and-normalization.md#t-21-04) |
| T-21-05 | Pre-norm | [CH-21](chapters/part-06/21-residual-streams-and-normalization.md#t-21-05) | drafted | [section](chapters/part-06/21-residual-streams-and-normalization.md#t-21-05) |
| T-21-06 | Post-norm | [CH-21](chapters/part-06/21-residual-streams-and-normalization.md#t-21-06) | drafted | [section](chapters/part-06/21-residual-streams-and-normalization.md#t-21-06) |
| T-22-01 | Feed-forward networks | [CH-22](chapters/part-06/22-feed-forward-networks-and-complete-blocks.md#t-22-01) | drafted | [section](chapters/part-06/22-feed-forward-networks-and-complete-blocks.md#t-22-01) |
| T-22-02 | GELU vs SwiGLU | [CH-22](chapters/part-06/22-feed-forward-networks-and-complete-blocks.md#t-22-02) | drafted | [section](chapters/part-06/22-feed-forward-networks-and-complete-blocks.md#t-22-02) |
| T-22-03 | MLP expansion | [CH-22](chapters/part-06/22-feed-forward-networks-and-complete-blocks.md#t-22-03) | drafted | [section](chapters/part-06/22-feed-forward-networks-and-complete-blocks.md#t-22-03) |
| T-22-04 | Complete Transformer block | [CH-22](chapters/part-06/22-feed-forward-networks-and-complete-blocks.md#t-22-04) | drafted | [section](chapters/part-06/22-feed-forward-networks-and-complete-blocks.md#t-22-04) |
| T-23-01 | Stack the blocks | [CH-23](chapters/part-06/23-stacking-vocabulary-projection-and-tying.md#t-23-01) | drafted | [section](chapters/part-06/23-stacking-vocabulary-projection-and-tying.md#t-23-01) |
| T-23-02 | Vocabulary projection | [CH-23](chapters/part-06/23-stacking-vocabulary-projection-and-tying.md#t-23-02) | drafted | [section](chapters/part-06/23-stacking-vocabulary-projection-and-tying.md#t-23-02) |
| T-23-03 | LM head | [CH-23](chapters/part-06/23-stacking-vocabulary-projection-and-tying.md#t-23-03) | drafted | [section](chapters/part-06/23-stacking-vocabulary-projection-and-tying.md#t-23-03) |
| T-23-04 | Weight tying | [CH-23](chapters/part-06/23-stacking-vocabulary-projection-and-tying.md#t-23-04) | drafted | [section](chapters/part-06/23-stacking-vocabulary-projection-and-tying.md#t-23-04) |
| T-24-01 | GPT implementation | [CH-24](chapters/part-06/24-build-our-gpt-from-scratch.md#t-24-01) | drafted | [section](chapters/part-06/24-build-our-gpt-from-scratch.md#t-24-01) |
| T-24-02 | Decoder-only model assembly | [CH-24](chapters/part-06/24-build-our-gpt-from-scratch.md#t-24-02) | drafted | [section](chapters/part-06/24-build-our-gpt-from-scratch.md#t-24-02) |
| T-24-03 | Model configuration | [CH-24](chapters/part-06/24-build-our-gpt-from-scratch.md#t-24-03) | drafted | [section](chapters/part-06/24-build-our-gpt-from-scratch.md#t-24-03) |
| T-24-04 | Forward-pass invariants | [CH-24](chapters/part-06/24-build-our-gpt-from-scratch.md#t-24-04) | drafted | [section](chapters/part-06/24-build-our-gpt-from-scratch.md#t-24-04) |
| T-25-01 | Preparing training sequences | [CH-25](chapters/part-07/25-sequences-batches-and-pretraining.md#t-25-01) | drafted | [section](chapters/part-07/25-sequences-batches-and-pretraining.md#t-25-01) |
| T-25-02 | Sequence packing | [CH-25](chapters/part-07/25-sequences-batches-and-pretraining.md#t-25-02) | drafted | [section](chapters/part-07/25-sequences-batches-and-pretraining.md#t-25-02) |
| T-25-03 | Batches | [CH-25](chapters/part-07/25-sequences-batches-and-pretraining.md#t-25-03) | drafted | [section](chapters/part-07/25-sequences-batches-and-pretraining.md#t-25-03) |
| T-25-04 | Mini-batches | [CH-25](chapters/part-07/25-sequences-batches-and-pretraining.md#t-25-04) | drafted | [section](chapters/part-07/25-sequences-batches-and-pretraining.md#t-25-04) |
| T-25-05 | Next-token prediction | [CH-25](chapters/part-07/25-sequences-batches-and-pretraining.md#t-25-05) | drafted | [section](chapters/part-07/25-sequences-batches-and-pretraining.md#t-25-05) |
| T-25-06 | Full pretraining | [CH-25](chapters/part-07/25-sequences-batches-and-pretraining.md#t-25-06) | drafted | [section](chapters/part-07/25-sequences-batches-and-pretraining.md#t-25-06) |
| T-25-07 | Batch size and sequence length dynamics | [CH-25](chapters/part-07/25-sequences-batches-and-pretraining.md#t-25-07) | drafted | [section](chapters/part-07/25-sequences-batches-and-pretraining.md#t-25-07) |
| T-26-01 | Training forward pass | [CH-26](chapters/part-07/26-the-training-step-and-schedule.md#t-26-01) | drafted | [section](chapters/part-07/26-the-training-step-and-schedule.md#t-26-01) |
| T-26-02 | Training loss | [CH-26](chapters/part-07/26-the-training-step-and-schedule.md#t-26-02) | drafted | [section](chapters/part-07/26-the-training-step-and-schedule.md#t-26-02) |
| T-26-03 | Training backward pass | [CH-26](chapters/part-07/26-the-training-step-and-schedule.md#t-26-03) | drafted | [section](chapters/part-07/26-the-training-step-and-schedule.md#t-26-03) |
| T-26-04 | Optimizer state updates in memory | [CH-26](chapters/part-07/26-the-training-step-and-schedule.md#t-26-04) | drafted | [section](chapters/part-07/26-the-training-step-and-schedule.md#t-26-04) |
| T-26-05 | Learning rates | [CH-26](chapters/part-07/26-the-training-step-and-schedule.md#t-26-05) | drafted | [section](chapters/part-07/26-the-training-step-and-schedule.md#t-26-05) |
| T-26-06 | Warmup | [CH-26](chapters/part-07/26-the-training-step-and-schedule.md#t-26-06) | drafted | [section](chapters/part-07/26-the-training-step-and-schedule.md#t-26-06) |
| T-26-07 | Gradient accumulation | [CH-26](chapters/part-07/26-the-training-step-and-schedule.md#t-26-07) | drafted | [section](chapters/part-07/26-the-training-step-and-schedule.md#t-26-07) |
| T-26-08 | Gradient clipping | [CH-26](chapters/part-07/26-the-training-step-and-schedule.md#t-26-08) | drafted | [section](chapters/part-07/26-the-training-step-and-schedule.md#t-26-08) |
| T-27-01 | Mixed-precision training | [CH-27](chapters/part-07/27-mixed-precision-and-checkpoint-anatomy.md#t-27-01) | drafted | [section](chapters/part-07/27-mixed-precision-and-checkpoint-anatomy.md#t-27-01) |
| T-27-02 | Loss scaling | [CH-27](chapters/part-07/27-mixed-precision-and-checkpoint-anatomy.md#t-27-02) | drafted | [section](chapters/part-07/27-mixed-precision-and-checkpoint-anatomy.md#t-27-02) |
| T-27-03 | Activation checkpointing | [CH-27](chapters/part-07/27-mixed-precision-and-checkpoint-anatomy.md#t-27-03) | drafted | [section](chapters/part-07/27-mixed-precision-and-checkpoint-anatomy.md#t-27-03) |
| T-27-04 | Checkpoints | [CH-27](chapters/part-07/27-mixed-precision-and-checkpoint-anatomy.md#t-27-04) | drafted | [section](chapters/part-07/27-mixed-precision-and-checkpoint-anatomy.md#t-27-04) |
| T-27-05 | Weights | [CH-27](chapters/part-07/27-mixed-precision-and-checkpoint-anatomy.md#t-27-05) | drafted | [section](chapters/part-07/27-mixed-precision-and-checkpoint-anatomy.md#t-27-05) |
| T-27-06 | Config | [CH-27](chapters/part-07/27-mixed-precision-and-checkpoint-anatomy.md#t-27-06) | drafted | [section](chapters/part-07/27-mixed-precision-and-checkpoint-anatomy.md#t-27-06) |
| T-27-07 | Tokenizer state | [CH-27](chapters/part-07/27-mixed-precision-and-checkpoint-anatomy.md#t-27-07) | drafted | [section](chapters/part-07/27-mixed-precision-and-checkpoint-anatomy.md#t-27-07) |
| T-27-08 | Optimizer state | [CH-27](chapters/part-07/27-mixed-precision-and-checkpoint-anatomy.md#t-27-08) | drafted | [section](chapters/part-07/27-mixed-precision-and-checkpoint-anatomy.md#t-27-08) |
| T-27-09 | Scheduler state | [CH-27](chapters/part-07/27-mixed-precision-and-checkpoint-anatomy.md#t-27-09) | drafted | [section](chapters/part-07/27-mixed-precision-and-checkpoint-anatomy.md#t-27-09) |
| T-27-10 | RNG state | [CH-27](chapters/part-07/27-mixed-precision-and-checkpoint-anatomy.md#t-27-10) | drafted | [section](chapters/part-07/27-mixed-precision-and-checkpoint-anatomy.md#t-27-10) |
| T-28-01 | Debugging training | [CH-28](chapters/part-07/28-debugging-and-training-our-tiny-model.md#t-28-01) | drafted | [section](chapters/part-07/28-debugging-and-training-our-tiny-model.md#t-28-01) |
| T-28-02 | NaNs | [CH-28](chapters/part-07/28-debugging-and-training-our-tiny-model.md#t-28-02) | drafted | [section](chapters/part-07/28-debugging-and-training-our-tiny-model.md#t-28-02) |
| T-28-03 | Exploding gradients | [CH-28](chapters/part-07/28-debugging-and-training-our-tiny-model.md#t-28-03) | drafted | [section](chapters/part-07/28-debugging-and-training-our-tiny-model.md#t-28-03) |
| T-28-04 | Bad initialization | [CH-28](chapters/part-07/28-debugging-and-training-our-tiny-model.md#t-28-04) | drafted | [section](chapters/part-07/28-debugging-and-training-our-tiny-model.md#t-28-04) |
| T-28-05 | Overfitting | [CH-28](chapters/part-07/28-debugging-and-training-our-tiny-model.md#t-28-05) | drafted | [section](chapters/part-07/28-debugging-and-training-our-tiny-model.md#t-28-05) |
| T-28-06 | Train a tiny language model | [CH-28](chapters/part-07/28-debugging-and-training-our-tiny-model.md#t-28-06) | drafted | [section](chapters/part-07/28-debugging-and-training-our-tiny-model.md#t-28-06) |
| T-29-01 | GPT to Llama-type architectures | [CH-29](chapters/part-08/29-transformer-families.md#t-29-01) | drafted | [section](chapters/part-08/29-transformer-families.md#t-29-01) |
| T-29-02 | Decoder-only Transformers | [CH-29](chapters/part-08/29-transformer-families.md#t-29-02) | drafted | [section](chapters/part-08/29-transformer-families.md#t-29-02) |
| T-29-03 | Encoder-only Transformers | [CH-29](chapters/part-08/29-transformer-families.md#t-29-03) | drafted | [section](chapters/part-08/29-transformer-families.md#t-29-03) |
| T-29-04 | BERT | [CH-29](chapters/part-08/29-transformer-families.md#t-29-04) | drafted | [section](chapters/part-08/29-transformer-families.md#t-29-04) |
| T-29-05 | Encoder-decoder Transformers | [CH-29](chapters/part-08/29-transformer-families.md#t-29-05) | drafted | [section](chapters/part-08/29-transformer-families.md#t-29-05) |
| T-29-06 | T5 | [CH-29](chapters/part-08/29-transformer-families.md#t-29-06) | drafted | [section](chapters/part-08/29-transformer-families.md#t-29-06) |
| T-29-07 | Cross-attention | [CH-29](chapters/part-08/29-transformer-families.md#t-29-07) | drafted | [section](chapters/part-08/29-transformer-families.md#t-29-07) |
| T-30-01 | RoPE deep dive | [CH-30](chapters/part-08/30-modern-positions-heads-and-mlps.md#t-30-01) | drafted | [section](chapters/part-08/30-modern-positions-heads-and-mlps.md#t-30-01) |
| T-30-02 | MHA | [CH-30](chapters/part-08/30-modern-positions-heads-and-mlps.md#t-30-02) | drafted | [section](chapters/part-08/30-modern-positions-heads-and-mlps.md#t-30-02) |
| T-30-03 | MQA | [CH-30](chapters/part-08/30-modern-positions-heads-and-mlps.md#t-30-03) | drafted | [section](chapters/part-08/30-modern-positions-heads-and-mlps.md#t-30-03) |
| T-30-04 | GQA | [CH-30](chapters/part-08/30-modern-positions-heads-and-mlps.md#t-30-04) | drafted | [section](chapters/part-08/30-modern-positions-heads-and-mlps.md#t-30-04) |
| T-30-05 | Modern MLPs | [CH-30](chapters/part-08/30-modern-positions-heads-and-mlps.md#t-30-05) | drafted | [section](chapters/part-08/30-modern-positions-heads-and-mlps.md#t-30-05) |
| T-30-06 | SwiGLU parameter accounting | [CH-30](chapters/part-08/30-modern-positions-heads-and-mlps.md#t-30-06) | drafted | [section](chapters/part-08/30-modern-positions-heads-and-mlps.md#t-30-06) |
| T-31-01 | MoE | [CH-31](chapters/part-08/31-mixture-of-experts.md#t-31-01) | drafted | [section](chapters/part-08/31-mixture-of-experts.md#t-31-01) |
| T-31-02 | Sparse activation | [CH-31](chapters/part-08/31-mixture-of-experts.md#t-31-02) | drafted | [section](chapters/part-08/31-mixture-of-experts.md#t-31-02) |
| T-31-03 | Expert routing | [CH-31](chapters/part-08/31-mixture-of-experts.md#t-31-03) | drafted | [section](chapters/part-08/31-mixture-of-experts.md#t-31-03) |
| T-31-04 | Capacity | [CH-31](chapters/part-08/31-mixture-of-experts.md#t-31-04) | drafted | [section](chapters/part-08/31-mixture-of-experts.md#t-31-04) |
| T-31-05 | Load balancing | [CH-31](chapters/part-08/31-mixture-of-experts.md#t-31-05) | drafted | [section](chapters/part-08/31-mixture-of-experts.md#t-31-05) |
| T-31-06 | Router losses | [CH-31](chapters/part-08/31-mixture-of-experts.md#t-31-06) | drafted | [section](chapters/part-08/31-mixture-of-experts.md#t-31-06) |
| T-31-07 | Expert parallelism introduction | [CH-31](chapters/part-08/31-mixture-of-experts.md#t-31-07) | drafted | [section](chapters/part-08/31-mixture-of-experts.md#t-31-07) |
| T-32-01 | Sparse attention | [CH-32](chapters/part-08/32-alternative-architectures-and-real-configs.md#t-32-01) | drafted | [section](chapters/part-08/32-alternative-architectures-and-real-configs.md#t-32-01) |
| T-32-02 | Sliding-window attention | [CH-32](chapters/part-08/32-alternative-architectures-and-real-configs.md#t-32-02) | drafted | [section](chapters/part-08/32-alternative-architectures-and-real-configs.md#t-32-02) |
| T-32-03 | Local attention | [CH-32](chapters/part-08/32-alternative-architectures-and-real-configs.md#t-32-03) | drafted | [section](chapters/part-08/32-alternative-architectures-and-real-configs.md#t-32-03) |
| T-32-04 | Global attention | [CH-32](chapters/part-08/32-alternative-architectures-and-real-configs.md#t-32-04) | drafted | [section](chapters/part-08/32-alternative-architectures-and-real-configs.md#t-32-04) |
| T-32-05 | State-space models | [CH-32](chapters/part-08/32-alternative-architectures-and-real-configs.md#t-32-05) | drafted | [section](chapters/part-08/32-alternative-architectures-and-real-configs.md#t-32-05) |
| T-32-06 | Recurrent hybrids | [CH-32](chapters/part-08/32-alternative-architectures-and-real-configs.md#t-32-06) | drafted | [section](chapters/part-08/32-alternative-architectures-and-real-configs.md#t-32-06) |
| T-32-07 | Hybrid models | [CH-32](chapters/part-08/32-alternative-architectures-and-real-configs.md#t-32-07) | drafted | [section](chapters/part-08/32-alternative-architectures-and-real-configs.md#t-32-07) |
| T-32-08 | Reading a real model config | [CH-32](chapters/part-08/32-alternative-architectures-and-real-configs.md#t-32-08) | drafted | [section](chapters/part-08/32-alternative-architectures-and-real-configs.md#t-32-08) |
| T-32-09 | Parameters | [CH-32](chapters/part-08/32-alternative-architectures-and-real-configs.md#t-32-09) | drafted | [section](chapters/part-08/32-alternative-architectures-and-real-configs.md#t-32-09) |
| T-32-10 | Attention dimensions | [CH-32](chapters/part-08/32-alternative-architectures-and-real-configs.md#t-32-10) | drafted | [section](chapters/part-08/32-alternative-architectures-and-real-configs.md#t-32-10) |
| T-32-11 | KV heads | [CH-32](chapters/part-08/32-alternative-architectures-and-real-configs.md#t-32-11) | drafted | [section](chapters/part-08/32-alternative-architectures-and-real-configs.md#t-32-11) |
| T-32-12 | MLP size | [CH-32](chapters/part-08/32-alternative-architectures-and-real-configs.md#t-32-12) | drafted | [section](chapters/part-08/32-alternative-architectures-and-real-configs.md#t-32-12) |
| T-32-13 | Memory footprint | [CH-32](chapters/part-08/32-alternative-architectures-and-real-configs.md#t-32-13) | drafted | [section](chapters/part-08/32-alternative-architectures-and-real-configs.md#t-32-13) |
| T-32-14 | FLOPs per token | [CH-32](chapters/part-08/32-alternative-architectures-and-real-configs.md#t-32-14) | drafted | [section](chapters/part-08/32-alternative-architectures-and-real-configs.md#t-32-14) |
| T-33-01 | Training data sources | [CH-33](chapters/part-09/33-data-sources-and-cleaning.md#t-33-01) | drafted | [section](chapters/part-09/33-data-sources-and-cleaning.md#t-33-01) |
| T-33-02 | Cleaning | [CH-33](chapters/part-09/33-data-sources-and-cleaning.md#t-33-02) | drafted | [section](chapters/part-09/33-data-sources-and-cleaning.md#t-33-02) |
| T-33-03 | Filtering | [CH-33](chapters/part-09/33-data-sources-and-cleaning.md#t-33-03) | drafted | [section](chapters/part-09/33-data-sources-and-cleaning.md#t-33-03) |
| T-33-04 | Deduplication | [CH-33](chapters/part-09/33-data-sources-and-cleaning.md#t-33-04) | drafted | [section](chapters/part-09/33-data-sources-and-cleaning.md#t-33-04) |
| T-33-05 | Dataset provenance | [CH-33](chapters/part-09/33-data-sources-and-cleaning.md#t-33-05) | drafted | [section](chapters/part-09/33-data-sources-and-cleaning.md#t-33-05) |
| T-34-01 | Dataset mixtures | [CH-34](chapters/part-09/34-mixtures-tokens-and-synthetic-data.md#t-34-01) | drafted | [section](chapters/part-09/34-mixtures-tokens-and-synthetic-data.md#t-34-01) |
| T-34-02 | Token budgets | [CH-34](chapters/part-09/34-mixtures-tokens-and-synthetic-data.md#t-34-02) | drafted | [section](chapters/part-09/34-mixtures-tokens-and-synthetic-data.md#t-34-02) |
| T-34-03 | Synthetic data | [CH-34](chapters/part-09/34-mixtures-tokens-and-synthetic-data.md#t-34-03) | drafted | [section](chapters/part-09/34-mixtures-tokens-and-synthetic-data.md#t-34-03) |
| T-34-04 | Data quality | [CH-34](chapters/part-09/34-mixtures-tokens-and-synthetic-data.md#t-34-04) | drafted | [section](chapters/part-09/34-mixtures-tokens-and-synthetic-data.md#t-34-04) |
| T-34-05 | Contamination | [CH-34](chapters/part-09/34-mixtures-tokens-and-synthetic-data.md#t-34-05) | drafted | [section](chapters/part-09/34-mixtures-tokens-and-synthetic-data.md#t-34-05) |
| T-34-06 | Split design | [CH-34](chapters/part-09/34-mixtures-tokens-and-synthetic-data.md#t-34-06) | drafted | [section](chapters/part-09/34-mixtures-tokens-and-synthetic-data.md#t-34-06) |
| T-35-01 | Evaluation | [CH-35](chapters/part-09/35-evaluation-and-meaningful-experiments.md#t-35-01) | drafted | [section](chapters/part-09/35-evaluation-and-meaningful-experiments.md#t-35-01) |
| T-35-02 | Perplexity | [CH-35](chapters/part-09/35-evaluation-and-meaningful-experiments.md#t-35-02) | drafted | [section](chapters/part-09/35-evaluation-and-meaningful-experiments.md#t-35-02) |
| T-35-03 | Downstream tasks | [CH-35](chapters/part-09/35-evaluation-and-meaningful-experiments.md#t-35-03) | drafted | [section](chapters/part-09/35-evaluation-and-meaningful-experiments.md#t-35-03) |
| T-35-04 | Reasoning benchmarks | [CH-35](chapters/part-09/35-evaluation-and-meaningful-experiments.md#t-35-04) | drafted | [section](chapters/part-09/35-evaluation-and-meaningful-experiments.md#t-35-04) |
| T-35-05 | Human evaluation | [CH-35](chapters/part-09/35-evaluation-and-meaningful-experiments.md#t-35-05) | drafted | [section](chapters/part-09/35-evaluation-and-meaningful-experiments.md#t-35-05) |
| T-35-06 | Experimental design | [CH-35](chapters/part-09/35-evaluation-and-meaningful-experiments.md#t-35-06) | drafted | [section](chapters/part-09/35-evaluation-and-meaningful-experiments.md#t-35-06) |
| T-35-07 | Uncertainty introduction | [CH-35](chapters/part-09/35-evaluation-and-meaningful-experiments.md#t-35-07) | drafted | [section](chapters/part-09/35-evaluation-and-meaningful-experiments.md#t-35-07) |
| T-36-01 | Scaling laws | [CH-36](chapters/part-09/36-scaling-laws.md#t-36-01) | drafted | [section](chapters/part-09/36-scaling-laws.md#t-36-01) |
| T-36-02 | Parameters vs data vs compute | [CH-36](chapters/part-09/36-scaling-laws.md#t-36-02) | drafted | [section](chapters/part-09/36-scaling-laws.md#t-36-02) |
| T-36-03 | Compute budgets | [CH-36](chapters/part-09/36-scaling-laws.md#t-36-03) | drafted | [section](chapters/part-09/36-scaling-laws.md#t-36-03) |
| T-36-04 | Scaling fits | [CH-36](chapters/part-09/36-scaling-laws.md#t-36-04) | drafted | [section](chapters/part-09/36-scaling-laws.md#t-36-04) |
| T-36-05 | Extrapolation limits | [CH-36](chapters/part-09/36-scaling-laws.md#t-36-05) | drafted | [section](chapters/part-09/36-scaling-laws.md#t-36-05) |
| T-37-01 | Pretraining vs post-training | [CH-37](chapters/part-10/37-pretraining-continued-pretraining-and-sft.md#t-37-01) | drafted | [section](chapters/part-10/37-pretraining-continued-pretraining-and-sft.md#t-37-01) |
| T-37-02 | Continued pretraining | [CH-37](chapters/part-10/37-pretraining-continued-pretraining-and-sft.md#t-37-02) | drafted | [section](chapters/part-10/37-pretraining-continued-pretraining-and-sft.md#t-37-02) |
| T-37-03 | Supervised fine-tuning | [CH-37](chapters/part-10/37-pretraining-continued-pretraining-and-sft.md#t-37-03) | drafted | [section](chapters/part-10/37-pretraining-continued-pretraining-and-sft.md#t-37-03) |
| T-37-04 | Chat templates | [CH-37](chapters/part-10/37-pretraining-continued-pretraining-and-sft.md#t-37-04) | drafted | [section](chapters/part-10/37-pretraining-continued-pretraining-and-sft.md#t-37-04) |
| T-37-05 | Loss masking | [CH-37](chapters/part-10/37-pretraining-continued-pretraining-and-sft.md#t-37-05) | drafted | [section](chapters/part-10/37-pretraining-continued-pretraining-and-sft.md#t-37-05) |
| T-38-01 | PEFT | [CH-38](chapters/part-10/38-parameter-efficient-adaptation.md#t-38-01) | drafted | [section](chapters/part-10/38-parameter-efficient-adaptation.md#t-38-01) |
| T-38-02 | Adapters | [CH-38](chapters/part-10/38-parameter-efficient-adaptation.md#t-38-02) | drafted | [section](chapters/part-10/38-parameter-efficient-adaptation.md#t-38-02) |
| T-38-03 | Prompt tuning | [CH-38](chapters/part-10/38-parameter-efficient-adaptation.md#t-38-03) | drafted | [section](chapters/part-10/38-parameter-efficient-adaptation.md#t-38-03) |
| T-38-04 | Prefix tuning | [CH-38](chapters/part-10/38-parameter-efficient-adaptation.md#t-38-04) | drafted | [section](chapters/part-10/38-parameter-efficient-adaptation.md#t-38-04) |
| T-38-05 | LoRA | [CH-38](chapters/part-10/38-parameter-efficient-adaptation.md#t-38-05) | drafted | [section](chapters/part-10/38-parameter-efficient-adaptation.md#t-38-05) |
| T-38-06 | QLoRA | [CH-38](chapters/part-10/38-parameter-efficient-adaptation.md#t-38-06) | drafted | [section](chapters/part-10/38-parameter-efficient-adaptation.md#t-38-06) |
| T-39-01 | Preference data | [CH-39](chapters/part-10/39-preferences-and-reinforcement-learning.md#t-39-01) | drafted | [section](chapters/part-10/39-preferences-and-reinforcement-learning.md#t-39-01) |
| T-39-02 | Reward models | [CH-39](chapters/part-10/39-preferences-and-reinforcement-learning.md#t-39-02) | drafted | [section](chapters/part-10/39-preferences-and-reinforcement-learning.md#t-39-02) |
| T-39-03 | RLHF | [CH-39](chapters/part-10/39-preferences-and-reinforcement-learning.md#t-39-03) | drafted | [section](chapters/part-10/39-preferences-and-reinforcement-learning.md#t-39-03) |
| T-39-04 | PPO | [CH-39](chapters/part-10/39-preferences-and-reinforcement-learning.md#t-39-04) | drafted | [section](chapters/part-10/39-preferences-and-reinforcement-learning.md#t-39-04) |
| T-39-05 | DPO-type objectives | [CH-39](chapters/part-10/39-preferences-and-reinforcement-learning.md#t-39-05) | drafted | [section](chapters/part-10/39-preferences-and-reinforcement-learning.md#t-39-05) |
| T-39-06 | Policy KL control | [CH-39](chapters/part-10/39-preferences-and-reinforcement-learning.md#t-39-06) | drafted | [section](chapters/part-10/39-preferences-and-reinforcement-learning.md#t-39-06) |
| T-40-01 | RL with verifiable rewards | [CH-40](chapters/part-10/40-reasoning-test-time-compute-and-distillation.md#t-40-01) | drafted | [section](chapters/part-10/40-reasoning-test-time-compute-and-distillation.md#t-40-01) |
| T-40-02 | Reasoning models | [CH-40](chapters/part-10/40-reasoning-test-time-compute-and-distillation.md#t-40-02) | drafted | [section](chapters/part-10/40-reasoning-test-time-compute-and-distillation.md#t-40-02) |
| T-40-03 | Why generation can produce reasoning-like behavior | [CH-40](chapters/part-10/40-reasoning-test-time-compute-and-distillation.md#t-40-03) | drafted | [section](chapters/part-10/40-reasoning-test-time-compute-and-distillation.md#t-40-03) |
| T-40-04 | Test-time compute | [CH-40](chapters/part-10/40-reasoning-test-time-compute-and-distillation.md#t-40-04) | drafted | [section](chapters/part-10/40-reasoning-test-time-compute-and-distillation.md#t-40-04) |
| T-40-05 | Distillation | [CH-40](chapters/part-10/40-reasoning-test-time-compute-and-distillation.md#t-40-05) | drafted | [section](chapters/part-10/40-reasoning-test-time-compute-and-distillation.md#t-40-05) |
| T-40-06 | Verifier limits | [CH-40](chapters/part-10/40-reasoning-test-time-compute-and-distillation.md#t-40-06) | drafted | [section](chapters/part-10/40-reasoning-test-time-compute-and-distillation.md#t-40-06) |
| T-41-01 | CPU vs GPU | [CH-41](chapters/part-11/41-why-gpus-and-how-they-execute.md#t-41-01) | drafted | [section](chapters/part-11/41-why-gpus-and-how-they-execute.md#t-41-01) |
| T-41-02 | Why GPUs | [CH-41](chapters/part-11/41-why-gpus-and-how-they-execute.md#t-41-02) | drafted | [section](chapters/part-11/41-why-gpus-and-how-they-execute.md#t-41-02) |
| T-41-03 | GPU anatomy | [CH-41](chapters/part-11/41-why-gpus-and-how-they-execute.md#t-41-03) | drafted | [section](chapters/part-11/41-why-gpus-and-how-they-execute.md#t-41-03) |
| T-41-04 | SMs | [CH-41](chapters/part-11/41-why-gpus-and-how-they-execute.md#t-41-04) | drafted | [section](chapters/part-11/41-why-gpus-and-how-they-execute.md#t-41-04) |
| T-41-05 | Threads | [CH-41](chapters/part-11/41-why-gpus-and-how-they-execute.md#t-41-05) | drafted | [section](chapters/part-11/41-why-gpus-and-how-they-execute.md#t-41-05) |
| T-41-06 | Warps | [CH-41](chapters/part-11/41-why-gpus-and-how-they-execute.md#t-41-06) | drafted | [section](chapters/part-11/41-why-gpus-and-how-they-execute.md#t-41-06) |
| T-41-07 | Blocks | [CH-41](chapters/part-11/41-why-gpus-and-how-they-execute.md#t-41-07) | drafted | [section](chapters/part-11/41-why-gpus-and-how-they-execute.md#t-41-07) |
| T-41-08 | CUDA cores | [CH-41](chapters/part-11/41-why-gpus-and-how-they-execute.md#t-41-08) | drafted | [section](chapters/part-11/41-why-gpus-and-how-they-execute.md#t-41-08) |
| T-41-09 | Tensor Cores | [CH-41](chapters/part-11/41-why-gpus-and-how-they-execute.md#t-41-09) | drafted | [section](chapters/part-11/41-why-gpus-and-how-they-execute.md#t-41-09) |
| T-41-10 | Registers | [CH-41](chapters/part-11/41-why-gpus-and-how-they-execute.md#t-41-10) | drafted | [section](chapters/part-11/41-why-gpus-and-how-they-execute.md#t-41-10) |
| T-42-01 | Memory hierarchy | [CH-42](chapters/part-11/42-memory-hierarchy-and-movement.md#t-42-01) | drafted | [section](chapters/part-11/42-memory-hierarchy-and-movement.md#t-42-01) |
| T-42-02 | Shared memory and SRAM | [CH-42](chapters/part-11/42-memory-hierarchy-and-movement.md#t-42-02) | drafted | [section](chapters/part-11/42-memory-hierarchy-and-movement.md#t-42-02) |
| T-42-03 | Caches | [CH-42](chapters/part-11/42-memory-hierarchy-and-movement.md#t-42-03) | drafted | [section](chapters/part-11/42-memory-hierarchy-and-movement.md#t-42-03) |
| T-42-04 | HBM | [CH-42](chapters/part-11/42-memory-hierarchy-and-movement.md#t-42-04) | drafted | [section](chapters/part-11/42-memory-hierarchy-and-movement.md#t-42-04) |
| T-42-05 | RAM | [CH-42](chapters/part-11/42-memory-hierarchy-and-movement.md#t-42-05) | drafted | [section](chapters/part-11/42-memory-hierarchy-and-movement.md#t-42-05) |
| T-42-06 | SSD | [CH-42](chapters/part-11/42-memory-hierarchy-and-movement.md#t-42-06) | drafted | [section](chapters/part-11/42-memory-hierarchy-and-movement.md#t-42-06) |
| T-42-07 | HBM bandwidth | [CH-42](chapters/part-11/42-memory-hierarchy-and-movement.md#t-42-07) | drafted | [section](chapters/part-11/42-memory-hierarchy-and-movement.md#t-42-07) |
| T-42-08 | Coalescing | [CH-42](chapters/part-11/42-memory-hierarchy-and-movement.md#t-42-08) | drafted | [section](chapters/part-11/42-memory-hierarchy-and-movement.md#t-42-08) |
| T-43-01 | Compute throughput | [CH-43](chapters/part-11/43-throughput-intensity-and-rooflines.md#t-43-01) | drafted | [section](chapters/part-11/43-throughput-intensity-and-rooflines.md#t-43-01) |
| T-43-02 | Arithmetic intensity | [CH-43](chapters/part-11/43-throughput-intensity-and-rooflines.md#t-43-02) | drafted | [section](chapters/part-11/43-throughput-intensity-and-rooflines.md#t-43-02) |
| T-43-03 | Compute-bound vs memory-bound | [CH-43](chapters/part-11/43-throughput-intensity-and-rooflines.md#t-43-03) | drafted | [section](chapters/part-11/43-throughput-intensity-and-rooflines.md#t-43-03) |
| T-43-04 | Roofline model | [CH-43](chapters/part-11/43-throughput-intensity-and-rooflines.md#t-43-04) | drafted | [section](chapters/part-11/43-throughput-intensity-and-rooflines.md#t-43-04) |
| T-44-01 | Decode memory bottlenecks | [CH-44](chapters/part-11/44-profiling-transformer-bottlenecks.md#t-44-01) | drafted | [section](chapters/part-11/44-profiling-transformer-bottlenecks.md#t-44-01) |
| T-44-02 | FLOPs and memory profiling | [CH-44](chapters/part-11/44-profiling-transformer-bottlenecks.md#t-44-02) | drafted | [section](chapters/part-11/44-profiling-transformer-bottlenecks.md#t-44-02) |
| T-44-03 | Bandwidth utilization | [CH-44](chapters/part-11/44-profiling-transformer-bottlenecks.md#t-44-03) | drafted | [section](chapters/part-11/44-profiling-transformer-bottlenecks.md#t-44-03) |
| T-44-04 | Latency measurement | [CH-44](chapters/part-11/44-profiling-transformer-bottlenecks.md#t-44-04) | drafted | [section](chapters/part-11/44-profiling-transformer-bottlenecks.md#t-44-04) |
| T-44-05 | Synchronization | [CH-44](chapters/part-11/44-profiling-transformer-bottlenecks.md#t-44-05) | drafted | [section](chapters/part-11/44-profiling-transformer-bottlenecks.md#t-44-05) |
| T-45-01 | GPU kernels | [CH-45](chapters/part-12/45-kernels-gemm-and-tiling.md#t-45-01) | drafted | [section](chapters/part-12/45-kernels-gemm-and-tiling.md#t-45-01) |
| T-45-02 | GEMM | [CH-45](chapters/part-12/45-kernels-gemm-and-tiling.md#t-45-02) | drafted | [section](chapters/part-12/45-kernels-gemm-and-tiling.md#t-45-02) |
| T-45-03 | Tiling | [CH-45](chapters/part-12/45-kernels-gemm-and-tiling.md#t-45-03) | drafted | [section](chapters/part-12/45-kernels-gemm-and-tiling.md#t-45-03) |
| T-45-04 | Tensor Core MMA | [CH-45](chapters/part-12/45-kernels-gemm-and-tiling.md#t-45-04) | drafted | [section](chapters/part-12/45-kernels-gemm-and-tiling.md#t-45-04) |
| T-45-05 | Kernel launch overhead | [CH-45](chapters/part-12/45-kernels-gemm-and-tiling.md#t-45-05) | drafted | [section](chapters/part-12/45-kernels-gemm-and-tiling.md#t-45-05) |
| T-45-06 | Kernel fusion | [CH-45](chapters/part-12/45-kernels-gemm-and-tiling.md#t-45-06) | drafted | [section](chapters/part-12/45-kernels-gemm-and-tiling.md#t-45-06) |
| T-46-01 | CUDA | [CH-46](chapters/part-12/46-cuda-triton-and-cutlass.md#t-46-01) | drafted | [section](chapters/part-12/46-cuda-triton-and-cutlass.md#t-46-01) |
| T-46-02 | Triton | [CH-46](chapters/part-12/46-cuda-triton-and-cutlass.md#t-46-02) | drafted | [section](chapters/part-12/46-cuda-triton-and-cutlass.md#t-46-02) |
| T-46-03 | CUTLASS-level concepts | [CH-46](chapters/part-12/46-cuda-triton-and-cutlass.md#t-46-03) | drafted | [section](chapters/part-12/46-cuda-triton-and-cutlass.md#t-46-03) |
| T-46-04 | Simple Triton kernel | [CH-46](chapters/part-12/46-cuda-triton-and-cutlass.md#t-46-04) | drafted | [section](chapters/part-12/46-cuda-triton-and-cutlass.md#t-46-04) |
| T-46-05 | GPU profiling | [CH-46](chapters/part-12/46-cuda-triton-and-cutlass.md#t-46-05) | drafted | [section](chapters/part-12/46-cuda-triton-and-cutlass.md#t-46-05) |
| T-47-01 | PyTorch eager execution | [CH-47](chapters/part-12/47-graphs-compilers-and-runtimes.md#t-47-01) | drafted | [section](chapters/part-12/47-graphs-compilers-and-runtimes.md#t-47-01) |
| T-47-02 | Computational graph capture | [CH-47](chapters/part-12/47-graphs-compilers-and-runtimes.md#t-47-02) | drafted | [section](chapters/part-12/47-graphs-compilers-and-runtimes.md#t-47-02) |
| T-47-03 | TorchDynamo | [CH-47](chapters/part-12/47-graphs-compilers-and-runtimes.md#t-47-03) | drafted | [section](chapters/part-12/47-graphs-compilers-and-runtimes.md#t-47-03) |
| T-47-04 | Intermediate representation | [CH-47](chapters/part-12/47-graphs-compilers-and-runtimes.md#t-47-04) | drafted | [section](chapters/part-12/47-graphs-compilers-and-runtimes.md#t-47-04) |
| T-47-05 | torch.compile | [CH-47](chapters/part-12/47-graphs-compilers-and-runtimes.md#t-47-05) | drafted | [section](chapters/part-12/47-graphs-compilers-and-runtimes.md#t-47-05) |
| T-47-06 | Inductor | [CH-47](chapters/part-12/47-graphs-compilers-and-runtimes.md#t-47-06) | drafted | [section](chapters/part-12/47-graphs-compilers-and-runtimes.md#t-47-06) |
| T-47-07 | Generated kernels | [CH-47](chapters/part-12/47-graphs-compilers-and-runtimes.md#t-47-07) | drafted | [section](chapters/part-12/47-graphs-compilers-and-runtimes.md#t-47-07) |
| T-47-08 | Compiler graph breaks | [CH-47](chapters/part-12/47-graphs-compilers-and-runtimes.md#t-47-08) | drafted | [section](chapters/part-12/47-graphs-compilers-and-runtimes.md#t-47-08) |
| T-48-01 | CUDA Graphs | [CH-48](chapters/part-12/48-cuda-graphs-and-execution-overhead.md#t-48-01) | drafted | [section](chapters/part-12/48-cuda-graphs-and-execution-overhead.md#t-48-01) |
| T-48-02 | Dispatch overhead | [CH-48](chapters/part-12/48-cuda-graphs-and-execution-overhead.md#t-48-02) | drafted | [section](chapters/part-12/48-cuda-graphs-and-execution-overhead.md#t-48-02) |
| T-48-03 | Graph replay | [CH-48](chapters/part-12/48-cuda-graphs-and-execution-overhead.md#t-48-03) | drafted | [section](chapters/part-12/48-cuda-graphs-and-execution-overhead.md#t-48-03) |
| T-48-04 | Shape specialization | [CH-48](chapters/part-12/48-cuda-graphs-and-execution-overhead.md#t-48-04) | drafted | [section](chapters/part-12/48-cuda-graphs-and-execution-overhead.md#t-48-04) |
| T-48-05 | Compilation amortization | [CH-48](chapters/part-12/48-cuda-graphs-and-execution-overhead.md#t-48-05) | drafted | [section](chapters/part-12/48-cuda-graphs-and-execution-overhead.md#t-48-05) |
| T-49-01 | Loading model weights | [CH-49](chapters/part-13/49-load-weights-and-trace-a-forward-pass.md#t-49-01) | drafted | [section](chapters/part-13/49-load-weights-and-trace-a-forward-pass.md#t-49-01) |
| T-49-02 | Prompt processing | [CH-49](chapters/part-13/49-load-weights-and-trace-a-forward-pass.md#t-49-02) | drafted | [section](chapters/part-13/49-load-weights-and-trace-a-forward-pass.md#t-49-02) |
| T-49-03 | GPU inference | [CH-49](chapters/part-13/49-load-weights-and-trace-a-forward-pass.md#t-49-03) | drafted | [section](chapters/part-13/49-load-weights-and-trace-a-forward-pass.md#t-49-03) |
| T-49-04 | End-to-end real-model forward-pass tracing | [CH-49](chapters/part-13/49-load-weights-and-trace-a-forward-pass.md#t-49-04) | drafted | [section](chapters/part-13/49-load-weights-and-trace-a-forward-pass.md#t-49-04) |
| T-50-01 | Prefill | [CH-50](chapters/part-13/50-prefill-decode-and-kv-cache.md#t-50-01) | drafted | [section](chapters/part-13/50-prefill-decode-and-kv-cache.md#t-50-01) |
| T-50-02 | Autoregressive decode | [CH-50](chapters/part-13/50-prefill-decode-and-kv-cache.md#t-50-02) | drafted | [section](chapters/part-13/50-prefill-decode-and-kv-cache.md#t-50-02) |
| T-50-03 | KV cache | [CH-50](chapters/part-13/50-prefill-decode-and-kv-cache.md#t-50-03) | drafted | [section](chapters/part-13/50-prefill-decode-and-kv-cache.md#t-50-03) |
| T-50-04 | Why cache K and V but not historical Q | [CH-50](chapters/part-13/50-prefill-decode-and-kv-cache.md#t-50-04) | drafted | [section](chapters/part-13/50-prefill-decode-and-kv-cache.md#t-50-04) |
| T-50-05 | Context length | [CH-50](chapters/part-13/50-prefill-decode-and-kv-cache.md#t-50-05) | drafted | [section](chapters/part-13/50-prefill-decode-and-kv-cache.md#t-50-05) |
| T-51-01 | Sampling | [CH-51](chapters/part-13/51-sampling-and-decoding-policies.md#t-51-01) | drafted | [section](chapters/part-13/51-sampling-and-decoding-policies.md#t-51-01) |
| T-51-02 | Greedy decoding | [CH-51](chapters/part-13/51-sampling-and-decoding-policies.md#t-51-02) | drafted | [section](chapters/part-13/51-sampling-and-decoding-policies.md#t-51-02) |
| T-51-03 | Temperature | [CH-51](chapters/part-13/51-sampling-and-decoding-policies.md#t-51-03) | drafted | [section](chapters/part-13/51-sampling-and-decoding-policies.md#t-51-03) |
| T-51-04 | Top-k | [CH-51](chapters/part-13/51-sampling-and-decoding-policies.md#t-51-04) | drafted | [section](chapters/part-13/51-sampling-and-decoding-policies.md#t-51-04) |
| T-51-05 | Top-p | [CH-51](chapters/part-13/51-sampling-and-decoding-policies.md#t-51-05) | drafted | [section](chapters/part-13/51-sampling-and-decoding-policies.md#t-51-05) |
| T-51-06 | Beam search | [CH-51](chapters/part-13/51-sampling-and-decoding-policies.md#t-51-06) | drafted | [section](chapters/part-13/51-sampling-and-decoding-policies.md#t-51-06) |
| T-51-07 | Stopping conditions | [CH-51](chapters/part-13/51-sampling-and-decoding-policies.md#t-51-07) | drafted | [section](chapters/part-13/51-sampling-and-decoding-policies.md#t-51-07) |
| T-52-01 | Inference memory accounting | [CH-52](chapters/part-13/52-inference-memory-and-latency-accounting.md#t-52-01) | drafted | [section](chapters/part-13/52-inference-memory-and-latency-accounting.md#t-52-01) |
| T-52-02 | Weights plus KV plus activations plus overhead | [CH-52](chapters/part-13/52-inference-memory-and-latency-accounting.md#t-52-02) | drafted | [section](chapters/part-13/52-inference-memory-and-latency-accounting.md#t-52-02) |
| T-52-03 | TTFT | [CH-52](chapters/part-13/52-inference-memory-and-latency-accounting.md#t-52-03) | drafted | [section](chapters/part-13/52-inference-memory-and-latency-accounting.md#t-52-03) |
| T-52-04 | Inter-token latency | [CH-52](chapters/part-13/52-inference-memory-and-latency-accounting.md#t-52-04) | drafted | [section](chapters/part-13/52-inference-memory-and-latency-accounting.md#t-52-04) |
| T-52-05 | TPOT | [CH-52](chapters/part-13/52-inference-memory-and-latency-accounting.md#t-52-05) | drafted | [section](chapters/part-13/52-inference-memory-and-latency-accounting.md#t-52-05) |
| T-52-06 | Throughput | [CH-52](chapters/part-13/52-inference-memory-and-latency-accounting.md#t-52-06) | drafted | [section](chapters/part-13/52-inference-memory-and-latency-accounting.md#t-52-06) |
| T-52-07 | Memory per token | [CH-52](chapters/part-13/52-inference-memory-and-latency-accounting.md#t-52-07) | drafted | [section](chapters/part-13/52-inference-memory-and-latency-accounting.md#t-52-07) |
| T-52-08 | FLOPs per token | [CH-52](chapters/part-13/52-inference-memory-and-latency-accounting.md#t-52-08) | drafted | [section](chapters/part-13/52-inference-memory-and-latency-accounting.md#t-52-08) |
| T-53-01 | Why naive inference is slow | [CH-53](chapters/part-14/53-flashattention-and-paged-kv-memory.md#t-53-01) | drafted | [section](chapters/part-14/53-flashattention-and-paged-kv-memory.md#t-53-01) |
| T-53-02 | FlashAttention | [CH-53](chapters/part-14/53-flashattention-and-paged-kv-memory.md#t-53-02) | drafted | [section](chapters/part-14/53-flashattention-and-paged-kv-memory.md#t-53-02) |
| T-53-03 | Attention IO scheduling | [CH-53](chapters/part-14/53-flashattention-and-paged-kv-memory.md#t-53-03) | drafted | [section](chapters/part-14/53-flashattention-and-paged-kv-memory.md#t-53-03) |
| T-53-04 | KV cache layout | [CH-53](chapters/part-14/53-flashattention-and-paged-kv-memory.md#t-53-04) | drafted | [section](chapters/part-14/53-flashattention-and-paged-kv-memory.md#t-53-04) |
| T-53-05 | Paged KV memory | [CH-53](chapters/part-14/53-flashattention-and-paged-kv-memory.md#t-53-05) | drafted | [section](chapters/part-14/53-flashattention-and-paged-kv-memory.md#t-53-05) |
| T-53-06 | PagedAttention | [CH-53](chapters/part-14/53-flashattention-and-paged-kv-memory.md#t-53-06) | drafted | [section](chapters/part-14/53-flashattention-and-paged-kv-memory.md#t-53-06) |
| T-54-01 | Prefix caching | [CH-54](chapters/part-14/54-caching-batching-and-prefill-scheduling.md#t-54-01) | drafted | [section](chapters/part-14/54-caching-batching-and-prefill-scheduling.md#t-54-01) |
| T-54-02 | Prefix reuse | [CH-54](chapters/part-14/54-caching-batching-and-prefill-scheduling.md#t-54-02) | drafted | [section](chapters/part-14/54-caching-batching-and-prefill-scheduling.md#t-54-02) |
| T-54-03 | Continuous batching | [CH-54](chapters/part-14/54-caching-batching-and-prefill-scheduling.md#t-54-03) | drafted | [section](chapters/part-14/54-caching-batching-and-prefill-scheduling.md#t-54-03) |
| T-54-04 | Chunked prefill | [CH-54](chapters/part-14/54-caching-batching-and-prefill-scheduling.md#t-54-04) | drafted | [section](chapters/part-14/54-caching-batching-and-prefill-scheduling.md#t-54-04) |
| T-54-05 | Cache correctness | [CH-54](chapters/part-14/54-caching-batching-and-prefill-scheduling.md#t-54-05) | drafted | [section](chapters/part-14/54-caching-batching-and-prefill-scheduling.md#t-54-05) |
| T-55-01 | Speculative decoding | [CH-55](chapters/part-14/55-speculative-decoding-and-dynamic-execution.md#t-55-01) | drafted | [section](chapters/part-14/55-speculative-decoding-and-dynamic-execution.md#t-55-01) |
| T-55-02 | Draft-verifier design | [CH-55](chapters/part-14/55-speculative-decoding-and-dynamic-execution.md#t-55-02) | drafted | [section](chapters/part-14/55-speculative-decoding-and-dynamic-execution.md#t-55-02) |
| T-55-03 | Speculative-model architectures | [CH-55](chapters/part-14/55-speculative-decoding-and-dynamic-execution.md#t-55-03) | drafted | [section](chapters/part-14/55-speculative-decoding-and-dynamic-execution.md#t-55-03) |
| T-55-04 | Sparsity | [CH-55](chapters/part-14/55-speculative-decoding-and-dynamic-execution.md#t-55-04) | drafted | [section](chapters/part-14/55-speculative-decoding-and-dynamic-execution.md#t-55-04) |
| T-55-05 | Pruning | [CH-55](chapters/part-14/55-speculative-decoding-and-dynamic-execution.md#t-55-05) | drafted | [section](chapters/part-14/55-speculative-decoding-and-dynamic-execution.md#t-55-05) |
| T-55-06 | Early exit | [CH-55](chapters/part-14/55-speculative-decoding-and-dynamic-execution.md#t-55-06) | drafted | [section](chapters/part-14/55-speculative-decoding-and-dynamic-execution.md#t-55-06) |
| T-55-07 | Layer skipping | [CH-55](chapters/part-14/55-speculative-decoding-and-dynamic-execution.md#t-55-07) | drafted | [section](chapters/part-14/55-speculative-decoding-and-dynamic-execution.md#t-55-07) |
| T-55-08 | CUDA Graph optimization | [CH-55](chapters/part-14/55-speculative-decoding-and-dynamic-execution.md#t-55-08) | drafted | [section](chapters/part-14/55-speculative-decoding-and-dynamic-execution.md#t-55-08) |
| T-56-01 | Quantization | [CH-56](chapters/part-14/56-quantization-across-the-inference-path.md#t-56-01) | drafted | [section](chapters/part-14/56-quantization-across-the-inference-path.md#t-56-01) |
| T-56-02 | PTQ | [CH-56](chapters/part-14/56-quantization-across-the-inference-path.md#t-56-02) | drafted | [section](chapters/part-14/56-quantization-across-the-inference-path.md#t-56-02) |
| T-56-03 | QAT | [CH-56](chapters/part-14/56-quantization-across-the-inference-path.md#t-56-03) | drafted | [section](chapters/part-14/56-quantization-across-the-inference-path.md#t-56-03) |
| T-56-04 | GPTQ | [CH-56](chapters/part-14/56-quantization-across-the-inference-path.md#t-56-04) | drafted | [section](chapters/part-14/56-quantization-across-the-inference-path.md#t-56-04) |
| T-56-05 | AWQ | [CH-56](chapters/part-14/56-quantization-across-the-inference-path.md#t-56-05) | drafted | [section](chapters/part-14/56-quantization-across-the-inference-path.md#t-56-05) |
| T-56-06 | Weight quantization | [CH-56](chapters/part-14/56-quantization-across-the-inference-path.md#t-56-06) | drafted | [section](chapters/part-14/56-quantization-across-the-inference-path.md#t-56-06) |
| T-56-07 | Activation quantization | [CH-56](chapters/part-14/56-quantization-across-the-inference-path.md#t-56-07) | drafted | [section](chapters/part-14/56-quantization-across-the-inference-path.md#t-56-07) |
| T-56-08 | KV quantization | [CH-56](chapters/part-14/56-quantization-across-the-inference-path.md#t-56-08) | drafted | [section](chapters/part-14/56-quantization-across-the-inference-path.md#t-56-08) |
| T-56-09 | FP8 inference | [CH-56](chapters/part-14/56-quantization-across-the-inference-path.md#t-56-09) | drafted | [section](chapters/part-14/56-quantization-across-the-inference-path.md#t-56-09) |
| T-56-10 | INT8 inference | [CH-56](chapters/part-14/56-quantization-across-the-inference-path.md#t-56-10) | drafted | [section](chapters/part-14/56-quantization-across-the-inference-path.md#t-56-10) |
| T-56-11 | INT4 inference | [CH-56](chapters/part-14/56-quantization-across-the-inference-path.md#t-56-11) | drafted | [section](chapters/part-14/56-quantization-across-the-inference-path.md#t-56-11) |
| T-56-12 | GGUF formats | [CH-56](chapters/part-14/56-quantization-across-the-inference-path.md#t-56-12) | drafted | [section](chapters/part-14/56-quantization-across-the-inference-path.md#t-56-12) |
| T-57-01 | Why one accelerator stops being enough | [CH-57](chapters/part-15/57-parallel-training-strategies.md#t-57-01) | drafted | [section](chapters/part-15/57-parallel-training-strategies.md#t-57-01) |
| T-57-02 | Data parallelism | [CH-57](chapters/part-15/57-parallel-training-strategies.md#t-57-02) | drafted | [section](chapters/part-15/57-parallel-training-strategies.md#t-57-02) |
| T-57-03 | DDP | [CH-57](chapters/part-15/57-parallel-training-strategies.md#t-57-03) | drafted | [section](chapters/part-15/57-parallel-training-strategies.md#t-57-03) |
| T-57-04 | ZeRO | [CH-57](chapters/part-15/57-parallel-training-strategies.md#t-57-04) | drafted | [section](chapters/part-15/57-parallel-training-strategies.md#t-57-04) |
| T-57-05 | FSDP | [CH-57](chapters/part-15/57-parallel-training-strategies.md#t-57-05) | drafted | [section](chapters/part-15/57-parallel-training-strategies.md#t-57-05) |
| T-57-06 | Sharded optimizer state | [CH-57](chapters/part-15/57-parallel-training-strategies.md#t-57-06) | drafted | [section](chapters/part-15/57-parallel-training-strategies.md#t-57-06) |
| T-58-01 | Tensor parallelism | [CH-58](chapters/part-15/58-partitioning-model-computation.md#t-58-01) | drafted | [section](chapters/part-15/58-partitioning-model-computation.md#t-58-01) |
| T-58-02 | Pipeline parallelism | [CH-58](chapters/part-15/58-partitioning-model-computation.md#t-58-02) | drafted | [section](chapters/part-15/58-partitioning-model-computation.md#t-58-02) |
| T-58-03 | Sequence parallelism | [CH-58](chapters/part-15/58-partitioning-model-computation.md#t-58-03) | drafted | [section](chapters/part-15/58-partitioning-model-computation.md#t-58-03) |
| T-58-04 | Context parallelism | [CH-58](chapters/part-15/58-partitioning-model-computation.md#t-58-04) | drafted | [section](chapters/part-15/58-partitioning-model-computation.md#t-58-04) |
| T-58-05 | Expert parallelism | [CH-58](chapters/part-15/58-partitioning-model-computation.md#t-58-05) | drafted | [section](chapters/part-15/58-partitioning-model-computation.md#t-58-05) |
| T-59-01 | Broadcast | [CH-59](chapters/part-15/59-collectives-and-interconnects.md#t-59-01) | drafted | [section](chapters/part-15/59-collectives-and-interconnects.md#t-59-01) |
| T-59-02 | All-reduce | [CH-59](chapters/part-15/59-collectives-and-interconnects.md#t-59-02) | drafted | [section](chapters/part-15/59-collectives-and-interconnects.md#t-59-02) |
| T-59-03 | All-gather | [CH-59](chapters/part-15/59-collectives-and-interconnects.md#t-59-03) | drafted | [section](chapters/part-15/59-collectives-and-interconnects.md#t-59-03) |
| T-59-04 | Reduce-scatter | [CH-59](chapters/part-15/59-collectives-and-interconnects.md#t-59-04) | drafted | [section](chapters/part-15/59-collectives-and-interconnects.md#t-59-04) |
| T-59-05 | All-to-all | [CH-59](chapters/part-15/59-collectives-and-interconnects.md#t-59-05) | drafted | [section](chapters/part-15/59-collectives-and-interconnects.md#t-59-05) |
| T-59-06 | NCCL | [CH-59](chapters/part-15/59-collectives-and-interconnects.md#t-59-06) | drafted | [section](chapters/part-15/59-collectives-and-interconnects.md#t-59-06) |
| T-59-07 | PCIe | [CH-59](chapters/part-15/59-collectives-and-interconnects.md#t-59-07) | drafted | [section](chapters/part-15/59-collectives-and-interconnects.md#t-59-07) |
| T-59-08 | NVLink | [CH-59](chapters/part-15/59-collectives-and-interconnects.md#t-59-08) | drafted | [section](chapters/part-15/59-collectives-and-interconnects.md#t-59-08) |
| T-59-09 | NVSwitch | [CH-59](chapters/part-15/59-collectives-and-interconnects.md#t-59-09) | drafted | [section](chapters/part-15/59-collectives-and-interconnects.md#t-59-09) |
| T-59-10 | InfiniBand | [CH-59](chapters/part-15/59-collectives-and-interconnects.md#t-59-10) | drafted | [section](chapters/part-15/59-collectives-and-interconnects.md#t-59-10) |
| T-60-01 | Distributed training failures | [CH-60](chapters/part-15/60-distributed-execution-and-failure-recovery.md#t-60-01) | drafted | [section](chapters/part-15/60-distributed-execution-and-failure-recovery.md#t-60-01) |
| T-60-02 | Distributed inference | [CH-60](chapters/part-15/60-distributed-execution-and-failure-recovery.md#t-60-02) | drafted | [section](chapters/part-15/60-distributed-execution-and-failure-recovery.md#t-60-02) |
| T-60-03 | Stragglers | [CH-60](chapters/part-15/60-distributed-execution-and-failure-recovery.md#t-60-03) | drafted | [section](chapters/part-15/60-distributed-execution-and-failure-recovery.md#t-60-03) |
| T-60-04 | Multi-GPU execution | [CH-60](chapters/part-15/60-distributed-execution-and-failure-recovery.md#t-60-04) | drafted | [section](chapters/part-15/60-distributed-execution-and-failure-recovery.md#t-60-04) |
| T-60-05 | Checkpoint recovery | [CH-60](chapters/part-15/60-distributed-execution-and-failure-recovery.md#t-60-05) | drafted | [section](chapters/part-15/60-distributed-execution-and-failure-recovery.md#t-60-05) |
| T-61-01 | Inference server architecture | [CH-61](chapters/part-16/61-anatomy-of-an-inference-server.md#t-61-01) | drafted | [section](chapters/part-16/61-anatomy-of-an-inference-server.md#t-61-01) |
| T-61-02 | HTTP requests | [CH-61](chapters/part-16/61-anatomy-of-an-inference-server.md#t-61-02) | drafted | [section](chapters/part-16/61-anatomy-of-an-inference-server.md#t-61-02) |
| T-61-03 | Request queues | [CH-61](chapters/part-16/61-anatomy-of-an-inference-server.md#t-61-03) | drafted | [section](chapters/part-16/61-anatomy-of-an-inference-server.md#t-61-03) |
| T-61-04 | Scheduling | [CH-61](chapters/part-16/61-anatomy-of-an-inference-server.md#t-61-04) | drafted | [section](chapters/part-16/61-anatomy-of-an-inference-server.md#t-61-04) |
| T-61-05 | Dynamic batching | [CH-61](chapters/part-16/61-anatomy-of-an-inference-server.md#t-61-05) | drafted | [section](chapters/part-16/61-anatomy-of-an-inference-server.md#t-61-05) |
| T-61-06 | KV allocation | [CH-61](chapters/part-16/61-anatomy-of-an-inference-server.md#t-61-06) | drafted | [section](chapters/part-16/61-anatomy-of-an-inference-server.md#t-61-06) |
| T-61-07 | Streaming | [CH-61](chapters/part-16/61-anatomy-of-an-inference-server.md#t-61-07) | drafted | [section](chapters/part-16/61-anatomy-of-an-inference-server.md#t-61-07) |
| T-62-01 | Multi-tenant serving | [CH-62](chapters/part-16/62-tenants-models-and-residency.md#t-62-01) | drafted | [section](chapters/part-16/62-tenants-models-and-residency.md#t-62-01) |
| T-62-02 | Multi-model serving | [CH-62](chapters/part-16/62-tenants-models-and-residency.md#t-62-02) | drafted | [section](chapters/part-16/62-tenants-models-and-residency.md#t-62-02) |
| T-62-03 | Memory residency | [CH-62](chapters/part-16/62-tenants-models-and-residency.md#t-62-03) | drafted | [section](chapters/part-16/62-tenants-models-and-residency.md#t-62-03) |
| T-62-04 | Model loading | [CH-62](chapters/part-16/62-tenants-models-and-residency.md#t-62-04) | drafted | [section](chapters/part-16/62-tenants-models-and-residency.md#t-62-04) |
| T-62-05 | Model offloading | [CH-62](chapters/part-16/62-tenants-models-and-residency.md#t-62-05) | drafted | [section](chapters/part-16/62-tenants-models-and-residency.md#t-62-05) |
| T-62-06 | GPU-RAM-SSD hierarchy | [CH-62](chapters/part-16/62-tenants-models-and-residency.md#t-62-06) | drafted | [section](chapters/part-16/62-tenants-models-and-residency.md#t-62-06) |
| T-63-01 | Prefill/decode disaggregation | [CH-63](chapters/part-16/63-disaggregation-and-runtime-comparisons.md#t-63-01) | drafted | [section](chapters/part-16/63-disaggregation-and-runtime-comparisons.md#t-63-01) |
| T-63-02 | vLLM internals | [CH-63](chapters/part-16/63-disaggregation-and-runtime-comparisons.md#t-63-02) | drafted | [section](chapters/part-16/63-disaggregation-and-runtime-comparisons.md#t-63-02) |
| T-63-03 | TensorRT-LLM internals | [CH-63](chapters/part-16/63-disaggregation-and-runtime-comparisons.md#t-63-03) | drafted | [section](chapters/part-16/63-disaggregation-and-runtime-comparisons.md#t-63-03) |
| T-63-04 | llama.cpp architecture comparison | [CH-63](chapters/part-16/63-disaggregation-and-runtime-comparisons.md#t-63-04) | drafted | [section](chapters/part-16/63-disaggregation-and-runtime-comparisons.md#t-63-04) |
| T-63-05 | Transfer overhead | [CH-63](chapters/part-16/63-disaggregation-and-runtime-comparisons.md#t-63-05) | drafted | [section](chapters/part-16/63-disaggregation-and-runtime-comparisons.md#t-63-05) |
| T-64-01 | Throughput vs latency | [CH-64](chapters/part-16/64-production-serving-and-gpu-clusters.md#t-64-01) | drafted | [section](chapters/part-16/64-production-serving-and-gpu-clusters.md#t-64-01) |
| T-64-02 | Tokens per second | [CH-64](chapters/part-16/64-production-serving-and-gpu-clusters.md#t-64-02) | drafted | [section](chapters/part-16/64-production-serving-and-gpu-clusters.md#t-64-02) |
| T-64-03 | Requests per second | [CH-64](chapters/part-16/64-production-serving-and-gpu-clusters.md#t-64-03) | drafted | [section](chapters/part-16/64-production-serving-and-gpu-clusters.md#t-64-03) |
| T-64-04 | p95 and p99 latency | [CH-64](chapters/part-16/64-production-serving-and-gpu-clusters.md#t-64-04) | drafted | [section](chapters/part-16/64-production-serving-and-gpu-clusters.md#t-64-04) |
| T-64-05 | Serving SLOs | [CH-64](chapters/part-16/64-production-serving-and-gpu-clusters.md#t-64-05) | drafted | [section](chapters/part-16/64-production-serving-and-gpu-clusters.md#t-64-05) |
| T-64-06 | Observability | [CH-64](chapters/part-16/64-production-serving-and-gpu-clusters.md#t-64-06) | drafted | [section](chapters/part-16/64-production-serving-and-gpu-clusters.md#t-64-06) |
| T-64-07 | Autoscaling | [CH-64](chapters/part-16/64-production-serving-and-gpu-clusters.md#t-64-07) | drafted | [section](chapters/part-16/64-production-serving-and-gpu-clusters.md#t-64-07) |
| T-64-08 | Failure recovery | [CH-64](chapters/part-16/64-production-serving-and-gpu-clusters.md#t-64-08) | drafted | [section](chapters/part-16/64-production-serving-and-gpu-clusters.md#t-64-08) |
| T-64-09 | GPU cluster scheduling | [CH-64](chapters/part-16/64-production-serving-and-gpu-clusters.md#t-64-09) | drafted | [section](chapters/part-16/64-production-serving-and-gpu-clusters.md#t-64-09) |
| T-65-01 | Edge constraints | [CH-65](chapters/part-17/65-cpu-and-edge-inference.md#t-65-01) | drafted | [section](chapters/part-17/65-cpu-and-edge-inference.md#t-65-01) |
| T-65-02 | CPU inference | [CH-65](chapters/part-17/65-cpu-and-edge-inference.md#t-65-02) | drafted | [section](chapters/part-17/65-cpu-and-edge-inference.md#t-65-02) |
| T-65-03 | SIMD | [CH-65](chapters/part-17/65-cpu-and-edge-inference.md#t-65-03) | drafted | [section](chapters/part-17/65-cpu-and-edge-inference.md#t-65-03) |
| T-65-04 | CPU vectorization | [CH-65](chapters/part-17/65-cpu-and-edge-inference.md#t-65-04) | drafted | [section](chapters/part-17/65-cpu-and-edge-inference.md#t-65-04) |
| T-65-05 | CPU threading | [CH-65](chapters/part-17/65-cpu-and-edge-inference.md#t-65-05) | drafted | [section](chapters/part-17/65-cpu-and-edge-inference.md#t-65-05) |
| T-66-01 | GPU offloading | [CH-66](chapters/part-17/66-hybrid-memory-and-local-loading.md#t-66-01) | drafted | [section](chapters/part-17/66-hybrid-memory-and-local-loading.md#t-66-01) |
| T-66-02 | CPU-GPU hybrid inference | [CH-66](chapters/part-17/66-hybrid-memory-and-local-loading.md#t-66-02) | drafted | [section](chapters/part-17/66-hybrid-memory-and-local-loading.md#t-66-02) |
| T-66-03 | Unified memory | [CH-66](chapters/part-17/66-hybrid-memory-and-local-loading.md#t-66-03) | drafted | [section](chapters/part-17/66-hybrid-memory-and-local-loading.md#t-66-03) |
| T-66-04 | Shared memory | [CH-66](chapters/part-17/66-hybrid-memory-and-local-loading.md#t-66-04) | drafted | [section](chapters/part-17/66-hybrid-memory-and-local-loading.md#t-66-04) |
| T-66-05 | Quantized formats | [CH-66](chapters/part-17/66-hybrid-memory-and-local-loading.md#t-66-05) | drafted | [section](chapters/part-17/66-hybrid-memory-and-local-loading.md#t-66-05) |
| T-66-06 | GGUF | [CH-66](chapters/part-17/66-hybrid-memory-and-local-loading.md#t-66-06) | drafted | [section](chapters/part-17/66-hybrid-memory-and-local-loading.md#t-66-06) |
| T-66-07 | Memory mapping | [CH-66](chapters/part-17/66-hybrid-memory-and-local-loading.md#t-66-07) | drafted | [section](chapters/part-17/66-hybrid-memory-and-local-loading.md#t-66-07) |
| T-66-08 | Startup and model loading | [CH-66](chapters/part-17/66-hybrid-memory-and-local-loading.md#t-66-08) | drafted | [section](chapters/part-17/66-hybrid-memory-and-local-loading.md#t-66-08) |
| T-67-01 | llama.cpp internals | [CH-67](chapters/part-17/67-local-runtimes-and-accelerators.md#t-67-01) | drafted | [section](chapters/part-17/67-local-runtimes-and-accelerators.md#t-67-01) |
| T-67-02 | OpenVINO | [CH-67](chapters/part-17/67-local-runtimes-and-accelerators.md#t-67-02) | drafted | [section](chapters/part-17/67-local-runtimes-and-accelerators.md#t-67-02) |
| T-67-03 | NPUs | [CH-67](chapters/part-17/67-local-runtimes-and-accelerators.md#t-67-03) | drafted | [section](chapters/part-17/67-local-runtimes-and-accelerators.md#t-67-03) |
| T-67-04 | Accelerator backends | [CH-67](chapters/part-17/67-local-runtimes-and-accelerators.md#t-67-04) | drafted | [section](chapters/part-17/67-local-runtimes-and-accelerators.md#t-67-04) |
| T-67-05 | Kernel coverage | [CH-67](chapters/part-17/67-local-runtimes-and-accelerators.md#t-67-05) | drafted | [section](chapters/part-17/67-local-runtimes-and-accelerators.md#t-67-05) |
| T-68-01 | Power limits | [CH-68](chapters/part-17/68-packaging-power-and-thermal-limits.md#t-68-01) | drafted | [section](chapters/part-17/68-packaging-power-and-thermal-limits.md#t-68-01) |
| T-68-02 | Thermal limits | [CH-68](chapters/part-17/68-packaging-power-and-thermal-limits.md#t-68-02) | drafted | [section](chapters/part-17/68-packaging-power-and-thermal-limits.md#t-68-02) |
| T-68-03 | Model packaging | [CH-68](chapters/part-17/68-packaging-power-and-thermal-limits.md#t-68-03) | drafted | [section](chapters/part-17/68-packaging-power-and-thermal-limits.md#t-68-03) |
| T-68-04 | Offline deployment | [CH-68](chapters/part-17/68-packaging-power-and-thermal-limits.md#t-68-04) | drafted | [section](chapters/part-17/68-packaging-power-and-thermal-limits.md#t-68-04) |
| T-68-05 | Edge distillation | [CH-68](chapters/part-17/68-packaging-power-and-thermal-limits.md#t-68-05) | drafted | [section](chapters/part-17/68-packaging-power-and-thermal-limits.md#t-68-05) |
| T-68-06 | Dynamic edge computation | [CH-68](chapters/part-17/68-packaging-power-and-thermal-limits.md#t-68-06) | drafted | [section](chapters/part-17/68-packaging-power-and-thermal-limits.md#t-68-06) |
| T-69-01 | Embeddings revisited | [CH-69](chapters/part-18/69-embeddings-contrastive-learning-and-vector-indexes.md#t-69-01) | drafted | [section](chapters/part-18/69-embeddings-contrastive-learning-and-vector-indexes.md#t-69-01) |
| T-69-02 | Sentence embeddings | [CH-69](chapters/part-18/69-embeddings-contrastive-learning-and-vector-indexes.md#t-69-02) | drafted | [section](chapters/part-18/69-embeddings-contrastive-learning-and-vector-indexes.md#t-69-02) |
| T-69-03 | Document embeddings | [CH-69](chapters/part-18/69-embeddings-contrastive-learning-and-vector-indexes.md#t-69-03) | drafted | [section](chapters/part-18/69-embeddings-contrastive-learning-and-vector-indexes.md#t-69-03) |
| T-69-04 | Contrastive embedding training | [CH-69](chapters/part-18/69-embeddings-contrastive-learning-and-vector-indexes.md#t-69-04) | drafted | [section](chapters/part-18/69-embeddings-contrastive-learning-and-vector-indexes.md#t-69-04) |
| T-69-05 | Vector search | [CH-69](chapters/part-18/69-embeddings-contrastive-learning-and-vector-indexes.md#t-69-05) | drafted | [section](chapters/part-18/69-embeddings-contrastive-learning-and-vector-indexes.md#t-69-05) |
| T-69-06 | Approximate nearest neighbors | [CH-69](chapters/part-18/69-embeddings-contrastive-learning-and-vector-indexes.md#t-69-06) | drafted | [section](chapters/part-18/69-embeddings-contrastive-learning-and-vector-indexes.md#t-69-06) |
| T-69-07 | HNSW | [CH-69](chapters/part-18/69-embeddings-contrastive-learning-and-vector-indexes.md#t-69-07) | drafted | [section](chapters/part-18/69-embeddings-contrastive-learning-and-vector-indexes.md#t-69-07) |
| T-69-08 | IVF | [CH-69](chapters/part-18/69-embeddings-contrastive-learning-and-vector-indexes.md#t-69-08) | drafted | [section](chapters/part-18/69-embeddings-contrastive-learning-and-vector-indexes.md#t-69-08) |
| T-69-09 | Product quantization | [CH-69](chapters/part-18/69-embeddings-contrastive-learning-and-vector-indexes.md#t-69-09) | drafted | [section](chapters/part-18/69-embeddings-contrastive-learning-and-vector-indexes.md#t-69-09) |
| T-69-10 | Vector databases | [CH-69](chapters/part-18/69-embeddings-contrastive-learning-and-vector-indexes.md#t-69-10) | drafted | [section](chapters/part-18/69-embeddings-contrastive-learning-and-vector-indexes.md#t-69-10) |
| T-70-01 | RAG | [CH-70](chapters/part-18/70-rag-and-retrieval-quality.md#t-70-01) | drafted | [section](chapters/part-18/70-rag-and-retrieval-quality.md#t-70-01) |
| T-70-02 | Chunking strategies | [CH-70](chapters/part-18/70-rag-and-retrieval-quality.md#t-70-02) | drafted | [section](chapters/part-18/70-rag-and-retrieval-quality.md#t-70-02) |
| T-70-03 | Retrieval strategies | [CH-70](chapters/part-18/70-rag-and-retrieval-quality.md#t-70-03) | drafted | [section](chapters/part-18/70-rag-and-retrieval-quality.md#t-70-03) |
| T-70-04 | Reranking | [CH-70](chapters/part-18/70-rag-and-retrieval-quality.md#t-70-04) | drafted | [section](chapters/part-18/70-rag-and-retrieval-quality.md#t-70-04) |
| T-70-05 | Retrieval evaluation | [CH-70](chapters/part-18/70-rag-and-retrieval-quality.md#t-70-05) | drafted | [section](chapters/part-18/70-rag-and-retrieval-quality.md#t-70-05) |
| T-70-06 | Grounding | [CH-70](chapters/part-18/70-rag-and-retrieval-quality.md#t-70-06) | drafted | [section](chapters/part-18/70-rag-and-retrieval-quality.md#t-70-06) |
| T-71-01 | Short-term memory | [CH-71](chapters/part-18/71-memory-tools-and-structured-output.md#t-71-01) | drafted | [section](chapters/part-18/71-memory-tools-and-structured-output.md#t-71-01) |
| T-71-02 | Persistent memory | [CH-71](chapters/part-18/71-memory-tools-and-structured-output.md#t-71-02) | drafted | [section](chapters/part-18/71-memory-tools-and-structured-output.md#t-71-02) |
| T-71-03 | Long-term memory | [CH-71](chapters/part-18/71-memory-tools-and-structured-output.md#t-71-03) | drafted | [section](chapters/part-18/71-memory-tools-and-structured-output.md#t-71-03) |
| T-71-04 | Tool calling | [CH-71](chapters/part-18/71-memory-tools-and-structured-output.md#t-71-04) | drafted | [section](chapters/part-18/71-memory-tools-and-structured-output.md#t-71-04) |
| T-71-05 | Structured outputs | [CH-71](chapters/part-18/71-memory-tools-and-structured-output.md#t-71-05) | drafted | [section](chapters/part-18/71-memory-tools-and-structured-output.md#t-71-05) |
| T-71-06 | Constrained decoding | [CH-71](chapters/part-18/71-memory-tools-and-structured-output.md#t-71-06) | drafted | [section](chapters/part-18/71-memory-tools-and-structured-output.md#t-71-06) |
| T-71-07 | Memory invalidation | [CH-71](chapters/part-18/71-memory-tools-and-structured-output.md#t-71-07) | drafted | [section](chapters/part-18/71-memory-tools-and-structured-output.md#t-71-07) |
| T-72-01 | Agents | [CH-72](chapters/part-18/72-agents-and-multi-model-economics.md#t-72-01) | drafted | [section](chapters/part-18/72-agents-and-multi-model-economics.md#t-72-01) |
| T-72-02 | Planning | [CH-72](chapters/part-18/72-agents-and-multi-model-economics.md#t-72-02) | drafted | [section](chapters/part-18/72-agents-and-multi-model-economics.md#t-72-02) |
| T-72-03 | Multi-agent systems | [CH-72](chapters/part-18/72-agents-and-multi-model-economics.md#t-72-03) | drafted | [section](chapters/part-18/72-agents-and-multi-model-economics.md#t-72-03) |
| T-72-04 | Multi-LLM systems | [CH-72](chapters/part-18/72-agents-and-multi-model-economics.md#t-72-04) | drafted | [section](chapters/part-18/72-agents-and-multi-model-economics.md#t-72-04) |
| T-72-05 | Agent compute economics | [CH-72](chapters/part-18/72-agents-and-multi-model-economics.md#t-72-05) | drafted | [section](chapters/part-18/72-agents-and-multi-model-economics.md#t-72-05) |
| T-72-06 | Routing and fallback | [CH-72](chapters/part-18/72-agents-and-multi-model-economics.md#t-72-06) | drafted | [section](chapters/part-18/72-agents-and-multi-model-economics.md#t-72-06) |
| T-73-01 | Hidden states | [CH-73](chapters/part-19/73-hidden-states-layers-and-attention-heads.md#t-73-01) | drafted | [section](chapters/part-19/73-hidden-states-layers-and-attention-heads.md#t-73-01) |
| T-73-02 | Residual stream analysis | [CH-73](chapters/part-19/73-hidden-states-layers-and-attention-heads.md#t-73-02) | drafted | [section](chapters/part-19/73-hidden-states-layers-and-attention-heads.md#t-73-02) |
| T-73-03 | Representation geometry analysis | [CH-73](chapters/part-19/73-hidden-states-layers-and-attention-heads.md#t-73-03) | drafted | [section](chapters/part-19/73-hidden-states-layers-and-attention-heads.md#t-73-03) |
| T-73-04 | What individual layers learn | [CH-73](chapters/part-19/73-hidden-states-layers-and-attention-heads.md#t-73-04) | drafted | [section](chapters/part-19/73-hidden-states-layers-and-attention-heads.md#t-73-04) |
| T-73-05 | Layer specialization | [CH-73](chapters/part-19/73-hidden-states-layers-and-attention-heads.md#t-73-05) | drafted | [section](chapters/part-19/73-hidden-states-layers-and-attention-heads.md#t-73-05) |
| T-73-06 | Attention-head analysis | [CH-73](chapters/part-19/73-hidden-states-layers-and-attention-heads.md#t-73-06) | drafted | [section](chapters/part-19/73-hidden-states-layers-and-attention-heads.md#t-73-06) |
| T-74-01 | Neurons | [CH-74](chapters/part-19/74-features-probes-and-mechanisms.md#t-74-01) | drafted | [section](chapters/part-19/74-features-probes-and-mechanisms.md#t-74-01) |
| T-74-02 | Features | [CH-74](chapters/part-19/74-features-probes-and-mechanisms.md#t-74-02) | drafted | [section](chapters/part-19/74-features-probes-and-mechanisms.md#t-74-02) |
| T-74-03 | Probing | [CH-74](chapters/part-19/74-features-probes-and-mechanisms.md#t-74-03) | drafted | [section](chapters/part-19/74-features-probes-and-mechanisms.md#t-74-03) |
| T-74-04 | Sparse autoencoders | [CH-74](chapters/part-19/74-features-probes-and-mechanisms.md#t-74-04) | drafted | [section](chapters/part-19/74-features-probes-and-mechanisms.md#t-74-04) |
| T-74-05 | Mechanistic interpretability | [CH-74](chapters/part-19/74-features-probes-and-mechanisms.md#t-74-05) | drafted | [section](chapters/part-19/74-features-probes-and-mechanisms.md#t-74-05) |
| T-74-06 | Causal interventions | [CH-74](chapters/part-19/74-features-probes-and-mechanisms.md#t-74-06) | drafted | [section](chapters/part-19/74-features-probes-and-mechanisms.md#t-74-06) |
| T-75-01 | Activation steering | [CH-75](chapters/part-19/75-steering-editing-and-representation-engineering.md#t-75-01) | drafted | [section](chapters/part-19/75-steering-editing-and-representation-engineering.md#t-75-01) |
| T-75-02 | Representation engineering | [CH-75](chapters/part-19/75-steering-editing-and-representation-engineering.md#t-75-02) | drafted | [section](chapters/part-19/75-steering-editing-and-representation-engineering.md#t-75-02) |
| T-75-03 | Model editing | [CH-75](chapters/part-19/75-steering-editing-and-representation-engineering.md#t-75-03) | drafted | [section](chapters/part-19/75-steering-editing-and-representation-engineering.md#t-75-03) |
| T-75-04 | Intervention side effects | [CH-75](chapters/part-19/75-steering-editing-and-representation-engineering.md#t-75-04) | drafted | [section](chapters/part-19/75-steering-editing-and-representation-engineering.md#t-75-04) |
| T-76-01 | Model merging | [CH-76](chapters/part-19/76-merging-stitching-and-representation-compatibility.md#t-76-01) | drafted | [section](chapters/part-19/76-merging-stitching-and-representation-compatibility.md#t-76-01) |
| T-76-02 | Layer stitching | [CH-76](chapters/part-19/76-merging-stitching-and-representation-compatibility.md#t-76-02) | drafted | [section](chapters/part-19/76-merging-stitching-and-representation-compatibility.md#t-76-02) |
| T-76-03 | Cross-model alignment | [CH-76](chapters/part-19/76-merging-stitching-and-representation-compatibility.md#t-76-03) | drafted | [section](chapters/part-19/76-merging-stitching-and-representation-compatibility.md#t-76-03) |
| T-76-04 | Normalization mismatch | [CH-76](chapters/part-19/76-merging-stitching-and-representation-compatibility.md#t-76-04) | drafted | [section](chapters/part-19/76-merging-stitching-and-representation-compatibility.md#t-76-04) |
| T-76-05 | Latent bridge cost | [CH-76](chapters/part-19/76-merging-stitching-and-representation-compatibility.md#t-76-05) | drafted | [section](chapters/part-19/76-merging-stitching-and-representation-compatibility.md#t-76-05) |
| T-77-01 | Efficient KV memory | [CH-77](chapters/part-20/77-efficient-memory-and-adaptive-computation.md#t-77-01) | drafted | [section](chapters/part-20/77-efficient-memory-and-adaptive-computation.md#t-77-01) |
| T-77-02 | KV-cache compression | [CH-77](chapters/part-20/77-efficient-memory-and-adaptive-computation.md#t-77-02) | drafted | [section](chapters/part-20/77-efficient-memory-and-adaptive-computation.md#t-77-02) |
| T-77-03 | KV-cache eviction | [CH-77](chapters/part-20/77-efficient-memory-and-adaptive-computation.md#t-77-03) | drafted | [section](chapters/part-20/77-efficient-memory-and-adaptive-computation.md#t-77-03) |
| T-77-04 | Activation compression | [CH-77](chapters/part-20/77-efficient-memory-and-adaptive-computation.md#t-77-04) | drafted | [section](chapters/part-20/77-efficient-memory-and-adaptive-computation.md#t-77-04) |
| T-77-05 | Dynamic computation | [CH-77](chapters/part-20/77-efficient-memory-and-adaptive-computation.md#t-77-05) | drafted | [section](chapters/part-20/77-efficient-memory-and-adaptive-computation.md#t-77-05) |
| T-77-06 | Conditional layer execution | [CH-77](chapters/part-20/77-efficient-memory-and-adaptive-computation.md#t-77-06) | drafted | [section](chapters/part-20/77-efficient-memory-and-adaptive-computation.md#t-77-06) |
| T-77-07 | Adaptive computation | [CH-77](chapters/part-20/77-efficient-memory-and-adaptive-computation.md#t-77-07) | drafted | [section](chapters/part-20/77-efficient-memory-and-adaptive-computation.md#t-77-07) |
| T-78-01 | Neural routing | [CH-78](chapters/part-20/78-routable-intelligence-and-neural-handoffs.md#t-78-01) | drafted | [section](chapters/part-20/78-routable-intelligence-and-neural-handoffs.md#t-78-01) |
| T-78-02 | Model cascades | [CH-78](chapters/part-20/78-routable-intelligence-and-neural-handoffs.md#t-78-02) | drafted | [section](chapters/part-20/78-routable-intelligence-and-neural-handoffs.md#t-78-02) |
| T-78-03 | Latent communication | [CH-78](chapters/part-20/78-routable-intelligence-and-neural-handoffs.md#t-78-03) | drafted | [section](chapters/part-20/78-routable-intelligence-and-neural-handoffs.md#t-78-03) |
| T-78-04 | Cross-model representations | [CH-78](chapters/part-20/78-routable-intelligence-and-neural-handoffs.md#t-78-04) | drafted | [section](chapters/part-20/78-routable-intelligence-and-neural-handoffs.md#t-78-04) |
| T-78-05 | Neural handoffs | [CH-78](chapters/part-20/78-routable-intelligence-and-neural-handoffs.md#t-78-05) | drafted | [section](chapters/part-20/78-routable-intelligence-and-neural-handoffs.md#t-78-05) |
| T-78-06 | Sparse expert intervention | [CH-78](chapters/part-20/78-routable-intelligence-and-neural-handoffs.md#t-78-06) | drafted | [section](chapters/part-20/78-routable-intelligence-and-neural-handoffs.md#t-78-06) |
| T-78-07 | Silent expert intervention | [CH-78](chapters/part-20/78-routable-intelligence-and-neural-handoffs.md#t-78-07) | drafted | [section](chapters/part-20/78-routable-intelligence-and-neural-handoffs.md#t-78-07) |
| T-78-08 | LLM dead-call elimination | [CH-78](chapters/part-20/78-routable-intelligence-and-neural-handoffs.md#t-78-08) | drafted | [section](chapters/part-20/78-routable-intelligence-and-neural-handoffs.md#t-78-08) |
| T-78-09 | Computation as a routable resource | [CH-78](chapters/part-20/78-routable-intelligence-and-neural-handoffs.md#t-78-09) | drafted | [section](chapters/part-20/78-routable-intelligence-and-neural-handoffs.md#t-78-09) |
| T-79-01 | Forming research questions | [CH-79](chapters/part-20/79-research-design-and-reproduction.md#t-79-01) | drafted | [section](chapters/part-20/79-research-design-and-reproduction.md#t-79-01) |
| T-79-02 | Literature search | [CH-79](chapters/part-20/79-research-design-and-reproduction.md#t-79-02) | drafted | [section](chapters/part-20/79-research-design-and-reproduction.md#t-79-02) |
| T-79-03 | Prior-art search | [CH-79](chapters/part-20/79-research-design-and-reproduction.md#t-79-03) | drafted | [section](chapters/part-20/79-research-design-and-reproduction.md#t-79-03) |
| T-79-04 | Reading papers critically | [CH-79](chapters/part-20/79-research-design-and-reproduction.md#t-79-04) | drafted | [section](chapters/part-20/79-research-design-and-reproduction.md#t-79-04) |
| T-79-05 | Designing a research experiment | [CH-79](chapters/part-20/79-research-design-and-reproduction.md#t-79-05) | drafted | [section](chapters/part-20/79-research-design-and-reproduction.md#t-79-05) |
| T-79-06 | Choosing baselines | [CH-79](chapters/part-20/79-research-design-and-reproduction.md#t-79-06) | drafted | [section](chapters/part-20/79-research-design-and-reproduction.md#t-79-06) |
| T-79-07 | Benchmark selection | [CH-79](chapters/part-20/79-research-design-and-reproduction.md#t-79-07) | drafted | [section](chapters/part-20/79-research-design-and-reproduction.md#t-79-07) |
| T-79-08 | Reproducing papers | [CH-79](chapters/part-20/79-research-design-and-reproduction.md#t-79-08) | drafted | [section](chapters/part-20/79-research-design-and-reproduction.md#t-79-08) |
| T-79-09 | Reproducibility | [CH-79](chapters/part-20/79-research-design-and-reproduction.md#t-79-09) | drafted | [section](chapters/part-20/79-research-design-and-reproduction.md#t-79-09) |
| T-79-10 | Scientific vs engineering claims | [CH-79](chapters/part-20/79-research-design-and-reproduction.md#t-79-10) | drafted | [section](chapters/part-20/79-research-design-and-reproduction.md#t-79-10) |
| T-80-01 | Ablations | [CH-80](chapters/part-20/80-evidence-ablations-and-publication.md#t-80-01) | drafted | [section](chapters/part-20/80-evidence-ablations-and-publication.md#t-80-01) |
| T-80-02 | Statistical significance | [CH-80](chapters/part-20/80-evidence-ablations-and-publication.md#t-80-02) | drafted | [section](chapters/part-20/80-evidence-ablations-and-publication.md#t-80-02) |
| T-80-03 | Confidence intervals | [CH-80](chapters/part-20/80-evidence-ablations-and-publication.md#t-80-03) | drafted | [section](chapters/part-20/80-evidence-ablations-and-publication.md#t-80-03) |
| T-80-04 | Uncertainty | [CH-80](chapters/part-20/80-evidence-ablations-and-publication.md#t-80-04) | drafted | [section](chapters/part-20/80-evidence-ablations-and-publication.md#t-80-04) |
| T-80-05 | Profiling research claims | [CH-80](chapters/part-20/80-evidence-ablations-and-publication.md#t-80-05) | drafted | [section](chapters/part-20/80-evidence-ablations-and-publication.md#t-80-05) |
| T-80-06 | FLOPs-memory-latency measurement | [CH-80](chapters/part-20/80-evidence-ablations-and-publication.md#t-80-06) | drafted | [section](chapters/part-20/80-evidence-ablations-and-publication.md#t-80-06) |
| T-80-07 | Writing papers | [CH-80](chapters/part-20/80-evidence-ablations-and-publication.md#t-80-07) | drafted | [section](chapters/part-20/80-evidence-ablations-and-publication.md#t-80-07) |
| T-80-08 | arXiv | [CH-80](chapters/part-20/80-evidence-ablations-and-publication.md#t-80-08) | drafted | [section](chapters/part-20/80-evidence-ablations-and-publication.md#t-80-08) |
| T-80-09 | Workshops | [CH-80](chapters/part-20/80-evidence-ablations-and-publication.md#t-80-09) | drafted | [section](chapters/part-20/80-evidence-ablations-and-publication.md#t-80-09) |
| T-80-10 | Conferences | [CH-80](chapters/part-20/80-evidence-ablations-and-publication.md#t-80-10) | drafted | [section](chapters/part-20/80-evidence-ablations-and-publication.md#t-80-10) |
| T-80-11 | Peer review | [CH-80](chapters/part-20/80-evidence-ablations-and-publication.md#t-80-11) | drafted | [section](chapters/part-20/80-evidence-ablations-and-publication.md#t-80-11) |
| T-80-12 | Finding unanswered questions | [CH-80](chapters/part-20/80-evidence-ablations-and-publication.md#t-80-12) | drafted | [section](chapters/part-20/80-evidence-ablations-and-publication.md#t-80-12) |
