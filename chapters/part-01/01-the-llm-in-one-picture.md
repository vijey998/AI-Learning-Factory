# 01. The LLM in One Picture

Status: **Draft — not yet technically reviewed.**

The purpose of this chapter is to let you trace a piece of text through a language model without treating any stage as magic. We will use a decoder-only Transformer as our running example. Other language-model families arrive in Chapter 29. You do not need calculus yet; you need to distinguish a symbol, an array of numbers and a probability distribution.

## The machine we are building

Imagine sending the text “The sky is” to a model. Its next output could be “blue,” but the model does not first construct an English sentence and then reveal it. In the autoregressive setup used here, one forward pass produces scores for possible next tokens. A decoding policy selects a token. The selected token is appended to the context, and the process repeats.

This already separates three jobs: encoding the input, computing predictions and deciding what to emit. A tokenizer, a neural network and a decoding policy perform those jobs. An application may add messages, tools, retrieval and a user interface around them. Those surrounding components matter, but they are not interchangeable with the model's weights.

<a id="t-01-01"></a>
## 1. Prompt: the input context

The prompt is the input presented to the model. In a chat application, the visible message may be only part of that input: a template may include role markers and previous messages. For now, our entire prompt is “The sky is.”

Be careful with the word *context*. At the text level it means the material supplied to the model. Later, at the tensor level, it also determines a sequence length. We will write that length as T. T counts tokens, not words or characters.

<a id="t-01-02"></a>
## 2. Tokenizer: text becomes integer IDs

A tokenizer converts text into a sequence of token IDs. For illustration, suppose our tokenizer produces `[17, 42, 9]`. These numbers are invented, not the encoding of any published tokenizer. A real tokenizer might split the same text differently, including spaces inside token pieces.

An ID is a lookup index. ID 42 is not twice as meaningful as ID 21. Treating token IDs as ordinary scalar measurements would impose a numerical relationship that the vocabulary does not promise.

Tokenization also defines the available output pieces. Some pieces correspond to complete words, some to word fragments or bytes, and some to special control markers. We will implement a tokenizer in Chapter 13 rather than assuming every token is a word.

<a id="t-01-03"></a>
## 3. Embeddings: IDs become vectors

Suppose the vocabulary has V entries and each embedding has D numbers. The token embedding table then has shape `[V, D]`. For every input ID, the model selects one row. Our three input IDs become an array of shape `[3, D]`.

With a batch dimension B, the usual conceptual shape is `[B, T, D]`. For B=1, T=3 and D=4, there are twelve numbers. D=4 is deliberately tiny; it makes the array easy to picture. We are describing dimensions, not recommending a useful model size.

The lookup vectors are learned parameters. They are not a hand-written dictionary of concepts. Position information also has to enter the computation, although the mechanism depends on the architecture. Some models add positional vectors; others apply position-dependent transformations inside attention. Chapter 16 separates these choices.

<a id="t-01-04"></a>
## 4. Transformer: context changes the representation

Transformer blocks transform the vectors. In our causal model, the representation at a position can use that position and earlier positions, but not later ones. Attention mixes information across the allowed positions. Feed-forward layers transform information within each position; residual connections and normalization support the overall computation.

The result is a sequence of contextual hidden states. The vector associated with “is” now depends on the preceding context, rather than being only the embedding-table row for that token. That is why we distinguish an input embedding from a contextual hidden state.

We will not pretend that each coordinate corresponds to a neat human concept such as “sky-ness.” A vector's usefulness is established by what the model does with it. Later chapters investigate internal representations with experiments instead of assigning meanings by intuition.

For this chapter, imagine each block accepts `[B, T, D]` and returns `[B, T, D]`. Keeping the outside shape constant does not mean the inside is cheap: attention projections, score arrays and expanded feed-forward layers may have different shapes and costs.

<a id="t-01-05"></a>
## 5. Logits: one score per vocabulary entry

At the final position, the model has a hidden vector of length D. A vocabulary projection turns it into V scores, called logits. Logits are unrestricted real numbers. They are not probabilities and need not sum to one.

Consider a deliberately tiny output vocabulary with four choices:

| Token | Logit | Softmax probability, rounded |
| --- | --- | --- |
| blue | 2.0 | 0.644 |
| green | 1.0 | 0.237 |
| clear | 0.0 | 0.087 |
| end marker | -1.0 | 0.032 |

These illustrative scores were chosen by hand. Softmax converts them to positive values whose sum is one. Its formula is `p[i] = exp(z[i]) / sum(exp(z[j]))`. Subtracting the largest logit before exponentiation gives the same mathematical distribution and avoids unnecessarily large exponentials. The accompanying CPU lab demonstrates this.

A training forward pass commonly produces logits at every position, with conceptual shape `[B, T, V]`. For choosing the next token after our prompt, only the last position's distribution is needed. Implementations may exploit that distinction to avoid work.

<a id="t-01-06"></a>
## 6. Sampling: choosing is separate from scoring

Greedy decoding selects the highest-scoring token: “blue” in the table. Sampling instead draws from a distribution, so it can select “green” even though “blue” is more likely. Temperature and filtering policies can modify the distribution before the draw. We will derive their behavior in Chapter 51.

The distinction matters when debugging. Two different outputs do not by themselves establish that the model's parameters changed. The decoding policy or its random draws may differ. Conversely, a fluent output is not proof that a claim is true: the scores predict token continuations, not a guaranteed factual verdict.

<a id="t-01-07"></a>
## 7. Output tokens: append and repeat

After selecting “blue,” append its ID to the sequence. The next prediction is conditioned on this longer sequence. Generation continues until a stopping condition is met, such as an end marker or a length limit. The output IDs are decoded to text for display.

A simple implementation can recompute the full growing sequence at every step. A more efficient implementation reuses cached state. Chapter 50 explains precisely what a KV cache stores and why it is valid. You do not need the cache to understand the logical operation: select a token, extend the context, predict again.

Tokens and displayed words need not align one-for-one. A fragment may complete a word from an earlier token. This is one reason tokens per second and words per second are different measurements.

<a id="t-01-08"></a>
## 8. What the model predicts

At step $t$, the model represents $P(x_t\mid x_{<t})$: a conditional distribution for the next token given previous tokens. For a fixed token sequence, the probability chain rule gives $P(x_{1:T})=\prod_{t=1}^{T}P(x_t\mid x_{<t})$. This factorization is exact; the modeling choice is how the network parameterizes each conditional distribution. Training and generation use the relationship in different ways.

During training, known sequences supply target next tokens. A loss measures how poorly the predictions fit those targets, and gradients guide parameter updates. During ordinary inference, the parameters remain fixed while the input and temporary state change. Inference can produce new text without performing a training update.

This is the central distinction to carry forward: hidden states can change for every request while the learned weights remain the same.

## Four ways to follow the same operation

**Follow the Token.** Text becomes IDs, lookup vectors, contextual states, vocabulary scores and another token ID. Track which representation is present at each stage.

**Follow the Gradient.** During training, a loss on predicted tokens leads back through the vocabulary projection and Transformer to trainable parameters. Ordinary inference does not need this backward pass. We will build it in Chapter 8 before relying on a framework's automatic differentiation.

**Follow the Byte.** A tensor's shape and numeric format determine its ideal storage. Our `[1,3,4]` array contains twelve values; at two bytes each it uses 24 bytes for its payload. Actual programs also allocate weights, temporary arrays, caches and bookkeeping. Counting only one visible array does not give total memory use.

**Follow the Request.** A user request can wait in a queue before the model runs. Its tokens may then be processed alongside other requests and streamed back incrementally. Thus a fast matrix multiplication does not automatically imply a fast user-visible response.

## First experiment

From the project root, run:

```bash
python code/resource_lab.py
```

The program does not run a trained Transformer. It makes the score-to-probability-to-token step executable and checks the first resource calculations. Change the logits and observe both the greedy choice and the probability distribution. Add 10,000 to every logit; the stable softmax should preserve the probabilities.

Then answer these questions before reading the answers:

1. Does token ID 42 mean something is quantitatively larger than token ID 17?
2. Where does `[B,T,D]` become scores over the vocabulary?
3. If sampling emits a different token on another run, must the weights have changed?
4. How many payload bytes does `[1024,4096]` require in BF16?
5. Does appending a token require retraining the model?

Answers: (1) No; IDs are indices. (2) At the vocabulary projection or LM head. (3) No; randomness and decoding choices can change the output. (4) 8,388,608 bytes, which is 8 MiB; this excludes metadata and other tensors. (5) No; the next forward computation uses the extended context with the same weights.

## What comes next

Chapter 2 separates the complete training and inference lifecycles. Chapter 5 turns shape and byte tracking into a habit. The rest of the book progressively replaces each box in this chapter with equations, runnable implementations and measured behavior.

Editorial note: this is an original introductory draft with a locally tested numerical example. It has not received an independent human technical review.

## References

- Vaswani et al., [Attention Is All You Need](https://arxiv.org/abs/1706.03762), 2017 — Transformer architecture and scaled dot-product attention.
- Sutskever, Vinyals, and Le, [Sequence to Sequence Learning with Neural Networks](https://arxiv.org/abs/1409.3215), 2014 — autoregressive sequence factorization and decoding.
