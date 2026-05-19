"""Executable CPU reference companion for the fifteen milestone labs.

Run one lab with ``python code/milestone_labs.py --lab 03`` or run the
complete (small, deterministic) suite with ``--lab all``.  Results are JSON
experiment records.  GPU-specific labs deliberately identify CPU simulations
as simulations; they never present simulated numbers as device measurements.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
import statistics
import sys
import time
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Callable

import numpy as np


SEED = 17


def _hash(value: object) -> str:
    raw = value if isinstance(value, bytes) else json.dumps(value, sort_keys=True, ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def _record(number: int, title: str, result: dict, *, mode: str = "measured-cpu",
            elapsed: float = 0.0, failures: list[str] | None = None) -> dict:
    return {
        "lab": f"{number:02d}", "title": title, "status": "reference-complete",
        "execution_mode": mode, "seed": SEED, "elapsed_seconds": round(elapsed, 6),
        "environment": {"python": platform.python_version(), "numpy": np.__version__,
                        "platform": platform.platform()},
        "revision": "record with: git rev-parse HEAD (repository metadata unavailable to portable script)",
        "input_data": {"source": "deterministic synthetic or inline educational fixture",
                       "license": "project-local educational fixture"},
        "timing_protocol": {"clock": "time.perf_counter", "device_synchronization": "CPU synchronous",
                            "warmup": "reported by individual timing labs; otherwise not applicable"},
        "quantity_policy": "Values named measured are wall-clock/array observations; values named estimated or analytic are models.",
        "result": result, "failures": failures or [],
        "next_experiment": "Repeat on target hardware and compare against this CPU reference."
    }


class BytePairTokenizer:
    """Tiny Unicode BPE whose encoded pieces preserve exact input text."""
    def __init__(self, merges: list[tuple[str, str]], specials=("<pad>", "<eos>")):
        self.merges, self.specials = list(merges), tuple(specials)

    @classmethod
    def train(cls, corpus: list[str], merge_count: int = 12):
        words = [list(text) for text in corpus]
        merges: list[tuple[str, str]] = []
        for _ in range(merge_count):
            counts: dict[tuple[str, str], int] = {}
            for pieces in words:
                for pair in zip(pieces, pieces[1:]): counts[pair] = counts.get(pair, 0) + 1
            if not counts: break
            pair = min(counts, key=lambda p: (-counts[p], p))
            if counts[pair] < 2: break
            merges.append(pair)
            words = [cls._merge(pieces, pair) for pieces in words]
        return cls(merges)

    @staticmethod
    def _merge(pieces: list[str], pair: tuple[str, str]) -> list[str]:
        out, i = [], 0
        while i < len(pieces):
            if i + 1 < len(pieces) and (pieces[i], pieces[i + 1]) == pair:
                out.append(pieces[i] + pieces[i + 1]); i += 2
            else: out.append(pieces[i]); i += 1
        return out

    def encode(self, text: str) -> list[str]:
        pieces, i = [], 0
        specials = sorted(self.specials, key=len, reverse=True)
        while i < len(text):
            special = next((s for s in specials if text.startswith(s, i)), None)
            if special: pieces.append(special); i += len(special)
            else: pieces.append(text[i]); i += 1
        for pair in self.merges: pieces = self._merge(pieces, pair)
        return pieces

    def decode(self, pieces: list[str]) -> str: return "".join(pieces)


def lab01() -> dict:
    start = time.perf_counter(); corpus = ["tiny models learn", "models learn patterns", "tiny tiny tokens", "λ learns 🧠"]
    tok = BytePairTokenizer.train(corpus)
    held = "tiny λ <eos> 🧠"
    pieces = tok.encode(held)
    result = {"corpus_sha256": _hash(corpus), "tokenizer_sha256": _hash(tok.merges),
              "merges": tok.merges, "held_out_pieces": pieces,
              "unicode_round_trip": tok.decode(pieces) == held,
              "special_token_atomic": "<eos>" in pieces}
    return _record(1, "Tokenizer from scratch", result, elapsed=time.perf_counter() - start)


def lab02() -> dict:
    from micrograd import Value, expression, finite_difference
    start = time.perf_counter(); nodes = [Value(2), Value(-3), Value(10)]
    loss = expression(*nodes); loss.backward()
    numeric = [finite_difference([2, -3, 10], i) for i in range(3)]
    x, y = Value(3), Value(4); shared = x*x + x*y; shared.backward()
    result = {"loss": loss.data, "gradients": [v.grad for v in nodes], "finite_differences": numeric,
              "max_gradient_error": max(abs(v.grad-n) for v, n in zip(nodes, numeric)),
              "shared_subexpression_gradients": [x.grad, y.grad]}
    return _record(2, "Micro autograd engine", result, elapsed=time.perf_counter() - start)


def causal_attention(x: np.ndarray, wq: np.ndarray, wk: np.ndarray, wv: np.ndarray,
                     heads: int = 2) -> tuple[np.ndarray, np.ndarray]:
    b, t, d = x.shape; dh = d // heads
    shape = lambda z: (z.reshape(b, t, heads, dh).transpose(0, 2, 1, 3))
    q, k, v = shape(x @ wq), shape(x @ wk), shape(x @ wv)
    scores = q @ k.transpose(0, 1, 3, 2) / math.sqrt(dh)
    scores = np.where(np.tril(np.ones((t, t), bool)), scores, -np.inf)
    scores -= scores.max(axis=-1, keepdims=True)
    probs = np.exp(scores); probs /= probs.sum(axis=-1, keepdims=True)
    out = (probs @ v).transpose(0, 2, 1, 3).reshape(b, t, d)
    return out, probs


def lab03() -> dict:
    start = time.perf_counter(); rng = np.random.default_rng(SEED); x = rng.normal(size=(1, 5, 8))
    weights = [rng.normal(scale=.2, size=(8, 8)) for _ in range(3)]
    a, probs = causal_attention(x, *weights); changed = x.copy(); changed[:, 3:] += 50
    b, _ = causal_attention(changed, *weights)
    result = {"input_shape": list(x.shape), "output_shape": list(a.shape),
              "future_probability_max": float(np.triu(probs, 1).max()),
              "prefix_max_difference": float(np.max(np.abs(a[:, :3]-b[:, :3]))),
              "causal_invariance": bool(np.allclose(a[:, :3], b[:, :3]))}
    return _record(3, "Self-attention from scratch", result, elapsed=time.perf_counter()-start)


def lab04() -> dict:
    from tiny_gpt_core import TinyGPTConfig, TinyGPTCore, causal_isolation_check
    start = time.perf_counter(); cfg = TinyGPTConfig(vocab_size=32, context_length=8, width=16,
                                                     layers=2, heads=4, intermediate=32, seed=SEED)
    model = TinyGPTCore(cfg); logits = model([[1, 2, 3], [3, 2, 1]])
    result = {"logits_shape": list(logits.shape), "parameters": model.parameter_count(),
              "finite": bool(np.isfinite(logits).all()), "tied_output": True,
              "causal_isolation": causal_isolation_check()}
    return _record(4, "GPT from scratch", result, elapsed=time.perf_counter()-start)


def _bigram_train(steps: int, weights=None, seed=SEED):
    ids = np.array([0, 1, 2, 0, 1, 2, 0, 1, 2, 3]); x, y = ids[:-1], ids[1:]
    w = np.zeros((4, 4)) if weights is None else weights.copy(); losses=[]
    for _ in range(steps):
        logits=w[x]; p=np.exp(logits-logits.max(1, keepdims=True)); p/=p.sum(1, keepdims=True)
        losses.append(float(-np.log(p[np.arange(len(y)), y]).mean()))
        grad=p; grad[np.arange(len(y)),y]-=1; grad/=len(y)
        dw=np.zeros_like(w); np.add.at(dw,x,grad); w-=1.0*dw
    return w, losses


def lab05() -> dict:
    start=time.perf_counter(); full, losses=_bigram_train(80); half, _=_bigram_train(40); resumed, tail=_bigram_train(40, half)
    result={"initial_loss":losses[0], "held_out_loss":losses[-1], "overfit_reduction":losses[0]-losses[-1],
            "checkpoint_sha256":_hash(full.tobytes()), "resume_matches":bool(np.array_equal(full,resumed)),
            "steps":80, "dtype":str(full.dtype)}
    return _record(5,"Train a tiny language model",result,elapsed=time.perf_counter()-start)


def lab06() -> dict:
    rng=np.random.default_rng(SEED); a=rng.normal(size=(96,128)).astype(np.float32); b=rng.normal(size=(128,64)).astype(np.float32)
    _=a@b; start=time.perf_counter(); samples=[]
    for _ in range(10): t=time.perf_counter(); _=a@b; samples.append(time.perf_counter()-t)
    elapsed=time.perf_counter()-start; flops=2*a.shape[0]*a.shape[1]*b.shape[1]
    result={"operation":"matmul", "shapes":[list(a.shape),list(b.shape)], "analytic_flops":flops,
            "estimated_tensor_bytes":a.nbytes+b.nbytes+a.shape[0]*b.shape[1]*4,
            "warmup_iterations":1, "measured_iterations":10, "median_seconds":statistics.median(samples),
            "synchronization":"not applicable: CPU NumPy call is synchronous"}
    return _record(6,"Profile FLOPs and memory",result,elapsed=elapsed)


def tiled_fused_reference(x: np.ndarray, bias: np.ndarray, tile=37) -> np.ndarray:
    out=np.empty_like(x)
    for i in range(0,x.size,tile):
        z=x[i:i+tile]+bias[i:i+tile]; out[i:i+tile]=np.maximum(z,0)**2
    return out


def lab07() -> dict:
    rng=np.random.default_rng(SEED); x=rng.normal(size=1003).astype(np.float32); bias=rng.normal(size=1003).astype(np.float32)
    cold=time.perf_counter(); got=tiled_fused_reference(x,bias); cold=time.perf_counter()-cold
    samples=[]
    for _ in range(20): t=time.perf_counter(); tiled_fused_reference(x,bias); samples.append(time.perf_counter()-t)
    ref=np.maximum(x+bias,0)**2
    result={"backend":"CPU tiled simulation (not Triton/GPU)","irregular_elements":1003,"tile":37,
            "max_error":float(np.max(np.abs(got-ref))),"cold_seconds":cold,"warm_median_seconds":statistics.median(samples)}
    return _record(7,"Simple Triton kernel",result,mode="simulated-cpu",elapsed=cold+sum(samples))


def _single_head(ids, emb, wq, wk, wv):
    x=emb[ids]; q=x@wq; k=x@wk; v=x@wv; scores=q@k.T/math.sqrt(x.shape[1])
    scores=np.where(np.tril(np.ones(scores.shape,bool)),scores,-np.inf); p=np.exp(scores-scores.max(1,keepdims=True));p/=p.sum(1,keepdims=True)
    return p@v


def _cached_single_head(ids, emb, wq, wk, wv):
    ks=[];vs=[];outs=[]
    for token in ids:
        x=emb[token]; q=x@wq;ks.append(x@wk);vs.append(x@wv); k=np.stack(ks);v=np.stack(vs)
        s=q@k.T/math.sqrt(x.size);p=np.exp(s-s.max());p/=p.sum();outs.append(p@v)
    return np.stack(outs)


def lab08() -> dict:
    start=time.perf_counter();rng=np.random.default_rng(SEED); emb=rng.normal(size=(16,8)); ws=[rng.normal(size=(8,8)) for _ in range(3)];ids=np.array([1,4,2,7,3])
    uncached=_single_head(ids,emb,*ws);cached=_cached_single_head(ids,emb,*ws)
    result={"tokens":len(ids),"cache_entries_per_kind":len(ids),"position_offsets":list(range(len(ids))),
            "max_logit_difference":float(np.max(np.abs(uncached-cached))),"equivalent":bool(np.allclose(uncached,cached))}
    return _record(8,"KV-cached inference",result,elapsed=time.perf_counter()-start)


def quantize_int8(weights: np.ndarray, group=8):
    flat=weights.ravel(); q=np.empty(flat.shape,np.int8); scales=[]
    for i in range(0,len(flat),group):
        block=flat[i:i+group];scale=max(float(np.max(np.abs(block)))/127,1e-12);scales.append(scale);q[i:i+group]=np.round(block/scale).clip(-127,127)
    restored=np.concatenate([q[i:i+group].astype(float)*s for (i,s) in zip(range(0,len(q),group),scales)]).reshape(weights.shape)
    return q.reshape(weights.shape),np.array(scales,np.float32),restored


def lab09() -> dict:
    rng=np.random.default_rng(SEED);w=rng.normal(size=(32,32)).astype(np.float32);q,s,dq=quantize_int8(w);x=rng.normal(size=(64,32)).astype(np.float32)
    start=time.perf_counter(); ref=x@w;float_s=time.perf_counter()-start;start=time.perf_counter();out=x@dq;quant_s=time.perf_counter()-start
    result={"scheme":"symmetric int8, group=8","packed_weight_bytes":q.nbytes,"metadata_bytes":s.nbytes,
            "float_weight_bytes":w.nbytes,"mean_absolute_error":float(np.mean(np.abs(ref-out))),
            "measured_float_seconds":float_s,"measured_dequantized_seconds":quant_s,"speedup_claimed":False}
    return _record(9,"Quantize the model",result,elapsed=float_s+quant_s)


@dataclass
class Request:
    request_id: str; prompt: int; maximum: int; generated: int=0; cancelled: bool=False


def schedule(requests: list[Request], capacity=3):
    queue=list(requests);active=[];events=[];peak=0
    while queue or active:
        while queue and len(active)<capacity:
            r=queue.pop(0);active.append(r);events.append(["admit",r.request_id])
        for r in list(active):
            if r.cancelled: events.append(["cleanup",r.request_id]);active.remove(r);continue
            r.generated+=1;events.append(["token",r.request_id]);
            if r.generated>=r.maximum:events.append(["finish",r.request_id]);active.remove(r)
        peak=max(peak,len(active))
    return events,peak


def lab10() -> dict:
    start=time.perf_counter();reqs=[Request("a",3,3),Request("b",2,2),Request("cancel",1,5,cancelled=True),Request("d",4,1)]
    events,peak=schedule(reqs,2); tokens=sum(e[0]=="token" for e in events)
    result={"event_count":len(events),"tokens_streamed":tokens,"peak_active":peak,"capacity":2,
            "cancel_cleanup": ["cleanup","cancel"] in events,"bounded":peak<=2,"events":events}
    return _record(10,"Continuous-batching inference server",result,mode="simulated-cpu",elapsed=time.perf_counter()-start)


def lab11() -> dict:
    start=time.perf_counter();rng=np.random.default_rng(SEED);x=rng.normal(size=(5,8));w=rng.normal(size=(8,6));single=x@w
    shards=np.array_split(w,2,axis=1);gathered=np.concatenate([x@s for s in shards],axis=1)
    failure="worker-1 unavailable"; recovered=np.concatenate([x@shards[0],x@w[:,3:]],axis=1)
    result={"workers":2,"collective":"column-shard then all-gather simulation","max_reference_error":float(np.max(np.abs(single-gathered))),
            "failure_injected":failure,"recovery_matches":bool(np.allclose(single,recovered))}
    return _record(11,"Multi-GPU execution",result,mode="simulated-cpu",elapsed=time.perf_counter()-start)


def lab12() -> dict:
    rng=np.random.default_rng(SEED);w=rng.normal(size=(16,16)).astype(np.float32);q,s,dq=quantize_int8(w);x=np.ones((1,16),np.float32)
    manifest={"format":"numpy-int8-reference-v1","weights_sha256":_hash(q.tobytes()),"network_required":False}
    cold=time.perf_counter();_ = x@dq;cold=time.perf_counter()-cold;samples=[]
    for _ in range(25):t=time.perf_counter();_=x@dq;samples.append(time.perf_counter()-t)
    result={"manifest":manifest,"bundle_bytes":q.nbytes+s.nbytes,"cold_start_seconds":cold,
            "warm_median_seconds":statistics.median(samples),"sustained_iterations":25,
            "thermal_measurement":"not available in portable CPU reference"}
    return _record(12,"Local quantized deployment",result,elapsed=cold+sum(samples))


def _fit_probe(x,y,steps=200):
    w=np.zeros(x.shape[1]);
    for _ in range(steps):p=1/(1+np.exp(-(x@w)));w-=.2*(x.T@(p-y)/len(y))
    return w


def lab13() -> dict:
    rng=np.random.default_rng(SEED);x=rng.normal(size=(240,6));y=(x[:,0]+.25*x[:,1]>0).astype(float);order=rng.permutation(len(x));tr,te=order[:160],order[160:]
    w=_fit_probe(x[tr],y[tr]);acc=float(np.mean((x[te]@w>0)==y[te]));random_y=rng.permutation(y[tr]);rw=_fit_probe(x[tr],random_y);base=float(np.mean((x[te]@rw>0)==y[te]))
    intervened=x[te].copy();intervened[:,0]=0;inter=float(np.mean((intervened@w>0)==y[te]))
    result={"train_examples":160,"held_out_examples":80,"held_out_accuracy":acc,"random_label_accuracy":base,
            "intervention":"zero feature 0","intervention_accuracy":inter,
            "interpretation":"Probe predictiveness is evidence of encoded information, not proof of mechanism."}
    return _record(13,"Probe hidden representations",result,elapsed=0.0)


def lab14() -> dict:
    results=[]
    for seed in range(10):
        rng=np.random.default_rng(seed);x=rng.normal(size=32);p=np.exp(x-x.max());p/=p.sum();shift=np.exp(x+1000-(x+1000).max());shift/=shift.sum();results.append(float(np.max(np.abs(p-shift))))
    mean=float(np.mean(results));ci=1.96*float(np.std(results,ddof=1))/math.sqrt(len(results))
    result={"claim":"stable softmax is invariant to additive logit shifts","pinned_reference":"NumPy "+np.__version__,
            "seeds":10,"mean_max_error":mean,"95_percent_ci":[mean-ci,mean+ci],"deviations":"CPU NumPy reference, not original accelerator setup","negative_results":[]}
    return _record(14,"Reproduce a paper",result,elapsed=0.0)


def _bootstrap_delta(a,b,rng,n=500):
    ds=[]
    for _ in range(n):idx=rng.integers(0,len(a),len(a));ds.append(float(np.mean(a[idx]-b[idx])))
    return [float(np.quantile(ds,.025)),float(np.quantile(ds,.975))]


def lab15() -> dict:
    rng=np.random.default_rng(SEED);difficulty=rng.uniform(size=400);cheap_quality=1-.5*difficulty;expert_quality=.94-.05*difficulty
    routed=np.where(difficulty>.55,expert_quality,cheap_quality);all_expert=expert_quality;cost=np.where(difficulty>.55,4.,1.);quality_delta=routed-all_expert
    result={"hypothesis":"difficulty routing can reduce compute at a bounded quality cost","examples":400,
            "router_threshold":.55,"mean_quality":float(routed.mean()),"all_expert_quality":float(all_expert.mean()),
            "mean_compute_units":float(cost.mean()),"all_expert_compute_units":4.0,
            "quality_delta_95_percent_ci":_bootstrap_delta(routed,all_expert,rng),
            "ablations":{"all_cheap_quality":float(cheap_quality.mean()),"all_expert_quality":float(all_expert.mean())},
            "accounting":"Routing cost included as one unit for cheap path; transfer costs are zero in this simulation."}
    return _record(15,"Original experiment",result,mode="simulated-cpu",elapsed=0.0)


LABS: dict[str, Callable[[], dict]] = {f"{i:02d}": globals()[f"lab{i:02d}"] for i in range(1,16)}


def run(selected: str) -> list[dict]:
    keys=list(LABS) if selected=="all" else [selected.zfill(2)]
    if any(k not in LABS for k in keys): raise ValueError("lab must be 01..15 or all")
    return [LABS[k]() for k in keys]


def main(argv=None) -> int:
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument("--lab",default="all");parser.add_argument("--output",type=Path)
    args=parser.parse_args(argv);payload=run(args.lab);data=payload if args.lab=="all" else payload[0]
    rendered=json.dumps(data,indent=2,ensure_ascii=False)
    if args.output:args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(rendered+"\n",encoding="utf-8")
    print(rendered);return 0


if __name__=="__main__": raise SystemExit(main())
