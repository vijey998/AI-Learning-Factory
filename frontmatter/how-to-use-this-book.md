# How to Use This Book {-}

Each chapter states an outcome, prerequisites, the mechanism, four operational perspectives, and an exit check. Readers new to the field should follow the numbered order through the first ten parts. Readers focused on systems can begin with Parts 11-17 after reviewing the tensor, attention, Transformer, and inference foundations. Researchers can use Parts 18-20 as a map, but should retain the evaluation and systems chapters: a novel mechanism without a fair measurement protocol is merely an anecdote with equations.

The four recurring perspectives are:

- **Follow the Token:** what representation exists at each boundary and which other tokens can influence it.
- **Follow the Gradient:** which parameters receive learning signal, what state the optimizer retains, and where training can become unstable.
- **Follow the Byte:** where weights, activations, caches, gradients, and optimizer state reside and move.
- **Follow the Request:** how online execution schedules, isolates, observes, and recovers a user's workload.

Notation is local to each chapter unless explicitly carried forward. Shapes use `B` for batch size, `T` for sequence length, `D` for model width, `H` for attention heads, and `V` for vocabulary size. Binary memory quantities use KiB, MiB, and GiB; decimal device specifications use KB, MB, and GB. FLOP counts state the multiply-add convention when it affects comparisons.

The companion repository contains executable reference implementations, milestone labs, tests, editable figures, coverage records, and reproducible PDF/HTML build commands. Measurements marked as simulated are teaching models, not hardware benchmark results.

