# Figures

This directory contains publication-ready, code-native SVG diagrams. All dimensions and numeric labels are conceptual unless a caption explicitly identifies a measurement. Regenerate the complete set with:

```bash
python figures/generate_figures.py
```

The generator is the editable source of truth. Each SVG includes a title and description for accessibility, uses a 1200 × 675 view box, and remains legible in grayscale because meaning is carried by labels and geometry as well as color.

## Catalog and chapter mapping

| Figure | Primary chapters | Teaching purpose |
| --- | --- | --- |
| [`01-end-to-end-llm-flow.svg`](01-end-to-end-llm-flow.svg) | 1–3, 49–51 | Follow text through tokenization, tensors, logits, decoding, and autoregressive repetition. |
| [`02-tensor-shape-ledger.svg`](02-tensor-shape-ledger.svg) | 5, 15, 18–20, 23 | Trace `[B,T]`, `[B,T,D]`, attention tensors, and `[B,T,V]` without silently dropping dimensions. |
| [`03-scaled-dot-product-attention.svg`](03-scaled-dot-product-attention.svg) | 17–20 | Separate Q/K routing, V content, scaling, masking, softmax, and weighted retrieval. |
| [`04-transformer-block.svg`](04-transformer-block.svg) | 21–24, 29–30 | Show a pre-norm decoder block and its two residual update paths. |
| [`05-training-loop.svg`](05-training-loop.svg) | 2, 8, 11–12, 25–28 | Distinguish forward, loss, backward, update, checkpoint, and reproducibility state. |
| [`06-kv-cache-lifecycle.svg`](06-kv-cache-lifecycle.svg) | 30, 50, 52–56 | Explain what prefill writes, what decode reads, cache growth, and the exact byte formula. |
| [`07-distributed-parallelism.svg`](07-distributed-parallelism.svg) | 57–60 | Contrast data, tensor, pipeline, and parameter-state sharding with their communication boundaries. |
| [`08-inference-serving.svg`](08-inference-serving.svg) | 54, 61–64 | Follow a request through admission, scheduling, KV allocation, runtime execution, metrics, and streaming. |
| [`09-rag-pipeline.svg`](09-rag-pipeline.svg) | 69–70 | Separate retrieval, authorization, reranking, context packing, generation, and citation verification. |
| [`10-agent-tool-loop.svg`](10-agent-tool-loop.svg) | 71–72, 78 | Show bounded planning, schema validation, authorization, execution, observations, and durable state. |
| [`11-research-evidence-loop.svg`](11-research-evidence-loop.svg) | 35–36, 73–80 | Connect falsifiable claims to preregistration, controls, uncertainty, ablations, and reproduction. |

## Editorial rules

- Keep shape symbols consistent: `B` batch, `T` sequence length, `D` model width, `H` query heads, `Hkv` key/value heads, `dₕ` head width, `L` layers, and `V` vocabulary size.
- State units for measured quantities and label hypothetical numbers as illustrative.
- Preserve SVG text as text; do not convert labels to paths.
- When architecture details vary, say which variant the figure depicts rather than presenting it as universal.
