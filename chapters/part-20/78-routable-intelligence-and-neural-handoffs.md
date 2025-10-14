# 78. Routable Intelligence and Neural Handoffs

Status: **Draft research agenda — hypotheses are not established results.**

Routing complete requests among models is established systems practice. Routing intermediate neural states between independently trained models is a research proposal with unresolved compatibility, quality, and economics. This chapter keeps those evidence levels separate.

<a id="t-78-01"></a>
## Neural routing

**Established:** mixture-of-experts models learn routers among experts trained inside a shared architecture, and cascades route whole requests among models. **Hypothesis:** a controller could also choose a model, layer segment, or expert intervention from intermediate state. A useful router must make its decision before the avoided compute, with overhead below the savings and low false-easy error. Inputs might include prompt features, early logits, uncertainty proxies, or hidden-state summaries.

<a id="t-78-02"></a>
## Model cascades

Cascades run a cheap model first and escalate selected cases. They provide the strongest baseline for any more exotic handoff because they require no latent compatibility. Evaluate a threshold sweep at fixed quality, including the latency of failed first attempts. Calibration drift and selective feedback are operational risks. If a cascade matches a neural handoff, prefer the simpler interface.

<a id="t-78-03"></a>
## Latent communication

**Established in bounded settings:** networks trained jointly can exchange learned latent messages; split computing transmits intermediate features; multimodal systems learn projection layers. **Open for unrelated LLMs:** whether a compact latent message can preserve the information another independently trained model needs across domains. Compare latent transfer with text, logits, retrieved evidence, and structured summaries under equal bandwidth and compute.

<a id="t-78-04"></a>
## Cross-model representations

Representations may be statistically alignable even when coordinates differ, as Chapter 76 showed. Alignment does not imply functional substitutability. A bridge must preserve the target model’s required signals, norms, position semantics, and token correspondence. Test translation on held-out distributions and use the target continuation behavior as the main metric. CKA or reconstruction can support analysis but cannot certify a handoff.

<a id="t-78-05"></a>
## Neural handoffs

A candidate handoff runs layers $0{:}i$ of model A, applies bridge $g$, then layers $j{:}L_B$ of model B. Falsifiable hypothesis: for named A, B, task distribution, and budget, the stitched system reaches within a predeclared quality margin of B while reducing measured cost or latency beyond bridge and transfer overhead. Baselines are B alone, A alone, whole-request cascade, textual handoff, same-model early exit, and a bridge with shuffled pairs. Failure means missing the quality margin or failing to save resources end to end.

Autoregressive handoff has an additional state problem: B's surviving attention layers need keys and values for all prior positions in B's own representation space. A prefill-time handoff can run the full prefix through B's suffix to create those caches. A mid-generation handoff must instead replay history, translate compatible KV state, or have maintained B's cache in parallel; each option can erase the proposed saving. Any experiment that transfers only the current hidden vector while ignoring destination KV history is not testing a valid cached decoder handoff.

<a id="t-78-06"></a>
## Sparse expert intervention

Instead of replacing a suffix, an expert might provide a sparse correction $\Delta h$ at selected tokens, layers, or features. This resembles adapters or residual experts when trained jointly. The research question is whether an independently trained expert can intervene reliably through a learned interface. Measure intervention frequency, bytes, target gain, collateral effects, and whether a conventional adapter with equal parameters performs better.

<a id="t-78-07"></a>
## Silent expert intervention

“Silent” means the expert communicates through latent state rather than user-visible text. It should not mean invisible to logs, policy, or evaluation. Hypothesis: latent advice may avoid output-token generation and preserve richer information. Counter-risk: it is harder to inspect, authorize, and debug. Require typed metadata, provenance, audit traces, and a text-handoff baseline.

<a id="t-78-08"></a>
## LLM dead-call elimination

A dead call is an LLM invocation whose removal does not reduce task quality under a defined test distribution and budget. Detect candidates by call-graph logging, then replay tasks while bypassing, caching, replacing, or combining calls. The causal test is an ablation, not a judgement based on plausible-looking transcripts. Hypothesis: many orchestration graphs contain redundant critic, summarizer, or formatter calls. Negative result: removal materially harms a predeclared quality or safety metric.

<a id="t-78-09"></a>
## Computation as a routable resource

The broader program treats layers, experts, models, retrieval, tools, and human review as actions with cost and expected value. This can be posed as constrained optimization: maximize expected utility subject to latency, money, energy, and risk budgets. In practice, rewards are incomplete and distribution shift is unavoidable. Start with logged, auditable rules and offline counterfactual evaluation before learned online routing.

## Minimal experiment

Use two small open models with frozen revisions. Train linear and low-rank bridges on paired states from one domain. Pre-register layer pairs, datasets, quality margin, hardware, maximum bridge parameters, and latency accounting. Compare six baselines listed above. Include shuffled-pair and same-model bridges, report three or more seeds, and profile serialization separately. Do not call the method successful if GPU kernel time falls but end-to-end latency rises.

State when the route is chosen—before prefill, after prefill, or during decode—and account for destination KV construction accordingly. Report resident memory for both models even when only one executes at a time.

## Four perspectives

- **Follow the Token:** define how token identities and positions align across tokenizers before any latent tensor crosses models.
- **Follow the Gradient:** bridge or router training changes only declared components unless joint training is an explicit baseline.
- **Follow the Byte:** count bridge weights, transferred activations, synchronization, KV compatibility, and duplicated resident models.
- **Follow the Request:** log routing decision, model revisions, hook locations, bridge version, fallbacks, and final verification.

## Lab and exit check

Write a preregistered experiment for one neural handoff and one dead-call ablation. Include hypotheses, baselines, fixed budget, quality and systems metrics, uncertainty, negative-result criteria, and artifact plan. Then run the smallest feasible pilot. The acceptable conclusion may be that text or whole-request routing wins; that is useful evidence, not a failed research process.

## References

- Jacobs et al., [Adaptive Mixtures of Local Experts](https://doi.org/10.1162/neco.1991.3.1.79), Neural Computation 1991.
- Teerapittayanon, McDanel, and Kung, [BranchyNet](https://arxiv.org/abs/1709.01686), 2017.
- Bansal, Nakkiran, and Barak, [Revisiting Model Stitching](https://proceedings.neurips.cc/paper/2021/hash/01ded4259d101feb739b06c399e9cd9c-Abstract.html), NeurIPS 2021.
- Kang et al., [Neurosurgeon: Collaborative Intelligence Between the Cloud and Mobile Edge](https://doi.org/10.1145/3037697.3037698), ASPLOS 2017.
