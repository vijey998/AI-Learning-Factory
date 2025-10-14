# 38. Parameter-Efficient Adaptation

Status: **Drafted.**

Part 10: Post-Training and Reasoning

## Learning outcome

Choose an adaptation method and count its trainable parameters, persistent storage, and optimizer memory.

## Prerequisites

CH-27 and CH-37.

<a id="t-38-01"></a>
## PEFT

Parameter-efficient fine-tuning (PEFT) freezes most base parameters and trains a small set of new or selected parameters. It reduces optimizer and gradient memory, enables many task variants to share one base checkpoint, and can simplify distribution. It does not eliminate forward/backward activation memory, and quality depends on where and how capacity is inserted.

Compare methods by trainable count, inference overhead, mergeability, task-switching cost, and quality. “One percent trainable” does not mean one percent of total training memory or compute.

<a id="t-38-02"></a>
## Adapters

A bottleneck adapter adds a residual module such as

$$h' = h + W_{up}\,\sigma(W_{down}h),$$

where $W_{down}\in\mathbb R^{r\times d}$ and $W_{up}\in\mathbb R^{d\times r}$. Ignoring biases, one adapter has $2dr$ trainable parameters. For $d=4096$, $r=64$, that is 524,288 parameters per insertion point. Adapters add inference operations unless folded into an equivalent linear transform, which nonlinear bottleneck adapters generally cannot be.

<a id="t-38-03"></a>
## Prompt tuning

Prompt tuning learns $m$ virtual embedding vectors of dimension $d$ prepended to the input. It trains $md$ parameters: 20 virtual tokens at $d=4096$ require 81,920. The base model stays frozen. Virtual tokens consume context positions and participate in attention. Prompt tuning can work well at sufficient model scale but provides limited capacity for large behavioral shifts.

<a id="t-38-04"></a>
## Prefix tuning

Prefix tuning learns continuous key/value-like states for multiple layers rather than only input embeddings. It influences attention at each adapted layer but increases KV memory and per-request prefix processing or storage. Implementations differ: some directly learn prefixes; others use a small network to generate them. State the parameterization before counting.

<a id="t-38-05"></a>
## LoRA

Low-Rank Adaptation represents a weight update as

$$W' = W + \frac{\alpha}{r}BA,$$

with frozen $W\in\mathbb R^{d_{out}\times d_{in}}$, $A\in\mathbb R^{r\times d_{in}}$, and $B\in\mathbb R^{d_{out}\times r}$. Trainable count is $r(d_{in}+d_{out})$. For a 4096-by-4096 projection with $r=16$, that is 131,072 parameters versus 16,777,216 in $W$—0.78125%.

LoRA can target attention, MLP, or other projections. Rank, targets, scaling, dropout, and initialization matter. At inference, a LoRA update can often be merged into weights; hot-swapping many adapters may instead use separate kernels. Combining adapters by adding deltas is not guaranteed to preserve either behavior.

<a id="t-38-06"></a>
## QLoRA

QLoRA stores the frozen base in a low-bit quantized representation while backpropagating into LoRA parameters. Its original formulation used 4-bit NormalFloat, double quantization, and paged optimizers. Computation still dequantizes blocks into a compute dtype; it is not “training in four-bit arithmetic.” Adapter weights and optimizer states use higher precision.

Quantization saves base-weight memory, but activations, temporary dequantized tiles, gradients for adapters, and optimizer state remain. Hardware kernels determine speed; smaller storage can even be slower if dequantization is inefficient. Validate final quality and peak allocated memory on the exact stack.

## Memory worked example

For 100M trainable parameters with AdamW, FP32 parameters, gradients, and two optimizer moments can approach 16 bytes per parameter, or 1.6 GB, before activations. A LoRA configuration with 1M trainable BF16 parameters and FP32 moments uses roughly 2 MB weights + 2 MB gradients + 8 MB moments = 12 MB, though framework copies and master weights may add more. Measure, do not infer from trainable count alone.

## Four recurring perspectives

- **Follow the Token:** prompt and prefix methods alter the states seen by every token; LoRA changes projections applied to them.
- **Follow the Gradient:** gradients stop at frozen weights but flow through the frozen computation into trainable modules.
- **Follow the Byte:** optimizer savings can be dramatic; activations and frozen-weight reads remain.
- **Follow the Request:** adapter selection becomes serving state, affecting batching, cache identity, and latency.

## Lab and exit check

Adapt one linear layer with LoRA, verify the count $r(d_{in}+d_{out})$, and compare outputs before and after merging. Train on a tiny mapping, log trainable bytes and peak memory, then reload base plus adapter and reproduce output. Explain what must be invalidated in a prefix cache when the adapter changes.

## Exercises

1. Apply rank-8 LoRA to Q and V projections in each of 32 layers with $d_{in}=d_{out}=4096$. Compute the trainable count. **Check:** $32\times2\times8\times(4096+4096)=4{,}194{,}304$.
2. State which listed methods consume additional sequence or cache capacity at inference. **Check:** prompt tuning consumes input positions; prefix tuning consumes per-layer attention-prefix/KV capacity; merged LoRA need not add sequence length or a separate matmul.

## References

- Houlsby et al., [Parameter-Efficient Transfer Learning for NLP](https://arxiv.org/abs/1902.00751), 2019.
- Li and Liang, [Prefix-Tuning](https://arxiv.org/abs/2101.00190), 2021.
- Hu et al., [LoRA](https://arxiv.org/abs/2106.09685), 2021.
- Dettmers et al., [QLoRA](https://arxiv.org/abs/2305.14314), 2023.
