# 75. Steering, Editing and Representation Engineering

Status: **Draft — not yet independently reviewed.**

Intervening on representations can change behavior without retraining every parameter. That makes these methods attractive and risky: a small vector or weight edit may work on a demonstration while shifting unrelated behavior elsewhere.

<a id="t-75-01"></a>
## Activation steering

A steering vector is often built from a contrast, such as the mean activation difference between positive and negative prompt sets at layer $\ell$:

$$v=\mathbb{E}[h^{(\ell)}\mid P^+]-\mathbb{E}[h^{(\ell)}\mid P^-].$$

During generation, replace $h^{(\ell)}$ with $h^{(\ell)}+\alpha v$ at selected positions. Sweep $\alpha$ rather than reporting one flattering value. Strong coefficients can damage fluency, overwhelm prompt intent, or trigger unrelated features. Controls include random directions of matched norm, reversed vectors, alternative prompt templates, and evaluation on non-target tasks.

Name the hook precisely: adding before normalization, after attention, or after the residual update are different interventions. State whether $v$ is normalized and whether its norm is comparable to the residual stream at that layer. Applying a fixed vector to every prompt and generated token is also different from steering only the final prompt position.

<a id="t-75-02"></a>
## Representation engineering

Representation engineering treats population-level internal patterns as objects for measurement and control. Choices include which layer and token to read, how to construct contrasts, whether to whiten or normalize, and whether to apply a linear or learned controller. A difference-of-means direction is interpretable and cheap; PCA on contrast activations can capture a broader subspace; trained controllers are more expressive but risk dataset shortcuts.

Generalization across topics, phrasing, languages, sequence positions, and decoding policies matters more than separation on the construction set. Report the data used to discover the direction separately from data used to evaluate it.

<a id="t-75-03"></a>
## Model editing

Model editing changes parameters to alter targeted associations or behavior. Rank-one model editing (ROME) updates selected MLP weights using a derived key-value association; MEMIT extends editing to many memories. Other methods fine-tune a small subset or use an external memory rather than altering weights. Evaluation should distinguish reliability on the exact edit, generalization to paraphrases, locality on unrelated prompts, portability to related implications, and retention after subsequent edits.

An edit that makes “X was born in Y” answer correctly but breaks other subjects is not local. An edit that works only for the training wording has not generalized. Repeated edits can interfere even when each single edit looks safe.

<a id="t-75-04"></a>
## Intervention side effects

Side effects arise because representations and weights participate in many computations. Steering may change style, certainty, refusal, or token frequency alongside the target. Weight edits may alter semantically neighboring facts. Evaluate perplexity, broad capability suites, target-specific controls, distribution shifts, and worst-case examples. Compare with prompt-based control, retrieval, fine-tuning, and doing nothing; an internal intervention is justified only when it wins on the actual product constraint.

Causal language should match the experiment. Adding a vector and observing a behavior change establishes an effect of that intervention in that context. It does not establish that the direction is the model’s unique representation of the named concept.

## Worked protocol

Construct 200 paired prompts for a narrow attribute and split them before computing the direction. Extract residual states at several layers and choose the layer using validation only. On the held-out set, sweep $\alpha$ and report target score, language-model loss, refusal rate, and two unrelated capabilities. Repeat with five matched random directions. Then test on a new topic and prompt format. This design exposes whether the vector controls a transferable feature or a narrow template artifact.

Correct for selection over layers and coefficients: the held-out test is evaluated once after choosing both on validation. Reporting the best test layer from the same sweep turns the test set into another tuning set.

## Four perspectives

- **Follow the Token:** an additive vector alters the residual state of selected positions, which changes downstream attention, MLP updates, and logits.
- **Follow the Gradient:** basic steering uses none; model editing solves or optimizes a parameter update and permanently changes later forward passes.
- **Follow the Byte:** steering stores small vectors but adds per-token reads and adds; editing creates weight versions and rollback checkpoints.
- **Follow the Request:** log model revision, intervention ID, layer, positions, coefficient, policy decision, and outcome for reproducibility.

## Lab and exit check

Build one contrastive steering vector on a small model. Use disjoint discovery, validation, and test sets; sweep strength; compare random and reversed controls; measure at least two side effects. Optionally perform a single weight edit and test exact, paraphrased, neighboring, and unrelated prompts. State only what the interventions demonstrate.

## References

- Turner et al., [Activation Addition](https://arxiv.org/abs/2308.10248), 2023.
- Zou et al., [Representation Engineering](https://arxiv.org/abs/2310.01405), 2023.
- Meng et al., [ROME](https://proceedings.neurips.cc/paper_files/paper/2022/hash/6f1d43d5a82a37e89b0665b33bf3a182-Abstract-Conference.html), NeurIPS 2022.
- Meng et al., [MEMIT](https://openreview.net/forum?id=MkbcAHIYgyS), ICLR 2023.
