# 03. Anatomy of the Modern LLM Stack

Status: **Draft — not yet independently reviewed.**

A slow or incorrect answer can originate far above or far below the Transformer. Treating the whole product as “the model” makes diagnosis almost impossible. This chapter builds a layer map and follows one request through it.

<a id="t-03-01"></a>
## Applications

The application owns the user-visible contract: authentication, conversation state, permissions, input validation, presentation, and product-specific policy. It may construct a prompt from several messages and stream partial output. If the UI freezes after receiving tokens, changing attention kernels will not fix it.

The application also decides what counts as success. A code assistant may value compilable patches; a search assistant may require citations; a drilling assistant may require offline operation and bounded latency. Model quality must be evaluated inside this contract.

<a id="t-03-02"></a>
## Agents and RAG in the stack

Retrieval-augmented generation adds a data path: query construction, search, filtering, reranking, and context assembly. An agent adds a control path: choose an action, validate arguments, execute a tool, observe the result, and decide whether to continue. Both eventually create model inputs, but many failures occur before or after the model call.

A missing document may be an indexing or retrieval failure. A correct document that never fits the context may be a packing failure. A malformed tool call may reflect model output, schema design, or validation. Record these stages separately.

<a id="t-03-03"></a>
## Inference server

The inference server accepts requests and turns them into scheduled model work. It tokenizes or accepts token IDs, manages queues, forms batches, allocates KV-cache blocks, invokes the runtime, samples output, and streams tokens. Under load, queue delay may dominate time to first token even when a single isolated request is fast.

The server balances competing goals: low latency for each user, high accelerator utilization, bounded memory, fairness, and failure isolation. Continuous batching lets new requests enter between decode iterations. Prefix caching can reuse work, but only when token sequences and relevant model state match correctly.

<a id="t-03-04"></a>
## Model runtime

The runtime implements model execution for a chosen device and numeric format. It loads weights, chooses operator implementations, manages caches and temporary buffers, and may partition computation across devices. PyTorch eager mode, compiled PyTorch, llama.cpp, vLLM, and TensorRT-LLM expose different abstractions, but all must ultimately produce numerically acceptable outputs from the same model definition.

A runtime can change latency or memory without changing the conceptual architecture. It can also change numerical results slightly through precision, reduction order, or fused operations. Correctness therefore means agreement within defined tolerances and task-level quality, not necessarily bitwise identity.

<a id="t-03-05"></a>
## PyTorch and the compiler

In an eager framework, Python requests tensor operations one by one. Compilation can capture a region of those operations, transform an intermediate representation, fuse work, and generate device code. Unsupported data-dependent behavior can break a graph into smaller regions, reducing optimization opportunities.

Compilation cost is real. A first request may spend time tracing, compiling, and warming kernels; later requests reuse the result. Honest latency reports separate cold start, compile time, warmup, and steady-state execution.

<a id="t-03-06"></a>
## Tensor operations

The Transformer is expressed through operations such as matrix multiplication, normalization, elementwise functions, indexing, reductions, and data movement. Shapes and dtypes determine legal operations and much of their cost. `[B,T,D] @ [D,4D]` is a feed-forward projection; `[B,H,T,Dh] @ [B,H,Dh,T]` creates attention scores. The formulas are architecture; their execution plan is systems engineering.

Tensor operations are a useful debugging boundary. If logits are already wrong after one layer, an HTTP timeout setting is irrelevant. If tensor outputs are correct but the streamed text is truncated, the error is above the runtime.

<a id="t-03-07"></a>
## GPU kernels

A kernel is a program executed across many device threads. Framework operations may launch one kernel, several kernels, or a fused kernel that performs multiple conceptual operations. Launch overhead, memory access, synchronization, and shape specialization can matter as much as the arithmetic count.

Kernel names in a profiler are evidence about what ran, not a complete explanation. To connect them to the model, map each kernel back to an operator, tensor shapes, transferred bytes, and the request phase: prefill or decode.

<a id="t-03-08"></a>
## GPU hardware

Accelerators supply parallel arithmetic units, registers, on-chip shared memory and caches, plus high-bandwidth device memory. Matrix engines achieve large throughput only when shapes, precision, and data movement allow them to remain busy. Decode often performs little work per byte of weight read, while large prefill matrices can expose more parallelism.

Peak specifications are ceilings under particular conditions. Application throughput also includes scheduling gaps, kernels that do not use matrix engines, communication, and idle capacity caused by small batches.

<a id="t-03-09"></a>
## Memory

Memory is a hierarchy rather than one capacity number. Model weights may reside in device memory, host RAM, or mapped storage. Active tensors move through caches, shared memory and registers. The serving layer separately manages KV-cache pages and allocator reservations.

“Out of memory” can mean the weights do not fit, a long-context cache exhausted its pool, temporary workspace peaked, or fragmentation prevented a sufficiently large allocation. Record allocated, reserved, active, and peak memory when the runtime exposes them.

<a id="t-03-10"></a>
## Silicon

At the bottom, transistors implement storage and arithmetic under limits imposed by area, power, heat, signaling, and manufacturing. Software cannot repeal these constraints. Quantization reduces the bits moved and may enable faster hardware paths; it helps only when the full stack has suitable kernels and acceptable accuracy.

Silicon details matter when they change a system decision: supported precision, memory capacity, interconnect bandwidth, power envelope, or thermal throttling. A block diagram becomes useful when it predicts a measurable bottleneck.

## Follow one request

A request enters the application, which assembles messages and retrieved context. The server queues it, tokenizes it, and reserves cache space. The runtime loads or references resident weights and invokes framework or compiled operators. Operators launch kernels that move bytes through the hardware hierarchy and execute arithmetic. Logits return upward; the server samples and streams a token; the application renders it. Decode repeats this loop.

Measure at the boundaries. Application latency, queue time, tokenization time, prefill time, time per output token, tool latency, and rendering time answer different questions. A single end-to-end stopwatch tells you that the user waited; it does not tell you what to fix.

## Diagnostic exercise

Classify each symptom before proposing a remedy:

| Symptom | First layers to inspect |
| --- | --- |
| Relevant document never reaches prompt | Retrieval, reranking, context assembly |
| First request slow; later identical requests fast | Loading, compilation, cache warmup |
| Latency explodes only under concurrency | Queueing, scheduler, KV allocation, batching |
| Correct tokens arrive but UI updates late | Streaming transport and application rendering |
| Single-token decode saturates memory bandwidth | Runtime kernels, weight/KV movement, hardware |
| Tool executes destructive malformed arguments | Agent policy, schema validation, permissions |

This table points to the first investigation, not a guaranteed root cause. Instrumentation must confirm it.

## Four perspectives

**Follow the Token:** trace text, token IDs, hidden tensors, logits, sampled IDs, and displayed text.

**Follow the Gradient:** training extends below the model into backward kernels and above it into data and objective design; ordinary serving omits that path.

**Follow the Byte:** locate weight, activation, cache, communication, and storage movement at each layer.

**Follow the Request:** include queueing, scheduling, tools, cancellation, streaming, and failure recovery—not only forward compute.

## References

- Kwon et al., [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://arxiv.org/abs/2309.06180), 2023 — KV-cache paging and serving throughput.
- Ansel et al., [PyTorch 2: Faster Machine Learning Through Dynamic Python Bytecode Transformation and Graph Compilation](https://doi.org/10.1145/3620665.3640366), 2024 — capture, graph breaks, and compilation in PyTorch 2.
- Williams, Waterman, and Patterson, [Roofline: An Insightful Visual Performance Model for Multicore Architectures](https://doi.org/10.1145/1498765.1498785), 2009 — relating arithmetic throughput to memory traffic.
