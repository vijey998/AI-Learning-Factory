# 76. Merging, Stitching and Representation Compatibility

Status: **Draft — not yet independently reviewed.**

Two models can have the same architecture and solve the same task while using different internal coordinates. Combining them therefore requires more than matching tensor shapes.

<a id="t-76-01"></a>
## Model merging

Weight averaging computes $\theta=\sum_i\alpha_i\theta_i$. It can work when models share initialization and remain in a connected low-loss region, as in checkpoint averaging or model soups. Independently trained networks have permutation symmetries: swapping hidden units and compensating downstream weights preserves function but makes naive averages destructive. Git Re-Basin aligns permutations before interpolation. Task-vector methods represent fine-tuning changes $\Delta_i=\theta_i-\theta_0$ and combine or remove them, but interference remains an empirical question.

Before arithmetic, verify identical parameter names, shapes, tokenizer vocabulary and ordering, positional scheme, normalization convention, and base checkpoint. Equal tensor shapes do not make two vocabulary rows semantically equivalent. For models fine-tuned from the same base, preserve the exact base hash used to define every task vector.

Measure each source, the merge, an ensemble, and a multi-task fine-tuned baseline. A merge that saves memory but loses the desired specializations may still be useful; say which objective it optimizes.

<a id="t-76-02"></a>
## Layer stitching

A stitched model runs early layers of source $A$, a connector $g$, then later layers of target $B$. The simplest connector is linear: $g(h)=hW+b$. Train it while freezing both models and compare with controls such as a same-model stitch and a randomly initialized source. Stitching accuracy can measure representational compatibility, but a high-capacity connector may learn the task rather than translate representations. Limit connector capacity and report training data.

<a id="t-76-03"></a>
## Cross-model alignment

Alignment seeks a mapping between representation spaces using paired activations from the same inputs. Orthogonal Procrustes preserves distances and solves for a rotation; linear regression also permits scaling and shear; nonlinear bridges are more expressive and less diagnostic. Match tokenization and positions carefully. Different vocabularies or sequence segmentations require semantic alignment before tensor alignment. Assess held-out reconstruction, neighborhood preservation, and downstream function after transfer.

<a id="t-76-04"></a>
## Normalization mismatch

A target layer expects a distribution shaped by its own preceding layers. Source states can differ in mean, RMS, covariance, outlier structure, and residual scale. Even RMSNorm models can encode learned scale through surrounding weights. Log per-layer norms and covariance spectra, test pre/post-normalization hook points, and consider calibrated affine maps. A bridge trained on one prompt distribution may fail when sequence length or domain changes.

<a id="t-76-05"></a>
## Latent bridge cost

For state $H\in\mathbb{R}^{B\times T\times D_A}$ and dense bridge $W\in\mathbb{R}^{D_A\times D_B}$, parameter count is $D_AD_B+D_B$ and application costs roughly $2BTD_AD_B$ FLOPs if one multiply-add counts as two. With $D_A=D_B=4096$, BF16 weights alone occupy about 33.6 MB decimal; at every decoded token they add a large matrix-vector read. A low-rank bridge $W=UV$ with rank $r$ reduces parameters to $r(D_A+D_B)$ but constrains translation.

Remote handoff also transfers $BTD_A$ elements. For one BF16 state with $B=1,T=2048,D_A=4096$, that is about 16.8 MB before protocol overhead. During token-by-token decode the state is smaller, but network latency and serialization can still erase saved compute. These calculations are feasibility filters, not performance predictions.

## Established result versus hypothesis

Model soups, permutation alignment, and stitching have empirical literature. Seamlessly replacing arbitrary middle layers across unrelated current LLMs is not an established general capability. Compatibility must be demonstrated for named models, hook points, distributions, and tasks. A low reconstruction error alone is insufficient; downstream behavior and cost decide usefulness.

## Four perspectives

- **Follow the Token:** source token states cross a learned coordinate map before the target continues processing.
- **Follow the Gradient:** bridge training updates the connector; merging directly constructs weights and may use no gradient.
- **Follow the Byte:** merged weights can replace several resident models, while bridges add parameters, activation transfer, and possibly network traffic.
- **Follow the Request:** routing must select compatible model revisions and reject a handoff when tokenizer, hook, or bridge metadata mismatches.

## Lab and exit check

Train a linear bridge between two small frozen models on paired inputs. Compare same-model and cross-model stitches, a low-rank bridge, and a nonlinear high-capacity connector. Report held-out reconstruction, task accuracy, parameter count, FLOPs, transfer bytes, and latency. If the nonlinear connector alone succeeds, do not claim the original spaces were naturally aligned.

Evaluate at least one unseen sequence length and domain. A bridge that reconstructs teacher-forced states but fails during autoregressive rollout has not established functional compatibility; report rollout error separately from one-step reconstruction.

## References

- Wortsman et al., [Model Soups](https://proceedings.mlr.press/v162/wortsman22a.html), ICML 2022.
- Ainsworth, Hayase, and Srinivasa, [Git Re-Basin](https://openreview.net/forum?id=CQsmMYmlP5T), ICLR 2023.
- Bansal, Nakkiran, and Barak, [Revisiting Model Stitching](https://proceedings.neurips.cc/paper/2021/hash/01ded4259d101feb739b06c399e9cd9c-Abstract.html), NeurIPS 2021.
- Ilharco et al., [Editing Models with Task Arithmetic](https://openreview.net/forum?id=6t0Kwf8-jrj), ICLR 2023.
