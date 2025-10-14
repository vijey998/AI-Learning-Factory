# 47. Graphs, Compilers and Runtimes

Status: **Drafted**

## From Python to device code

The goal is to trace a function through capture, intermediate representations (IR), lowering, generated kernels, and execution.

<a id="t-47-01"></a>
## PyTorch eager execution

Eager Python runs operator by operator. Each call performs framework dispatch, selects an implementation, and may launch GPU work. It is interactive and debuggable, but sees only local operations, which limits fusion and repeats host overhead.

<a id="t-47-02"></a>
## Computational graph capture

Capture turns a region of dynamic execution into a graph of tensor operations plus assumptions called guards. Explicit dependencies permit fusion, constant propagation, layout selection, and memory planning. This differs from the autograd graph: one records executable tensor programs, the other derivative dependencies.

<a id="t-47-03"></a>
## TorchDynamo

TorchDynamo observes Python frames and extracts compatible operations into FX graphs while preserving semantics through guards. A guard can assert dtype, rank, device, a global value, or a shape relationship. If later inputs violate guards, the system can recompile or fall back. Data-dependent control, unsupported extensions, and side effects can end a captured region.

<a id="t-47-04"></a>
## Intermediate representation

FX is a relatively high-level IR; later IRs express loops, indexing, memory, and device choices. Multiple levels let one pass reason about algebra while another schedules hardware work. “The compiler optimized it” is incomplete: ask which IR, transformation, and artifact.

<a id="t-47-05"></a>
## torch.compile

torch.compile(model) is the user entry point. Behavior depends on PyTorch version, backend, mode, dynamic-shape setting, model, and inputs. The first call can be much slower because capture and compilation occur. Benchmark cold startup separately and exercise all expected shape families.

<a id="t-47-06"></a>
## Inductor

TorchInductor is the default PyTorch compiler backend for supported workloads. It lowers graphs, schedules loops, fuses work, and emits target code—often Triton for GPU regions and vectorized C++ for CPU. Calls may remain external where mature libraries win.

<a id="t-47-07"></a>
## Generated kernels

For layer_norm(x+bias), eager execution may materialize x+b before normalization. A compiler may fuse addition and plan buffers. Inspect code and traces: graph count, kernel count, bytes, and latency reveal whether fusion occurred. Compare numerics on representative extremes because reassociation changes rounding.

<a id="t-47-08"></a>
## Compiler graph breaks

A graph break returns control to Python, then capture may resume. Frequent breaks reduce optimization. A **recompile storm** from varying shapes or Python values is worse. Use diagnostics and decide whether shapes should be static, symbolic, padded, or bucketed.

For example, a service that specializes independently for sequence lengths 1 through 2048 can pay 2,048 compilation costs and retain as many artifacts. Bucketing to powers of two needs 12 length families but adds padding; symbolic shapes may use fewer artifacts but can restrict scheduling choices. Record the number of unique graphs and cumulative compilation time under a production-shaped trace, not just one warmed input.

## Four perspectives and exit check

- **Follow the Token:** identical tensor semantics pass through several program representations.
- **Follow the Gradient:** AOTAutograd can stage forward and backward graphs; saved tensors affect memory.
- **Follow the Byte:** fusion matters when it removes allocations and HBM traffic.
- **Follow the Request:** guards decide reuse, recompilation, or fallback.

Compile a two-layer MLP with two shape families, inspect its graph, count breaks, recompilations, guards, and kernels, and report cold versus warm time. Add a third shape that violates a guard and predict whether it recompiles or falls back before observing the trace. Failures include hiding breaks, timing compilation as inference, excessive specialization, mutation, unsupported operators, and assuming compiled is always faster.

## Primary references

- PyTorch, [TorchDynamo overview](https://docs.pytorch.org/docs/stable/torch.compiler_dynamo_overview.html), version-sensitive; accessed 2026-09-19.
- PyTorch, [`torch.compile` programming model](https://docs.pytorch.org/docs/stable/torch.compiler.html), version-sensitive; accessed 2026-09-19.
- PyTorch, [FX documentation](https://docs.pytorch.org/docs/stable/fx.html), version-sensitive; accessed 2026-09-19.
- PyTorch, [TorchInductor documentation](https://docs.pytorch.org/docs/stable/torch.compiler_inductor.html), version-sensitive; accessed 2026-09-19. Pin PyTorch release or commit, backend, flags, CUDA/Triton, model revision, and inputs.
