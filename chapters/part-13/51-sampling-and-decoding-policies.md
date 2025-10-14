# 51. Sampling and Decoding Policies

Status: **Drafted**

## From logits to a sequence

The model produces logits z in R^V. A decoding policy transforms or searches these scores. Keep two ideas separate: temperature/top-k/top-p change the next-token distribution; beam search maintains multiple sequence hypotheses.

<a id="t-51-01"></a>
## Sampling

Stable probabilities are $p_i=\exp(z_i-m)/\sum_j\exp(z_j-m)$, where $m=\max(z)$. A categorical draw uses an explicit random generator and seed for reproducibility. Sampling is conditional at every step, so one early choice changes all later logits. Report prompts, seed, tokenizer, policy, and model revision.

<a id="t-51-02"></a>
## Greedy decoding

Greedy chooses argmax z. It is deterministic given deterministic logits and tie handling, cheap, and useful for correctness tests. It does not maximize whole-sequence probability: the locally best token can lead to a worse continuation. Repetition and bland outputs are common failure modes.

<a id="t-51-03"></a>
## Temperature

Temperature tau>0 computes softmax(z/tau). Tau below one sharpens differences; above one flattens them. As tau approaches zero, behavior approaches argmax, so implementations should switch to greedy rather than divide by zero. Temperature must precede truncation when defining a policy precisely.

Example logits [2,1,0] have probabilities approximately [0.665,0.245,0.090] at tau=1 and [0.867,0.117,0.016] at tau=0.5.

<a id="t-51-04"></a>
## Top-k

Keep the k largest logits, set the rest to negative infinity, renormalize, then sample. It fixes candidate count regardless of uncertainty. k=1 equals greedy; k larger than V changes nothing. Ties and a minimum number of retained tokens need explicit behavior.

<a id="t-51-05"></a>
## Top-p

Sort probabilities descending and keep the smallest prefix whose cumulative mass reaches p, usually retaining at least one token. The candidate count adapts: peaked distributions keep few; flat ones keep many. Implementations differ over whether the threshold-crossing token is included; document it. Filtering on logits without first computing normalized probability mass is wrong.

<a id="t-51-06"></a>
## Beam search

Beam search maintains K partial sequences ranked by cumulative log probability, expands candidates, and retains the best. Raw sums favor short sequences because log probabilities are negative, so length penalties or normalized scores are common. Beam search suits tasks with constrained targets, but large beams do not guarantee globally optimal or human-preferred text and multiply cache/state costs.

<a id="t-51-07"></a>
## Stopping conditions

Stop on EOS, maximum new tokens, total length, matched token sequences, cancellation, or time budget. A displayed string may not align with token boundaries, so string-stop handling must retain enough suffix and define whether matched text is returned. Batched generation needs per-sequence finished masks; completed rows must not corrupt active rows.

## Worked comparison and four perspectives

For logits [2,1,0], greedy selects the first token. At temperature 0.5 the probabilities are approximately [0.867,0.117,0.016]. At temperature 1, top-2 renormalizes the first two probabilities to approximately [0.731,0.269,0]. With top-p=0.8, the first token contributes only 0.665, so the threshold-crossing second token is included and the retained set is the first two tokens. State whether temperature is applied before top-p; otherwise this example has more than one answer.

Draw 10,000 seeded samples from each resulting distribution and compare counts with binomial standard errors, for example $\sqrt{Np(1-p)}$ for one category. An exact match to expected counts is not required; reproducibility means the same implementation, seed, generator, device, and numeric path reproduce the same sequence.

- **Follow the Token:** the selected ID becomes the next model input.
- **Follow the Gradient:** decoding is normally outside learning; policy-gradient training is a separate process.
- **Follow the Byte:** logits [B,V], sort/top-k workspaces, beam KV copies, and RNG state consume memory.
- **Follow the Request:** policies affect output length, latency, cache occupancy, and reproducibility.

Failures include unstable softmax, applying filters in an undocumented order, using different RNGs, decoding special tokens incorrectly, length-normalization errors, and stop leakage. The exit check distinguishes distribution transformation from sequence search and reproduces seeded results.

## Primary references

- Holtzman et al., [The Curious Case of Neural Text Degeneration](https://arxiv.org/abs/1904.09751), 2020.
- Hugging Face, [Generation API](https://huggingface.co/docs/transformers/main/en/main_classes/text_generation), version-sensitive; accessed 2026-09-19.
- Hugging Face, [Generation strategies](https://huggingface.co/docs/transformers/main/en/generation_strategies), version-sensitive; accessed 2026-09-19. Pin Transformers, model and tokenizer revisions, generation config, seed, device, and numeric mode.
