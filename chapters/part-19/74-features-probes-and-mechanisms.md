# 74. Features, Probes and Mechanisms

Status: **Draft — not yet independently reviewed.**

Mechanistic interpretability asks for executable accounts of how model components produce behavior. Its evidence ladder runs from observation, through prediction, to intervention. Each rung rules out more alternative explanations.

<a id="t-74-01"></a>
## Neurons

A neuron is one scalar coordinate after a learned affine transformation and nonlinearity. Inspecting the inputs that maximize it can reveal a pattern, but polysemantic neurons may respond to unrelated contexts. Dataset search also misses rare activations. A neuron’s effect depends on its outgoing weights and the rest of the network; high activation alone does not establish importance.

<a id="t-74-02"></a>
## Features

A feature is a hypothesized direction or pattern that represents a property relevant to computation. Features need not align with neurons. Superposition proposes that networks can represent more features than dimensions by using non-orthogonal directions when features are sparse. This is a useful model supported by toy and empirical work, not a licence to assign a clean concept name to every direction.

<a id="t-74-03"></a>
## Probing

A probe predicts labels from frozen activations. Linear probes ask whether labels are linearly accessible; nonlinear probes blur representation and probe capability. Use selectivity controls, limited capacity, held-out data, and minimum-description-length or sample-efficiency analyses where appropriate. A successful probe establishes decodability under its setup. Causal use requires intervention.

<a id="t-74-04"></a>
## Sparse autoencoders

A sparse autoencoder learns encoder $z=\phi(W_eh+b_e)$ and decoder $\hat h=W_dz+b_d$, balancing reconstruction error with sparsity. The hope is that sparse latent units separate features entangled in dense activations. Evaluate reconstruction loss, sparsity, dead latents, feature stability, and downstream behavior under reconstruction. Human labels assigned from top activations can be incomplete or misleading. SAE features are learned model artifacts, not ground-truth atoms of thought.

Dictionary features are not automatically identifiable: different seeds, widths, penalties, or activation samples can produce different bases with similar reconstruction. Match features across runs and report stability, but do not treat matching failure as proof that no useful feature exists. Compare against PCA, random dictionaries, and reconstruction-matched baselines to isolate what sparsity contributes.

<a id="t-74-05"></a>
## Mechanistic interpretability

A mechanism is a compact account connecting inputs, internal operations, and outputs. One workflow is: localize a behavior, identify candidate components, form a circuit hypothesis, intervene, measure specificity, and test on new examples. Faithfulness asks whether the proposed mechanism captures the model’s actual computation; completeness asks how much behavior it explains. Circuits can be approximate and context-dependent.

<a id="t-74-06"></a>
## Causal interventions

Activation patching runs a clean and corrupted prompt, then replaces a selected corrupted activation with its clean counterpart. Recovery of the target metric localizes a causally relevant site under that corruption. Ablation replaces a component with zero, mean, resampled, or another reference value; each choice creates different distribution shifts. Path patching attempts to isolate routes between components. Interventions should include negative controls, matched prompts, multiple seeds, and tests for collateral behavior.

Report both absolute recovery and a normalized score such as $(m_{patched}-m_{corrupt})/(m_{clean}-m_{corrupt})$ when the denominator is safely nonzero. Values above one or below zero are possible and should not be clipped; they reveal overshoot or harm. Define the metric sign before inspecting patches.

Suppose changing a subject token flips a factual answer. Patch each layer-position residual state from the clean run into the corrupted run and measure logit-difference recovery. A peak identifies a location worth deeper study. It does not prove the fact “lives” there: the patch may restore an upstream signal used elsewhere.

## Evidence ladder

1. **Observation:** component activates on selected examples.
2. **Association:** signal predicts behavior on held-out data.
3. **Necessity:** removing it degrades the behavior.
4. **Sufficiency:** inserting it induces or restores behavior.
5. **Mechanism:** a compositional account predicts novel interventions.

Even necessity can be obscured by redundancy, and sufficiency can reflect out-of-distribution forcing. Report the precise level reached.

## Four perspectives

- **Follow the Token:** candidate features emerge at positions and travel through residual paths to output logits.
- **Follow the Gradient:** probes and SAEs learn mappings from frozen states; causal patching uses forward execution without model training.
- **Follow the Byte:** activation datasets and SAE training can require far more storage than the base weights.
- **Follow the Request:** instrumentation needs deterministic prompt pairs, hook versions, metrics, and replayable intervention traces.

## Lab and exit check

Define one narrow behavior and build clean/corrupted prompt pairs. Compare a linear probe, activation patching, and ablation. Include a shuffled-label control and a non-target behavior. State the strongest justified conclusion using the evidence ladder. If the intervention damages all outputs, it has not demonstrated specificity.

## References

- Alain and Bengio, [Understanding Intermediate Layers Using Linear Classifier Probes](https://arxiv.org/abs/1610.01644), 2016.
- Hewitt and Liang, [Designing and Interpreting Probes with Control Tasks](https://aclanthology.org/D19-1275/), EMNLP-IJCNLP 2019.
- Meng et al., [Locating and Editing Factual Associations in GPT](https://proceedings.neurips.cc/paper_files/paper/2022/hash/6f1d43d5a82a37e89b0665b33bf3a182-Abstract-Conference.html), NeurIPS 2022.
- Bricken et al., [Towards Monosemanticity](https://transformer-circuits.pub/2023/monosemantic-features/index.html), 2023; empirical research report, not peer-reviewed conference evidence.
