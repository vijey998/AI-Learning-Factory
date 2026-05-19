# 11. Multi-GPU execution

Status: executable CPU simulation; multi-GPU validation remains. Chapter: CH-60.

## Run

`python code/milestone_labs.py --lab 11`

## Hardware

At least two supported GPUs for completion; CPU simulation is preparatory.

## Deliverable

Partition or replicate a tiny model and exercise collectives.

## Acceptance conditions

Check distributed output/gradients against single-device reference and inject a worker failure.

## Required experiment record

Environment and revision; input data and licenses; shape/dtype; seeds; correctness checks; warmup and synchronization; elapsed time and memory; measured vs estimated quantities; failures; next experiment.
