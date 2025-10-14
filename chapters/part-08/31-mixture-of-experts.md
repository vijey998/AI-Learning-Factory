# 31. Mixture of Experts

Status: **Drafted — technical and editorial review pending.**

Part 8: Modern LLM Architecture

## Learning outcome

Simulate top-k routing and measure imbalance and token overflow.

## Prerequisites

CH-30.

A mixture-of-experts layer replaces one dense MLP with many candidate MLPs and activates only a small subset per token. It expands parameter capacity without using every parameter on every token, while creating routing, communication, and reliability problems.

<a id="t-31-01"></a>
### MoE

Coverage ID: `T-31-01`.

For token state $x\in\mathbb{R}^D$, a router emits expert logits $r=xW_r\in\mathbb{R}^E$. After softmax and top-$k$ selection $\mathcal T(x)$,

$$
y=\sum_{e\in\mathcal T(x)}g_e(x)\,\mathrm{Expert}_e(x).
$$

Experts are typically MLPs with separate parameters. Attention may remain dense. “A trillion-parameter MoE” therefore does not execute a trillion parameters per token, though all weights must be stored or distributed.

<a id="t-31-02"></a>
### Sparse activation

Coverage ID: `T-31-02`.

With $E=64,k=2$, only two experts process each token. Active expert compute scales with $k$, while parameter storage scales with $E$. Router work, dispatch, gathering, and communication remain. Sparse activation means conditional computation, not sparse weight matrices.

<a id="t-31-03"></a>
### Expert routing

Coverage ID: `T-31-03`.

Routing turns a flat set of $N=BT$ token vectors into per-expert buffers. Stable implementations track original token indices, selected expert, gate weight, and rank. After expert computation, outputs are weighted and scattered back. Top-k is discrete; training uses gradients through selected gate weights and auxiliary mechanisms, not ordinary gradients through the selection boundary.

A router can collapse, sending most tokens to a few experts. Small input or numerical changes near a top-k boundary may change dispatch abruptly.

<a id="t-31-04"></a>
### Capacity

Coverage ID: `T-31-04`.

A common capacity per expert is

$$
C=\left\lceil \text{capacity factor}\cdot\frac{Nk}{E}\right\rceil.
$$

For $N=1024,E=8,k=2$, balanced load is 256 assignments per expert. With factor 1.25, $C=320$. Assignments above capacity must be dropped, rerouted, or handled by overflow logic. Each choice changes output and cost. Capacity computed per device or microbatch can behave differently at small batch sizes.

<a id="t-31-05"></a>
### Load balancing

Coverage ID: `T-31-05`.

Measure assignment counts, gate-probability mass, maximum-to-mean load, coefficient of variation, entropy, and overflow. Equal counts are not the sole goal: experts should specialize without stranding capacity. Batch composition affects observed balance, so report distributions across steps rather than one average.

<a id="t-31-06"></a>
### Router losses

Coverage ID: `T-31-06`.

Auxiliary losses encourage balanced probability and assignment. One family penalizes correlation between fraction of assignments $f_e$ and mean router probability $p_e$, scaled by $E\sum_e f_ep_e$. Exact definitions differ by model. Too weak allows collapse; too strong can prioritize uniformity over task loss. Router z-losses may penalize large log-sum-exp values to stabilize logits.

<a id="t-31-07"></a>
### Expert parallelism introduction

Coverage ID: `T-31-07`.

When experts live on different devices, tokens travel to their selected experts and outputs return, commonly through all-to-all collectives. Compute may be sparse while network traffic is dense and irregular. Placement, topology, token balance, and capacity determine utilization. Expert parallelism will be developed in Part XV; here the key point is that routing becomes a distributed systems operation.

## Four recurring perspectives

- **Follow the Token:** router logits choose expert destinations; outputs are gathered back into the original sequence order.
- **Follow the Gradient:** task loss trains chosen experts and gates; auxiliary loss shapes routing statistics.
- **Follow the Byte:** all expert weights consume storage, while only selected weights and activations execute; distributed dispatch moves token vectors.
- **Follow the Request:** small or decode batches can underutilize experts and make communication dominate latency.

## Lab and exit check

Simulate (N=1000,E=8,k=2) routing with biased logits. Compute capacity, assignment histogram, coefficient of variation, entropy, and overflow for factors 1.0 and 1.25. Compare dropping versus rerouting and name the resulting semantic difference. Repeat with a small decode batch and explain utilization.

## Exercises

1. For $N=1000,E=8,k=2$, calculate per-expert capacity at factors 1.0 and 1.25. **Check:** 250 and 313 after applying the ceiling.
2. One expert receives 340 assignments when capacity is 313. How many assignments overflow, and why is the token-drop rate not determined until the routing ranks are inspected? **Check:** 27 assignments overflow; a token may lose one of two routes or all routes depending on which assignments are dropped.

## References

- Shazeer et al., [Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer](https://arxiv.org/abs/1701.06538), 2017.
- Fedus, Zoph, and Shazeer, [Switch Transformers](https://jmlr.org/papers/v23/21-0998.html), 2021.
- Lepikhin et al., [GShard](https://arxiv.org/abs/2006.16668), 2020.
