# 08. Gradients, Graphs and Autodiff

Status: **Draft — not yet independently reviewed.**

Training becomes less mysterious when `backward()` is treated as organized chain-rule bookkeeping.

<a id="t-08-01"></a>
## Derivatives

A derivative measures local sensitivity. For $f(x)=x^2$, $df/dx=2x$. At $x=3$, a small change $\Delta x$ changes the output by approximately $6\Delta x$. The approximation improves as the change shrinks, until floating-point cancellation interferes.

<a id="t-08-02"></a>
## Gradients

For scalar loss $L$ and parameter vector $\theta$, the gradient collects partial derivatives: $\nabla_\theta L=[\partial L/\partial\theta_1,\ldots]$. It points toward steepest local increase under the Euclidean metric; gradient descent moves opposite it.

<a id="t-08-03"></a>
## Chain rule

If $y=f(x)$ and $L=g(y)$, then $dL/dx=(dL/dy)(dy/dx)$. Computation graphs apply this locally. For $L=(ab+c)^2$, each operation needs only its inputs and the gradient arriving from downstream.

<a id="t-08-04"></a>
## Computational graphs

A graph node represents a value; an edge records dependency through an operation. Shared values require gradient accumulation. If `a` contributes through two paths, its total derivative is the sum of both path contributions. A topological order ensures downstream gradients arrive before a node propagates backward.

<a id="t-08-05"></a>
## Automatic differentiation

Automatic differentiation applies analytic derivative rules for primitive operations to the executed graph, while the values and derivative calculations remain subject to floating-point rounding. At nondifferentiable points, a library must choose a convention or report that no derivative exists. Autodiff differs from symbolic differentiation, which manipulates formulas, and numerical differentiation, which perturbs inputs.

<a id="t-08-06"></a>
## Reverse-mode autodiff

Reverse mode is efficient when many parameters influence one scalar loss. The forward pass records parents and local backward rules. The backward pass seeds loss gradient 1 and traverses nodes in reverse topological order, accumulating contributions into parents. PyTorch uses reverse automatic differentiation and rebuilds its dynamic graph each iteration.

<a id="t-08-07"></a>
## Finite-difference checks

A centered check estimates $df/dx\approx[f(x+h)-f(x-h)]/(2h)$. Too-large $h$ creates truncation error; too-small $h$ creates rounding and cancellation error. Check smooth toy inputs away from nondifferentiable points, use float64 where possible, and compare relative as well as absolute error.

## The micro-autograd engine

Run:

```bash
python code/micrograd.py
```

For `L=(ab+c)^2` at `a=2,b=-3,c=10`, the intermediate `ab+c=4`, so `L=16`. Analytically: `dL/da=2(4)b=-24`, `dL/db=2(4)a=16`, and `dL/dc=8`. The program checks these values and finite differences.

The engine accumulates with `+=`. Replacing accumulation with assignment fails when a value has multiple children. It also rebuilds the graph for each expression; reusing it after mutating values would no longer describe the executed computation.

## Four perspectives

**Follow the Token:** token losses at many positions reduce to a scalar objective.

**Follow the Gradient:** the scalar seed travels backward through loss, logits, blocks, and parameters.

**Follow the Byte:** saved forward values trade memory for the ability to compute local derivatives; checkpointing later recomputes some values instead.

**Follow the Request:** ordinary serving omits this graph. Accidentally recording it wastes memory even if no optimizer step occurs.

## Exit check

Modify the program to use `L=(a*a)+(a*b)`. Confirm that `a.grad=2a+b`, demonstrating path accumulation. Test finite differences at several values. A passing example supports the implemented primitives; it does not validate a future tensor engine, broadcasting rules, or nondifferentiable operations.

## References

- [PyTorch autograd mechanics](https://docs.pytorch.org/docs/stable/notes/autograd) — dynamic graph construction, saved tensors, reverse-mode behavior, and grad controls. Accessed 2026-09-18.
