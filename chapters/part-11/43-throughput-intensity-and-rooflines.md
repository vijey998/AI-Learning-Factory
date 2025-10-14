# 43. Throughput, Intensity and Rooflines

Status: **Drafted.**

Part 11: GPU Fundamentals

## Learning outcome

Place simplified prefill and decode operations on a roofline under explicit FLOP and byte assumptions.

<a id="t-43-01"></a>
## Compute throughput

Compute throughput is completed operations per second. Peak values assume particular dtypes, instruction forms, clocks, sparsity conditions, and full utilization. A quoted Tensor Core TOPS value cannot be compared directly with FP32 scalar FLOPs unless conventions match.

For matrix multiplication $C_{m\times n}=A_{m\times k}B_{k\times n}$, count about $2mnk$ FLOPs when multiply and add each count as one. Achieved throughput is that count divided by measured kernel time. Report shapes, dtype, and whether time includes data transfer.

<a id="t-43-02"></a>
## Arithmetic intensity

Arithmetic intensity is operations divided by bytes transferred across the memory boundary being analyzed:

$$I=\frac{\text{FLOPs}}{\text{bytes}}.$$

The boundary matters. HBM intensity differs from L2 or shared-memory intensity. For an ideal large GEMM, each matrix is loaded or stored once, giving

$$I\approx\frac{2mnk}{s(mk+kn+mn)},$$

where $s$ is bytes per element. Real traffic includes partial tiles, write allocation, and intermediate operations. Fusion increases intensity when it avoids materializing intermediates.

<a id="t-43-03"></a>
## Compute-bound vs memory-bound

Let peak compute be $P$ FLOP/s and memory bandwidth $W$ bytes/s. The ridge point is $I^*=P/W$. Operations below it cannot feed enough arithmetic and are memory-bound under the model; above it they may be compute-bound.

Suppose $P=300$ TFLOP/s and $W=3$ TB/s. The ridge is 100 FLOP/byte. A kernel at 20 FLOP/byte has bandwidth ceiling $20\times3=60$ TFLOP/s. A kernel at 200 FLOP/byte has roofline ceiling 300 TFLOP/s.

Decode at batch one often has low weight reuse: producing one token reads most weights once for one sequence, so matrix-vector-like work can be memory-bound. Prefill processes many token positions together, turning projections into larger matrix multiplications that reuse weights and increase intensity. “Decode is memory-bound” is conditional: larger batches, quantization, MoE routing, cache operations, and hardware can shift the bottleneck.

<a id="t-43-04"></a>
## Roofline model

The roofline bound is

$$\text{attainable FLOP/s}\le\min(P,WI).$$

Plot achieved throughput against intensity on log axes. The sloped line is the bandwidth roof; the flat line is compute peak. Points far below both roofs suffer other limits: launch overhead, insufficient parallelism, dependencies, divergence, synchronization, or a different bandwidth level.

A roofline is a diagnostic model, not a performance promise. Use measured sustainable bandwidth and relevant instruction throughput when possible. End-to-end Transformer layers mix kernels; plotting only GEMM hides normalization, attention, layout conversions, and CPU gaps.

### Worked prefill/decode comparison

Take a BF16 $4096\times4096$ weight matrix. One token requires about $2\times4096^2=33.6$ MFLOPs and reads roughly 33.6 MB of weights, around 1 FLOP/byte before caches and output traffic. A prefill with 512 token rows performs about 17.2 GFLOPs while the same weights can be reused across rows; idealized weight-only intensity is roughly 512 FLOP/byte. Counting one read of the 4 MiB input, one read of the 32 MiB weight, and one 4 MiB output write gives 40 MiB and about 410 FLOP/byte. Real traffic lowers that number further, yet the contrast explains why prefill more readily reaches compute-oriented kernels.

At batch 16 decode, one weight read serves 16 rows, increasing idealized intensity about sixteenfold. Continuous batching therefore changes both serving efficiency and the hardware regime.

## Four recurring perspectives

- **Follow the Token:** decode handles one new position per sequence while prefill exposes many positions in parallel.
- **Follow the Gradient:** backward operations have different FLOP and byte balances and additional tensor reads/writes.
- **Follow the Byte:** intensity states how much computation each transferred byte enables at a named boundary.
- **Follow the Request:** batching and sequence phase move a request's kernels across the roofline.

## Lab and exit check

Use measured bandwidth and compute peaks for one device. Calculate ideal intensity for a projection at prefill lengths 1, 32, and 512 and decode batches 1, 8, and 32. Plot roofline ceilings, then benchmark actual GEMMs. Explain points below the predicted roof.

## References

- Williams, Waterman, and Patterson, [Roofline: An Insightful Visual Performance Model](https://doi.org/10.1145/1498765.1498785), 2009.
- NVIDIA, [Nsight Compute Roofline Analysis](https://docs.nvidia.com/nsight-compute/ProfilingGuide/index.html#roofline-charts) (version-sensitive; accessed September 2026).
