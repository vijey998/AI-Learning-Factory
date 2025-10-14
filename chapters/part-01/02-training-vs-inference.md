# 02. Training vs Inference

Status: **Draft — not yet independently reviewed.**

A language model has two main operating modes. **Training** changes learned parameters so future predictions improve under an objective. **Inference** uses fixed parameters to compute predictions for new input. Both modes can run the same forward equations; their state, memory needs, and purpose differ.

<a id="t-02-01"></a>
## Training versus inference

Let a model with parameters $\theta$ receive tokens $x$ and return logits $f_\theta(x)$. During training, known target tokens $y$ let us compute a scalar loss:

$$L(\theta)=\operatorname{CrossEntropy}(f_\theta(x),y).$$

A backward pass computes gradients $\nabla_\theta L$. An optimizer uses those gradients and its own state to produce new parameters. One simplified SGD update is

$$\theta_{k+1}=\theta_k-\eta\nabla_\theta L,$$

where $\eta$ is the learning rate. AdamW is more involved, but the defining point remains: training includes a parameter update.

Inference stops after the forward computation and a decoding decision. The weights normally remain unchanged. The prompt grows during autoregressive generation, and temporary activations and caches change, but those changes do not mean the model learned.

| Stage | Training | Autoregressive inference |
| --- | --- | --- |
| Input | Training sequences and targets | Prompt plus generated tokens |
| Forward pass | Yes | Yes |
| Loss | Usually | Usually absent |
| Backward graph | Yes for paths to trainable parameters; frozen subgraphs may avoid it | Unnecessary |
| Optimizer step | Yes | No |
| Persistent weight change | Yes | No |
| Sampling | Optional for evaluation | Common for generation |

The word *evaluation* creates a common ambiguity. Evaluating validation loss uses inference-like execution because parameters do not update, even though the output is a loss rather than generated prose. Benchmark generation is also evaluation. The mode is defined by state changes and graph requirements, not by whether a human sees text.

<a id="t-02-02"></a>
## Parameters versus activations

**Parameters** are persistent learned tensors: embedding tables, attention projections, feed-forward matrices, normalization scales, and similar values. They are shared across requests until a training or editing procedure changes them.

**Activations** are values computed for particular inputs: embeddings selected for this batch, attention results, residual states, and logits. A new request creates new activations. Training often retains selected activations or equivalent information because the backward pass needs them. This is a major reason a model that fits for inference can require far more memory for training.

Training also introduces persistent optimizer state and transient gradients. For Adam-like optimization, each trainable parameter commonly has a gradient and two moment estimates in addition to the parameter itself. Exact storage depends on precision, sharding, optimizer variant, and implementation, so “four times the model size” is a rough story rather than a universal law.

Inference has different growing state. During generation, a decoder can retain attention keys and values for processed positions. This KV cache is request-specific. It can become the dominant memory consumer at long contexts or high concurrency while the model weights remain fixed.

Classify each tensor by asking two questions:

1. Does it survive after this request or training step?
2. Does it describe learned behavior, optimizer history, or this input’s computation?

That avoids vague labels such as “model memory,” which can hide weights, caches, allocator reservations, and temporary workspaces inside one number.

<a id="t-02-03"></a>
## Loss versus generated text

A loss is a numerical objective. Generated text is the consequence of repeatedly selecting tokens from predicted distributions. These are related, but neither substitutes for the other.

Suppose the correct next token has probability 0.8. Its negative log-likelihood is about 0.223. If its probability is 0.2, the loss is about 1.609. Training can use this smooth signal even when the greedy choice is unchanged. Conversely, a model can generate a plausible sentence while assigning poor probabilities across a broad held-out corpus.

Loss is normally computed with teacher forcing: at each training position, the model receives the true preceding tokens. During free-running generation, it receives its own selected tokens. One early mistake can therefore change all later contexts. This difference helps explain why a modest validation-loss improvement and a visible generation improvement need not move together.

Perplexity, benchmark scores, task success, factuality, safety, latency, and human preference measure different properties. “The loss went down” is evidence about the specified objective and data distribution; it is not a universal quality certificate.

<a id="t-02-04"></a>
## Learning versus execution

Execution means running an existing computation. Learning means changing persistent state according to data and an objective. A retrieval system can improve an answer by adding documents without changing model parameters. A longer prompt can alter behavior without training. A tool result can correct a calculation without being stored in the model. These are execution-time interventions.

Fine-tuning changes some or all trainable parameters. LoRA training changes small adapter parameters while the base weights remain frozen. Prompt tuning may train persistent prompt vectors. In-context learning changes the model’s behavior through context while leaving its parameters fixed. The same word *learning* is sometimes used for all of these; the state table tells you what actually happened.

Framework controls must also be kept separate. In PyTorch, `model.eval()` changes the behavior of modules such as dropout or batch normalization; it does **not** disable gradient recording. `torch.no_grad()` and inference mode control autograd recording. PyTorch’s autograd documentation states that the dynamic graph is rebuilt on each iteration and that inference mode avoids additional tracking with restrictions on later autograd use. These are execution controls, not optimizer steps.

## Trace one training step

For a batch of token sequences:

1. Read parameters $\theta_k$ and optimizer state.
2. Build activations and logits in the forward pass.
3. Compare logits with targets to compute loss.
4. Traverse the recorded graph backward to accumulate parameter gradients.
5. Apply clipping or scaling if configured.
6. Update optimizer state and produce $\theta_{k+1}$.
7. Clear or reset gradients before the next accumulation window.

For one inference request:

1. Read fixed parameters $\theta$.
2. Tokenize the prompt and build activations.
3. Produce logits and select a token.
4. Append the token and update request-local cache state.
5. Repeat until a stopping condition.
6. Release request-local state.

The same matrix multiplications can appear in both lists. The backward graph, optimizer, and persistent update make training a different system.

## Four perspectives

**Follow the Token:** training consumes known next-token targets; generation feeds selected tokens back as new input.

**Follow the Gradient:** only training needs the gradient path to parameters. Frozen parameters can participate in a forward and still receive no stored gradient.

**Follow the Byte:** training retains backward information, gradients, and optimizer state; inference retains request activations and often a KV cache.

**Follow the Request:** a production request should not silently mutate shared weights. Online adaptation, when desired, must be an explicit isolated workflow with versioning and rollback.

## Exit check

For each item, label it persistent or request/step-local, then say whether it changes during ordinary inference: model weights, prompt IDs, hidden activations, KV cache, parameter gradients, Adam moments, random-generator state. The answer depends on the boundary you choose, so state the boundary. For a single request: weights and optimizer state are persistent; prompt IDs, activations, and KV cache are local; gradients are absent; random state advances if sampling uses it.

## References

- [PyTorch autograd mechanics](https://docs.pytorch.org/docs/stable/notes/autograd) — dynamic graphs, saved tensors, grad modes, and the distinction between evaluation mode and gradient control. Accessed 2026-09-18.
