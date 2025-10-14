# 39. Preferences and Reinforcement Learning

Status: **Drafted.**

Part 10: Post-Training and Reasoning

## Learning outcome

Compare the data, objective, and update path for reward-model/PPO-style RLHF and direct preference optimization.

## Prerequisites

CH-26, CH-35, and CH-37.

<a id="t-39-01"></a>
## Preference data

A preference record contains a prompt $x$ and responses $y_w$ and $y_l$, where a rater or rule prefers the winner. Collection quality depends on response diversity, randomized order, a rubric, rater expertise, and treatment of ties. Preferences are conditional: “more helpful” can conflict with “shorter,” “safer,” or “more factual.” Preserve criterion-level labels where possible instead of compressing every judgment prematurely.

Sampling only obviously good versus obviously bad responses teaches little near the decision boundary. Include difficult pairs, audit disagreement, and split by prompt source or conversation to prevent leakage.

<a id="t-39-02"></a>
## Reward models

A reward model maps $(x,y)$ to scalar $r_\phi(x,y)$. A common Bradley–Terry objective is

$$\mathcal L_{RM}=-\log\sigma(r_\phi(x,y_w)-r_\phi(x,y_l)).$$

It learns ordering, not an absolute unit. Adding a constant to all rewards changes nothing. Reward models can exploit length, format, or artifacts and can be confidently wrong off distribution. Evaluate held-out pair accuracy, calibration where meaningful, and adversarial slices; never treat reward as ground truth.

<a id="t-39-03"></a>
## RLHF

In the classic pipeline, SFT initializes a policy, preference data trains a reward model, and reinforcement learning updates the policy to produce higher-reward outputs while remaining near a reference. The loop samples prompts, generates responses, scores them, estimates advantages, and updates parameters. This is on-policy and operationally expensive because generation sits inside training.

The reward model becomes part of the environment. Optimizing it too hard invites reward hacking. Periodically inspect raw generations and evaluate independently of the training reward.

<a id="t-39-04"></a>
## PPO

Proximal Policy Optimization limits destructive policy jumps using a clipped probability-ratio objective. For token actions, ratio $r_t(\theta)=\pi_\theta(a_t|s_t)/\pi_{old}(a_t|s_t)$. The surrogate is

$$\mathbb E[\min(r_tA_t,\operatorname{clip}(r_t,1-\epsilon,1+\epsilon)A_t)].$$

LLM PPO typically also trains a value function and adds a KL penalty to a reference. Correct implementation requires masks for variable lengths, consistent old log-probabilities, advantage normalization choices, and stable generation. PPO clipping does not guarantee a hard trust region, and token-level credit from a sequence-level reward is noisy.

<a id="t-39-05"></a>
## DPO-type objectives

Direct Preference Optimization avoids a separately deployed reward model and on-policy rollouts by optimizing policy likelihood ratios on fixed preference pairs. One form minimizes

$$-\log\sigma\left(\beta\left[\log\frac{\pi_\theta(y_w|x)}{\pi_{ref}(y_w|x)}-\log\frac{\pi_\theta(y_l|x)}{\pi_{ref}(y_l|x)}\right]\right).$$

Sequence log-probabilities sum token log-probabilities under appropriate masks. DPO is simpler operationally, but remains sensitive to preference quality, length effects, reference choice, and distribution shift. “No reward model” does not mean no reward assumptions; the derivation encodes a particular preference model and KL-regularized optimum.

<a id="t-39-06"></a>
## Policy KL control

KL control penalizes movement from a reference policy:

$$\mathbb E[r(x,y)]-\beta D_{KL}(\pi_\theta(\cdot|x)\|\pi_{ref}(\cdot|x)).$$

Too little control allows exploitation and drift; too much prevents learning. Implementations often estimate token-level sampled KL rather than the full distributional KL. Log both the estimator and response behavior. A target-KL controller may adapt $\beta$, but it cannot ensure the model stays safe or correct.

## Four recurring perspectives

- **Follow the Token:** a response is a sequence of actions; masks determine which log-probabilities enter rewards and objectives.
- **Follow the Gradient:** RM gradients train $\phi$; PPO gradients use sampled advantages; DPO gradients contrast winner and loser likelihood ratios.
- **Follow the Byte:** PPO may hold policy, reference, reward, and value models plus rollout buffers; DPO usually needs policy, reference, and paired batches.
- **Follow the Request:** prompt distribution, sampling policy, and rubric decide which deployment behaviors get optimized.

## Lab and exit check

For one preference pair, compute reward-model loss and DPO loss from supplied scalar rewards and sequence log-probabilities. Draw PPO's generation-to-update path and list every frozen and trainable model. Change response length and show how summed versus averaged log-probabilities alter the comparison.

## Exercises

1. If $r(y_w)=2.0$ and $r(y_l)=0.5$, compute the reward-model loss. **Check:** $-\log\sigma(1.5)\approx0.201$.
2. For $A_t>0$, compare PPO's unclipped and clipped terms when $r_t=1.4$ and $\epsilon=0.2$. **Check:** the minimum uses $1.2A_t$; clipping limits this positive-advantage incentive but does not impose a hard policy-distance bound.

## References

- Christiano et al., [Deep Reinforcement Learning from Human Preferences](https://arxiv.org/abs/1706.03741), 2017.
- Schulman et al., [Proximal Policy Optimization Algorithms](https://arxiv.org/abs/1707.06347), 2017.
- Ouyang et al., [Training Language Models to Follow Instructions with Human Feedback](https://arxiv.org/abs/2203.02155), 2022.
- Rafailov et al., [Direct Preference Optimization](https://arxiv.org/abs/2305.18290), 2023.
