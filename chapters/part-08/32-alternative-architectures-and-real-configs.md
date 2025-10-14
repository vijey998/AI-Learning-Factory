# 32. Alternative Architectures and Real Configs

Status: **Drafted — technical and editorial review pending.**

Part 8: Modern LLM Architecture

## Learning outcome

Read a pinned model config and independently estimate its cost.

## Prerequisites

CH-31.

Quadratic full attention is powerful but not mandatory. This chapter surveys structured attention, recurrent/state-space mechanisms, and hybrids, then turns a real configuration into parameter, memory, and compute estimates.

<a id="t-32-01"></a>
### Sparse attention

Coverage ID: `T-32-01`.

Sparse attention restricts the $T\times T$ score pattern. If each query attends to $w\ll T$ keys, score work and storage can approach $O(Tw)$ rather than $O(T^2)$. The actual speedup requires kernels and layouts that exploit the pattern; storing a dense matrix with many masked entries saves nothing.

<a id="t-32-02"></a>
### Sliding-window attention

Coverage ID: `T-32-02`.

A causal sliding window lets position $t$ attend to positions $\max(0,t-w+1),\ldots,t$. Per-layer receptive field is limited, but stacking layers lets information propagate farther. KV eviction becomes possible for layers using only the window. The model cannot directly retrieve an arbitrarily old token through that layer.

<a id="t-32-03"></a>
### Local attention

Coverage ID: `T-32-03`.

Local attention is the broader idea of neighborhood-limited connectivity and may be causal or bidirectional, one-dimensional or blocked. Boundary handling and dilation define which positions interact. It offers locality and regularity but can miss long-range dependencies.

<a id="t-32-04"></a>
### Global attention

Coverage ID: `T-32-04`.

Selected global tokens or periodic full-attention layers create long-range routes. A pattern combining local windows with $g$ global positions costs roughly $O(T(w+g))$. Which tokens become global is a modeling decision; excessive global connectivity restores quadratic cost.

<a id="t-32-05"></a>
### State-space models

Coverage ID: `T-32-05`.

A state-space model updates a fixed-size state recurrently,

$$
h_t=\bar A h_{t-1}+\bar Bx_t,\qquad y_t=Ch_t+Dx_t,
$$

with modern variants making parts input-dependent and implementing training with parallel scans or convolutions. Recurrence gives linear sequence scaling and constant-size inference state with respect to context length, but the state compresses history rather than retaining every K/V vector for direct lookup.

<a id="t-32-06"></a>
### Recurrent hybrids

Coverage ID: `T-32-06`.

Recurrent hybrids add gating, convolution, attention, or recurrent state to balance retrieval and efficient streaming. “Recurrent” describes sequential state evolution at inference; training may still use parallel algorithms. Evaluate quality, state size, kernel maturity, and latency rather than assuming asymptotic complexity predicts performance.

<a id="t-32-07"></a>
### Hybrid models

Coverage ID: `T-32-07`.

A hybrid can interleave attention and state-space layers or combine local and global mechanisms. Attention layers provide content-addressable access; recurrent layers process long streams cheaply. The optimal ratio depends on tasks and hardware. Interfaces still carry ([B,T,D]) tensors, making composition easy at the shape level, though training dynamics remain architecture-specific.

<a id="t-32-08"></a>
### Reading a real model config

Coverage ID: `T-32-08`.

Pin the exact configuration file or release. Extract (V,D,L,H,H_{kv},M,C), norm type, positional settings, tying, biases, and architecture class. As a worked configuration, use the published Llama 2 7B architecture values: (D=4096,L=32,H=32,H_{kv}=32,M=11008,V=32000). Treat the following as estimates; implementation details such as biases and tying must be checked against the pinned artifact.

<a id="t-32-09"></a>
### Parameters

Coverage ID: `T-32-09`.

Per layer, standard attention has approximately $4D^2=67.11$ million weights. SwiGLU has $3DM\approx135.27$ million. Together that is about 202.38 million; across 32 layers, 6.476 billion. Add embeddings/head and norms to approach the advertised scale. Advertised names are rounded, so derive from tensors when exactness matters.

<a id="t-32-10"></a>
### Attention dimensions

Coverage ID: `T-32-10`.

Head dimension is $d_h=D/H=128$. Q/K/V under MHA each project to 4096 values per token. Score shape for batch $B$ and context $T$ is `[B,32,T,T]` when materialized, motivating IO-aware kernels.

<a id="t-32-11"></a>
### KV heads

Coverage ID: `T-32-11`.

Here $H_{kv}=32$, so this configuration uses MHA. A config with GQA would replace K/V projection output width $D$ with $H_{kv}d_h$. Never infer KV heads from query-head count.

<a id="t-32-12"></a>
### MLP size

Coverage ID: `T-32-12`.

The intermediate width 11008 gives expansion $11008/4096\approx2.6875$. Because SwiGLU has three matrices, this is close in parameter count to a two-matrix 4× FFN.

<a id="t-32-13"></a>
### Memory footprint

Coverage ID: `T-32-13`.

Seven billion parameters require roughly 14 GB at two bytes each, 28 GB at four bytes, before allocator metadata, activations, KV cache, temporary workspaces, or framework overhead. Decimal GB and binary GiB differ. Quantized files also include scales and metadata, so “4-bit” does not imply exactly 0.5 byte per parameter in memory.

For MHA, BF16 KV cache per token is $L\times2\times H_{kv}\times d_h\times2$ bytes: $32\times2\times32\times128\times2=524{,}288$ bytes per token across layers, about 512 KiB, before batching and overhead.

<a id="t-32-14"></a>
### FLOPs per token

Coverage ID: `T-32-14`.

A common dense-model estimate is roughly two FLOPs per active weight per token for the matrix multiplies, about 14 GFLOPs/token for 7B active parameters, plus attention terms and other operations. During training, forward plus backward is often estimated near six FLOPs per parameter-token, but activation recomputation and implementation details change it. During prefill, attention adds terms growing with context; decode rereads weights and attends over cached positions. Always state whether the estimate is training, prefill, or decode.

## Four recurring perspectives

- **Follow the Token:** sparse attention restricts explicit history; state-space recurrence compresses history; hybrids combine both.
- **Follow the Gradient:** parallel scans and sparse patterns change backward execution even when layer interfaces match.
- **Follow the Byte:** configuration fields determine weight and state/KV storage; asymptotic savings require supporting kernels.
- **Follow the Request:** prefill and streaming decode stress different mechanisms, so architecture comparisons require matched workloads and quality.

## Lab and exit check

Download or record one exact official config revision, then compute (d_h), attention/MLP parameters, weight bytes by dtype, and KV bytes for (B=1,T=4096). Compare your sum with framework tensor counts and explain every discrepancy. For one sparse or state-space alternative, name information it cannot access as directly as full attention.

## Exercises

1. Using the Llama 2 7B values in this chapter, compute BF16 KV storage at $B=1,T=4096$. **Check:** $524{,}288\times4096=2{,}147{,}483{,}648$ bytes, exactly 2 GiB before overhead.
2. A causal window has $w=512$ and $L=24$ layers. Give an upper bound on how far information can propagate through stacked local-attention layers and state why this is not equivalent to one-layer direct retrieval. **Check:** roughly $L(w-1)=12{,}264$ positions through successive hops, subject to boundary and implementation details.

## References

- Beltagy, Peters, and Cohan, [Longformer](https://arxiv.org/abs/2004.05150), 2020.
- Gu and Dao, [Mamba: Linear-Time Sequence Modeling with Selective State Spaces](https://arxiv.org/abs/2312.00752), 2023.
- Touvron et al., [Llama 2](https://arxiv.org/abs/2307.09288), 2023.
