# 66. Hybrid Memory and Local Loading

Status: **Drafted.**

Part 17: LLMs on Your Laptop

## Learning outcome

Compare cold/warm startup and compute a CPU-GPU placement budget.

## Prerequisites

CH-65.

<a id="t-66-01"></a>
## GPU offloading

Coverage ID: `T-66-01`.

A local runtime may place some layers on a discrete GPU and leave the rest on CPU. GPU-resident layers benefit from faster kernels and memory bandwidth; CPU layers avoid exceeding VRAM. Layer count is only a proxy for bytes because embeddings and output heads can be unusually large.

The boundary transfers hidden states. With stable placement, this may occur only at placement transitions per token; with active layer swapping it can occur repeatedly and dominate. Measure the actual transfer path and whether kernels overlap it.

<a id="t-66-02"></a>
## CPU-GPU hybrid inference

Coverage ID: `T-66-02`.

Hybrid execution needs a placement plan for weights, KV cache, compute buffers, and graph workspaces. Keeping KV with attention compute avoids repeated cache movement. A 12 GB GPU cannot safely host 11.8 GB of weights if the runtime later needs 2 GB of KV and 1 GB workspace.

A practical planner reserves fixed workspace and safety margin, computes KV growth from model dimensions and maximum context, then places weights in remaining VRAM. Benchmark boundary choices; “maximum layers offloaded” is not always fastest if it triggers paging.

<a id="t-66-03"></a>
## Unified memory

Coverage ID: `T-66-03`.

CUDA unified memory presents a shared virtual address space whose pages may migrate between CPU and GPU. It simplifies programming but does not eliminate physical location or transfer cost. Oversubscription can produce page faults and thrashing, especially when the working set alternates.

Prefetch and access-advice mechanisms may help when access is predictable. Treat unified memory as managed placement and measure migrations; do not market it as infinite VRAM.

<a id="t-66-04"></a>
## Shared memory

Coverage ID: `T-66-04`.

On integrated systems, CPU and GPU may access one physical memory pool. This avoids discrete PCIe copies but both processors compete for bandwidth and capacity. “Unified” product memory also does not imply equal coherent access costs for every engine.

Reserve memory for the OS and application. Measure sustained GPU inference while the CPU performs realistic tokenization/UI work; isolated accelerator bandwidth numbers overstate the shared workload.

<a id="t-66-05"></a>
## Quantized formats

Coverage ID: `T-66-05`.

A quantized artifact stores low-bit weight blocks plus scales and metadata. Format choice must match available kernels. Smaller files can improve loading and weight-stream bandwidth, but dequantization and accuracy differ by scheme, group size, and layer sensitivity.

File size is not runtime memory: mappings, KV cache, compute buffers, and possibly repacked weights add capacity. Compare task quality as well as tokens per second.

<a id="t-66-06"></a>
## GGUF

Coverage ID: `T-66-06`.

GGUF is a versioned container used by the ggml ecosystem. It stores named tensors and model/tokenizer metadata and supports multiple tensor quantization types. The container is not itself one quantization algorithm. Runtime compatibility depends on architecture support, metadata expectations, and quantization kernels.

Record converter revision, source-model revision, GGUF version, and per-tensor quantization. An artifact that opens but uses the wrong tokenizer metadata can generate plausible nonsense.

<a id="t-66-07"></a>
## Memory mapping

Coverage ID: `T-66-07`.

Memory mapping lets the OS map file pages into virtual memory and load them on demand. Warm starts benefit from page cache; cold starts must read storage. Mapping avoids an eager userspace copy but does not make disk reads free. Random faults can create latency spikes.

Measure after clearing or bypassing cache only when the procedure is documented and safe; otherwise label the run warm. Hashing the full artifact also adds startup I/O but may be required for integrity.

Define “cold” operationally. Dropping the operating-system page cache affects unrelated workloads and may require privilege, while reading a different large file is an unreliable substitute. A defensible report can use a freshly booted test host or direct-I/O staging, record the method, and present both cold and warm distributions rather than one stopwatch result.

<a id="t-66-08"></a>
## Startup and model loading

Coverage ID: `T-66-08`.

Separate phases: executable launch, manifest validation, artifact integrity, file map/read, metadata parse, GPU transfer, kernel initialization, graph capture, warmup, and ready signal. Timestamp each. Cold, warm, and already-resident paths serve different operational questions.

Use an atomic readiness gate. If loading fails, keep the prior known-good version available or return a clear unavailable state; never expose a partially initialized worker.

## Four recurring perspectives

- **Follow the Token:** trace the representation and its ownership across the execution boundary.
- **Follow the Gradient:** identify synchronized or sharded learning state; for inference-only paths, state explicitly that no gradient exists.
- **Follow the Byte:** calculate persistent state, temporary buffers, transfers, and the relevant bandwidth tier.
- **Follow the Request:** include admission, scheduling, cancellation, failure, and externally visible latency.

## Lab and exit check

For a device with 8 GiB VRAM and 32 GiB RAM, budget a 6 GiB quantized model, workspace, maximum-context KV, and 15% VRAM reserve. Choose CPU/GPU placement. Measure process start to readiness after cold storage and warm page cache, plus first-token latency. Explain every difference.

Verify the plan at the maximum declared context, not only an empty-cache startup. Include a failed-allocation test and show that readiness is withdrawn without corrupting the previous usable model.

## Primary references

- [CUDA Unified Memory programming guide](https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#unified-memory-programming), accessed 2026-09-19.
- [GGUF specification](https://github.com/ggml-org/ggml/blob/master/docs/gguf.md), accessed 2026-09-19.
- [Linux mmap documentation](https://man7.org/linux/man-pages/man2/mmap.2.html).
