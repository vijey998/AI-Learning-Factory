# 10. Continuous-batching inference server

Status: executable CPU simulation; model-backend integration remains. Chapter: CH-61.

## Run

`python code/milestone_labs.py --lab 10`

## Hardware

CPU simulation then model backend.

## Deliverable

Implement admission, prefill/decode scheduling, streaming and cancellation.

## Acceptance conditions

Compare with serial execution; test cancellation cleanup and memory bounds; report tails under load.

## Required experiment record

Environment and revision; input data and licenses; shape/dtype; seeds; correctness checks; warmup and synchronization; elapsed time and memory; measured vs estimated quantities; failures; next experiment.
