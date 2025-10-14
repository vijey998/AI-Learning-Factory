# 61. Anatomy of an Inference Server

Status: **Drafted.**

Part 16: Serving LLMs as a System

## Learning outcome

Build a tiny continuous-batching server with cancellation and cleanup.

## Prerequisites

CH-60.

<a id="t-61-01"></a>
## Inference server architecture

Coverage ID: `T-61-01`.

An inference server is a state machine around a model runtime. A front end authenticates and validates; an admission controller checks capacity; a scheduler forms work; a model worker executes prefill and decode; a sampler chooses tokens; a streamer emits them; cleanup releases KV blocks. Tokenization may run in a CPU pool. Every boundary needs an owner and timeout.

The model is only one component. A fast kernel cannot rescue a queue overloaded by unbounded prompts, and a disconnected client must not leave an orphan sequence consuming KV memory.

<a id="t-61-02"></a>
## HTTP requests

Coverage ID: `T-61-02`.

An HTTP request carries prompt or messages, generation limits, sampling options, model/adapters, and streaming preference. Validate maximum input, output, and combined token budgets after tokenization. Idempotency is nuanced: deterministic greedy generation may be replayable, while sampled output is not identical unless RNG state and scheduling semantics are fixed.

Return overload explicitly, typically with retry guidance, rather than accepting work into an infinite queue. Authentication and tenant quotas should run before expensive tokenization where possible.

<a id="t-61-03"></a>
## Request queues

Coverage ID: `T-61-03`.

One FIFO hides distinct resource demands. Separate or classify long prefills, decodes, priority traffic, and administrative work. Queue delay equals start time minus admission time and must be measured independently from compute. Aging can prevent starvation; deadlines can reject requests that cannot meet useful service time.

A queue capacity should derive from memory and latency budgets. Length alone is insufficient: ten 100-token requests and ten 100,000-token requests are radically different liabilities.

Use token work, not request count, for a first overload check. If admitted work arrives at 12,000 token-equivalents/s while the pinned configuration sustains 10,000, no scheduling policy can make the queue stable. Little's law, $N=\lambda W$, is also a useful consistency check: at 20 admitted requests/s and 0.5 s mean time in system, about ten requests should be present on average. A large mismatch often exposes dropped measurements, retries, or work waiting outside the instrumented queue.

<a id="t-61-04"></a>
## Scheduling

Coverage ID: `T-61-04`.

The scheduler chooses which sequences prefill or decode each iteration under token and KV budgets. Decode usually advances one token per active sequence; prefill can consume thousands. Chunked prefill limits monopolization by dividing a long prompt across iterations.

Fairness has a cost. Strict shortest-job-first improves average latency but can starve long contexts. Weighted fair scheduling can protect tenants. Record the policy because benchmark results are inseparable from it.

<a id="t-61-05"></a>
## Dynamic batching

Coverage ID: `T-61-05`.

Dynamic batching waits briefly to combine compatible work. Continuous batching goes further: finished sequences leave and waiting sequences enter between decode iterations. Padding is reduced because sequences need not start and finish together.

Larger batches improve device utilization but raise queue delay and KV pressure. The optimum depends on prompt/output distributions, not a fixed magic size. Evaluate TTFT and inter-token latency alongside aggregate tokens per second.

<a id="t-61-06"></a>
## KV allocation

Coverage ID: `T-61-06`.

Each live sequence needs per-layer key/value state. Paged allocation maps logical token blocks to noncontiguous physical blocks, reducing external fragmentation and enabling sharing. Admission must reserve enough blocks for current tokens and planned growth or deliberately support preemption.

Cancellation must decrement references for shared prefix blocks and free private blocks exactly once. Memory leaks appear as declining admission capacity over time; double-free appears as corrupted generations.

<a id="t-61-07"></a>
## Streaming

Coverage ID: `T-61-07`.

Streaming sends tokens or text deltas as generation proceeds. Byte-pair tokens do not always decode to valid standalone Unicode, so the streamer needs incremental detokenization. Network backpressure must not block the model loop; use bounded per-client buffers and cancel or disconnect slow consumers by policy.

A client disconnect should propagate cancellation to the scheduler, sampler, and KV allocator. Define whether already-generated usage is billed and logged.

## Four recurring perspectives

- **Follow the Token:** trace the representation and its ownership across the execution boundary.
- **Follow the Gradient:** identify synchronized or sharded learning state; for inference-only paths, state explicitly that no gradient exists.
- **Follow the Byte:** calculate persistent state, temporary buffers, transfers, and the relevant bandwidth tier.
- **Follow the Request:** include admission, scheduling, cancellation, failure, and externally visible latency.

## Lab and exit check

Implement a CPU simulator with arrival times, prompt lengths, output limits, a token-budget scheduler, paged KV counter, cancellation, and bounded stream queues. Assert that all pages return after every request completes or cancels. Compare FIFO and continuous batching using TTFT and completion time.

Exit questions: under overload, where is admission rejected; after a disconnect, which component owns final KV release; and can every accepted request reach exactly one terminal state (`completed`, `cancelled`, or `failed`)?

## Primary references

- [vLLM architecture documentation](https://docs.vllm.ai/en/latest/design/arch_overview.html), accessed 2026-09-19.
- Kwon et al., [Efficient Memory Management for LLM Serving with PagedAttention](https://arxiv.org/abs/2309.06180), 2023.
