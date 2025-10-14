# 73. Hidden States, Layers and Attention Heads

Status: **Draft — not yet independently reviewed.**

A transformer exposes many tensors that correlate with behavior. Looking at them can generate hypotheses, but a colorful plot is not yet an explanation. This chapter establishes what is actually measured before later chapters intervene on it.

<a id="t-73-01"></a>
## Hidden states

For batch $B$, sequence length $T$, and model width $D$, a decoder layer produces hidden states $H^{(\ell)}\in\mathbb{R}^{B\times T\times D}$. The vector at a position is contextual: it depends on earlier tokens under causal masking. Coordinates do not arrive with human labels. A direction or distributed pattern can carry information even when no individual coordinate is interpretable.

Unembedding an intermediate state with the final output matrix creates a “logit lens”: $H^{(\ell)}W_U$. It is a useful diagnostic, but earlier states may not inhabit the distribution expected by the final normalization and unembedding. Tuned lenses learn translations to reduce this mismatch, adding parameters and another source of interpretation.

For architectures with a final LayerNorm or RMSNorm, a faithful naive lens usually applies that published final normalization before $W_U$; omitting it changes scale and sometimes ranking. Even with it, the lens asks what the current state would predict through the final readout, not what the remaining layers will actually compute.

<a id="t-73-02"></a>
## Residual stream analysis

Each attention and MLP sublayer writes an update into a shared residual stream. In a simplified pre-norm block, $h' = h + A(N(h))$ and $h''=h'+M(N(h'))$. This additive structure permits decomposition of a final logit into contributions from components under stated linearization and normalization assumptions. It does not mean components operate independently: later normalization and nonlinear modules respond to the sum.

Record where states are taken—before or after normalization, attention, MLP, or residual addition. “Layer 12 activation” is otherwise ambiguous.

<a id="t-73-03"></a>
## Representation geometry analysis

Geometry tools compare distances, angles, subspaces, covariance, and neighborhood structure. Centered Kernel Alignment (CKA) compares representations while tolerating some transformations; canonical correlation methods compare correlated subspaces. PCA finds high-variance directions, which need not be task-causal. Results depend on token sampling, centering, normalization, prompt distribution, and layer location. A two-dimensional projection is a lossy view and should carry explained-variance or neighborhood-preservation information.

<a id="t-73-04"></a>
## What individual layers learn

Layerwise decodability studies often find changing accessibility of lexical, syntactic, or task information. The careful claim is “a specified probe decoded label $y$ from states at layer $\ell$ on dataset $D$.” It is stronger than raw correlation and weaker than “the layer computes concept $y$.” Information can be present but unused, or a powerful probe can learn the task itself. Compare with controls, random labels, simple probes, and baselines from embeddings.

<a id="t-73-05"></a>
## Layer specialization

Specialization can mean a layer is necessary for a behavior, uniquely informative, or merely more linearly decodable. These definitions are not interchangeable. Test necessity with ablation or replacement, sufficiency by transplanting or activating the component, and specificity across tasks. Distributed computation makes sharp boundaries unlikely: removing one layer may be repaired by redundant paths, while deleting many layers can shift normalization and create out-of-distribution states.

<a id="t-73-06"></a>
## Attention-head analysis

An attention head produces weights $P=\operatorname{softmax}(QK^T/\sqrt{d_h}+M)$ and output $PVW_O$. Weight maps show routing probabilities, not the full signed contribution to logits. A large weight can carry a small value vector; a modest weight can matter through a large output projection. Analyze patterns over a dataset, then test head outputs with ablation, patching, or path-specific interventions. Induction-head research provides a concrete example of combining pattern discovery with mechanistic tests, but findings in small models do not automatically generalize to every architecture.

## Worked measurement protocol

Choose a frozen model revision and 500 prompts representing both target and control behaviors. Capture states at a precisely named hook, fit a linear probe on a train split, tune on validation, and report held-out accuracy beside a majority baseline and a probe on shuffled labels. Then replace the candidate component with its mean activation or patch it from a counterfactual prompt. If decoding stays high while behavior is unchanged under intervention, the representation is readable but not shown causal.

Split by source template, entity, or document rather than by individual token when those units share lexical cues. Otherwise the probe may memorize correlated examples across the split. Fit every preprocessing transform—including centering and PCA—on the training split only.

## Four perspectives

- **Follow the Token:** each position accumulates contextual updates across layers and is eventually projected to logits.
- **Follow the Gradient:** probes may learn with frozen model states; their gradients train the probe, not evidence that the base model uses the decoded feature.
- **Follow the Byte:** capturing every layer costs $B\,T\,D\,L$ elements and can dwarf ordinary inference memory.
- **Follow the Request:** instrumentation changes latency and storage; sample or stream activations with privacy and retention controls.

## Lab and exit check

Capture three layer locations for a small open model. Compare a logit lens, linear probe, and component ablation on held-out prompts. Report shapes, hook definitions, baselines, uncertainty, and one case where a correlational signal fails a causal test. Explain why attention weights alone are not feature importance.

## References

- Elhage et al., [A Mathematical Framework for Transformer Circuits](https://transformer-circuits.pub/2021/framework/index.html), 2021.
- Belinkov, [Probing Classifiers](https://aclanthology.org/J22-2003/), Computational Linguistics 2022.
- Kornblith et al., [Similarity of Neural Network Representations Revisited](https://proceedings.mlr.press/v97/kornblith19a.html), ICML 2019.
- Olsson et al., [In-context Learning and Induction Heads](https://arxiv.org/abs/2209.11895), 2022.
