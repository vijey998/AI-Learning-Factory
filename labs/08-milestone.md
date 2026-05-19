# 08. KV-cached inference

Status: executable CPU reference. Chapter: CH-50.

## Run

`python code/milestone_labs.py --lab 08`

## Hardware

CPU; optional GPU.

## Deliverable

Add per-layer K/V state and offset-correct position handling.

## Acceptance conditions

Compare cached and uncached logits within tolerance across prompt lengths and generated steps.

## Required experiment record

Environment and revision; input data and licenses; shape/dtype; seeds; correctness checks; warmup and synchronization; elapsed time and memory; measured vs estimated quantities; failures; next experiment.
