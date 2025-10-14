# 68. Packaging, Power and Thermal Limits

Status: **Drafted.**

Part 17: LLMs on Your Laptop

## Learning outcome

Package a reproducible local demo and record sustained latency under thermal load.

## Prerequisites

CH-67.

<a id="t-68-01"></a>
## Power limits

Coverage ID: `T-68-01`.

Power caps determine sustainable clocks and therefore latency. A short benchmark may use burst power unavailable over a long session. Measure wall power when possible and device package power when available, stating the tool and sampling interval. Energy per generated token, joules/token, connects performance to battery and cooling.

Lowering a power limit can sometimes improve efficiency with modest latency cost. Compare a curve of tokens/s and joules/token rather than selecting maximum wattage automatically.

Compute energy over a bounded phase: $E=\int_{t_0}^{t_1}P(t)\,dt$ and joules/token $=E/N_{generated}$. Subtracting idle power answers incremental device energy; retaining it answers wall-energy cost. Report which definition is used, whether display and host power are included, and the uncertainty of low-rate power sensors.

<a id="t-68-02"></a>
## Thermal limits

Coverage ID: `T-68-02`.

Heat accumulates until cooling reaches equilibrium. When temperature or power policy limits are reached, clocks fall. Record cold-start performance and a sustained run long enough to stabilize, with temperature, clocks, power, fan state, and token latency over time.

Laptop position, ambient temperature, power adapter, battery state, and fan mode are test conditions. A five-token demo is not evidence for an hour-long workload.

<a id="t-68-03"></a>
## Model packaging

Coverage ID: `T-68-03`.

A reproducible package contains the executable/runtime, exact model and tokenizer artifacts or an explicit provision step, configuration schema, licenses, checksums, supported hardware matrix, and diagnostics. Keep model data separate from code when size or licensing demands it, but bind them with a signed manifest.

Avoid embedding writable state inside installation directories. Version logs, caches, conversation data, and models independently. Startup should verify compatibility before allocating scarce memory.

<a id="t-68-04"></a>
## Offline deployment

Coverage ID: `T-68-04`.

Offline means every runtime dependency, artifact, trust root, and recovery tool is available without a network. Build on a connected staging system, generate a software bill of materials and hashes, scan, sign, then transfer through the approved channel. Installation should verify signatures and free-space requirements.

Include rollback and uninstall. Logs must avoid secrets and have bounded retention. Exercise installation on a clean offline machine; developer laptops often conceal cached libraries and drivers.

<a id="t-68-05"></a>
## Edge distillation

Coverage ID: `T-68-05`.

Distillation trains a smaller student to imitate teacher outputs or internal distributions, often mixing hard labels with soft targets. It can preserve more task capability than simply choosing an untrained small model. The student still needs independent evaluation for quality, calibration, robustness, and domain shift.

Teacher-generated data can carry teacher errors and licensing/privacy constraints. Record prompts, filtering, temperature, objective, and data provenance. Distillation changes learning; quantization changes representation. They may be combined but solve different problems.

<a id="t-68-06"></a>
## Dynamic edge computation

Coverage ID: `T-68-06`.

Dynamic computation adapts work to request difficulty or device state: early exit, speculative decoding, retrieval routing, model cascades, context truncation policies, or feature degradation under thermal pressure. A controller needs observable signals and safe bounds.

Optimization must include controller errors. An early-exit confidence threshold can be overconfident out of domain; a cascade can spend more energy after escalation than a single larger call. Evaluate total quality, latency, energy, and escalation rate by workload slice. During thermal stress, prefer explicit degraded modes over unpredictable throttling.

## Four recurring perspectives

- **Follow the Token:** trace the representation and its ownership across the execution boundary.
- **Follow the Gradient:** identify synchronized or sharded learning state; for inference-only paths, state explicitly that no gradient exists.
- **Follow the Byte:** calculate persistent state, temporary buffers, transfers, and the relevant bandwidth tier.
- **Follow the Request:** include admission, scheduling, cancellation, failure, and externally visible latency.

## Lab and exit check

Create an offline package with manifest, hashes, configuration, license inventory, diagnostic command, rollback, and clean uninstall. On a clean target, measure startup, first token, steady decode, peak memory, package power, temperature, clocks, and latency for at least 30 minutes. Compare two power modes and document thermal steady state. Validate one corrupt-artifact and one interrupted-install recovery.

Acceptance requires that the package installs with networking disabled and an empty application cache. Re-run the artifact hash and license inventory from the transferred bundle rather than trusting the staging machine's manifest.

## Primary references

- [NIST Secure Software Development Framework](https://csrc.nist.gov/pubs/sp/800/218/final), accessed 2026-09-19.
- Hinton et al., [Distilling the Knowledge in a Neural Network](https://arxiv.org/abs/1503.02531), 2015.
- [SPDX specification](https://spdx.github.io/spdx-spec/), accessed 2026-09-19.
