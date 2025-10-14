# 49. Load Weights and Trace a Forward Pass

Status: **Drafted**

## Goal and notation

We trace a decoder-only model with batch B, sequence T, width D, query heads H, KV heads Hkv, head width Dh=D/H, layers L, vocabulary V, and MLP width F.

<a id="t-49-01"></a>
## Loading model weights

A checkpoint is more than a bag of numbers. Configuration defines architecture and shapes; tokenizer files define the token-ID contract; parameter names map stored tensors to modules; dtype and sharding determine bytes and placement. Load metadata before allocating, validate model revision and tensor shapes, and use a format that avoids executing untrusted code.

A rough weight budget is parameter count times stored bytes. Seven billion BF16 parameters require about 14 decimal GB before allocator, runtime, KV, activations, and temporary workspaces. Quantized storage can reduce capacity requirements, but kernels may unpack or dequantize values during execution.

<a id="t-49-02"></a>
## Prompt processing

Text becomes IDs [B,T]. Embedding lookup produces X [B,T,D]. Each layer normalizes X, forms Q [B,H,T,Dh], K and V [B,Hkv,T,Dh], applies position encoding, performs causal attention, projects back to [B,T,D], and applies an MLP through [B,T,F]. Residual additions preserve the [B,T,D] stream. Final normalization and the LM head produce logits [B,T,V]. Generation normally needs only logits at the final valid position.

Padding needs an attention mask and correct position IDs. Left- versus right-padding changes indexing. A trace should record shape, dtype, device, stride, and live byte size at module boundaries, not print tensor contents.

<a id="t-49-03"></a>
## GPU inference

Inference disables gradient recording and uses evaluation behavior. Parameters reside on the chosen device; inputs must follow. Automatic mixed precision, fused attention, compiler modes, and tensor parallelism alter execution without changing the model contract. Host-to-device copies, lazy library initialization, compilation, and first allocation belong to cold startup, not steady forward latency.

GPU execution is asynchronous. Moving a scalar to Python, printing a CUDA tensor, or calling certain convenience APIs can force synchronization. Profile the complete request before “optimizing” a kernel.

<a id="t-49-04"></a>
## End-to-end real-model forward-pass tracing

Use hooks or an exported graph on a pinned, small open model. Record:

| Boundary | Shape |
|---|---|
| IDs | [B,T] |
| embedding/residual | [B,T,D] |
| Q | [B,H,T,Dh] |
| K,V | [B,Hkv,T,Dh] |
| attention result | [B,H,T,Dh] |
| MLP expansion | [B,T,F] |
| logits | [B,T,V] |

For B=2,T=128,D=4096 in BF16, one residual tensor is 2 MiB. Logits with V=128,000 occupy 62.5 MiB if all positions are materialized, showing why last-token-only paths matter during decode. Temporary memory can exceed boundary tensors because attention, GEMM, and compiler workspaces live inside operators.

Check the units directly: the residual contains $2\times128\times4096=1{,}048{,}576$ elements, or 2,097,152 bytes. The logits contain 32,768,000 elements, or 65,536,000 bytes. Reporting both element count and bytes catches accidental FP32 promotion and confusion between MB and MiB.

Verify the trace by checking parameter count against the config, confirming every layer preserves residual shape, and comparing final logits with a trusted eager run. Hooks can inhibit compilation or alter lifetimes, so profile uninstrumented execution separately.

## Four perspectives and debugging

- **Follow the Token:** an ID selects an embedding, traverses L residual updates, and becomes V logits.
- **Follow the Gradient:** inference creates no autograd state; accidental grad tracking wastes memory.
- **Follow the Byte:** weights dominate residency, while activations and logits scale with B and T.
- **Follow the Request:** loading is a lifecycle cost; tokenization and transfer precede prefill.

Failures include tokenizer/model mismatch, wrong transposition, silent dtype conversion, missing eval mode, invalid positions, and comparing revisions. The exit check is a table of all boundary shapes and strides, calculated live bytes for at least residual and logits, and a numerical equality check against untraced eager output.

## Primary references

- PyTorch, [`inference_mode`](https://docs.pytorch.org/docs/stable/generated/torch.autograd.grad_mode.inference_mode.html), version-sensitive; accessed 2026-09-19.
- Hugging Face, [Transformers model documentation](https://huggingface.co/docs/transformers/main/en/models), version-sensitive; accessed 2026-09-19.
- Hugging Face, [Transformers model loading](https://huggingface.co/docs/transformers/main/en/models#loading-models), version-sensitive; accessed 2026-09-19. Pin framework versions, model commit, tokenizer commit, dtype, attention backend, and hardware.
