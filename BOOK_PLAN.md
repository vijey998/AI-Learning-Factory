# Book plan

Working title: **Inside the LLM: From Tokens to Systems to Research**.

Twenty parts, 80 substantial chapters. Each chapter below has a concrete exit artifact. The 206 V2 headings are subsections, not 206 chapters. The consolidated inventory also retains the explicit V1 audit corrections.

## Ordering rationale

Start with an end-to-end mental model, then introduce shapes and resource accounting before neural networks. Build gradients, tokenization, attention and a tiny GPT before large-model architectures. Basic held-out evaluation and sampling are introduced when needed for training; their rigorous treatments follow. Hardware, kernels and compilers precede advanced inference optimization. Distributed systems precede production serving. Interpretability and frontier experiments come after the reader can account for both tensors and execution costs.

The four perspectives recur throughout: information (token), learning (gradient), hardware (byte), and service execution (request). A chapter may explain that a perspective is inapplicable rather than invent a gradient or hardware claim.

## Intended depth

Main chapters explain mechanisms, equations and representative code. Companion labs hold full implementations and measurements. Total word count is an editorial planning variable, not a completion criterion. Topic evidence and learner outcomes determine completeness.

## Part 01 — What Is This Machine?

### 01. [The LLM in One Picture](chapters/part-01/01-the-llm-in-one-picture.md)

**Exit artifact:** Trace a short prompt through IDs, hidden states, logits and one generated token.

**Required scope:** Prompt; Tokenizer; Embeddings; Transformer; Logits; Sampling; Output tokens; Next-token conditional distribution.

### 02. [Training vs Inference](chapters/part-01/02-training-vs-inference.md)

**Exit artifact:** Annotate exactly which tensors persist and which change in each mode.

**Required scope:** Training vs inference; Parameters vs activations; Loss vs generated text; Learning vs execution.

### 03. [Anatomy of the Modern LLM Stack](chapters/part-01/03-anatomy-of-the-modern-llm-stack.md)

**Exit artifact:** Classify a slow request by the layer that could cause its delay.

**Required scope:** Applications; Agents and RAG in the stack; Inference server; Model runtime; PyTorch and compiler; Tensor operations; GPU kernels; GPU hardware; Memory; Silicon.

### 04. [Building Our Tiny Laboratory](chapters/part-01/04-building-our-tiny-laboratory.md)

**Exit artifact:** Run a CPU experiment and save a reproducible environment record.

**Required scope:** Python; NumPy; PyTorch; Notebooks; Profiling tools; CPU baseline; Seeds and environment records.

## Part 02 — Tensors, Math and Computation

### 05. [Tensors and Resource Accounting](chapters/part-02/05-tensors-and-resource-accounting.md)

**Exit artifact:** Calculate the shape, storage and FLOPs of batched linear projections.

**Required scope:** Scalars; Vectors; Matrices; Tensors; Shapes; Dimensions; Indexing; Transpose; Batch dimensions; Broadcasting; Dtypes; Element counts; Bytes; FLOPs; Matrix multiplication.

### 06. [Geometry and Number Formats](chapters/part-02/06-geometry-and-number-formats.md)

**Exit artifact:** Compare cosine and dot-product rankings and explain a low-precision failure.

**Required scope:** Dot products; Cosine similarity; Magnitude; Basis; Subspaces; Orthogonality; Projections; Linear transformations; FP32; FP16; BF16; FP8; INT8; INT4; Overflow; Underflow; Numerical stability.

### 07. [Probability, Logits and Loss](chapters/part-02/07-probability-logits-and-loss.md)

**Exit artifact:** Derive stable cross-entropy and distinguish likelihood from sampled accuracy.

**Required scope:** Conditional probability; Likelihood; Log-probability; Entropy; KL divergence; Softmax; Logits; Cross-entropy; Log-sum-exp.

### 08. [Gradients, Graphs and Autodiff](chapters/part-02/08-gradients-graphs-and-autodiff.md)

**Exit artifact:** Implement a micro autograd engine and compare its derivatives numerically.

**Required scope:** Derivatives; Gradients; Chain rule; Computational graphs; Automatic differentiation; Reverse-mode autodiff; Finite-difference checks.

## Part 03 — Neural Networks Before Transformers

### 09. [Linear Layers and Nonlinearities](chapters/part-03/09-linear-layers-and-nonlinearities.md)

**Exit artifact:** Fit a nonlinear dataset and show why stacked linear maps alone cannot do it.

**Required scope:** Linear layers; Biases; Nonlinearities; ReLU; GELU; Parameter shapes.

### 10. [A Tiny Network, Forward and Backward](chapters/part-03/10-a-tiny-network-forward-and-backward.md)

**Exit artifact:** Compute a two-layer network update on paper and reproduce it in code.

**Required scope:** Building a tiny neural network; Forward propagation; Backpropagation by hand; Gradient shapes.

### 11. [Optimization and State](chapters/part-03/11-optimization-and-state.md)

**Exit artifact:** Account for parameters, gradients and optimizer tensors before and after a step.

**Required scope:** SGD; Momentum; AdamW; Optimizer states; Learning-rate schedules; Weight decay.

### 12. [Initialization and Training Stability](chapters/part-03/12-initialization-and-training-stability.md)

**Exit artifact:** Diagnose an unstable training run using loss and gradient traces.

**Required scope:** Initialization; Gradient norms; Clipping; Warmup; Vanishing gradients; Exploding gradients; Stability diagnostics.

## Part 04 — Turning Language Into Numbers

### 13. [Tokenization Algorithms](chapters/part-04/13-tokenization-algorithms.md)

**Exit artifact:** Train a BPE tokenizer and verify encode/decode round trips.

**Required scope:** Why machines need tokens; Characters; Words; Subwords; BPE from scratch; WordPiece; SentencePiece; Byte-level tokenization.

### 14. [Vocabulary and Token IDs](chapters/part-04/14-vocabulary-and-token-ids.md)

**Exit artifact:** Show how changing a vocabulary changes embedding lookup and model compatibility.

**Required scope:** Vocabulary; Token IDs; Special tokens; Unknown tokens; Tokenizer-model compatibility.

### 15. [Embedding Matrices and Geometry](chapters/part-04/15-embedding-matrices-and-geometry.md)

**Exit artifact:** Trace lookup gradients and separate token-table vectors from contextual states.

**Required scope:** Embedding matrices; Static embeddings; Contextual embeddings; Representation geometry; Embedding lookup.

### 16. [Position and Sequence Order](chapters/part-04/16-position-and-sequence-order.md)

**Exit artifact:** Demonstrate why permutation-insensitive attention needs order information.

**Required scope:** Position and sequence order; Sinusoidal positions; Learned positions; Relative-position methods; RoPE introduction.

## Part 05 — Attention From First Principles

### 17. [Sequence Modeling and the Attention Idea](chapters/part-05/17-sequence-modeling-and-the-attention-idea.md)

**Exit artifact:** Compare recurrent state compression with context-dependent weighted retrieval.

**Required scope:** Sequence modeling bottlenecks; RNNs; LSTMs; The attention idea; Content-based retrieval.

### 18. [Queries, Keys, Values and Scaling](chapters/part-05/18-queries-keys-values-and-scaling.md)

**Exit artifact:** Calculate one attention output by hand from small Q, K and V matrices.

**Required scope:** Query; Key; Value; QKV projections; Scaled dot-product attention; Square-root scaling; Attention weights.

### 19. [Causal and Multi-Head Attention](chapters/part-05/19-causal-and-multi-head-attention.md)

**Exit artifact:** Implement multi-head causal attention and check future-token isolation.

**Required scope:** Causal attention; Causal masks; Multi-head attention; Head concatenation; Output projection.

### 20. [Attention Shapes and Compute Cost](chapters/part-05/20-attention-shapes-and-compute-cost.md)

**Exit artifact:** Derive score tensor bytes and attention FLOPs for a chosen batch and context.

**Required scope:** Attention tensor shapes; Attention compute cost; Quadratic sequence cost; Attention memory accounting.

## Part 06 — Build a Transformer

### 21. [Residual Streams and Normalization](chapters/part-06/21-residual-streams-and-normalization.md)

**Exit artifact:** Implement both normalization placements and inspect residual scales.

**Required scope:** Residual connections; Residual streams; LayerNorm; RMSNorm; Pre-norm; Post-norm.

### 22. [Feed-Forward Networks and Complete Blocks](chapters/part-06/22-feed-forward-networks-and-complete-blocks.md)

**Exit artifact:** Build a block with explicit shapes and a parameter-count breakdown.

**Required scope:** Feed-forward networks; GELU vs SwiGLU; MLP expansion; Complete Transformer block.

### 23. [Stacking, Vocabulary Projection and Tying](chapters/part-06/23-stacking-vocabulary-projection-and-tying.md)

**Exit artifact:** Trace hidden states to vocabulary logits and verify shared-weight gradients.

**Required scope:** Stack the blocks; Vocabulary projection; LM head; Weight tying.

### 24. [Build Our GPT From Scratch](chapters/part-06/24-build-our-gpt-from-scratch.md)

**Exit artifact:** Assemble a runnable tiny GPT with no pretrained-model wrapper.

**Required scope:** GPT implementation; Decoder-only model assembly; Model configuration; Forward-pass invariants.

## Part 07 — Train the Thing

### 25. [Sequences, Batches and Pretraining](chapters/part-07/25-sequences-batches-and-pretraining.md)

**Exit artifact:** Construct shifted labels and packed sequences without unintended cross-example attention.

**Required scope:** Preparing training sequences; Sequence packing; Batches; Mini-batches; Next-token prediction; Full pretraining; Batch size and sequence length dynamics.

### 26. [The Training Step and Schedule](chapters/part-07/26-the-training-step-and-schedule.md)

**Exit artifact:** Show equivalence of accumulated and full-batch gradients under matched conditions.

**Required scope:** Training forward pass; Training loss; Training backward pass; Optimizer state updates in memory; Learning rates; Warmup; Gradient accumulation; Gradient clipping.

### 27. [Mixed Precision and Checkpoint Anatomy](chapters/part-07/27-mixed-precision-and-checkpoint-anatomy.md)

**Exit artifact:** Resume a run with matching next-step behavior and explain memory tradeoffs.

**Required scope:** Mixed-precision training; Loss scaling; Activation checkpointing; Checkpoints; Weights; Config; Tokenizer state; Optimizer state; Scheduler state; RNG state.

### 28. [Debugging and Training Our Tiny Model](chapters/part-07/28-debugging-and-training-our-tiny-model.md)

**Exit artifact:** Overfit a tiny batch, then train with a held-out split and document failures.

**Required scope:** Debugging training; NaNs; Exploding gradients; Bad initialization; Overfitting; Train a tiny language model.

## Part 08 — Modern LLM Architecture

### 29. [Transformer Families](chapters/part-08/29-transformer-families.md)

**Exit artifact:** Compare masks and objectives across three Transformer families.

**Required scope:** GPT to Llama-type architectures; Decoder-only Transformers; Encoder-only Transformers; BERT; Encoder-decoder Transformers; T5; Cross-attention.

### 30. [Modern Positions, Heads and MLPs](chapters/part-08/30-modern-positions-heads-and-mlps.md)

**Exit artifact:** Derive KV dimensions and parameter counts for three head-sharing configurations.

**Required scope:** RoPE deep dive; MHA; MQA; GQA; Modern MLPs; SwiGLU parameter accounting.

### 31. [Mixture of Experts](chapters/part-08/31-mixture-of-experts.md)

**Exit artifact:** Simulate top-k routing and measure imbalance and token overflow.

**Required scope:** MoE; Sparse activation; Expert routing; Capacity; Load balancing; Router losses; Expert parallelism introduction.

### 32. [Alternative Architectures and Real Configs](chapters/part-08/32-alternative-architectures-and-real-configs.md)

**Exit artifact:** Read a pinned model config and independently estimate its cost.

**Required scope:** Sparse attention; Sliding-window attention; Local attention; Global attention; State-space models; Recurrent hybrids; Hybrid models; Reading a real model config; Parameters; Attention dimensions; KV heads; MLP size; Memory footprint; FLOPs per token.

## Part 09 — Data, Scaling and Evaluation

### 33. [Data Sources and Cleaning](chapters/part-09/33-data-sources-and-cleaning.md)

**Exit artifact:** Create a small corpus with reproducible filtering and exact/near duplicate checks.

**Required scope:** Training data sources; Cleaning; Filtering; Deduplication; Dataset provenance.

### 34. [Mixtures, Tokens and Synthetic Data](chapters/part-09/34-mixtures-tokens-and-synthetic-data.md)

**Exit artifact:** Design a token allocation and detect evaluation leakage.

**Required scope:** Dataset mixtures; Token budgets; Synthetic data; Data quality; Contamination; Split design.

### 35. [Evaluation and Meaningful Experiments](chapters/part-09/35-evaluation-and-meaningful-experiments.md)

**Exit artifact:** Report a baseline comparison with paired examples and uncertainty.

**Required scope:** Evaluation; Perplexity; Downstream tasks; Reasoning benchmarks; Human evaluation; Experimental design; Uncertainty introduction.

### 36. [Scaling Laws](chapters/part-09/36-scaling-laws.md)

**Exit artifact:** Fit a small scaling experiment and disclose its extrapolation uncertainty.

**Required scope:** Scaling laws; Parameters vs data vs compute; Compute budgets; Scaling fits; Extrapolation limits.

## Part 10 — Post-Training and Reasoning

### 37. [Pretraining, Continued Pretraining and SFT](chapters/part-10/37-pretraining-continued-pretraining-and-sft.md)

**Exit artifact:** Specify a continued-pretraining and SFT pipeline with correct loss masks.

**Required scope:** Pretraining vs post-training; Continued pretraining; Supervised fine-tuning; Chat templates; Loss masking.

### 38. [Parameter-Efficient Adaptation](chapters/part-10/38-parameter-efficient-adaptation.md)

**Exit artifact:** Train a small adapter and count trainable parameters and optimizer memory.

**Required scope:** PEFT; Adapters; Prompt tuning; Prefix tuning; LoRA; QLoRA.

### 39. [Preferences and Reinforcement Learning](chapters/part-10/39-preferences-and-reinforcement-learning.md)

**Exit artifact:** Compare the data, objective and update path for PPO-style RLHF and DPO.

**Required scope:** Preference data; Reward models; RLHF; PPO; DPO-type objectives; Policy KL control.

### 40. [Reasoning, Test-Time Compute and Distillation](chapters/part-10/40-reasoning-test-time-compute-and-distillation.md)

**Exit artifact:** Compare sampling/search budgets at fixed cost and assess a distilled student.

**Required scope:** RL with verifiable rewards; Reasoning models; Why generation can produce reasoning-like behavior; Test-time compute; Distillation; Verifier limits.

## Part 11 — GPU Fundamentals

### 41. [Why GPUs and How They Execute](chapters/part-11/41-why-gpus-and-how-they-execute.md)

**Exit artifact:** Map a tensor operation to threads, blocks and compute units.

**Required scope:** CPU vs GPU; Why GPUs; GPU anatomy; SMs; Threads; Warps; Blocks; CUDA cores; Tensor Cores; Registers.

### 42. [Memory Hierarchy and Movement](chapters/part-11/42-memory-hierarchy-and-movement.md)

**Exit artifact:** Draw a tensor's memory route and estimate transfer lower bounds.

**Required scope:** Memory hierarchy; Shared memory and SRAM; Caches; HBM; RAM; SSD; HBM bandwidth; Coalescing.

### 43. [Throughput, Intensity and Rooflines](chapters/part-11/43-throughput-intensity-and-rooflines.md)

**Exit artifact:** Place prefill and decode examples on a roofline using stated assumptions.

**Required scope:** Compute throughput; Arithmetic intensity; Compute-bound vs memory-bound; Roofline model.

### 44. [Profiling Transformer Bottlenecks](chapters/part-11/44-profiling-transformer-bottlenecks.md)

**Exit artifact:** Measure a CPU baseline and define an honest GPU profiling protocol.

**Required scope:** Decode memory bottlenecks; FLOPs and memory profiling; Bandwidth utilization; Latency measurement; Synchronization.

## Part 12 — Kernels and the Software Stack

### 45. [Kernels, GEMM and Tiling](chapters/part-12/45-kernels-gemm-and-tiling.md)

**Exit artifact:** Explain a tiled GEMM and identify which bytes fusion can avoid.

**Required scope:** GPU kernels; GEMM; Tiling; Tensor Core MMA; Kernel launch overhead; Kernel fusion.

### 46. [CUDA, Triton and CUTLASS](chapters/part-12/46-cuda-triton-and-cutlass.md)

**Exit artifact:** Implement and validate a fused elementwise kernel before benchmarking.

**Required scope:** CUDA; Triton; CUTLASS-level concepts; Simple Triton kernel; GPU profiling.

### 47. [Graphs, Compilers and Runtimes](chapters/part-12/47-graphs-compilers-and-runtimes.md)

**Exit artifact:** Trace eager operators through capture, IR and generated code on a pinned stack.

**Required scope:** PyTorch eager execution; Computational graph capture; TorchDynamo; Intermediate representation; torch.compile; Inductor; Generated kernels; Compiler graph breaks.

### 48. [CUDA Graphs and Execution Overhead](chapters/part-12/48-cuda-graphs-and-execution-overhead.md)

**Exit artifact:** Compare warmed eager, compiled and graph-replayed execution with setup costs separated.

**Required scope:** CUDA Graphs; Dispatch overhead; Graph replay; Shape specialization; Compilation amortization.

## Part 13 — LLM Inference From First Principles

### 49. [Load Weights and Trace a Forward Pass](chapters/part-13/49-load-weights-and-trace-a-forward-pass.md)

**Exit artifact:** Record tensor shapes from token IDs through all layers to vocabulary logits.

**Required scope:** Loading model weights; Prompt processing; GPU inference; End-to-end real-model forward-pass tracing.

### 50. [Prefill, Decode and KV Cache](chapters/part-13/50-prefill-decode-and-kv-cache.md)

**Exit artifact:** Implement KV-cached inference and check logits against uncached execution.

**Required scope:** Prefill; Autoregressive decode; KV cache; Why cache K and V but not historical Q; Context length.

### 51. [Sampling and Decoding Policies](chapters/part-13/51-sampling-and-decoding-policies.md)

**Exit artifact:** Compare policies on fixed logits and distinguish distribution changes from search.

**Required scope:** Sampling; Greedy decoding; Temperature; Top-k; Top-p; Beam search; Stopping conditions.

### 52. [Inference Memory and Latency Accounting](chapters/part-13/52-inference-memory-and-latency-accounting.md)

**Exit artifact:** Calculate and measure a request budget, including allocator and workspace overhead.

**Required scope:** Inference memory accounting; Weights plus KV plus activations plus overhead; TTFT; Inter-token latency; TPOT; Throughput; Memory per token; FLOPs per token.

## Part 14 — Making Inference Fast

### 53. [FlashAttention and Paged KV Memory](chapters/part-14/53-flashattention-and-paged-kv-memory.md)

**Exit artifact:** Explain online softmax and compare contiguous vs paged KV allocation.

**Required scope:** Why naive inference is slow; FlashAttention; Attention IO scheduling; KV cache layout; Paged KV memory; PagedAttention.

### 54. [Caching, Batching and Prefill Scheduling](chapters/part-14/54-caching-batching-and-prefill-scheduling.md)

**Exit artifact:** Simulate arriving requests and compare completion latency and memory usage.

**Required scope:** Prefix caching; Prefix reuse; Continuous batching; Chunked prefill; Cache correctness.

### 55. [Speculative Decoding and Dynamic Execution](chapters/part-14/55-speculative-decoding-and-dynamic-execution.md)

**Exit artifact:** Measure accepted tokens per verification pass and separate exact from approximate methods.

**Required scope:** Speculative decoding; Draft-verifier design; Speculative-model architectures; Sparsity; Pruning; Early exit; Layer skipping; CUDA Graph optimization.

### 56. [Quantization Across the Inference Path](chapters/part-14/56-quantization-across-the-inference-path.md)

**Exit artifact:** Quantize a tiny matrix and report reconstruction error, bytes and downstream impact.

**Required scope:** Quantization; PTQ; QAT; GPTQ; AWQ; Weight quantization; Activation quantization; KV quantization; FP8 inference; INT8 inference; INT4 inference; GGUF formats.

## Part 15 — Distributed LLMs

### 57. [Parallel Training Strategies](chapters/part-15/57-parallel-training-strategies.md)

**Exit artifact:** Account for parameter, gradient and optimizer storage under replication and sharding.

**Required scope:** Why one accelerator stops being enough; Data parallelism; DDP; ZeRO; FSDP; Sharded optimizer state.

### 58. [Partitioning Model Computation](chapters/part-15/58-partitioning-model-computation.md)

**Exit artifact:** Place a model across devices and derive communication on its critical path.

**Required scope:** Tensor parallelism; Pipeline parallelism; Sequence parallelism; Context parallelism; Expert parallelism.

### 59. [Collectives and Interconnects](chapters/part-15/59-collectives-and-interconnects.md)

**Exit artifact:** Match each parallel strategy to collectives and estimate transfer time.

**Required scope:** Broadcast; All-reduce; All-gather; Reduce-scatter; All-to-all; NCCL; PCIe; NVLink; NVSwitch; InfiniBand.

### 60. [Distributed Execution and Failure Recovery](chapters/part-15/60-distributed-execution-and-failure-recovery.md)

**Exit artifact:** Run a two-process CPU simulation and specify the real multi-GPU validation gate.

**Required scope:** Distributed training failures; Distributed inference; Stragglers; Multi-GPU execution; Checkpoint recovery.

## Part 16 — Serving LLMs as a System

### 61. [Anatomy of an Inference Server](chapters/part-16/61-anatomy-of-an-inference-server.md)

**Exit artifact:** Build a tiny continuous-batching server with cancellation and cleanup.

**Required scope:** Inference server architecture; HTTP requests; Request queues; Scheduling; Dynamic batching; KV allocation; Streaming.

### 62. [Tenants, Models and Residency](chapters/part-16/62-tenants-models-and-residency.md)

**Exit artifact:** Design admission and eviction policies for concurrent models within a memory budget.

**Required scope:** Multi-tenant serving; Multi-model serving; Memory residency; Model loading; Model offloading; GPU-RAM-SSD hierarchy.

### 63. [Disaggregation and Runtime Comparisons](chapters/part-16/63-disaggregation-and-runtime-comparisons.md)

**Exit artifact:** Compare pinned runtime architectures and calculate when KV transfer negates disaggregation gains.

**Required scope:** Prefill/decode disaggregation; vLLM internals; TensorRT-LLM internals; llama.cpp architecture comparison; Transfer overhead.

### 64. [Production Serving and GPU Clusters](chapters/part-16/64-production-serving-and-gpu-clusters.md)

**Exit artifact:** Run a load test with queue delay, tail latency, errors and recovery reported.

**Required scope:** Throughput vs latency; Tokens per second; Requests per second; p95 and p99 latency; Serving SLOs; Observability; Autoscaling; Failure recovery; GPU cluster scheduling.

## Part 17 — LLMs on Your Laptop

### 65. [CPU and Edge Inference](chapters/part-17/65-cpu-and-edge-inference.md)

**Exit artifact:** Measure CPU decode with controlled thread counts and explain memory bandwidth effects.

**Required scope:** Edge constraints; CPU inference; SIMD; CPU vectorization; CPU threading.

### 66. [Hybrid Memory and Local Loading](chapters/part-17/66-hybrid-memory-and-local-loading.md)

**Exit artifact:** Compare cold/warm startup and compute a CPU-GPU placement budget.

**Required scope:** GPU offloading; CPU-GPU hybrid inference; Unified memory; Shared memory; Quantized formats; GGUF; Memory mapping; Startup and model loading.

### 67. [Local Runtimes and Accelerators](chapters/part-17/67-local-runtimes-and-accelerators.md)

**Exit artifact:** Trace a pinned local runtime and identify unsupported-operation fallback.

**Required scope:** llama.cpp internals; OpenVINO; NPUs; Accelerator backends; Kernel coverage.

### 68. [Packaging, Power and Thermal Limits](chapters/part-17/68-packaging-power-and-thermal-limits.md)

**Exit artifact:** Package a reproducible local demo and record sustained latency under thermal load.

**Required scope:** Power limits; Thermal limits; Model packaging; Offline deployment; Edge distillation; Dynamic edge computation.

## Part 18 — Retrieval, Memory and Agents

### 69. [Embeddings, Contrastive Learning and Vector Indexes](chapters/part-18/69-embeddings-contrastive-learning-and-vector-indexes.md)

**Exit artifact:** Build a small retrieval index and compare recall and latency against exact search.

**Required scope:** Embeddings revisited; Sentence embeddings; Document embeddings; Contrastive embedding training; Vector search; Approximate nearest neighbors; HNSW; IVF; Product quantization; Vector databases.

### 70. [RAG and Retrieval Quality](chapters/part-18/70-rag-and-retrieval-quality.md)

**Exit artifact:** Evaluate retrieval and answer quality separately on an answerable/unanswerable set.

**Required scope:** RAG; Chunking strategies; Retrieval strategies; Reranking; Retrieval evaluation; Grounding.

### 71. [Memory, Tools and Structured Output](chapters/part-18/71-memory-tools-and-structured-output.md)

**Exit artifact:** Validate tool arguments and demonstrate stale-memory handling in a bounded workflow.

**Required scope:** Short-term memory; Persistent memory; Long-term memory; Tool calling; Structured outputs; Constrained decoding; Memory invalidation.

### 72. [Agents and Multi-Model Economics](chapters/part-18/72-agents-and-multi-model-economics.md)

**Exit artifact:** Build a bounded workflow and measure which model calls contribute to task success.

**Required scope:** Agents; Planning; Multi-agent systems; Multi-LLM systems; Agent compute economics; Routing and fallback.

## Part 19 — Inside the Model: Representations and Intervention

### 73. [Hidden States, Layers and Attention Heads](chapters/part-19/73-hidden-states-layers-and-attention-heads.md)

**Exit artifact:** Collect layer activations and test a specialization hypothesis with controls.

**Required scope:** Hidden states; Residual stream analysis; Representation geometry analysis; What individual layers learn; Layer specialization; Attention-head analysis.

### 74. [Features, Probes and Mechanisms](chapters/part-19/74-features-probes-and-mechanisms.md)

**Exit artifact:** Compare probe accuracy with an intervention and state what each establishes.

**Required scope:** Neurons; Features; Probing; Sparse autoencoders; Mechanistic interpretability; Causal interventions.

### 75. [Steering, Editing and Representation Engineering](chapters/part-19/75-steering-editing-and-representation-engineering.md)

**Exit artifact:** Measure target behavior changes and collateral regression from one intervention.

**Required scope:** Activation steering; Representation engineering; Model editing; Intervention side effects.

### 76. [Merging, Stitching and Representation Compatibility](chapters/part-19/76-merging-stitching-and-representation-compatibility.md)

**Exit artifact:** Specify a bridge between two residual spaces with shape, scale and compute checks.

**Required scope:** Model merging; Layer stitching; Cross-model alignment; Normalization mismatch; Latent bridge cost.

## Part 20 — Frontier Architecture and Research

### 77. [Efficient Memory and Adaptive Computation](chapters/part-20/77-efficient-memory-and-adaptive-computation.md)

**Exit artifact:** Compare a memory-saving method against a quality-matched latency baseline.

**Required scope:** Efficient KV memory; KV-cache compression; KV-cache eviction; Activation compression; Dynamic computation; Conditional layer execution; Adaptive computation.

### 78. [Routable Intelligence and Neural Handoffs](chapters/part-20/78-routable-intelligence-and-neural-handoffs.md)

**Exit artifact:** Design a falsifiable intervention/call-elimination experiment with transfer and routing costs.

**Required scope:** Neural routing; Model cascades; Latent communication; Cross-model representations; Neural handoffs; Sparse expert intervention; Silent expert intervention; LLM dead-call elimination; Computation as a routable resource.

### 79. [Research Design and Reproduction](chapters/part-20/79-research-design-and-reproduction.md)

**Exit artifact:** Write a preregistered experiment card and reproduce one baseline.

**Required scope:** Forming research questions; Literature search; Prior-art search; Reading papers critically; Designing a research experiment; Choosing baselines; Benchmark selection; Reproducing papers; Reproducibility; Scientific vs engineering claims.

### 80. [Evidence, Ablations and Publication](chapters/part-20/80-evidence-ablations-and-publication.md)

**Exit artifact:** Produce a claim-evidence table with uncertainty, ablations and a reproducibility package.

**Required scope:** Ablations; Statistical significance; Confidence intervals; Uncertainty; Profiling research claims; FLOPs-memory-latency measurement; Writing papers; arXiv; Workshops; Conferences; Peer review; Finding unanswered questions.

## Milestone projects

See [labs/README.md](labs/README.md) for fifteen implementation milestones and their hardware/acceptance conditions. Multi-GPU measurements require suitable hardware; CPU simulations do not fulfill that gate.
