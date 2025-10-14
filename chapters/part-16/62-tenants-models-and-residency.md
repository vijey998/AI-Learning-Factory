# 62. Tenants, Models and Residency

Status: **Drafted.**

Part 16: Serving LLMs as a System

## Learning outcome

Design admission and eviction policies for concurrent models within a memory budget.

## Prerequisites

CH-61.

<a id="t-62-01"></a>
## Multi-tenant serving

Coverage ID: `T-62-01`.

Tenants share compute, queue capacity, KV memory, and sometimes prefix caches. Isolation needs quotas on prompt/output tokens, concurrent sequences, KV blocks, and rate. Weighted scheduling makes business priority explicit; per-tenant metrics expose noisy neighbors.

Cache sharing can leak whether another tenant used a prefix through timing or content mistakes. Scope caches by trust boundary and include model, tokenizer, adapter, and relevant decoding configuration in cache keys.

Isolation must be tested, not inferred from namespaces. Construct two tenants with identical text and verify that prefix hits, logs, traces, cancellation, and quota exhaustion do not cross the intended boundary. A cache key prevents accidental aliasing only if authorization is checked before lookup and cache-hit metadata is not exposed across tenants.

<a id="t-62-02"></a>
## Multi-model serving

Coverage ID: `T-62-02`.

Multiple models may occupy separate workers, time-share one device, or share a base with adapters. Routing must resolve an immutable model revision before admission. Compatibility includes tokenizer and chat template, not merely parameter shape.

Loading on demand saves residency but adds cold-start tails. Keeping every model hot can leave too little KV capacity. Model popularity, load time, size, and SLO should drive placement.

<a id="t-62-03"></a>
## Memory residency

Coverage ID: `T-62-03`.

A device budget includes weights, runtime workspace, graph pools, KV cache, temporary activations, and fragmentation reserve. On a 24 GiB GPU, a 14 GiB weight image plus 2 GiB workspace and 2 GiB safety reserve leaves only 6 GiB for KV and other state.

Residency planners should use measured peaks for pinned runtime/model combinations. Marketing capacity and raw file size omit dequantization buffers, duplicated mappings, and backend workspaces.

<a id="t-62-04"></a>
## Model loading

Coverage ID: `T-62-04`.

Loading includes locating artifacts, integrity verification, mapping or reading pages, deserialization, device transfer, kernel preparation, and optional graph capture/autotuning. Separate cold startup from warm startup: page cache and compiled kernels can make the second run deceptively fast.

Publish readiness only after a representative warmup and health check. If traffic reaches a half-loaded worker, failures masquerade as random availability problems.

<a id="t-62-05"></a>
## Model offloading

Coverage ID: `T-62-05`.

Offloading moves inactive layers or state to host memory and restores them before use. It expands capacity at the price of transfers on the critical path. Sequential decode revisits all layers per token, so layer swapping every token is usually punishing unless transfers overlap or placement is stable.

Offload is a placement strategy, not free memory. Host RAM, pinned buffers, PCIe traffic, and CPU contention become serving resources.

<a id="t-62-06"></a>
## GPU-RAM-SSD hierarchy

Coverage ID: `T-62-06`.

GPU memory offers compute-near bandwidth; RAM is larger and slower across an interconnect; SSD is persistent and slower again. A 20 GB transfer over an effective 20 GB/s PCIe path has a one-second lower bound. At 3 GB/s SSD read bandwidth it exceeds six seconds before verification and device copy.

Admission should distinguish evicting KV, unloading a model to RAM, and dropping it to disk. Each has a different recovery latency. A useful policy scores freed bytes against reload cost and near-term request probability, while pinning SLO-critical models.

For example, evicting a 6 GiB idle model that takes 0.35 s to restore may be preferable to evicting a 10 GiB model that takes 4 s, even though the second frees more memory. State the policy as a measurable objective—such as expected SLO penalty per GiB freed—and add hysteresis so alternating requests do not repeatedly unload and reload both models.

## Four recurring perspectives

- **Follow the Token:** trace the representation and its ownership across the execution boundary.
- **Follow the Gradient:** identify synchronized or sharded learning state; for inference-only paths, state explicitly that no gradient exists.
- **Follow the Byte:** calculate persistent state, temporary buffers, transfers, and the relevant bandwidth tier.
- **Follow the Request:** include admission, scheduling, cancellation, failure, and externally visible latency.

## Lab and exit check

Given 24 GiB GPU, 64 GiB RAM, two 14 GiB models, 2 GiB workspace each, and a 6 GiB peak KV demand, design residency and eviction. Use explicit PCIe and SSD bandwidth to estimate cold transitions. Test an arrival trace with alternating models and report SLO misses.

Include one adversarial trace that alternates models just faster than their reload time. Report whether admission, hysteresis, or pinning prevents thrash and how much unused capacity the protection costs.

## Primary references

- [NVIDIA Triton model management](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/model_management.html), accessed 2026-09-19.
- [CUDA Best Practices: data transfer](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/), accessed 2026-09-19.
