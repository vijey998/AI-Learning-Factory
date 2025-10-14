# 29. Transformer Families

Status: **Drafted — technical and editorial review pending.**

Part 8: Modern LLM Architecture

## Learning outcome

Compare masks and objectives across three Transformer families.

## Prerequisites

CH-28.

The Transformer is a component family, not one fixed model. Encoder-only, decoder-only, and encoder-decoder systems differ primarily in information flow and training objective. Those differences determine what can be cached, what can be generated, and which representation serves a downstream task.

<a id="t-29-01"></a>
### GPT to Llama-type architectures

Coverage ID: `T-29-01`.

Early GPT-style models established the decoder-only, causal, next-token recipe. Llama-type models retain that recipe while commonly replacing learned absolute positions with RoPE, LayerNorm with RMSNorm, GELU FFNs with SwiGLU, and in later variants full multi-head KV projections with grouped-query attention. These are concrete engineering choices, not a new Transformer family. Always read the pinned config: “Llama-like” is too vague to load weights or count memory.

<a id="t-29-02"></a>
### Decoder-only Transformers

Coverage ID: `T-29-02`.

A decoder-only stack uses causal self-attention. At position (t), Q comes from token (t), while K and V come from positions (0..t). Pretraining predicts (x_{t+1}). This alignment directly supports open-ended generation and KV-cached decode. It can also perform classification or extraction when cast as generation or by adding a task head.

<a id="t-29-03"></a>
### Encoder-only Transformers

Coverage ID: `T-29-03`.

Encoder self-attention is usually bidirectional: every non-padding token can attend to every other input token. This is ideal for contextual representations of a known sequence but cannot autoregressively generate without adding a causal decoder or iterative procedure. Padding masks hide absent tokens; they are distinct from causal masks.

<a id="t-29-04"></a>
### BERT

Coverage ID: `T-29-04`.

BERT pretrains an encoder by corrupting selected tokens and predicting them from bidirectional context, alongside the original next-sentence prediction objective. A `[CLS]` representation is often fed to task heads. Because masked tokens appear during pretraining but not ordinary use, masked-language modeling differs from left-to-right likelihood. Later encoders changed objectives, but the core BERT example makes the family distinction clear.

<a id="t-29-05"></a>
### Encoder-decoder Transformers

Coverage ID: `T-29-05`.

An encoder maps source IDs of length $S$ to $H_e\in\mathbb{R}^{B\times S\times D}$ using bidirectional attention. A causal decoder processes target prefix length $T$, alternating self-attention with cross-attention to $H_e$. This separates source understanding from target generation and naturally supports translation, summarization, and conditional generation.

<a id="t-29-06"></a>
### T5

Coverage ID: `T-29-06`.

T5 expresses tasks as text-to-text and pretrains with span corruption: contiguous spans are replaced by sentinel tokens, and the decoder generates the missing spans. Its original design uses relative position biases and an encoder-decoder stack. “T5” should not be reduced to ordinary token masking; sentinel-based span targets define its example construction.

<a id="t-29-07"></a>
### Cross-attention

Coverage ID: `T-29-07`.

For decoder state $X_d\in\mathbb{R}^{B\times T\times D}$ and encoder state $H_e\in\mathbb{R}^{B\times S\times D}$:

$$
Q=X_dW_Q,\quad K=H_eW_K,\quad V=H_eW_V,
$$
$$
\mathrm{CrossAttn}(X_d,H_e)=\mathrm{softmax}(QK^\top/\sqrt{d_h})V.
$$

Scores have shape ([B,H,T,S]). The decoder’s causal mask applies to decoder self-attention, not ordinarily across the source; a source padding mask still applies. During autoregressive decode, encoder K/V can be computed once and reused.

## Comparison

| Family | Self-attention visibility | Common objective | Native output |
|---|---|---|---|
| Encoder-only | bidirectional | corruption/masked token | representations |
| Decoder-only | causal | next token | continuation |
| Encoder-decoder | encoder bidirectional; decoder causal | conditional/span generation | source-conditioned sequence |

## Four recurring perspectives

- **Follow the Token:** visibility masks determine which surrounding tokens can shape each representation.
- **Follow the Gradient:** objectives supervise corrupted tokens, next tokens, or conditional targets differently.
- **Follow the Byte:** encoder-decoder models store source states and cross-attention K/V in addition to decoder state.
- **Follow the Request:** classification may use one encoder pass; decoder generation repeats sequential decode; source encoding is reusable.

## Lab and exit check

For a four-token source and three-token target, draw all permitted entries in encoder self-attention, decoder self-attention, and cross-attention masks. State which K/V tensors can be cached during generation and why. Compare the labels produced by BERT masking, GPT shifting, and T5 span corruption on one sentence.

## Exercises

1. Give the materialized score shapes for encoder self-attention, decoder self-attention, and cross-attention with $B=2,H=8,S=5,T=3$. **Check:** `[2,8,5,5]`, `[2,8,3,3]`, and `[2,8,3,5]`.
2. Explain why the decoder's cross-attention keys and values can be reused across generated positions but its self-attention cache grows. **Check:** the encoded source is fixed, whereas each emitted target token adds a new decoder key and value.

## References

- Devlin et al., [BERT](https://arxiv.org/abs/1810.04805), 2018.
- Raffel et al., [Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer](https://jmlr.org/papers/v21/20-074.html), 2019.
- Touvron et al., [LLaMA](https://arxiv.org/abs/2302.13971), 2023.
