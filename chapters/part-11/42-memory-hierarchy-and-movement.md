# 42. Memory Hierarchy and Movement

Status: **Drafted.**

Part 11: GPU Fundamentals

## Learning outcome

Draw a tensor's route through storage levels and estimate hard transfer-time lower bounds.

<a id="t-42-01"></a>
## Memory hierarchy

The useful hierarchy spans thread registers, on-chip shared memory and caches, device memory such as HBM or GDDR, host RAM, and SSD or network storage. Capacity generally increases downward while latency and energy per access increase. The exact physical relationship varies by architecture, but the optimization goal is stable: reuse data near compute and avoid unnecessary movement.

Allocation location and access path are different questions. A tensor allocated in HBM may be fetched into L2, then L1 or shared memory, then registers before arithmetic. A performant kernel changes the schedule so each expensive load supports many operations.

<a id="t-42-02"></a>
## Shared memory and SRAM

CUDA shared memory is programmer-managed on-chip storage shared by threads in a block. It is built from SRAM-like on-chip structures and has far lower latency and higher bandwidth than device memory. Tiled matrix multiplication loads submatrices once, synchronizes, reuses them for many multiply-accumulates, then advances.

Shared memory is finite and allocated per block. Large tiles reduce redundant loads but may lower residency. Bank conflicts can serialize accesses when lanes address the same memory bank in incompatible ways. Padding or layout changes can remove conflicts.

<a id="t-42-03"></a>
## Caches

Hardware caches exploit locality automatically. NVIDIA designs commonly expose per-SM L1 behavior and a chip-wide L2, but sizes and policies vary. Cache hit rate alone is not a goal: a streaming kernel may perform well with low reuse, while an apparent high hit rate can hide redundant traffic. Interpret hits with requested bytes, sectors, and runtime.

The KV cache in LLM inference is conceptually unrelated to hardware caches: it is an explicit tensor holding past keys and values, usually in device memory. Hardware caches may temporarily hold pieces of that tensor.

<a id="t-42-04"></a>
## HBM

High Bandwidth Memory places stacked DRAM near the accelerator and uses wide interfaces to provide high aggregate bandwidth. Model weights, activations, KV state, and optimizer tensors usually reside there during computation. “HBM” is often used loosely for device memory, but some GPUs use GDDR; check the product.

HBM is large relative to on-chip SRAM and tiny relative to datasets. Reading a 140 GB BF16 checkpoint once per generated token would already imply enormous traffic; batching is one way to reuse each loaded weight across multiple tokens.

<a id="t-42-05"></a>
## RAM

Host RAM stages datasets and weights and can hold offloaded model state. Transfers to a discrete GPU cross PCIe or another interconnect and are typically much slower than on-device memory traffic. Pinned host memory enables efficient asynchronous DMA but is a limited system resource. Unified virtual addressing does not make bandwidth uniform.

<a id="t-42-06"></a>
## SSD

SSD stores checkpoints and dataset shards. Model startup reads files, may decompress or dequantize them, copies into RAM, and then into device memory. Memory mapping can defer pages, but first access still incurs storage traffic and page faults. Loading a 100 GB checkpoint from an SSD sustaining 5 GB/s has a best-case read time of 20 seconds before parsing and device transfer.

<a id="t-42-07"></a>
## HBM bandwidth

Bandwidth is bytes transferred per second. A lower bound for moving $B$ bytes through a link with sustainable bandwidth $W$ is $t\ge B/W$. Moving 80 GB through a measured 2 TB/s path takes at least 40 ms when both quantities use decimal units. Peak datasheet bandwidth is a ceiling; access patterns, contention, ECC behavior, and controllers reduce achieved bandwidth. Do not silently divide GiB by GB/s: convert both to bytes first.

Read and write traffic both count. For vector addition of three FP32 arrays, each output element requires two 4-byte reads and one 4-byte write: at least 12 bytes for one addition, ignoring cache effects.

<a id="t-42-08"></a>
## Coalescing

Coalescing combines memory requests from neighboring warp lanes into a small number of aligned transactions. If lane $i$ reads `x[base+i]`, accesses are contiguous. If it reads `x[base+i*large_stride]`, the warp may require many transactions and fetch unused bytes. Transposes and tensor layouts therefore change performance without changing FLOP count.

Alignment, element size, cache-line or sector rules, and architecture determine the precise transaction count. Use profiler metrics to verify. A structure-of-arrays layout often coalesces fields better than an array of large structures.

## Four recurring perspectives

- **Follow the Token:** its vector may begin on SSD, be loaded to RAM/HBM, then move through cache, shared memory, and registers.
- **Follow the Gradient:** training adds activation saves, gradient writes, optimizer reads, and parameter writes.
- **Follow the Byte:** calculate compulsory traffic first, then measure how reuse and transactions change it.
- **Follow the Request:** cold loading, cache residency, and offload determine startup and tail latency.

## Lab and exit check

For a 7-billion-parameter BF16 model, calculate the 14.0 GB (about 13.0 GiB) weight payload and lower bounds for SSD-to-RAM, RAM-to-GPU, and one HBM scan using measured bandwidths. Draw the route and label every value GB or GiB. Then compare contiguous and strided vector reads in a profiler and explain transaction efficiency.

## References

- NVIDIA, [CUDA C++ Best Practices Guide](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/) (version-sensitive; accessed September 2026).
- NVIDIA, [CUDA C++ Programming Guide: Memory Hierarchy](https://docs.nvidia.com/cuda/cuda-c-programming-guide/#memory-hierarchy) (accessed September 2026).
