# 24. Build Our GPT From Scratch

Status: **Drafted — executable lab included; technical and editorial review pending.**

Part 6: Build a Transformer

## Learning outcome

Assemble a runnable tiny GPT with no pretrained-model wrapper.

## Prerequisites

CH-23.

This milestone joins the mechanisms already derived. “From scratch” means we use tensor primitives and ordinary neural-network modules rather than loading a pretrained Transformer or delegating the architecture to a model wrapper. Autograd may still compute derivatives.

<a id="t-24-01"></a>
### GPT implementation

Coverage ID: `T-24-01`.

A minimal GPT contains token and position representations, $L$ decoder blocks, a final norm, and an LM head. The reference implementation is `code/tiny_gpt_core.py`. Its attention explicitly forms Q, K, and V, applies a causal mask, merges heads, and projects the result. This favors inspectability over kernel efficiency.

```python
x = token_embedding(ids) + position_embedding(position_ids)
for block in blocks:
    x = block(x)
logits = lm_head(final_norm(x))
```

<a id="t-24-02"></a>
### Decoder-only model assembly

Coverage ID: `T-24-02`.

Decoder-only means every position attends only to itself and earlier positions, and the model predicts the next token at every training position. For IDs $I\in\mathbb{N}^{B\times T}$: embeddings are $[B,T,D]$; Q/K/V are $[B,H,T,d_h]$; attention scores are $[B,H,T,T]$; logits are $[B,T,V]$. The causal invariant is: changing input position $j>i$ cannot change logits at position $i$ in evaluation mode.

<a id="t-24-03"></a>
### Model configuration

Coverage ID: `T-24-03`.

Configuration is an architectural contract:

```text
vocab_size V       context_length C
width D             layers L
attention_heads H   intermediate_width M
normalization       activation/gating
position method     dropout/bias/tie_embeddings
```

Require $D\bmod H=0$, input $T\le C$, IDs in `[0,V)`, and valid padding/mask semantics. A tiny example uses $V=64,C=32,D=48,L=2,H=4,M=128$. Its small size supports CPU tests; it says nothing about large-model quality.

<a id="t-24-04"></a>
### Forward-pass invariants

Coverage ID: `T-24-04`.

The implementation should enforce:

1. output shape is `[B,T,V]`;
2. residual shape stays `[B,T,D]`;
3. all probabilities are finite after softmax;
4. causal isolation holds in `eval()` mode;
5. tied weights share storage when enabled;
6. loss uses logits at positions `0..T-2` against IDs at `1..T-1`;
7. inputs exceeding context length fail loudly.

A causality test runs two inputs that share a prefix but differ later. Their logits through the last shared prediction position must match within floating-point tolerance. Dropout must be disabled, otherwise randomness can imitate a causality failure.

## Parameter and compute sanity check

Ignoring biases, learned positions, and norms, standard MHA plus SwiGLU contributes per layer approximately $4D^2+3DM$ weights. Embedding/head contribute $VD$ when tied or $2VD$ when untied. A rough dense forward estimate is about two FLOPs per weight used per token plus attention score/value work; it is a reasoning estimate, not a measured runtime.

## Four recurring perspectives

- **Follow the Token:** ID → embedding → residual updates → vocabulary logits → next ID.
- **Follow the Gradient:** cross-entropy sends error through the head, every block, and the embedding table.
- **Follow the Byte:** parameters persist; activations and attention matrices scale with batch and context.
- **Follow the Request:** prompt tokens run together in prefill; generated tokens later run one step at a time with cached state.

## Lab and exit check

Run `python code/tiny_gpt_core.py`. Confirm shape, finite logits, parameter count, tied storage, and causal isolation. Then deliberately remove the causal mask and observe the isolation test fail. Explain why passing a shape test alone cannot establish correctness.

## Exercises

1. For the tiny configuration $V=64,C=32,D=48,L=2,H=4,M=128$, state the shapes of Q, attention scores, and logits for $B=3,T=20$. **Check:** `[3,4,20,12]`, `[3,4,20,20]`, and `[3,20,64]`.
2. Design a causality test in which two inputs share positions 0 through 5 and differ afterward. Specify exactly which logits must agree. **Check:** in evaluation mode, logits at positions 0 through 5 agree within numerical tolerance.

## References

- Radford et al., [Improving Language Understanding by Generative Pre-Training](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf), 2018.
- Vaswani et al., [Attention Is All You Need](https://arxiv.org/abs/1706.03762), 2017.
- PyTorch documentation for `nn.Module`, pinned by the environment record for executable results.
