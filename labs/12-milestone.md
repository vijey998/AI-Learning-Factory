# 12. Local quantized deployment

Status: executable CPU reference; target-device thermal validation remains. Chapter: CH-68.

## Run

`python code/milestone_labs.py --lab 12`

## Hardware

Target CPU laptop; optional GPU/NPU.

## Deliverable

Bundle a pinned model/runtime and an offline runnable entry point.

## Acceptance conditions

Measure cold start, warm latency, memory and sustained thermal behavior; run without network access.

## Required experiment record

Environment and revision; input data and licenses; shape/dtype; seeds; correctness checks; warmup and synchronization; elapsed time and memory; measured vs estimated quantities; failures; next experiment.
