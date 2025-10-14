# 17. Sequence Modeling and the Attention Idea

Status: **Draft — not yet independently reviewed.**

A sequence model must combine information across positions while respecting order and, for generation, causality. Recurrence and attention offer different routes through that problem.

<a id="t-17-01"></a>
## Sequence modeling bottlenecks

To predict the next word in “The keys to the cabinet are…,” a model must preserve which noun controls the verb across intervening words. A fixed-width state may need to carry many facts, and a serial dependency path makes distant learning harder. Any architecture also faces compute and memory limits; attention moves the bottleneck rather than abolishing it.

<a id="t-17-02"></a>
## RNNs

A basic recurrent network updates $h_t=\phi(W_xx_t+W_hh_{t-1}+b)$ and emits from $h_t$. The same parameters are reused at every step. This naturally summarizes a prefix and supports streaming with constant state size, but training unfolds a chain of length $T$. Later states cannot be computed before earlier ones, limiting parallelism. Gradients multiply through recurrent Jacobians, encouraging vanishing or explosion.

With $h_t=0.5h_{t-1}+x_t$ and $h_0=0$, inputs `[2,0,0]` leave states `[2,1,0.5]`: the first input survives but decays. This scalar example makes the compression explicit.

<a id="t-17-03"></a>
## LSTMs

An LSTM adds a cell state and learned gates controlling writing, forgetting, and reading. The cell update $c_t=f_t\odot c_{t-1}+i_t\odot\tilde c_t$ creates a more direct gradient path when forget gates stay near one. It improves long-range learning but remains sequential and does not guarantee indefinite memory. Gates can saturate, state capacity is finite, and all past information is still compressed into fixed-width vectors.

<a id="t-17-04"></a>
## The attention idea

Attention lets each position build a weighted mixture of source states. Rather than asking one recurrent state to preserve everything, the current position scores candidate states, normalizes the scores, and retrieves their values. In self-attention, source and destination positions belong to the same sequence.

This shortens the dependency path between distant tokens: one attention layer can connect them directly. During training, positions can be processed in parallel. The tradeoff is that dense attention compares many pairs and typically has quadratic score storage or work in sequence length.

<a id="t-17-05"></a>
## Content-based retrieval

Suppose a query produces scores `[2,0,-1]` for three earlier states. Softmax yields approximately `[0.844,0.114,0.042]`. If scalar values are `[10,4,-2]`, the retrieved result is about $8.81$. The weights are data-dependent and differentiable, so training can shape both the addressing scheme and retrieved content.

Attention weights are not automatically faithful explanations of model decisions. They show coefficients in one operation; residual paths, value vectors, later layers, and nonlinearities also matter. Causal claims require interventions, not attractive heatmaps.

## Four perspectives

**Follow the Token:** recurrence repeatedly rewrites one summary; attention retrieves from many position states. **Follow the Gradient:** recurrent paths traverse time steps, while attention offers shorter paths but couples many token pairs. **Follow the Byte:** RNN inference holds compact state; attention may retain per-token KV state. **Follow the Request:** recurrent decoding is inherently serial; Transformer prefill parallelizes positions, while autoregressive decode remains sequential across generated tokens.

## Exit check

Calculate the scalar RNN states for `[1,2,3]` with coefficient 0.25. Then choose three values and reproduce the weighted retrieval above. State one advantage and one cost of each mechanism without declaring either universally superior.

## References

- Elman, [Finding Structure in Time](https://doi.org/10.1207/s15516709cog1402_1), 1990.
- Hochreiter and Schmidhuber, [Long Short-Term Memory](https://doi.org/10.1162/neco.1997.9.8.1735), 1997.
- Bahdanau, Cho, and Bengio, [Neural Machine Translation by Jointly Learning to Align and Translate](https://arxiv.org/abs/1409.0473), 2014.
