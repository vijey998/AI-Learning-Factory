# 56. Quantization Across the Inference Path

Status: **Drafted**

## Representing useful signal with fewer bits

Quantization maps real values to a finite codebook. For affine uniform quantization, \(q=clip(round(x/s)+z)\) and reconstruction is \(\hat{x}=s(q-z)\). Scale s and zero point z may be per tensor, channel, group, or token. Fewer bits reduce storage and bandwidth only when kernels execute the format efficiently.

<a id="t-56-01"></a>
## Quantization error and a worked matrix

For symmetric signed n-bit quantization with Q=2^(n-1)-1, choose s=max|x|/Q, q=round(x/s), and reconstruct sq. On values [-1.0,-0.2,0.3,0.9] with INT4, Q=7 and s=1/7, codes are [-7,-1,2,6], reconstructing [-1,-0.143,0.286,0.857]. The maximum absolute error is about 0.057 and the MSE is about 0.00133. Four packed codes occupy 2 bytes; one FP16 scale makes this toy group 4 bytes total, only 2x smaller than its 8-byte BF16 source rather than the payload-only 4x. Real packing may add alignment and padding.

<a id="t-56-02"></a>
## Post-training quantization

PTQ calibrates or quantizes a pretrained model without full retraining. Weight-only PTQ may need no activation dataset; activation quantization needs representative calibration. Outliers and domain shift can destroy accuracy. Calibration set, objective, group size, clipping, and kernel backend are part of the method.

<a id="t-56-03"></a>
## Quantization-aware training

QAT simulates quantize/dequantize effects during training, often with a straight-through estimator for rounding. It can adapt weights to error and support harder activation formats, at training cost and with approximation in the backward pass. QAT is not guaranteed to beat a strong PTQ pipeline.

<a id="t-56-04"></a>
## GPTQ

GPTQ is a layerwise post-training weight quantization method using approximate second-order information to quantize weights while compensating error in remaining weights. Results depend on calibration data, ordering, damping, group size, and implementation. The artifact still requires a matching runtime kernel.

<a id="t-56-05"></a>
## AWQ

Activation-aware Weight Quantization observes that a small fraction of weight channels are especially important relative to activation magnitudes. It searches scaling that protects salient weights while enabling low-bit weight-only execution. It is also calibration- and backend-dependent; “AWQ 4-bit” does not uniquely specify a format or speed.

<a id="t-56-06"></a>
## Weight quantization

Weight-only INT4 can shrink the dominant model residency and reduce weight bandwidth during decode. Scales, zero points, packing, group metadata, padding, and sometimes full-precision outliers add overhead. Dequantization may fuse into GEMM; otherwise conversion traffic can erase gains.

<a id="t-56-07"></a>
## Activation quantization

Activations vary by token and contain outliers. INT8 schemes use static calibration or dynamic per-token/per-channel scales. Dynamic scaling costs reductions and metadata but adapts to inputs. SmoothQuant-like methods move quantization difficulty between activations and weights through equivalent scaling. Validate residual paths and normalization, not only linear layers.

<a id="t-56-08"></a>
## KV quantization

KV cache grows with context and concurrency, so FP8/INT8/INT4 caches can unlock capacity. Error affects attention repeatedly over future tokens. Keys influence similarity scores; values influence weighted sums. Granularity, asymmetric ranges, outlier handling, and dequantization inside attention matter. Evaluate long-context quality, retrieval, and generation, not short perplexity alone.

<a id="t-56-09"></a>
## FP8 inference

FP8 formats trade exponent range against mantissa precision, commonly E4M3- and E5M2-like variants. Hardware and frameworks may use scaling recipes and higher-precision accumulation. “FP8” must state format, scale granularity, accumulation, and which tensors remain higher precision.

<a id="t-56-10"></a>
## INT8 inference

INT8 offers mature matrix instructions on many platforms and often supports weight-and-activation quantization. Effective compression versus BF16 is near 2x before metadata, but realized latency varies with shape and conversion overhead.

<a id="t-56-11"></a>
## INT4 inference

INT4 halves packed weight bytes again, but representational error, packing, scale overhead, and hardware support become more important. Weight-only INT4 is more common than fully INT4 activation paths. Small batches can benefit from bandwidth reduction; large prefill may be compute-bound and see different gains.

<a id="t-56-12"></a>
## GGUF formats

GGUF is a versioned container used by the ggml/llama.cpp ecosystem for tensors and metadata. It can hold many quantization types; the extension alone does not mean “4-bit.” Tokenizer metadata, architecture fields, tensor types, and runtime support must agree. Keep the original model license and provenance, and pin converter/runtime commits.

## Four perspectives, validation, and exit check

- **Follow the Token:** its activations are scaled, rounded, accumulated, and reconstructed along the path.
- **Follow the Gradient:** PTQ has no model training; QAT inserts simulated error into forward training.
- **Follow the Byte:** count packed payload plus scales, zeros, padding, and temporary dequantized buffers.
- **Follow the Request:** lower residency raises concurrency, but conversion and quality constraints shape latency.

Quantize a tiny matrix per tensor and per row; report reconstruction metrics, physical bytes, and downstream matmul error. Then evaluate a pinned model on perplexity plus task and long-context sets at matched prompts. Failures include file-size-only accounting, comparing different kernels, calibration leakage, unspecified group size, and claiming universal quality from one benchmark.

## Primary references

- Frantar et al., [GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers](https://arxiv.org/abs/2210.17323), 2022.
- Lin et al., [AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration](https://arxiv.org/abs/2306.00978), 2023.
- Xiao et al., [SmoothQuant: Accurate and Efficient Post-Training Quantization for Large Language Models](https://arxiv.org/abs/2211.10438), 2022.
- Open Compute Project, [8-bit Floating Point Specification](https://www.opencompute.org/documents/ocp-8-bit-floating-point-specification-ofp8-revision-1-0-2023-06-20-pdf), revision 1.0, 2023; and ggml-org, [llama.cpp source and GGUF implementation](https://github.com/ggml-org/llama.cpp), version-sensitive; accessed 2026-09-19. Pin method implementation, commit, model and calibration data, quantization type and group size, hardware, and kernels.
