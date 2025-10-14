# 34. Mixtures, Tokens and Synthetic Data

Status: **Drafted.**

Part 9: Data, Scaling and Evaluation

## Learning outcome

Design a defensible token allocation, construct splits by unit of independence, and detect evaluation leakage.

## Prerequisites

CH-33.

<a id="t-34-01"></a>
## Dataset mixtures

A mixture specifies the probability that the next training example comes from each component. Raw availability should not decide this automatically. If a corpus contains 90% web prose and 1% code, sampling in those proportions may undertrain code. Upsampling code to 20% changes both capabilities and the number of epochs seen by that component.

Let component $i$ contain $D_i$ tokens and receive probability $p_i$. Over budget $T$, expected sampled tokens are $p_iT$, and expected epochs are $p_iT/D_i$. With $T=10$B, a 100M-token curated corpus at $p=0.05$ is seen five times. Mixtures may be fixed, staged, or adaptive. Always save realized counts, not just intended probabilities.

<a id="t-34-02"></a>
## Token budgets

A token budget is the number of tokens processed, including repetitions. It connects data to compute: for a dense decoder Transformer, a planning approximation is roughly $6ND$ FLOPs for $N$ non-embedding parameters and $D$ training tokens. The constant varies with architecture and implementation, so profile before procurement.

Allocate the budget in a table with available tokens, sampling weight, expected sampled tokens, expected epochs, and rationale. Account for tokenizer differences: “one billion tokens” is not language-neutral. Packing efficiency matters too; padding consumes compute while teaching nothing.

<a id="t-34-03"></a>
## Synthetic data

Synthetic data is generated or transformed by models, programs, simulators, or rules. It can target rare skills, create verifiable exercises, translate material, or attach explanations. Its value comes from controlled coverage and verification.

A robust pipeline separates generator and judge, retains generator version and prompt, validates answers with an external oracle where possible, and samples failures for human review. Execute code tests in a sandbox and recompute arithmetic. Common failures are self-imitation, collapsed style, plausible wrong answers, and amplification of generator bias. As of September 2026, claims that synthetic data either inevitably poisons models or universally solves scarcity remain too broad.

<a id="t-34-04"></a>
## Data quality

Quality is conditional on intended behavior. A novel is poor data for exact API usage; terse compiler errors may be excellent debugging data. Define measurable dimensions: correctness, relevance, diversity, freshness, formatting integrity, and source trust. Track quality by slice and validate it against downstream experiments. Loss alone is insufficient: repetitive or leaked data can be easy to predict.

<a id="t-34-05"></a>
## Contamination

Contamination occurs when evaluation content, answers, or close variants influence training. Exact matching catches only easy cases. Search normalized n-grams, near duplicates, problem templates, translations, and solution text. Date splits help only when timestamps are reliable.

Leakage inflates an estimate without improving the underlying capability. If a benchmark problem appears verbatim, a correct response may measure recall. If only a solution pattern appears, the boundary is murkier; report methods and thresholds instead of claiming binary purity.

<a id="t-34-06"></a>
## Split design

Random row splits are often wrong because rows are not independent. Split by author, repository, website, conversation, patient, or deduplication cluster—whichever unit carries shared signal. Repeatedly inspecting test failures turns the test set into development data; freeze it or introduce a fresh final set.

For temporal products, train before a cutoff and test afterward. For code, split repositories rather than files. For conversations, keep each thread together. Document exclusions and slice counts.

## Four recurring perspectives

- **Follow the Token:** a source weight becomes a sampled document, tokenized sequence, and position in a packed batch.
- **Follow the Gradient:** mixture weights scale how frequently each distribution supplies gradient signals.
- **Follow the Byte:** token budgets determine stored shards and total training traffic.
- **Follow the Request:** split design must resemble future requests; leakage can make offline scores irrelevant.

## Lab and exit check

Given components of 8B, 2B, 500M, and 100M unique tokens, allocate a 12B-token run and compute expected epochs. Plant five exact and five paraphrased benchmark leaks; test hash and shingle detectors. Explain false positives and false negatives.

## Exercises

1. A 200M-token component has mixture weight 0.08 in a 15B-token run. Compute its expected sampled tokens and epochs. **Check:** 1.2B sampled tokens and six expected epochs.
2. Give one contamination detector likely to miss translated benchmark items and one stronger follow-up. **Check:** exact hashes miss translations; multilingual semantic retrieval followed by human or model-assisted adjudication is stronger but has false positives.

## References

- Gao et al., [The Pile](https://arxiv.org/abs/2101.00027), 2020.
- Longpre et al., [A Pretrainer's Guide to Training Data](https://arxiv.org/abs/2305.13169), 2023.
- Carlini et al., [Quantifying Memorization Across Neural Language Models](https://arxiv.org/abs/2202.07646), 2022.
