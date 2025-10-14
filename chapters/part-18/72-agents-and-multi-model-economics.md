# 72. Agents and Multi-Model Economics

Status: **Draft — not yet independently reviewed.**

An agent is a control loop that lets a model observe state, choose an action, receive a result, and continue toward a goal. The loop—not a special kind of intelligence—is the defining engineering object. Its value must exceed the cost and new failure modes introduced by extra calls.

<a id="t-72-01"></a>
## Agents

A minimal agent has state $s_t$, available actions $A(s_t)$, a policy that proposes $a_t$, an environment transition, and a termination rule. State may include messages, files, tool results, budgets, and a task graph. Restrict actions by capability and validate each call. Termination needs success criteria, maximum steps, cost limits, and stuck detection. Otherwise a harmless ambiguity becomes a very expensive while-loop.

<a id="t-72-02"></a>
## Planning

Planning decomposes a goal into intermediate actions. ReAct interleaves reasoning traces and actions; other systems keep an explicit task graph or replan after observations. Plans help with long dependencies but can become stale after the first tool result. Use them as revisable state, record observable rationales such as assumptions and chosen actions, and avoid depending on private chain-of-thought as a system interface. Verify completion from environment state rather than the model’s declaration.

<a id="t-72-03"></a>
## Multi-agent systems

Multiple agents can specialize, debate, or execute tasks in parallel. They also duplicate context, propagate the same misconception, and add coordination overhead. Independent agents provide value when tasks are separable or evidence sources are diverse. A critic is useful only if it has a rubric and permission to reject; agreement among correlated models is weak evidence. Compare against one agent with equal total tokens, tools, and latency budget.

<a id="t-72-04"></a>
## Multi-LLM systems

Different models can serve roles based on capability, latency, context length, modality, deployment location, or cost. Interfaces should pass typed artifacts—retrieval results, patches, test reports—rather than vague prose whenever possible. Model versions change, so record provider, model revision, decoding settings, prompt version, and tool schema. Cross-model escalation is a routing decision, not proof that the second model will repair the first.

<a id="t-72-05"></a>
## Agent compute economics

For path $r$, expected request cost can be written

$$E[C]=\sum_r P(r)(C_{tokens,r}+C_{tools,r}+C_{compute,r}+C_{failure,r}).$$

Latency requires a critical-path calculation: parallel calls add the maximum branch latency plus coordination, while sequential calls add. Include retries, cache misses, human review, and failure remediation. Quality should be measured at a fixed budget, and cost at a fixed quality. Seven calls that equal one strong call are an orchestration tax, not a feature.

For a simple cascade, if the cheap path costs 1 unit, escalation costs another 8, and 25% of requests escalate, expected model cost is $1+0.25\cdot8=3$ units before tools and failures. Its escalated latency is sequential, not the probability-weighted average experienced by tail users. Publish the full path distribution so a low mean does not hide an expensive or slow cohort.

<a id="t-72-06"></a>
## Routing and fallback

A router can use simple rules, a learned classifier, uncertainty signals, or staged escalation. Start with auditable rules and a strong single-model baseline. Evaluate routing accuracy, end-task quality, escalation rate, cost, tail latency, and failures by cohort. Fallbacks need bounded retries and must preserve state safely. A cheaper model timing out before every expensive fallback increases both cost and latency.

Use shadow evaluation before sending live traffic: replay a representative set through candidate routes and log counterfactual outcomes. Online adaptation requires guardrails because feedback is selective—only routed paths reveal their outcomes.

## Four perspectives

- **Follow the Token:** each handoff serializes context; repeated summaries can lose constraints or multiply prompt tokens.
- **Follow the Gradient:** most orchestrators route frozen models; learned routers receive gradients from labelled outcomes or proxy rewards.
- **Follow the Byte:** model residency, KV caches, network payloads, and duplicated context determine whether parallelism is practical.
- **Follow the Request:** the trace must show route, tools, retries, budgets, termination reason, and final verification.

## Lab and exit check

Build a router with a cheap path, a strong path, one tool, bounded retry, and explicit abstention. Compare it with the strong model alone under matched quality and workload. Report success, cost, p50/p95 latency, calls per task, escalation, and failure recovery. Add an ablation that removes the planner or critic. Keep the component only if its marginal value survives that comparison.

Evaluate on frozen tasks with sandboxed side effects. Re-running a benchmark that mutates files, tickets, or accounts can change later trials; reset the environment or score from immutable snapshots so route order is not a confounder.

## References

- Yao et al., [ReAct](https://openreview.net/forum?id=WE_vluYUL-X), ICLR 2023.
- Shinn et al., [Reflexion](https://proceedings.neurips.cc/paper_files/paper/2023/hash/1b44b878bb782e6954cd888628510e90-Abstract-Conference.html), NeurIPS 2023.
- Chen, Zaharia, and Zou, [FrugalGPT](https://arxiv.org/abs/2305.05176), 2023.
