"""Deterministic top-k routing accounting used by Chapter 31."""
import numpy as np

def route(logits, k=2, capacity_factor=1.0):
    logits = np.asarray(logits, dtype=np.float64)
    n, experts = logits.shape
    chosen = np.argpartition(logits, -k, axis=1)[:, -k:]
    counts = np.bincount(chosen.ravel(), minlength=experts)
    capacity = int(np.ceil(capacity_factor * n * k / experts))
    overflow = int(np.maximum(counts - capacity, 0).sum())
    mean = counts.mean()
    cv = float(counts.std() / mean) if mean else 0.0
    p = counts / counts.sum()
    entropy = float(-(p[p > 0] * np.log(p[p > 0])).sum())
    return {"counts": counts, "capacity": capacity, "overflow": overflow,
            "coefficient_of_variation": cv, "assignment_entropy": entropy}

if __name__ == "__main__":
    rng = np.random.default_rng(31)
    logits = rng.normal(size=(1000, 8)); logits[:, 0] += 1.5
    for factor in (1.0, 1.25):
        result = route(logits, 2, factor)
        print(factor, {**result, "counts": result["counts"].tolist()})
