# 10. A Tiny Network, Forward and Backward

Status: **Draft — not yet independently reviewed.**

We now make learning concrete with a two-layer scalar network. Every number is small enough to check by hand.

<a id="t-10-01"></a>
## Building a tiny neural network

Let $x=2$, target $y=0$, and $h=\operatorname{ReLU}(w_1x+b_1)$, $\hat y=w_2h+b_2$, $L=\tfrac12(\hat y-y)^2$. Choose $w_1=0.5,b_1=0,w_2=-1,b_2=2$. These four scalars are model state. The intermediate activation and loss belong to this execution.

This network has one hidden unit only so the arithmetic stays visible. Real networks replace scalars with matrices, but the graph and local derivative rules are the same.

<a id="t-10-02"></a>
## Forward propagation

Compute in program order: $z_1=1$, $h=1$, $\hat y=1$, and $L=0.5$. A forward pass is evaluation; it neither discovers a gradient nor updates a parameter. For a batch, inputs become $X[B,D_{in}]$, hidden states $H[B,D_h]$, and outputs $Y[B,D_{out}]$. Vectorization changes execution efficiency, not the per-example function.

<a id="t-10-03"></a>
## Backpropagation by hand

Begin at the loss: $\partial L/\partial\hat y=\hat y-y=1$. Therefore $\partial L/\partial w_2=h=1$, $\partial L/\partial b_2=1$, and $\partial L/\partial h=w_2=-1$. Because $z_1=1>0$, ReLU's local derivative is 1. Thus $\partial L/\partial w_1=(-1)(1)x=-2$ and $\partial L/\partial b_1=-1$.

With learning rate $0.1$, one SGD step gives $w_1=0.7,b_1=0.1,w_2=-1.1,b_2=1.9$. Re-evaluating yields $h=1.5$, $\hat y=0.25$, and $L=0.03125$: a lower loss for this example. The decrease is evidence for this step, not a guarantee for arbitrary learning rates.

<a id="t-10-04"></a>
## Gradient shapes

Every parameter gradient has the parameter's shape. For $Z=XW+b$, upstream $G=\partial L/\partial Z$ gives $\partial L/\partial W=X^TG$, $\partial L/\partial X=GW^T$, and $\partial L/\partial b=\sum_{i=1}^{B}G_i$. Shape reasoning catches transpose and reduction errors before numerical debugging.

Gradients accumulate when a parameter is reused. If a weight participates at several sequence positions, its gradient is the sum of all those paths. Accidentally overwriting rather than accumulating produces a plausible but incorrect update.

## Four perspectives

**Follow the Token:** the example becomes a hidden activation and a prediction. **Follow the Gradient:** sensitivity travels in reverse through the exact executed path. **Follow the Byte:** backward needs saved $x,z_1,h$ or must recompute them. **Follow the Request:** training requests retain a graph and mutate parameters after aggregation; serving requests normally do neither.

## Exit check

Repeat the calculation with $b_1=-2$, making $z_1=-1$. Which first-layer gradients become zero, and why? Verify the original derivatives with centered finite differences. State what happens if the loss is summed rather than averaged over a batch.

## Implementation discipline

A trustworthy tiny-network lab should make parameter mutation explicit. First clear accumulated gradients. Then run the forward graph, reduce the loss, run backward once, optionally clip gradients, update each parameter under a no-gradient context, and only then begin the next graph. Record loss both before and after the update on the same example. Compare analytical gradients with finite differences in float64 and avoid ReLU's kink during the check. A correct scalar example does not validate broadcasting, batched reductions, or device kernels, so add shape assertions as the implementation grows.

There are two useful failure injections. Replace gradient accumulation by assignment and reuse a weight twice; the shared-path test should fail. Then update a parameter before all backward computations finish; the saved forward values no longer match the mutated model. These bugs explain why mature frameworks track graph versions and separate parameter updates from differentiation.

## References

- [PyTorch autograd mechanics](https://docs.pytorch.org/docs/stable/notes/autograd). Accessed 2026-09-19.
