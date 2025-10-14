# 04. Building Our Tiny Laboratory

Status: **Draft — not yet independently reviewed.**

The book’s laboratory has one purpose: make claims executable. We begin with a CPU-only standard-library baseline so every reader can run the first experiments. NumPy, PyTorch, profilers, accelerators, and notebooks are added when a chapter needs them and pinned when introduced.

<a id="t-04-01"></a>
## Python

Use Python 3.10 or newer for the starter project. Run commands from the repository root so relative paths are stable. A virtual environment isolates project packages from unrelated applications:

```bash
python -m venv .venv
```

Activate it with `.venv/bin/activate` on common POSIX shells or `.venv\Scripts\Activate.ps1` in PowerShell. Activation is a convenience, not a requirement; invoking the environment’s Python executable directly is more explicit. Python’s documentation describes virtual environments as disposable and non-portable, so record dependencies and recreate them rather than copying the environment directory.

The current starter has no third-party dependencies. That is deliberate: `python code/resource_lab.py` should run before package installation succeeds. Later chapters will add a lockable research environment for NumPy, PyTorch, plotting, and optional GPU tools.

<a id="t-04-02"></a>
## NumPy

NumPy will be our transparent array workbench. It makes shapes, strides, broadcasting, matrix multiplication and dtype effects visible without the training framework’s module system. We will use it for small reference implementations, never as proof that a GPU kernel behaves the same way.

When NumPy is introduced, print its version and array dtype in experiment output. Default dtypes can differ across libraries and operations. An unnoticed `float64` reference compared with a `float16` implementation can make accuracy and memory conclusions misleading.

<a id="t-04-03"></a>
## PyTorch

PyTorch will carry the main training implementation because it combines tensor operations, automatic differentiation, neural-network modules, compilation, and device backends. We will first build important pieces ourselves, then compare them with framework implementations.

Version pins matter. Operator semantics, compiler behavior, supported dtypes, and kernels change. Every measured result must record the PyTorch version, device backend, and model configuration. A code snippet that was correct under one pinned revision is not a timeless benchmark.

Keep three controls distinct:

- `model.train()` and `model.eval()` control module behavior.
- grad mode, `no_grad`, and inference mode control autograd recording.
- the optimizer step changes parameters.

Confusing them is a reliable way to produce silent evaluation errors.

<a id="t-04-04"></a>
## Notebooks

Notebooks are useful for explanation and exploration, but hidden state makes them poor sole records of an experiment. A cell can depend on variables created by an earlier execution order that the displayed document no longer reflects.

Put reusable logic in importable modules. A notebook should orchestrate an experiment, visualize results, and state conclusions. Before accepting a result, restart the kernel and run all cells from top to bottom. For automated validation, expose a script or test that does not require clicking through a notebook.

<a id="t-04-05"></a>
## Profiling tools

Begin with the least invasive measurement that answers the question. Wall-clock timing tells you user-visible duration. Operator profilers attribute framework time. System profilers reveal CPU scheduling and device activity. Kernel profilers expose launches, occupancy and memory behavior.

Every profiler perturbs execution. Warmup, asynchronous devices, compilation, clock changes, and background work can overwhelm the effect being measured. Later GPU labs require synchronization around timed regions and separate cold from steady-state measurements.

A profile is a trace of a workload under stated conditions. It does not prove that the same bottleneck exists at another batch size, sequence length, concurrency, dtype, or device.

<a id="t-04-06"></a>
## CPU baseline

Run the included baseline:

```bash
python code/resource_lab.py
```

It demonstrates stable softmax, seeded sampling, tensor payload storage, linear-layer FLOP accounting, and KV-cache byte accounting. It labels its logits as illustrative because they do not come from a trained model.

Then run the tests:

```bash
python -m unittest discover -s tests -v
```

A CPU reference gives us something portable to compare against. It is not a performance proxy for a GPU. When an accelerated implementation arrives, compare correctness first, then performance under a workload that actually uses the target hardware.

<a id="t-04-07"></a>
## Seeds and environment records

A seed controls a pseudorandom stream; it does not freeze every source of variation. Parallel reductions, nondeterministic kernels, library algorithms, compiler decisions, data order, and hardware can still differ. Record the seed because it enables investigation, not because it guarantees identical floating-point bits.

Create an environment record:

```bash
python code/environment_record.py > build/environment.json
```

The record includes Python, platform, processor information, project revision when available, and installed packages. It intentionally avoids environment variables because they can contain credentials. Add model, dataset and accelerator metadata to each experiment record rather than pretending one machine-level file describes every run.

## Minimal experiment protocol

1. State the hypothesis and the metric before running.
2. Record code revision, environment, input shapes, dtypes, seeds, and workload.
3. Establish a correctness reference and tolerance.
4. Separate setup, compilation, warmup, measurement, and teardown.
5. Repeat enough times to expose variability; report the aggregation method.
6. Save raw observations, including failures.
7. Change one factor at a time or use an explicit experimental design.
8. Report what the result does and does not support.

For example, “the fused implementation is 1.3× faster” is incomplete. Faster for which shapes, device, dtype, warmup, number of repetitions, and correctness tolerance? Did compilation time count? Did quality change? The laboratory exists to force those questions into the record.

## Four perspectives

**Follow the Token:** save small inputs and expected outputs so transformations can be inspected.

**Follow the Gradient:** use finite differences or a trusted reference on smooth toy cases before trusting training.

**Follow the Byte:** derive ideal payload size, then measure process or device memory and explain the gap.

**Follow the Request:** measure end-to-end behavior separately from isolated operators and preserve queueing/concurrency conditions.

## Exit artifact

Run the baseline and tests, create `build/environment.json`, and write a short experiment note containing: hypothesis, command, expected result, actual result, and one limitation. If another person cannot identify what ran, the experiment is not reproducible enough for this book.

## References

- [Python virtual environments](https://docs.python.org/3.12/library/venv.html) — creation, isolation, activation, and portability constraints. Accessed 2026-09-18.
- [PyTorch autograd mechanics](https://docs.pytorch.org/docs/stable/notes/autograd) — graph recording and grad-mode semantics. Accessed 2026-09-18.
