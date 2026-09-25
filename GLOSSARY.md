# Working glossary

| Term | Meaning used in this book |
| --- | --- |
| Token | One element of a tokenizer-defined sequence, not necessarily a word |
| Token ID | Integer vocabulary index |
| Embedding | Vector representation; distinguish lookup embeddings from contextual states |
| Parameter | Learned persistent model value |
| Activation | Intermediate value computed for an input |
| Logit | Unnormalized score before probability normalization |
| Gradient | Derivative used to guide a parameter update |
| Prefill | Processing input context to prepare generation |
| Decode | Successive autoregressive generation steps |
| KV cache | Reused attention keys and values for previously processed positions |
| B / T / D | Batch size / token sequence length / hidden width |
| H / Hkv / Dh | Query head count / KV head count / per-head dimension |
| FLOP | Floating-point operation; this book counts multiply-add as two unless stated |
| MiB / GiB | 2^20 / 2^30 bytes |
| TTFT | Time to first output token; specify whether queue and network time are included |
| TPOT | Time per output token; specify aggregation and whether prefill is excluded |
| SLO | Operational target for a measured service outcome |

Expand this glossary as chapters are drafted; definitions here are introductory, not substitutes for the detailed chapters.
