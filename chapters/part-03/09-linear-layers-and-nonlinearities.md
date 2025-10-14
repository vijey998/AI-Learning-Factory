# 09. Linear Layers and Nonlinearities

Status: **Draft — not yet independently reviewed.**

A neural network begins with a modest operation: mix input coordinates, shift the result, then bend it. The bend is what lets depth create functions a single affine map cannot express.

<a id="t-09-01"></a>
## Linear layers

For an input row vector $x\in\mathbb{R}^{D_{in}}$, a layer computes $z=xW+b$, with $W\in\mathbb{R}^{D_{in}\times D_{out}}$. A batch $X\in\mathbb{R}^{B\times D_{in}}$ produces $Z\in\mathbb{R}^{B\times D_{out}}$. Each output coordinate is a learned weighted sum of every input coordinate.

Strictly, $xW+b$ is *affine* when $b\ne0$, though libraries call it linear. Two such layers without an activation collapse: $(xW_1+b_1)W_2+b_2=x(W_1W_2)+(b_1W_2+b_2)$. Depth alone adds no new function class.

<a id="t-09-02"></a>
## Biases

The bias moves a decision boundary away from the origin. For one feature, $z=2x-3$ crosses zero at $x=1.5$; without the bias it must cross at zero. In batched code the same bias vector is broadcast across rows. A common bug is to give each example its own bias, changing both meaning and parameter count.

<a id="t-09-03"></a>
## Nonlinearities

An activation $a=\phi(z)$ prevents adjacent affine maps from collapsing. With enough hidden units, bent regions can approximate curved functions and disconnected decision regions. It does not create information: if a projection destroyed a distinction, an activation cannot recover it.

<a id="t-09-04"></a>
## ReLU

$\operatorname{ReLU}(z)=\max(0,z)$ is cheap and has derivative 1 for positive inputs and 0 for negative inputs. It creates piecewise-linear networks. At zero, frameworks choose a subgradient convention. A unit that remains negative for all data receives zero upstream gradient and may become a “dead” unit.

Worked example: $x=[2,-1]$, $W=\begin{bmatrix}1&-2\\3&1\end{bmatrix}$, and $b=[0,1]$ give $z=[-1,-4]$ and ReLU output $[0,0]$. The shape is correct, but this particular example sends no gradient through either activation.

<a id="t-09-05"></a>
## GELU

GELU scales rather than sharply gates: $\operatorname{GELU}(x)=x\Phi(x)$, where $\Phi$ is the standard-normal CDF. Negative values can survive weakly, and the derivative changes smoothly. Transformer implementations often use an exact or tanh-based approximation; mixing variants can cause small reproducibility differences.

<a id="t-09-06"></a>
## Parameter shapes and cost

The layer has $D_{in}D_{out}+D_{out}$ trainable scalars. With $D_{in}=768$, $D_{out}=3072$, BF16 parameters occupy about 4.72 MB (decimal), before gradients or optimizer state. A forward batch costs roughly $2BD_{in}D_{out}$ FLOPs if a multiply and add count as two.

## Four perspectives

**Follow the Token:** one token state of width $D_{in}$ becomes a state of width $D_{out}$. **Follow the Gradient:** $\partial L/\partial W=X^T(\partial L/\partial Z)$ and bias gradients sum across the batch. **Follow the Byte:** weights are reused across examples; their movement can dominate small batches. **Follow the Request:** inference applies identical learned parameters to each request and stores no optimizer state.

## Exit check

Prove algebraically that three affine layers collapse to one. Then sketch a two-ReLU construction for a one-dimensional “tent” function. Explain why a wrong bias shape might run successfully under broadcasting while learning the wrong model.

## A nonlinear test case

The XOR dataset makes the limitation visible: inputs `(0,0)` and `(1,1)` share class 0, while `(0,1)` and `(1,0)` share class 1. No single line separates those pairs. A two-layer network can create hidden half-spaces and combine them into the required disconnected region. When testing an implementation, compare a linear classifier against the same training loop with a hidden activation, repeat across seeds, and report both optimization failures and successful fits. One lucky run is not an architectural proof; the geometry establishes impossibility for the linear model, while repeated execution checks the code.

## References

- [PyTorch `Linear`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Linear.html) and [activation functions](https://docs.pytorch.org/docs/stable/nn.functional.html). Accessed 2026-09-19.
- Hendrycks and Gimpel, [Gaussian Error Linear Units](https://arxiv.org/abs/1606.08415), 2016.
