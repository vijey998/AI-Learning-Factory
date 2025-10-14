# 44. Profiling Transformer Bottlenecks

Status: **Drafted.**

Part 11: GPU Fundamentals

## Learning outcome

Measure a CPU baseline and define an honest, synchronized GPU profiling protocol that separates latency, FLOPs, and memory traffic.

<a id="t-44-01"></a>
## Decode memory bottlenecks

At low batch, autoregressive decode repeatedly reads large weights to produce few token rows. Approximate minimum time from weights alone as weight bytes divided by sustainable bandwidth. A 14 GB quantized checkpoint at 1 TB/s requires at least 14 ms per full scan; actual execution adds KV reads, activations, sampling, launches, and imperfect bandwidth. This bound is useful because no kernel optimization can beat required traffic without reuse, compression, or changing computation.

Do not diagnose from low GPU utilization alone. Utilization metrics can mean “some kernel active,” not arithmetic saturation. Batch sweep, memory throughput, Tensor Core utilization, and kernel timeline distinguish memory limits from small launches or CPU starvation.

<a id="t-44-02"></a>
## FLOPs and memory profiling

Start with analytic counts for major operations, then compare profiler counters. For each kernel record shape, dtype, theoretical FLOPs, requested bytes, measured device-memory bytes, duration, and launch count. Profiler FLOP metrics are architecture- and instruction-specific; tensor instructions may be counted differently from scalar ones. State the convention.

End-to-end bytes are not the sum of tensor sizes if caches and fusion reuse data. Conversely, temporary layouts can add traffic invisible in a high-level graph. Nsight Systems shows CPU/GPU timelines; Nsight Compute provides per-kernel hardware counters. PyTorch Profiler relates framework operations to kernels, with overhead that must be acknowledged.

<a id="t-44-03"></a>
## Bandwidth utilization

Effective bandwidth is bytes attributed to the operation divided by time. Hardware bandwidth utilization uses measured memory-controller traffic relative to a sustainable or peak rate. They answer different questions. A kernel can achieve high controller bandwidth while wasting transactions on uncoalesced loads.

For FP32 vector addition over $n$ elements, a logical-traffic estimate is $12n$ bytes: two 4-byte reads and one 4-byte write. If $n=2^{28}$ and elapsed device time is 4 ms, that estimate is 3 GiB / 4 ms = 750 GiB/s. Call it *effective logical bandwidth*, not controller bandwidth; cache write policies and memory transactions can make the hardware counter differ.

Compare achieved bandwidth with a copy benchmark on the same device, dtype, clocks, and concurrency. Inspect read/write balance, cache hit rates, sectors per request, and stalls. A low percentage may be expected for a tiny kernel that cannot expose enough concurrent requests.

<a id="t-44-04"></a>
## Latency measurement

Define boundaries: kernel latency, model-step latency, time to first token, or inter-token latency. Warm up compilation, allocator pools, caches, and clocks. Use representative shapes, fixed synchronization points, enough repetitions, and distributions such as median and p95 rather than one best sample.

GPU work launches asynchronously. A host timer around a CUDA call often measures enqueue time. Use CUDA events for device intervals or synchronize before stopping the host timer. Avoid synchronizing inside the normal hot path simply to measure it; instrumentation can destroy overlap.

For CPU baselines, control thread count, affinity if needed, warmups, input allocation, and power state. Report hardware and library versions. A fair CPU/GPU comparison includes or excludes transfer and startup consistently.

<a id="t-44-05"></a>
## Synchronization

Synchronization establishes ordering or host visibility but can create idle gaps. Device-wide synchronization waits for all prior work; stream events express narrower dependencies. Within a block, barriers coordinate shared-memory phases. Incorrect omission causes races; excessive barriers reduce overlap.

Operations such as copying a scalar to the host, printing a CUDA tensor, or calling certain timing APIs may synchronize implicitly. Timeline profiling reveals these gaps. In distributed settings, collectives introduce further synchronization, covered later.

### A defensible protocol

1. Pin model, inputs, batch/sequence lengths, dtype, clocks policy, framework, driver, and device.
2. Separate cold start, first compiled run, warmed steady state, prefill, and decode.
3. Warm up until timings stabilize, then collect enough repeated requests.
4. Measure end-to-end latency without profiler; collect representative profiler traces separately because profiling adds overhead.
5. Sweep batch and sequence lengths. Calculate analytic lower bounds and explain the gap.
6. Save raw traces, summary scripts, and environment metadata.

## Four recurring perspectives

- **Follow the Token:** mark when each request token enters prefill, decode, sampling, and streaming.
- **Follow the Gradient:** training profiles must include backward, optimizer, communication, and any recomputation.
- **Follow the Byte:** compare compulsory bytes, measured controller traffic, and effective bandwidth.
- **Follow the Request:** end-to-end latency includes CPU scheduling and gaps that kernel-only reports omit.

## Lab and exit check

Benchmark a matrix multiplication and a tiny autoregressive loop on CPU. Define the equivalent GPU protocol with warmup, CUDA events, end-to-end synchronization, and batch sweep. If CUDA is available, collect one systems timeline and one kernel report. Identify the largest interval and state what evidence would falsify your bottleneck diagnosis.

## References

- NVIDIA, [Nsight Systems User Guide](https://docs.nvidia.com/nsight-systems/UserGuide/) (version-sensitive; accessed September 2026).
- NVIDIA, [Nsight Compute Profiling Guide](https://docs.nvidia.com/nsight-compute/ProfilingGuide/) (version-sensitive; accessed September 2026).
- PyTorch, [Profiler documentation](https://pytorch.org/docs/stable/profiler.html) (version-sensitive; accessed September 2026).
