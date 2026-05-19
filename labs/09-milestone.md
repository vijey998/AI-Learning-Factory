# 09. Quantize the model

Status: executable CPU reference. Chapter: CH-56.

## Run

`python code/milestone_labs.py --lab 09`

## Hardware

CPU; backend-dependent GPU optional.

## Deliverable

Quantize toy weights and then the tiny model with documented scales and grouping.

## Acceptance conditions

Report real packed size plus metadata, error, held-out loss and measured latency; no assumed speedup.

## Required experiment record

Environment and revision; input data and licenses; shape/dtype; seeds; correctness checks; warmup and synchronization; elapsed time and memory; measured vs estimated quantities; failures; next experiment.
