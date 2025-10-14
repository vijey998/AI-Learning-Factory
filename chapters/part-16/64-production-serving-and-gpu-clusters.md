# 64. Production Serving and GPU Clusters

Status: **Drafted.**

Part 16: Serving LLMs as a System

## Learning outcome

Run a load test with queue delay, tail latency, errors and recovery reported.

## Prerequisites

CH-63.

<a id="t-64-01"></a>
## Throughput vs latency

Coverage ID: `T-64-01`.

Throughput counts completed work per time; latency follows one request. Batching can raise tokens per second while increasing queue delay and time to first token. Plot load against latency: near saturation, a small arrival increase can cause queues to explode.

Benchmark with realistic prompt/output distributions and arrival patterns. Closed-loop clients that wait before sending again hide overload; open-loop arrivals reveal it.

<a id="t-64-02"></a>
## Tokens per second

Coverage ID: `T-64-02`.

Report prompt tokens per second separately from generated tokens per second because prefill and decode differ. Per-user decode rate differs from aggregate rate: 1,000 tokens/s across 100 sequences may feel like 10 tokens/s each. State whether tokenization and rejected work are included.

<a id="t-64-03"></a>
## Requests per second

Coverage ID: `T-64-03`.

Requests per second is meaningful only with workload shape. One request may generate one token or a thousand. Pair RPS with input/output token distributions, concurrency, cancellation, and success rate. Capacity planning in RPS alone is a classic category error.

<a id="t-64-04"></a>
## p95 and p99 latency

Coverage ID: `T-64-04`.

Percentiles expose tails hidden by averages. Report TTFT, inter-token latency or TPOT, and end-to-end completion separately at p50/p95/p99. Use enough samples for the percentile: a p99 from 100 requests is essentially one observation. Preserve coordinated-omission-resistant arrival timing.

Attach uncertainty to tail estimates. With $n$ independent requests, an empirical p99 is an order statistic near the largest $0.01n$ observations; 100 samples cannot characterize tail shape. Bootstrap only at an independent unit and preserve temporal blocks when load varies, because treating correlated tokens or burst traffic as independent produces falsely narrow intervals.

<a id="t-64-05"></a>
## Serving SLOs

Coverage ID: `T-64-05`.

An SLO defines a measured target over a window, such as 99% successful requests with TTFT below 800 ms for prompts under 2,000 tokens. Segment by declared workload class. Error budgets turn reliability into an operational decision: deployments and experiments consume budget when they cause misses.

<a id="t-64-06"></a>
## Observability

Coverage ID: `T-64-06`.

Correlate request traces with queue delay, scheduler iteration, batch composition, model/adapter revision, KV occupancy, prefix hits, kernel time, GPU memory, power, errors, and cancellation. High-cardinality request IDs belong in traces, not metric labels. Logs must avoid raw sensitive prompts by default.

<a id="t-64-07"></a>
## Autoscaling

Coverage ID: `T-64-07`.

GPU workers start slowly, so scaling only on GPU utilization reacts late. Queueing delay, admitted token backlog, KV pressure, and predicted demand are better signals. Scale-down must drain or migrate stateful sequences. Maintain warm capacity when cold start exceeds the SLO horizon.

<a id="t-64-08"></a>
## Failure recovery

Coverage ID: `T-64-08`.

Remove unhealthy workers from routing, stop admission, and decide which in-flight requests can retry. Streaming retries can duplicate text unless the protocol includes sequence position and the client reconciles it. Model-parallel groups usually fail as a unit. Test worker crash, network partition, OOM, and corrupt artifact.

<a id="t-64-09"></a>
## GPU cluster scheduling

Coverage ID: `T-64-09`.

Cluster scheduling must place entire gangs, honor topology, GPU type, memory, and NIC affinity, and limit fragmentation. Packing small jobs improves utilization but may create interference; spreading can waste fast links. Track useful tokens per accelerator-hour and SLO attainment, not allocation percentage alone.

Hardware figures vary by exact SKU, power mode, topology, drivers, and precision. Treat vendor peaks as ceilings and publish measured results with the environment.

## Four recurring perspectives

- **Follow the Token:** trace the representation and its ownership across the execution boundary.
- **Follow the Gradient:** identify synchronized or sharded learning state; for inference-only paths, state explicitly that no gradient exists.
- **Follow the Byte:** calculate persistent state, temporary buffers, transfers, and the relevant bandwidth tier.
- **Follow the Request:** include admission, scheduling, cancellation, failure, and externally visible latency.

## Lab and exit check

Run an open-loop load test that ramps beyond saturation. Report queue delay, TTFT, TPOT, completion, prompt/generated tokens per second, RPS, p50/p95/p99, errors, and cancellations. Kill one worker mid-test and show detection, routing removal, recovery, and user-visible impact.

Publish the offered-load trace as well as achieved throughput. Verify the accounting identity `offered = completed + rejected + cancelled + still in flight` over the test window, with retries represented explicitly rather than disappearing into client code.

## Primary references

- [OpenTelemetry specification](https://opentelemetry.io/docs/specs/), accessed 2026-09-19.
- [Kubernetes device plugins](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/), accessed 2026-09-19.
- [NVIDIA DCGM documentation](https://docs.nvidia.com/datacenter/dcgm/latest/), accessed 2026-09-19.
