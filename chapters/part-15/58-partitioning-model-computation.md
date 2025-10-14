# 58. Partitioning Model Computation

Status: **Drafted.**

Part 15: Distributed LLMs

## Learning outcome

Place a model across devices and derive communication on its critical path.

## Prerequisites

CH-20, CH-41, CH-57.

<a id="t-58-01"></a>
## Tensor parallelism

Coverage ID: `T-58-01`.

Tensor parallelism splits matrix operations. For (Y=XW), column-parallel execution partitions (W) along outputs; ranks compute slices of (Y). A following row-parallel layer can consume those slices and reduce partial outputs. Implementations pair layouts so some intermediates remain sharded.

If a full BF16 residual `[B,T,4096]` must be reduced, its logical payload is $B T 4096\times2$ bytes. At $B=8,T=2048$, that is 128 MiB before collective factors. This communication occurs inside blocks, so tensor parallelism favors fast intra-node links.

“Payload” is the logical tensor size, not bytes injected by each rank. A ring all-reduce communicates approximately $2(N-1)/N$ payload bytes per rank; with four tensor-parallel ranks, a 128 MiB residual implies about 192 MiB sent/received per rank under that model. Algorithm, chunking, topology, and overlap determine observed time.

<a id="t-58-02"></a>
## Pipeline parallelism

Coverage ID: `T-58-02`.

Pipeline parallelism assigns consecutive layer groups to stages. Microbatches flow between them. For (p) stages and (m) microbatches, simple forward-only utilization is approximately (m/(m+p-1)); too few microbatches create a bubble. Training interleaves forward and backward but retains or recomputes activations.

Stages exchange boundary activations. The slowest stage sets cadence. Equal parameter counts do not ensure balance when attention cost varies with sequence length or MoE routing is skewed.

<a id="t-58-03"></a>
## Sequence parallelism

Coverage ID: `T-58-03`.

Sequence parallelism shards suitable activation operations along the token dimension, often alongside tensor parallelism. Pointwise normalization and dropout can remain local, reducing replicated activations. Attention still requires global contextual information.

Label every tensor dimension replicated or sharded. A residual ([B,T,D]) split over (T) may need a transpose-like collective before an operation expecting (D)-shards. Confusing layout with semantics is a common bug.

<a id="t-58-04"></a>
## Context parallelism

Coverage ID: `T-58-04`.

Context parallelism divides a long sequence while preserving exact attention. Ranks exchange KV blocks or partial attention statistics so each query includes allowed context. Ring algorithms stream blocks and maintain online-softmax maxima and sums rather than materializing all scores centrally.

Splitting tokens alone produces a different model if cross-rank context is omitted. Cost depends on causal masking, head layout, context length, and measured link bandwidth.

<a id="t-58-05"></a>
## Expert parallelism

Coverage ID: `T-58-05`.

Expert parallelism places different MoE experts on different ranks. Routing is followed by all-to-all dispatch of token states, local expert MLPs, then all-to-all return. Traffic follows routed representations; balance follows router decisions.

A popular expert can overflow capacity or stall peers. Average GPU utilization hides the problem, so record per-expert token counts, dropped tokens, and all-to-all tail latency. Large systems compose data, tensor, pipeline, context, and expert axes; their degrees must multiply to world size and map sensibly onto topology.

## Four recurring perspectives

- **Follow the Token:** trace the representation and its ownership across the execution boundary.
- **Follow the Gradient:** identify synchronized or sharded learning state; for inference-only paths, state explicitly that no gradient exists.
- **Follow the Byte:** calculate persistent state, temporary buffers, transfers, and the relevant bandwidth tier.
- **Follow the Request:** include admission, scheduling, cancellation, failure, and externally visible latency.

## Lab and exit check

Place a 32-layer model on eight devices using two pipeline stages and four-way tensor parallelism. For $B=4,T=1024,D=4096$, a full BF16 boundary activation is 32 MiB. Calculate both that logical payload and per-rank ring traffic for the residual-sized tensor collective; identify which communication repeats each layer and which repeats at each stage boundary. Then state how microbatching changes boundary-message size and count without changing total logical examples.

## Primary references

- Shoeybi et al., [Megatron-LM](https://arxiv.org/abs/1909.08053), 2019.
- Huang et al., [GPipe](https://arxiv.org/abs/1811.06965), 2019.
- Lepikhin et al., [GShard](https://arxiv.org/abs/2006.16668), 2020.
