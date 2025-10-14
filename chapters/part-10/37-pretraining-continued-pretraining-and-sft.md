# 37. Pretraining, Continued Pretraining and SFT

Status: **Drafted.**

Part 10: Post-Training and Reasoning

## Learning outcome

Specify a continued-pretraining and supervised fine-tuning pipeline with correct templates and loss masks.

## Prerequisites

CH-25 through CH-28 and CH-33 through CH-36.

<a id="t-37-01"></a>
## Pretraining vs post-training

Pretraining learns broad statistical structure, usually through next-token prediction over large heterogeneous corpora. Given tokens $x_1,\ldots,x_T$, the causal loss is

$$\mathcal L=-\sum_{t=1}^{T-1}\log p_\theta(x_{t+1}\mid x_{\le t}).$$

Every eligible position supplies a label. The resulting base model can complete text, but it has not necessarily learned the conversational contract “follow this user's instruction.” Post-training changes behavior using narrower data and objectives: supervised demonstrations, preferences, rewards, safety examples, or domain adaptation. These stages do not install a separate reasoning module; they modify the same parameters or attached modules.

Keep checkpoint names precise. “Base,” “continued pretrained,” “instruction tuned,” and “preference optimized” describe different distributions and should not be used interchangeably. Evaluate after each stage so later gains do not hide earlier regressions.

<a id="t-37-02"></a>
## Continued pretraining

Continued pretraining resumes the language-model objective on new material: a domain, language, recent period, or revised mixture. It is useful when vocabulary and knowledge distributions differ materially. It can also cause catastrophic forgetting or shift the model's style.

Use a conservative learning rate, mix some general replay data when retention matters, and compare domain and general validation loss. If the tokenizer poorly represents the new domain, adding tokens changes embedding and output matrices and requires careful initialization. Domain documents that contain instructions are still treated as sequences; continued pretraining does not automatically teach which spans are user requests versus answers.

Example: adapt a 7B base model to maintenance manuals. Pack complete document sections, mask padding, retain source boundaries, and monitor both manual perplexity and general benchmarks. If domain loss improves but instruction following later degrades, the problem may be mixture or stage ordering rather than insufficient capacity.

<a id="t-37-03"></a>
## Supervised fine-tuning

Supervised fine-tuning (SFT) trains on demonstrations of desired responses. A record may contain system instructions, user messages, assistant responses, and tool events. Teacher forcing supplies the correct previous tokens during training. The model learns response format and behavior patterns, but it can also memorize stylistic artifacts and errors.

Curate for correctness, coverage, and diversity. A small high-quality set can outperform a larger repetitive one. Mix multi-turn and refusal examples only in proportions justified by deployment. Monitor length: long answers contribute more token losses and can dominate unless examples or tokens are reweighted.

<a id="t-37-04"></a>
## Chat templates

A chat template serializes roles into tokens. A conceptual record might become:

```text
<bos><system>You are concise.<eot>
<user>What is 6*7?<eot>
<assistant>42<eot>
```

The exact tokens are tokenizer- and model-specific. Training and inference must use the same template, including beginning, end, tool, and generation-prompt tokens. Duplicating a BOS token or omitting the assistant marker changes conditioning. Treat templates as versioned model artifacts and test round-trip rendering.

<a id="t-37-05"></a>
## Loss masking

An attention mask controls what positions can be read; a loss mask controls which target positions contribute gradients. They solve different problems. For assistant-only SFT, system and user tokens remain visible as context but receive label `-100` (or equivalent) so cross-entropy ignores them. Assistant response tokens are labels.

For the sequence above, a simplified mask is:

```text
tokens: system... user... assistant: 4 2 <eot>
loss:      0...    0...            1 1   1
```

Mask padding and decide explicitly whether tool outputs, assistant headers, and end tokens are trained. An off-by-one shift can train the model to predict the first response token from the wrong prefix. Unit-test token IDs, rendered text, labels, and the count of supervised positions.

## Four recurring perspectives

- **Follow the Token:** source text becomes a chat serialization; context tokens may be visible while excluded from loss.
- **Follow the Gradient:** pretraining updates on nearly every non-padding target; assistant-only SFT updates only selected spans.
- **Follow the Byte:** full fine-tuning stores gradients and optimizer state for the entire model, often far beyond weight memory.
- **Follow the Request:** the exact deployed template determines whether learned role boundaries are reproduced.

## Lab and exit check

Render three multi-turn records with a pinned tokenizer. Print token IDs, roles, attention masks, and labels. Assert that only intended assistant spans contribute loss, including after truncation and packing. Draft a continued-pretraining mixture with general replay and define domain-retention gates.

## Exercises

1. A rendered example has 120 context tokens, 80 assistant tokens, and 10 padding tokens. Under assistant-only loss, how many targets may contribute before accounting for the one-token shift? **Check:** 80, provided the response and end-token policy define all 80 as supervised.
2. Explain why setting user-token labels to an ignore index must not also hide those tokens in the attention mask. **Check:** they provide conditioning context even though they do not directly contribute cross-entropy terms.

## References

- Ouyang et al., [Training Language Models to Follow Instructions with Human Feedback](https://arxiv.org/abs/2203.02155), 2022.
- Wei et al., [Finetuned Language Models Are Zero-Shot Learners](https://arxiv.org/abs/2109.01652), 2021.
- Hugging Face, [Chat templates documentation](https://huggingface.co/docs/transformers/chat_templating) (version-sensitive; accessed September 2026).
