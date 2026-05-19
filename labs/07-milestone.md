# 07. Simple Triton kernel

Status: executable CPU simulation; target GPU validation remains. Chapter: CH-46.

## Run

`python code/milestone_labs.py --lab 07`

## Hardware

Supported GPU and pinned Triton environment.

## Deliverable

Implement fused elementwise operations, then a tiled operation.

## Acceptance conditions

Compare output tolerance against a reference across irregular sizes; report warm and cold timing.

## Required experiment record

Environment and revision; input data and licenses; shape/dtype; seeds; correctness checks; warmup and synchronization; elapsed time and memory; measured vs estimated quantities; failures; next experiment.
