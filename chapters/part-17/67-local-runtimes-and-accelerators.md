# 67. Local Runtimes and Accelerators

Status: **Drafted.**

Part 17: LLMs on Your Laptop

## Learning outcome

Trace a pinned local runtime and identify unsupported-operation fallback.

## Prerequisites

CH-66.

<a id="t-67-01"></a>
## llama.cpp internals

Coverage ID: `T-67-01`.

llama.cpp loads model metadata and tensors through ggml/GGUF, builds a computation graph, allocates backend buffers, selects CPU or accelerator kernels, and evaluates prompt and decode graphs. Quantized weights are consumed by specialized kernels; model state includes a KV cache and runtime buffers. Optional server and sampling layers sit above the core graph.

The project changes quickly. Pin a commit or release, compiler flags, backend, artifact hash, context/batch settings, and command. A performance number without these is hard to reproduce.

<a id="t-67-02"></a>
## OpenVINO

Coverage ID: `T-67-02`.

OpenVINO converts or reads a model representation, applies graph transformations, compiles it for a selected device, and executes inference requests through plugins. CPU, GPU, and NPU capabilities differ. Model conversion can reshape or fuse graphs, and compiled-model caching can affect startup.

Validate outputs against a reference at representative lengths and decoding settings. Report conversion revision and precision. A successful compile on CPU does not prove the same graph runs entirely on an NPU.

For numerical comparison, first compare logits or fixed-token teacher-forced outputs. Free-running sampled text diverges chaotically after a small logit perturbation and is therefore a poor equality test. Declare absolute/relative tolerances and separately measure task quality for any intentionally lossy precision change.

<a id="t-67-03"></a>
## NPUs

Coverage ID: `T-67-03`.

Neural processing units target efficient tensor operations under tight power budgets. They often impose supported operation, shape, datatype, and memory constraints. LLM execution may require static buckets, quantized paths, or CPU participation for tokenization, sampling, and unsupported nodes.

Vendor TOPS is an operation-rate peak at a specified precision, not tokens per second. End-to-end decode includes weight/KV movement, host orchestration, and fallback. Measure power and sustained latency on the actual device.

<a id="t-67-04"></a>
## Accelerator backends

Coverage ID: `T-67-04`.

A backend maps a logical graph to CUDA, Metal, Vulkan, SYCL, OpenCL, vendor NPUs, or CPU implementations. Selection can be per tensor or operation. Device discovery, allocation, copies, synchronization, and kernel launch are part of the backend contract.

Reproducible evaluation records driver, runtime, backend build flags, and device identifiers. “GPU enabled” may mean only some layers or operations run there.

<a id="t-67-05"></a>
## Kernel coverage

Coverage ID: `T-67-05`.

Kernel coverage is the set of model operations, dtypes, shapes, and layouts the backend implements efficiently. Unsupported work may fail compilation, fall back to CPU, or insert conversions. One fallback inside every transformer block can erase accelerator gains through synchronization and copies.

Trace placement using runtime logs or profiler events and build a table: operation, count per token, chosen device, dtype, fallback reason, transfer bytes, and time. Compare outputs to a CPU reference with tolerances suitable for quantization. The acceptance criterion is complete enough coverage for the pinned model path, not a vendor compatibility logo.

## Four recurring perspectives

- **Follow the Token:** trace the representation and its ownership across the execution boundary.
- **Follow the Gradient:** identify synchronized or sharded learning state; for inference-only paths, state explicitly that no gradient exists.
- **Follow the Byte:** calculate persistent state, temporary buffers, transfers, and the relevant bandwidth tier.
- **Follow the Request:** include admission, scheduling, cancellation, failure, and externally visible latency.

## Lab and exit check

Pin a model artifact and runtime revision. Capture one prefill and five decode steps in logs or a profiler. Produce an operation-placement table and flag every host-device copy or CPU fallback. Deliberately select one unsupported configuration, record the failure/fallback, and verify numerical output against a reference.

The report must distinguish an explicit failure, a documented fallback, and a silent fallback inferred from traces. Treat silent placement changes as a reproducibility defect even when output remains correct.

## Primary references

- [llama.cpp repository](https://github.com/ggml-org/llama.cpp), accessed 2026-09-19.
- [OpenVINO documentation](https://docs.openvino.ai/), accessed 2026-09-19.
- [OpenVINO GenAI repository](https://github.com/openvinotoolkit/openvino.genai), accessed 2026-09-19.
