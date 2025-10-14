# 07. Probability, Logits and Loss

Status: **Draft — not yet independently reviewed.**

A language model returns a conditional distribution. Probability gives us the vocabulary for interpreting it; log space makes the computation practical.

<a id="t-07-01"></a>
## Conditional probability

$P(x_t\mid x_{<t})$ is the probability assigned to the next token given preceding tokens. The chain rule factorizes a sequence: $P(x_{1:T})=\prod_{t=1}^{T} P(x_t\mid x_{<t})$, where $x_{<1}$ denotes the chosen start condition. The equality is a probability identity; an autoregressive model approximates the conditional factors.

<a id="t-07-02"></a>
## Likelihood

Given observed training tokens, likelihood treats model parameters as variable and asks how much probability the model assigns to the data. Maximum-likelihood training chooses parameters that increase this value. High likelihood on training data alone may reflect memorization.

<a id="t-07-03"></a>
## Log-probability

Products of many probabilities become sums of log-probabilities: $\log P(x_{1:T})=\sum_t\log P(x_t\mid x_{<t})$. Sums are numerically safer and easier to optimize. Log-probabilities are nonpositive because probabilities do not exceed one.

<a id="t-07-04"></a>
## Entropy

Entropy $H(p)=-\sum_i p_i\log p_i$ measures uncertainty inside one distribution. A point mass has zero entropy; a uniform distribution over $V$ tokens has entropy $\log V$. Entropy is not factuality: a confidently wrong model has low entropy.

<a id="t-07-05"></a>
## KL divergence

$D_{KL}(p\|q)=\sum_i p_i\log[p_i/q_i]$ measures the expected log-ratio under $p$. It is nonnegative but asymmetric and is not a distance metric. In post-training, KL penalties can discourage a policy from moving too far from a reference under a chosen direction and sampling distribution.

<a id="t-07-06"></a>
## Softmax

For logits $z$, $p_i=\exp(z_i)/\sum_j\exp(z_j)$. Adding the same constant to every logit leaves probabilities unchanged. Subtract $m=\max z$ before exponentiation to stay in range.

<a id="t-07-07"></a>
## Logits

Logits are unnormalized scores. Their differences determine odds: $p_i/p_j=\exp(z_i-z_j)$. Absolute offsets do not matter to softmax. Temperature divides logits before softmax; it changes relative sharpness without retraining weights.

<a id="t-07-08"></a>
## Cross-entropy

For target distribution $y$, cross-entropy is $H(y,p)=-\sum_i y_i\log p_i$. With a one-hot target class $k$, it becomes $-\log p_k$. Averaging token losses requires a declared denominator and mask; padding and ignored prompt tokens can otherwise corrupt comparisons.

<a id="t-07-09"></a>
## Log-sum-exp

Combining softmax and negative log-likelihood yields stable token loss

$$L=-z_k + m + \log\sum_j\exp(z_j-m).$$

This avoids first constructing tiny probabilities. The derivative with respect to logit $z_i$ is $p_i-y_i$: raise the target logit and reduce competing logits in proportion to their predicted probability.

## Worked example

For logits `[2,1,0]`, stable exponentials are `[1,e^-1,e^-2]`, probabilities are about `[0.665,0.245,0.090]`, and loss for target 0 is about 0.408. Greedy accuracy is one for this example. Changing logits to `[2,1.9,0]` keeps greedy accuracy one but increases target loss: likelihood detects reduced confidence that accuracy hides.

Sampled accuracy is noisier still. A token with probability 0.665 is omitted about one-third of draws. Sampling evaluates a decoding process; cross-entropy evaluates assigned probability to known targets.

## Exit derivation

Prove shift invariance by replacing every $z_i$ with $z_i+c$ and cancelling $e^c$. Then derive the one-hot loss above. Finally explain three distinct facts: entropy belongs to one distribution, cross-entropy compares targets with predictions, and KL compares two normalized distributions in a direction-sensitive way.

## References

- Shannon, [A Mathematical Theory of Communication](https://doi.org/10.1002/j.1538-7305.1948.tb01338.x), 1948 — entropy and information measures.
- Goodfellow, Bengio, and Courville, [Deep Learning, Chapter 3](https://www.deeplearningbook.org/contents/prob.html), 2016 — probability, cross-entropy, and KL divergence.
