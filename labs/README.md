# Milestone labs

All fifteen milestones now have deterministic executable reference implementations in `code/milestone_labs.py`. Run one with `python code/milestone_labs.py --lab 01`, or generate the complete experiment record with `python code/milestone_labs.py --lab all --output build/milestone-labs.json`.

CPU-feasible labs execute real reference computations. Hardware-specific labs provide explicitly labeled CPU simulations whose remaining target-device validation is tracked below; simulated timings are never presented as accelerator measurements.

| Milestone | Chapter | Reference status | Target hardware |
| --- | --- | --- | --- |
| [01. Tokenizer from scratch](01-milestone.md) | CH-13 | Executable CPU reference | CPU |
| [02. Micro autograd engine](02-milestone.md) | CH-08 | Executable CPU reference | CPU |
| [03. Self-attention from scratch](03-milestone.md) | CH-19 | Executable CPU reference | CPU; optional GPU |
| [04. GPT from scratch](04-milestone.md) | CH-24 | Executable CPU reference | CPU; optional GPU |
| [05. Train a tiny language model](05-milestone.md) | CH-28 | Executable CPU smoke test | GPU optional for longer runs |
| [06. Profile FLOPs and memory](06-milestone.md) | CH-44 | Executable CPU measurement | GPU required for device results |
| [07. Simple Triton kernel](07-milestone.md) | CH-46 | CPU simulation | Supported GPU and pinned Triton |
| [08. KV-cached inference](08-milestone.md) | CH-50 | Executable CPU reference | CPU; optional GPU |
| [09. Quantize the model](09-milestone.md) | CH-56 | Executable CPU reference | Backend-dependent GPU optional |
| [10. Continuous-batching server](10-milestone.md) | CH-61 | Deterministic scheduler simulation | Model-serving backend |
| [11. Multi-GPU execution](11-milestone.md) | CH-60 | Communication simulation | At least two supported GPUs |
| [12. Local quantized deployment](12-milestone.md) | CH-68 | Executable local reference | Target CPU laptop; optional GPU/NPU |
| [13. Probe hidden representations](13-milestone.md) | CH-74 | Executable CPU toy model | GPU optional |
| [14. Reproduce a paper](14-milestone.md) | CH-79 | Executable reproduction protocol | Depends on selected paper |
| [15. Original experiment](15-milestone.md) | CH-80 | Deterministic experiment simulation | Target chosen after profiling |
