# Consolidated chapter references

Generated from the canonical chapter reference sections. Entries remain grouped by chapter because repeated sources may support different claims. Software documentation is version-sensitive; access dates in the chapters are authoritative.

## 1. The LLM in One Picture

- Vaswani et al., [Attention Is All You Need](https://arxiv.org/abs/1706.03762), 2017 — Transformer architecture and scaled dot-product attention.
- Sutskever, Vinyals, and Le, [Sequence to Sequence Learning with Neural Networks](https://arxiv.org/abs/1409.3215), 2014 — autoregressive sequence factorization and decoding.

## 2. Training vs Inference

- [PyTorch autograd mechanics](https://docs.pytorch.org/docs/stable/notes/autograd) — dynamic graphs, saved tensors, grad modes, and the distinction between evaluation mode and gradient control. Accessed 2026-09-18.

## 3. Anatomy of the Modern LLM Stack

- Kwon et al., [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://arxiv.org/abs/2309.06180), 2023 — KV-cache paging and serving throughput.
- Ansel et al., [PyTorch 2: Faster Machine Learning Through Dynamic Python Bytecode Transformation and Graph Compilation](https://doi.org/10.1145/3620665.3640366), 2024 — capture, graph breaks, and compilation in PyTorch 2.
- Williams, Waterman, and Patterson, [Roofline: An Insightful Visual Performance Model for Multicore Architectures](https://doi.org/10.1145/1498765.1498785), 2009 — relating arithmetic throughput to memory traffic.

## 4. Building Our Tiny Laboratory

- [Python virtual environments](https://docs.python.org/3.12/library/venv.html) — creation, isolation, activation, and portability constraints. Accessed 2026-09-18.
- [PyTorch autograd mechanics](https://docs.pytorch.org/docs/stable/notes/autograd) — graph recording and grad-mode semantics. Accessed 2026-09-18.

## 5. Tensors and Resource Accounting

- [NumPy documentation](https://numpy.org/) — multidimensional arrays, indexing, vectorization, and broadcasting. Accessed 2026-09-18.

## 6. Geometry and Number Formats

- IEEE, [IEEE Standard for Floating-Point Arithmetic (IEEE 754-2019)](https://doi.org/10.1109/IEEESTD.2019.8766229), 2019.
- Micikevicius et al., [Mixed Precision Training](https://arxiv.org/abs/1710.03740), 2017.

## 7. Probability, Logits and Loss

- Shannon, [A Mathematical Theory of Communication](https://doi.org/10.1002/j.1538-7305.1948.tb01338.x), 1948 — entropy and information measures.
- Goodfellow, Bengio, and Courville, [Deep Learning, Chapter 3](https://www.deeplearningbook.org/contents/prob.html), 2016 — probability, cross-entropy, and KL divergence.

## 8. Gradients, Graphs and Autodiff

- [PyTorch autograd mechanics](https://docs.pytorch.org/docs/stable/notes/autograd) — dynamic graph construction, saved tensors, reverse-mode behavior, and grad controls. Accessed 2026-09-18.

## 9. Linear Layers and Nonlinearities

- [PyTorch `Linear`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Linear.html) and [activation functions](https://docs.pytorch.org/docs/stable/nn.functional.html). Accessed 2026-09-19.
- Hendrycks and Gimpel, [Gaussian Error Linear Units](https://arxiv.org/abs/1606.08415), 2016.

## 10. A Tiny Network, Forward and Backward

- [PyTorch autograd mechanics](https://docs.pytorch.org/docs/stable/notes/autograd). Accessed 2026-09-19.

## 11. Optimization and State

- Kingma and Ba, [Adam](https://arxiv.org/abs/1412.6980), 2014.
- Loshchilov and Hutter, [Decoupled Weight Decay Regularization](https://arxiv.org/abs/1711.05101), 2017.
- [PyTorch optimizer documentation](https://docs.pytorch.org/docs/stable/optim.html). Accessed 2026-09-19.

## 12. Initialization and Training Stability

- Glorot and Bengio, [Understanding the difficulty of training deep feedforward neural networks](https://proceedings.mlr.press/v9/glorot10a.html), 2010.
- He et al., [Delving Deep into Rectifiers](https://arxiv.org/abs/1502.01852), 2015.
- [PyTorch gradient clipping](https://docs.pytorch.org/docs/stable/generated/torch.nn.utils.clip_grad_norm_.html). Accessed 2026-09-19.

## 13. Tokenization Algorithms

- Sennrich, Haddow, and Birch, [Neural Machine Translation of Rare Words with Subword Units](https://aclanthology.org/P16-1162/), 2016.
- Kudo and Richardson, [SentencePiece](https://aclanthology.org/D18-2012/), 2018.
- Schuster and Nakajima, [Japanese and Korean Voice Search](https://research.google/pubs/japanese-and-korean-voice-search/), 2012.

## 14. Vocabulary and Token IDs

- [Hugging Face tokenizer summary](https://huggingface.co/docs/transformers/tokenizer_summary) and [special tokens](https://huggingface.co/docs/tokenizers/api/added-tokens). Accessed 2026-09-19.

## 15. Embedding Matrices and Geometry

- [PyTorch `Embedding`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Embedding.html). Accessed 2026-09-19.
- Mikolov et al., [Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/abs/1301.3781), 2013.
- Peters et al., [Deep contextualized word representations](https://aclanthology.org/N18-1202/), 2018.

## 16. Position and Sequence Order

- Vaswani et al., [Attention Is All You Need](https://arxiv.org/abs/1706.03762), 2017.
- Shaw, Uszkoreit, and Vaswani, [Self-Attention with Relative Position Representations](https://aclanthology.org/N18-2074/), 2018.
- Su et al., [RoFormer](https://arxiv.org/abs/2104.09864), 2021.

## 17. Sequence Modeling and the Attention Idea

- Elman, [Finding Structure in Time](https://doi.org/10.1207/s15516709cog1402_1), 1990.
- Hochreiter and Schmidhuber, [Long Short-Term Memory](https://doi.org/10.1162/neco.1997.9.8.1735), 1997.
- Bahdanau, Cho, and Bengio, [Neural Machine Translation by Jointly Learning to Align and Translate](https://arxiv.org/abs/1409.0473), 2014.

## 18. Queries, Keys, Values and Scaling

- Vaswani et al., [Attention Is All You Need](https://arxiv.org/abs/1706.03762), 2017.

## 19. Causal and Multi-Head Attention

- Vaswani et al., [Attention Is All You Need](https://arxiv.org/abs/1706.03762), 2017.
- [PyTorch scaled dot-product attention](https://docs.pytorch.org/docs/stable/generated/torch.nn.functional.scaled_dot_product_attention.html). Accessed 2026-09-19.

## 20. Attention Shapes and Compute Cost

- Vaswani et al., [Attention Is All You Need](https://arxiv.org/abs/1706.03762), 2017.
- Dao et al., [FlashAttention](https://arxiv.org/abs/2205.14135), 2022.

## 21. Residual Streams and Normalization

- He et al., [Deep Residual Learning for Image Recognition](https://arxiv.org/abs/1512.03385), 2015.
- Ba, Kiros, and Hinton, [Layer Normalization](https://arxiv.org/abs/1607.06450), 2016.
- Zhang and Sennrich, [Root Mean Square Layer Normalization](https://arxiv.org/abs/1910.07467), 2019.
- Vaswani et al., [Attention Is All You Need](https://arxiv.org/abs/1706.03762), 2017.

## 22. Feed-Forward Networks and Complete Blocks

- Vaswani et al., [Attention Is All You Need](https://arxiv.org/abs/1706.03762), 2017.
- Hendrycks and Gimpel, [Gaussian Error Linear Units](https://arxiv.org/abs/1606.08415), 2016.
- Shazeer, [GLU Variants Improve Transformer](https://arxiv.org/abs/2002.05202), 2020.

## 23. Stacking, Vocabulary Projection and Tying

- Press and Wolf, [Using the Output Embedding to Improve Language Models](https://arxiv.org/abs/1608.05859), 2016.
- Inan, Khosravi, and Socher, [Tying Word Vectors and Word Classifiers](https://arxiv.org/abs/1611.01462), 2016.

## 24. Build Our GPT From Scratch

- Radford et al., [Improving Language Understanding by Generative Pre-Training](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf), 2018.
- Vaswani et al., [Attention Is All You Need](https://arxiv.org/abs/1706.03762), 2017.
- PyTorch documentation for `nn.Module`, pinned by the environment record for executable results.

## 25. Sequences, Batches and Pretraining

- Vaswani et al., [Attention Is All You Need](https://arxiv.org/abs/1706.03762), 2017.
- Brown et al., [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165), 2020.

## 26. The Training Step and Schedule

- Kingma and Ba, [Adam: A Method for Stochastic Optimization](https://arxiv.org/abs/1412.6980), 2014.
- Loshchilov and Hutter, [Decoupled Weight Decay Regularization](https://arxiv.org/abs/1711.05101), 2017.
- Pascanu, Mikolov, and Bengio, [On the Difficulty of Training Recurrent Neural Networks](https://proceedings.mlr.press/v28/pascanu13.html), 2013.

## 27. Mixed Precision and Checkpoint Anatomy

- Micikevicius et al., [Mixed Precision Training](https://arxiv.org/abs/1710.03740), 2017.
- Chen et al., [Training Deep Nets with Sublinear Memory Cost](https://arxiv.org/abs/1604.06174), 2016.
- PyTorch reproducibility and automatic mixed precision documentation, version pinned for execution.

## 28. Debugging and Training Our Tiny Model

- Goodfellow, Bengio, and Courville, [*Deep Learning*](https://www.deeplearningbook.org/), optimization chapters, 2016.
- PyTorch autograd anomaly detection and reproducibility documentation, version pinned for execution.

## 29. Transformer Families

- Devlin et al., [BERT](https://arxiv.org/abs/1810.04805), 2018.
- Raffel et al., [Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer](https://jmlr.org/papers/v21/20-074.html), 2019.
- Touvron et al., [LLaMA](https://arxiv.org/abs/2302.13971), 2023.

## 30. Modern Positions, Heads and MLPs

- Su et al., [RoFormer: Enhanced Transformer with Rotary Position Embedding](https://arxiv.org/abs/2104.09864), 2021.
- Shazeer, [Fast Transformer Decoding: One Write-Head is All You Need](https://arxiv.org/abs/1911.02150), 2019.
- Ainslie et al., [GQA: Training Generalized Multi-Query Transformer Models](https://arxiv.org/abs/2305.13245), 2023.

## 31. Mixture of Experts

- Shazeer et al., [Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer](https://arxiv.org/abs/1701.06538), 2017.
- Fedus, Zoph, and Shazeer, [Switch Transformers](https://jmlr.org/papers/v23/21-0998.html), 2021.
- Lepikhin et al., [GShard](https://arxiv.org/abs/2006.16668), 2020.

## 32. Alternative Architectures and Real Configs

- Beltagy, Peters, and Cohan, [Longformer](https://arxiv.org/abs/2004.05150), 2020.
- Gu and Dao, [Mamba: Linear-Time Sequence Modeling with Selective State Spaces](https://arxiv.org/abs/2312.00752), 2023.
- Touvron et al., [Llama 2](https://arxiv.org/abs/2307.09288), 2023.

## 33. Data Sources and Cleaning

- Lee et al., [Deduplicating Training Data Makes Language Models Better](https://arxiv.org/abs/2107.06499), 2021.
- Dodge et al., [Documenting Large Webtext Corpora](https://arxiv.org/abs/2104.08758), 2021.
- Penedo et al., [The RefinedWeb Dataset for Falcon LLM](https://arxiv.org/abs/2306.01116), 2023.

## 34. Mixtures, Tokens and Synthetic Data

- Gao et al., [The Pile](https://arxiv.org/abs/2101.00027), 2020.
- Longpre et al., [A Pretrainer's Guide to Training Data](https://arxiv.org/abs/2305.13169), 2023.
- Carlini et al., [Quantifying Memorization Across Neural Language Models](https://arxiv.org/abs/2202.07646), 2022.

## 35. Evaluation and Meaningful Experiments

- Liang et al., [Holistic Evaluation of Language Models](https://arxiv.org/abs/2211.09110), 2022.
- Dror et al., [Testing Statistical Significance in NLP](https://aclanthology.org/P18-1128/), 2018.
- Mitchell et al., [Model Cards for Model Reporting](https://arxiv.org/abs/1810.03993), 2018.

## 36. Scaling Laws

- Kaplan et al., [Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361), 2020.
- Hoffmann et al., [Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556), 2022.
- Bian et al., [Scaling Inference-Efficient Language Models](https://arxiv.org/abs/2501.18107), 2025.

## 37. Pretraining, Continued Pretraining and SFT

- Ouyang et al., [Training Language Models to Follow Instructions with Human Feedback](https://arxiv.org/abs/2203.02155), 2022.
- Wei et al., [Finetuned Language Models Are Zero-Shot Learners](https://arxiv.org/abs/2109.01652), 2021.
- Hugging Face, [Chat templates documentation](https://huggingface.co/docs/transformers/chat_templating) (version-sensitive; accessed September 2026).

## 38. Parameter-Efficient Adaptation

- Houlsby et al., [Parameter-Efficient Transfer Learning for NLP](https://arxiv.org/abs/1902.00751), 2019.
- Li and Liang, [Prefix-Tuning](https://arxiv.org/abs/2101.00190), 2021.
- Hu et al., [LoRA](https://arxiv.org/abs/2106.09685), 2021.
- Dettmers et al., [QLoRA](https://arxiv.org/abs/2305.14314), 2023.

## 39. Preferences and Reinforcement Learning

- Christiano et al., [Deep Reinforcement Learning from Human Preferences](https://arxiv.org/abs/1706.03741), 2017.
- Schulman et al., [Proximal Policy Optimization Algorithms](https://arxiv.org/abs/1707.06347), 2017.
- Ouyang et al., [Training Language Models to Follow Instructions with Human Feedback](https://arxiv.org/abs/2203.02155), 2022.
- Rafailov et al., [Direct Preference Optimization](https://arxiv.org/abs/2305.18290), 2023.

## 40. Reasoning, Test-Time Compute and Distillation

- Wang et al., [Self-Consistency Improves Chain of Thought Reasoning](https://arxiv.org/abs/2203.11171), 2022.
- Hinton et al., [Distilling the Knowledge in a Neural Network](https://arxiv.org/abs/1503.02531), 2015.
- Cobbe et al., [Training Verifiers to Solve Math Word Problems](https://arxiv.org/abs/2110.14168), 2021.
- Gao et al., [On Designing Effective RL Reward at Training Time for LLM Reasoning](https://arxiv.org/abs/2410.15115), 2024.

## 41. Why GPUs and How They Execute

- NVIDIA, [CUDA C++ Programming Guide](https://docs.nvidia.com/cuda/cuda-c-programming-guide/) (version-sensitive; accessed September 2026).
- NVIDIA, [GPU Performance Background User's Guide](https://docs.nvidia.com/deeplearning/performance/dl-performance-gpu-background/index.html) (accessed September 2026).

## 42. Memory Hierarchy and Movement

- NVIDIA, [CUDA C++ Best Practices Guide](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/) (version-sensitive; accessed September 2026).
- NVIDIA, [CUDA C++ Programming Guide: Memory Hierarchy](https://docs.nvidia.com/cuda/cuda-c-programming-guide/#memory-hierarchy) (accessed September 2026).

## 43. Throughput, Intensity and Rooflines

- Williams, Waterman, and Patterson, [Roofline: An Insightful Visual Performance Model](https://doi.org/10.1145/1498765.1498785), 2009.
- NVIDIA, [Nsight Compute Roofline Analysis](https://docs.nvidia.com/nsight-compute/ProfilingGuide/index.html#roofline-charts) (version-sensitive; accessed September 2026).

## 44. Profiling Transformer Bottlenecks

- NVIDIA, [Nsight Systems User Guide](https://docs.nvidia.com/nsight-systems/UserGuide/) (version-sensitive; accessed September 2026).
- NVIDIA, [Nsight Compute Profiling Guide](https://docs.nvidia.com/nsight-compute/ProfilingGuide/) (version-sensitive; accessed September 2026).
- PyTorch, [Profiler documentation](https://pytorch.org/docs/stable/profiler.html) (version-sensitive; accessed September 2026).

## 45. Kernels, GEMM and Tiling

- NVIDIA, [CUDA C++ Programming Guide](https://docs.nvidia.com/cuda/cuda-c-programming-guide/), version-sensitive; accessed 2026-09-19.
- NVIDIA, [Parallel Thread Execution ISA](https://docs.nvidia.com/cuda/parallel-thread-execution/), version-sensitive; accessed 2026-09-19.
- NVIDIA, [CUTLASS documentation](https://docs.nvidia.com/cutlass/), version-sensitive; accessed 2026-09-19. Pin GPU architecture, toolkit, driver, library commit, dtype, and shapes.

## 46. CUDA, Triton and CUTLASS

- NVIDIA, [CUDA C++ Programming Guide](https://docs.nvidia.com/cuda/cuda-c-programming-guide/), version-sensitive; accessed 2026-09-19.
- OpenAI, [Triton tutorials](https://triton-lang.org/main/getting-started/tutorials/), version-sensitive; accessed 2026-09-19.
- NVIDIA, [CUTLASS documentation](https://docs.nvidia.com/cutlass/), version-sensitive; accessed 2026-09-19.
- NVIDIA, [Nsight Compute documentation](https://docs.nvidia.com/nsight-compute/), version-sensitive; accessed 2026-09-19. Pin Python, PyTorch, Triton, toolkit, driver, GPU, and commits.

## 47. Graphs, Compilers and Runtimes

- PyTorch, [TorchDynamo overview](https://docs.pytorch.org/docs/stable/torch.compiler_dynamo_overview.html), version-sensitive; accessed 2026-09-19.
- PyTorch, [`torch.compile` programming model](https://docs.pytorch.org/docs/stable/torch.compiler.html), version-sensitive; accessed 2026-09-19.
- PyTorch, [FX documentation](https://docs.pytorch.org/docs/stable/fx.html), version-sensitive; accessed 2026-09-19.
- PyTorch, [TorchInductor documentation](https://docs.pytorch.org/docs/stable/torch.compiler_inductor.html), version-sensitive; accessed 2026-09-19. Pin PyTorch release or commit, backend, flags, CUDA/Triton, model revision, and inputs.

## 48. CUDA Graphs and Execution Overhead

- NVIDIA, [CUDA C++ Programming Guide: CUDA Graphs](https://docs.nvidia.com/cuda/cuda-c-programming-guide/#cuda-graphs), version-sensitive; accessed 2026-09-19.
- NVIDIA, [CUDA Runtime API: Graph Management](https://docs.nvidia.com/cuda/cuda-runtime-api/group__CUDART__GRAPH.html), version-sensitive; accessed 2026-09-19.
- PyTorch, [CUDA semantics: CUDA Graphs](https://docs.pytorch.org/docs/stable/notes/cuda.html#cuda-graphs), version-sensitive; accessed 2026-09-19. Pin driver, toolkit, PyTorch, allocator, graph mode, and shapes.

## 49. Load Weights and Trace a Forward Pass

- PyTorch, [`inference_mode`](https://docs.pytorch.org/docs/stable/generated/torch.autograd.grad_mode.inference_mode.html), version-sensitive; accessed 2026-09-19.
- Hugging Face, [Transformers model documentation](https://huggingface.co/docs/transformers/main/en/models), version-sensitive; accessed 2026-09-19.
- Hugging Face, [Transformers model loading](https://huggingface.co/docs/transformers/main/en/models#loading-models), version-sensitive; accessed 2026-09-19. Pin framework versions, model commit, tokenizer commit, dtype, attention backend, and hardware.

## 50. Prefill, Decode and KV Cache

- Vaswani et al., [Attention Is All You Need](https://arxiv.org/abs/1706.03762), 2017.
- Ainslie et al., [GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints](https://arxiv.org/abs/2305.13245), 2023.
- Hugging Face, [Caching](https://huggingface.co/docs/transformers/main/en/cache_explanation), version-sensitive; accessed 2026-09-19. Pin model code and revision because cache structure and position handling are architecture-specific.

## 51. Sampling and Decoding Policies

- Holtzman et al., [The Curious Case of Neural Text Degeneration](https://arxiv.org/abs/1904.09751), 2020.
- Hugging Face, [Generation API](https://huggingface.co/docs/transformers/main/en/main_classes/text_generation), version-sensitive; accessed 2026-09-19.
- Hugging Face, [Generation strategies](https://huggingface.co/docs/transformers/main/en/generation_strategies), version-sensitive; accessed 2026-09-19. Pin Transformers, model and tokenizer revisions, generation config, seed, device, and numeric mode.

## 52. Inference Memory and Latency Accounting

- MLCommons, [MLPerf Inference: Datacenter benchmark](https://mlcommons.org/benchmarks/inference-datacenter/), version-sensitive; accessed 2026-09-19.
- Kwon et al., [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://arxiv.org/abs/2309.06180), 2023.
- vLLM, [official documentation](https://docs.vllm.ai/en/latest/), version-sensitive; accessed 2026-09-19. Pin engine commit and configuration, model revision, hardware clocks and power, workload, tokenizer, and measurement boundary.

## 53. FlashAttention and Paged KV Memory

- Dao et al., [FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness](https://arxiv.org/abs/2205.14135), 2022.
- Dao, [FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning](https://arxiv.org/abs/2307.08691), 2023.
- Kwon et al., [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://arxiv.org/abs/2309.06180), 2023.
- vLLM, [official documentation](https://docs.vllm.ai/), version-sensitive; accessed 2026-09-19. Pin kernel version, attention backend, dtype, mask, model, block size, GPU, and workload.

## 54. Caching, Batching and Prefill Scheduling

- Yu et al., [Orca: A Distributed Serving System for Transformer-Based Generative Models](https://www.usenix.org/conference/osdi22/presentation/yu), 2022.
- Kwon et al., [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://arxiv.org/abs/2309.06180), 2023.
- Agrawal et al., [Taming Throughput-Latency Tradeoff in LLM Inference with Sarathi-Serve](https://arxiv.org/abs/2403.02310), 2024.
- vLLM, [Automatic Prefix Caching](https://docs.vllm.ai/en/latest/features/automatic_prefix_caching.html), version-sensitive; accessed 2026-09-19. Pin engine commit and configuration, block size, arrival trace, model revision, and SLO.

## 55. Speculative Decoding and Dynamic Execution

- Leviathan, Kalman, and Matias, [Fast Inference from Transformers via Speculative Decoding](https://arxiv.org/abs/2211.17192), 2023.
- Chen et al., [Accelerating Large Language Model Decoding with Speculative Sampling](https://arxiv.org/abs/2302.01318), 2023.
- NVIDIA, [CUDA C++ Programming Guide: CUDA Graphs](https://docs.nvidia.com/cuda/cuda-c-programming-guide/#cuda-graphs), version-sensitive; accessed 2026-09-19. Pin algorithm variant, draft and target revisions, engine commit, draft length, batch and concurrency, prompts, precision, and graph policy.

## 56. Quantization Across the Inference Path

- Frantar et al., [GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers](https://arxiv.org/abs/2210.17323), 2022.
- Lin et al., [AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration](https://arxiv.org/abs/2306.00978), 2023.
- Xiao et al., [SmoothQuant: Accurate and Efficient Post-Training Quantization for Large Language Models](https://arxiv.org/abs/2211.10438), 2022.
- Open Compute Project, [8-bit Floating Point Specification](https://www.opencompute.org/documents/ocp-8-bit-floating-point-specification-ofp8-revision-1-0-2023-06-20-pdf), revision 1.0, 2023; and ggml-org, [llama.cpp source and GGUF implementation](https://github.com/ggml-org/llama.cpp), version-sensitive; accessed 2026-09-19. Pin method implementation, commit, model and calibration data, quantization type and group size, hardware, and kernels.

## 57. Parallel Training Strategies

- [PyTorch FSDP2 tutorial](https://docs.pytorch.org/tutorials/intermediate/FSDP_tutorial.html), accessed 2026-09-19.
- Rajbhandari et al., [ZeRO](https://arxiv.org/abs/1910.02054), 2020.
- [PyTorch DistributedDataParallel API](https://docs.pytorch.org/docs/stable/generated/torch.nn.parallel.DistributedDataParallel.html).

## 58. Partitioning Model Computation

- Shoeybi et al., [Megatron-LM](https://arxiv.org/abs/1909.08053), 2019.
- Huang et al., [GPipe](https://arxiv.org/abs/1811.06965), 2019.
- Lepikhin et al., [GShard](https://arxiv.org/abs/2006.16668), 2020.

## 59. Collectives and Interconnects

- [NCCL collective operations](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/usage/collectives.html), accessed 2026-09-19.
- [NVIDIA GPUDirect RDMA](https://docs.nvidia.com/cuda/gpudirect-rdma/), accessed 2026-09-19.
- Patarasuk and Yuan, [Bandwidth Optimal All-reduce](https://doi.org/10.1016/j.jpdc.2009.05.002), 2009.

## 60. Distributed Execution and Failure Recovery

- [PyTorch distributed overview](https://docs.pytorch.org/docs/stable/distributed.html), accessed 2026-09-19.
- [PyTorch Distributed Checkpoint](https://docs.pytorch.org/docs/stable/distributed.checkpoint.html), accessed 2026-09-19.
- [NCCL troubleshooting](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/troubleshooting.html), accessed 2026-09-19.

## 61. Anatomy of an Inference Server

- [vLLM architecture documentation](https://docs.vllm.ai/en/latest/design/arch_overview.html), accessed 2026-09-19.
- Kwon et al., [Efficient Memory Management for LLM Serving with PagedAttention](https://arxiv.org/abs/2309.06180), 2023.

## 62. Tenants, Models and Residency

- [NVIDIA Triton model management](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/model_management.html), accessed 2026-09-19.
- [CUDA Best Practices: data transfer](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/), accessed 2026-09-19.

## 63. Disaggregation and Runtime Comparisons

- [vLLM documentation](https://docs.vllm.ai/), accessed 2026-09-19.
- Kwon et al., [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://arxiv.org/abs/2309.06180), 2023.
- [TensorRT-LLM documentation](https://nvidia.github.io/TensorRT-LLM/), accessed 2026-09-19.
- [llama.cpp repository](https://github.com/ggml-org/llama.cpp), accessed 2026-09-19.

## 64. Production Serving and GPU Clusters

- [OpenTelemetry specification](https://opentelemetry.io/docs/specs/), accessed 2026-09-19.
- [Kubernetes device plugins](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/), accessed 2026-09-19.
- [NVIDIA DCGM documentation](https://docs.nvidia.com/datacenter/dcgm/latest/), accessed 2026-09-19.

## 65. CPU and Edge Inference

- [llama.cpp performance documentation and source](https://github.com/ggml-org/llama.cpp), accessed 2026-09-19.
- [Intel Intrinsics Guide](https://www.intel.com/content/www/us/en/docs/intrinsics-guide/index.html), accessed 2026-09-19.
- [Arm ACLE](https://arm-software.github.io/acle/), accessed 2026-09-19.

## 66. Hybrid Memory and Local Loading

- [CUDA Unified Memory programming guide](https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#unified-memory-programming), accessed 2026-09-19.
- [GGUF specification](https://github.com/ggml-org/ggml/blob/master/docs/gguf.md), accessed 2026-09-19.
- [Linux mmap documentation](https://man7.org/linux/man-pages/man2/mmap.2.html).

## 67. Local Runtimes and Accelerators

- [llama.cpp repository](https://github.com/ggml-org/llama.cpp), accessed 2026-09-19.
- [OpenVINO documentation](https://docs.openvino.ai/), accessed 2026-09-19.
- [OpenVINO GenAI repository](https://github.com/openvinotoolkit/openvino.genai), accessed 2026-09-19.

## 68. Packaging, Power and Thermal Limits

- [NIST Secure Software Development Framework](https://csrc.nist.gov/pubs/sp/800/218/final), accessed 2026-09-19.
- Hinton et al., [Distilling the Knowledge in a Neural Network](https://arxiv.org/abs/1503.02531), 2015.
- [SPDX specification](https://spdx.github.io/spdx-spec/), accessed 2026-09-19.

## 69. Embeddings, Contrastive Learning and Vector Indexes

- Reimers and Gurevych, [Sentence-BERT](https://aclanthology.org/D19-1410/), EMNLP-IJCNLP 2019.
- Karpukhin et al., [Dense Passage Retrieval](https://aclanthology.org/2020.emnlp-main.550/), EMNLP 2020.
- Malkov and Yashunin, [Efficient and Robust Approximate Nearest Neighbor Search Using HNSW](https://doi.org/10.1109/TPAMI.2018.2889473), IEEE TPAMI 2020.
- Jégou, Douze, and Schmid, [Product Quantization for Nearest Neighbor Search](https://doi.org/10.1109/TPAMI.2010.57), IEEE TPAMI 2011.
- Johnson, Douze, and Jégou, [Billion-scale similarity search with GPUs](https://doi.org/10.1109/TBDATA.2019.2921572), IEEE Transactions on Big Data 2021.

## 70. RAG and Retrieval Quality

- Lewis et al., [Retrieval-Augmented Generation](https://proceedings.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html), NeurIPS 2020.
- Robertson and Zaragoza, [The Probabilistic Relevance Framework: BM25 and Beyond](https://doi.org/10.1561/1500000019), 2009.
- Khattab and Zaharia, [ColBERT](https://doi.org/10.1145/3397271.3401075), SIGIR 2020.
- Thakur et al., [BEIR](https://openreview.net/forum?id=wCu6T5xFjeJ), ICLR 2021.
- Craswell et al., [Overview of the TREC 2020 Deep Learning Track](https://trec.nist.gov/pubs/trec29/papers/OVERVIEW.DL.pdf), TREC 2020.

## 71. Memory, Tools and Structured Output

- Schick et al., [Toolformer](https://proceedings.neurips.cc/paper_files/paper/2023/hash/d842425e4bf79ba039352da0f658a906-Abstract-Conference.html), NeurIPS 2023.
- Poesia et al., [Synchromesh](https://openreview.net/forum?id=KmtVD97J43e), ICLR 2022.
- [JSON Schema 2020-12 specification](https://json-schema.org/specification-links#2020-12), accessed 2026-09-19.

## 72. Agents and Multi-Model Economics

- Yao et al., [ReAct](https://openreview.net/forum?id=WE_vluYUL-X), ICLR 2023.
- Shinn et al., [Reflexion](https://proceedings.neurips.cc/paper_files/paper/2023/hash/1b44b878bb782e6954cd888628510e90-Abstract-Conference.html), NeurIPS 2023.
- Chen, Zaharia, and Zou, [FrugalGPT](https://arxiv.org/abs/2305.05176), 2023.

## 73. Hidden States, Layers and Attention Heads

- Elhage et al., [A Mathematical Framework for Transformer Circuits](https://transformer-circuits.pub/2021/framework/index.html), 2021.
- Belinkov, [Probing Classifiers](https://aclanthology.org/J22-2003/), Computational Linguistics 2022.
- Kornblith et al., [Similarity of Neural Network Representations Revisited](https://proceedings.mlr.press/v97/kornblith19a.html), ICML 2019.
- Olsson et al., [In-context Learning and Induction Heads](https://arxiv.org/abs/2209.11895), 2022.

## 74. Features, Probes and Mechanisms

- Alain and Bengio, [Understanding Intermediate Layers Using Linear Classifier Probes](https://arxiv.org/abs/1610.01644), 2016.
- Hewitt and Liang, [Designing and Interpreting Probes with Control Tasks](https://aclanthology.org/D19-1275/), EMNLP-IJCNLP 2019.
- Meng et al., [Locating and Editing Factual Associations in GPT](https://proceedings.neurips.cc/paper_files/paper/2022/hash/6f1d43d5a82a37e89b0665b33bf3a182-Abstract-Conference.html), NeurIPS 2022.
- Bricken et al., [Towards Monosemanticity](https://transformer-circuits.pub/2023/monosemantic-features/index.html), 2023; empirical research report, not peer-reviewed conference evidence.

## 75. Steering, Editing and Representation Engineering

- Turner et al., [Activation Addition](https://arxiv.org/abs/2308.10248), 2023.
- Zou et al., [Representation Engineering](https://arxiv.org/abs/2310.01405), 2023.
- Meng et al., [ROME](https://proceedings.neurips.cc/paper_files/paper/2022/hash/6f1d43d5a82a37e89b0665b33bf3a182-Abstract-Conference.html), NeurIPS 2022.
- Meng et al., [MEMIT](https://openreview.net/forum?id=MkbcAHIYgyS), ICLR 2023.

## 76. Merging, Stitching and Representation Compatibility

- Wortsman et al., [Model Soups](https://proceedings.mlr.press/v162/wortsman22a.html), ICML 2022.
- Ainsworth, Hayase, and Srinivasa, [Git Re-Basin](https://openreview.net/forum?id=CQsmMYmlP5T), ICLR 2023.
- Bansal, Nakkiran, and Barak, [Revisiting Model Stitching](https://proceedings.neurips.cc/paper/2021/hash/01ded4259d101feb739b06c399e9cd9c-Abstract.html), NeurIPS 2021.
- Ilharco et al., [Editing Models with Task Arithmetic](https://openreview.net/forum?id=6t0Kwf8-jrj), ICLR 2023.

## 77. Efficient Memory and Adaptive Computation

- Graves, [Adaptive Computation Time for Recurrent Neural Networks](https://arxiv.org/abs/1603.08983), 2016.
- Xin et al., [DeeBERT](https://aclanthology.org/2020.acl-main.204/), ACL 2020.
- Xiao et al., [Efficient Streaming Language Models with Attention Sinks](https://openreview.net/forum?id=NG7sS51zVF), ICLR 2024.
- Zhang et al., [H2O: Heavy-Hitter Oracle for Efficient Generative Inference](https://proceedings.neurips.cc/paper_files/paper/2023/hash/6ceefa7b15572587b78ecfcebb2827f8-Abstract-Conference.html), NeurIPS 2023.

## 78. Routable Intelligence and Neural Handoffs

- Jacobs et al., [Adaptive Mixtures of Local Experts](https://doi.org/10.1162/neco.1991.3.1.79), Neural Computation 1991.
- Teerapittayanon, McDanel, and Kung, [BranchyNet](https://arxiv.org/abs/1709.01686), 2017.
- Bansal, Nakkiran, and Barak, [Revisiting Model Stitching](https://proceedings.neurips.cc/paper/2021/hash/01ded4259d101feb739b06c399e9cd9c-Abstract.html), NeurIPS 2021.
- Kang et al., [Neurosurgeon: Collaborative Intelligence Between the Cloud and Mobile Edge](https://doi.org/10.1145/3037697.3037698), ASPLOS 2017.

## 79. Research Design and Reproduction

- Pineau et al., [Improving Reproducibility in Machine Learning Research](https://jmlr.org/papers/v22/20-303.html), JMLR 2021.
- Gundersen and Kjensmo, [State of the Art: Reproducibility in Artificial Intelligence](https://ojs.aaai.org/index.php/AAAI/article/view/11503), AAAI 2018.
- [NeurIPS Paper Checklist](https://neurips.cc/public/guides/PaperChecklist), current author guidance, accessed 2026-09-19.
- [ACM Artifact Review and Badging](https://www.acm.org/publications/policies/artifact-review-and-badging-current), accessed 2026-09-19.
- National Academies, [Reproducibility and Replicability in Science](https://doi.org/10.17226/25303), 2019.

## 80. Evidence, Ablations and Publication

- Dodge et al., [Show Your Work: Improved Reporting of Experimental Results](https://aclanthology.org/D19-1224/), EMNLP-IJCNLP 2019.
- Dror et al., [The Hitchhiker’s Guide to Testing Statistical Significance in NLP](https://aclanthology.org/P18-1128/), ACL 2018.
- Agarwal et al., [Deep Reinforcement Learning at the Edge of the Statistical Precipice](https://proceedings.neurips.cc/paper/2021/hash/f514cec81cb148559cf475e7426eed5e-Abstract.html), NeurIPS 2021.
- Wasserstein, Schirm, and Lazar, [Moving to a World Beyond “p < 0.05”](https://doi.org/10.1080/00031305.2019.1583913), The American Statistician 2019.
- [arXiv submission help](https://info.arxiv.org/help/submit/index.html), accessed 2026-09-19.
- [NeurIPS Paper Checklist](https://neurips.cc/public/guides/PaperChecklist), accessed 2026-09-19.
