#!/usr/bin/env python3
"""Generate the book's publication SVG figures from one consistent source."""

from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent
W, H = 1200, 675


def start(title, desc):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="675" viewBox="0 0 1200 675" role="img" aria-labelledby="title desc">
  <title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc>
  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L0,6 L9,3 z" fill="#24364b"/></marker>
    <style>
      .bg{{fill:#fbfcfe}} .box{{fill:#eef4fb;stroke:#315a84;stroke-width:2}} .accent{{fill:#e8f6ef;stroke:#28755a;stroke-width:2}}
      .warm{{fill:#fff3e4;stroke:#9a5c13;stroke-width:2}} .muted{{fill:#f4f1f8;stroke:#6a5681;stroke-width:2}}
      .line{{fill:none;stroke:#24364b;stroke-width:2.4;marker-end:url(#arrow)}} .dash{{fill:none;stroke:#56697d;stroke-width:2;stroke-dasharray:8 6;marker-end:url(#arrow)}}
      .title{{font:700 30px system-ui,sans-serif;fill:#172536}} .label{{font:600 19px system-ui,sans-serif;fill:#172536}} .small{{font:16px system-ui,sans-serif;fill:#33475b}}
      .tiny{{font:14px ui-monospace,monospace;fill:#33475b}} .math{{font:17px ui-monospace,monospace;fill:#172536}} .note{{font:italic 15px system-ui,sans-serif;fill:#56697d}}
    </style>
  </defs><rect class="bg" width="1200" height="675"/><text class="title" x="56" y="55">{escape(title)}</text>'''


def box(x, y, w, h, title, detail="", cls="box"):
    detail_lines = detail.split("\n") if detail else []
    out = [f'<rect class="{cls}" x="{x}" y="{y}" width="{w}" height="{h}" rx="12"/>',
           f'<text class="label" x="{x+w/2}" y="{y+31}" text-anchor="middle">{escape(title)}</text>']
    for i, line in enumerate(detail_lines):
        out.append(f'<text class="tiny" x="{x+w/2}" y="{y+57+i*21}" text-anchor="middle">{escape(line)}</text>')
    return "".join(out)


def arrow(x1, y1, x2, y2, dashed=False):
    return f'<path class="{"dash" if dashed else "line"}" d="M{x1} {y1} L{x2} {y2}"/>'


def label(x, y, text, anchor="middle", cls="small"):
    return f'<text class="{cls}" x="{x}" y="{y}" text-anchor="{anchor}">{escape(text)}</text>'


def finish(parts, note=""):
    if note:
        parts.append(label(600, 646, note, cls="note"))
    return "\n".join(parts) + "\n</svg>\n"


def write(name, title, desc, parts, note=""):
    (OUT / name).write_text(start(title, desc) + "\n" + finish(parts, note), encoding="utf-8")


def main():
    p=[]
    xs=[55,245,435,625,815,1005]; names=[("Text","UTF-8"),("Tokenizer","IDs [T]"),("Embedding","[B,T,D]"),("Transformer ×L","[B,T,D]"),("LM head","[B,T,V]"),("Decoder","next ID")]
    for i,(n,d) in enumerate(names):
        p.append(box(xs[i],150,140,105,n,d,["warm","box","accent","muted","box","warm"][i]));
        if i<5:p.append(arrow(xs[i]+140,202,xs[i+1],202))
    p += [arrow(1075,255,1075,360), box(935,360,280,95,"Append token","context length T → T+1","accent"),
          arrow(935,407,125,407), box(55,360,185,95,"Repeat forward","weights unchanged","muted")]
    write("01-end-to-end-llm-flow.svg","End-to-end autoregressive LLM flow","Text becomes token IDs, tensors, logits, and an appended next token in a repeated inference loop.",p,"Shapes are conceptual; B=batch, T=sequence, D=model width, V=vocabulary.")

    p=[]
    stages=[(55,150,170,"IDs","[B,T]"),(270,150,190,"Embedding","[V,D] lookup"),(510,150,180,"Hidden","[B,T,D]"),(745,150,180,"Projection","[D,V]"),(975,150,170,"Logits","[B,T,V]")]
    for i,(x,y,w,n,d) in enumerate(stages):
        p.append(box(x,y,w,100,n,d,["warm","box","accent","box","warm"][i]));
        if i<len(stages)-1:p.append(arrow(x+w,200,stages[i+1][0],200))
    p += [box(130,355,220,100,"Q, K, V","[B,H,T,dₕ]","box"),box(490,355,220,100,"Scores","[B,H,T,T]","warm"),box(850,355,220,100,"Head output","[B,H,T,dₕ]","accent"),
          arrow(350,405,490,405),arrow(710,405,850,405),label(420,385,"QKᵀ"),label(780,385,"softmax · V"),label(600,520,"D = H·dₕ; payload bytes = element count × bytes/element",cls="math")]
    write("02-tensor-shape-ledger.svg","Tensor shape ledger","A shape trace from IDs through embeddings and attention to vocabulary logits, including attention score dimensions.",p,"Preserve the outer [B,T,D] shape across a Transformer block; internal tensors differ.")

    p=[]
    p += [box(55,135,190,95,"Input X","[B,T,D]","accent"),box(325,115,190,75,"Q = XWQ","[B,H,T,dₕ]"),box(325,215,190,75,"K = XWK","[B,H,T,dₕ]"),box(325,315,190,75,"V = XWV","[B,H,T,dᵥ]"),
          box(590,165,220,100,"Scaled scores","QKᵀ / √dₕ\n[B,H,T,T]","warm"),box(590,330,220,100,"Masked softmax","future → −∞","muted"),box(895,245,240,105,"Weighted values","A·V\n[B,H,T,dᵥ]","box")]
    p += [arrow(245,182,325,152),arrow(245,182,325,252),arrow(245,182,325,352),arrow(515,152,590,205),arrow(515,252,590,215),arrow(700,265,700,330),arrow(810,380,895,315),arrow(515,352,895,300)]
    p += [label(700,475,"Aᵢⱼ = 0 for j > i (causal mask)",cls="math"),label(700,510,"Each row of A sums to 1",cls="math")]
    write("03-scaled-dot-product-attention.svg","Scaled dot-product attention","Queries and keys form scaled, causally masked scores whose softmax weights retrieve values.",p,"Scaling keeps score variance controlled when dₕ grows.")

    p=[]
    p += [box(60,135,190,80,"Residual stream","x: [B,T,D]","accent"),box(340,120,200,90,"RMSNorm","same shape","box"),box(630,120,220,90,"Causal attention","[B,T,D]","warm"),box(930,120,190,90,"Add","x + attn","accent"),
          box(930,330,190,90,"RMSNorm","same shape","box"),box(630,330,220,90,"SwiGLU MLP","D → M → D","warm"),box(340,330,200,90,"Add","stream + mlp","accent"),box(60,330,190,90,"Block output","[B,T,D]","muted")]
    p += [arrow(250,175,340,165),arrow(540,165,630,165),arrow(850,165,930,165),arrow(1025,210,1025,330),arrow(930,375,850,375),arrow(630,375,540,375),arrow(340,375,250,375)]
    p += [f'<path class="dash" d="M155 215 L155 270 L1025 270 L1025 210"/>',f'<path class="dash" d="M1025 420 L1025 495 L440 495 L440 420"/>',label(600,555,"Pre-norm decoder block; both sublayers update one persistent residual stream",cls="math")]
    write("04-transformer-block.svg","Pre-norm Transformer block","A decoder block applies normalization, causal attention, residual addition, then normalization, MLP, and another residual addition.",p,"Dashed paths are identity residual connections.")

    p=[]
    steps=[(70,130,190,"Batch","tokens + labels"),(310,130,190,"Forward","logits [B,T,V]"),(550,130,190,"Loss","masked mean CE"),(790,130,190,"Backward","∂L/∂θ"),(1030,130,130,"Update","θ ← opt(θ,g)")]
    for i,(x,y,w,n,d) in enumerate(steps):
        p.append(box(x,y,w,100,n,d,["warm","box","accent","muted","warm"][i]));
        if i<len(steps)-1:p.append(arrow(x+w,180,steps[i+1][0],180))
    p += [arrow(1095,230,1095,370),box(870,370,280,90,"Checkpoint boundary","θ + optimizer + RNG + step","box"),arrow(870,415,165,415),box(70,370,190,90,"Next batch","schedule advances","accent"),
          label(600,525,"zero_grad → forward → loss → backward → clip/check → optimizer.step",cls="math"),label(600,565,"Gradient accumulation scales by valid-token count, not blindly by microbatch count",cls="small")]
    write("05-training-loop.svg","One reproducible training step","A batch flows through forward computation, loss, backpropagation, update, checkpoint state, and the next step.",p,"Ordinary inference stops after forward/decoding; it does not update θ.")

    p=[]
    p += [box(60,120,270,100,"Prefill","process T prompt tokens\nwrite K,V for every layer","warm"),box(465,120,270,100,"KV cache","per layer: K and V\n[B,Hkv,T,dₕ]","accent"),box(870,120,270,100,"Decode step","one new query\nread historical K,V","box"),
          arrow(330,170,465,170),arrow(735,170,870,170),box(60,360,270,95,"Append","new K,V at position T","accent"),box(465,360,270,95,"Cache grows","T → T+1","warm"),box(870,360,270,95,"Emit token","then repeat decode","muted"),
          arrow(1005,220,195,360),arrow(330,407,465,407),arrow(735,407,870,407),label(600,520,"bytes = 2 · L · B · Hkv · T · dₕ · bytes/element",cls="math"),label(600,555,"2 accounts for K and V; cache stores activations, not attention scores",cls="small")]
    write("06-kv-cache-lifecycle.svg","KV cache lifecycle","Prefill writes key and value states; each decode step reads history and appends one new position.",p,"Cached K/V avoids recomputing earlier token projections, but attention still reads history.")

    p=[]
    p += [box(50,120,250,100,"Data parallel","replicate θ\nshard batches","box"),box(345,120,250,100,"Tensor parallel","shard matrix axes\ncollective each layer","warm"),box(640,120,250,100,"Pipeline parallel","shard layer ranges\nsend activations","accent"),box(935,120,215,100,"ZeRO / FSDP","shard state\ngather as needed","muted")]
    p += [box(90,355,180,80,"Rank 0","batch A"),box(365,355,180,80,"Rank 1","matrix shard"),box(640,355,180,80,"Stage 0","layers 0…15"),box(915,355,180,80,"Stage 1","layers 16…31"),
          arrow(270,395,365,395),arrow(545,395,640,395),arrow(820,395,915,395),label(318,375,"all-reduce"),label(592,375,"activation"),label(868,375,"send/recv"),label(600,520,"Hybrid example: DP=2 × TP=2 × PP=2 → world size 8",cls="math")]
    write("07-distributed-parallelism.svg","Distributed parallelism axes","Data, tensor, pipeline, and state sharding divide different dimensions of training work and communication.",p,"Every sharding boundary implies a specific tensor and collective; account for both.")

    p=[]
    p += [box(55,120,170,90,"Client","HTTP / stream","warm"),box(285,120,190,90,"Gateway","auth + limits","box"),box(535,120,190,90,"Scheduler","admit + batch","accent"),box(785,120,170,90,"Worker","prefill/decode","muted"),box(1015,120,140,90,"Stream","tokens","warm")]
    for a,b in [(225,285),(475,535),(725,785),(955,1015)]:p.append(arrow(a,165,b,165))
    p += [box(535,340,190,90,"KV allocator","pages + refs","box"),box(785,340,170,90,"Model + runtime","weights + kernels","accent"),box(285,340,190,90,"Metrics","queue/TTFT/TPOT","muted"),
          arrow(630,210,630,340),arrow(725,385,785,385),arrow(870,340,870,210),arrow(535,385,475,385),label(600,505,"completion = queue + prefill + decode + stream overhead",cls="math"),label(600,545,"Cancellation must free KV pages and stop downstream work",cls="small")]
    write("08-inference-serving.svg","Inference serving request path","A request passes through gateway, scheduler, worker, KV allocator, runtime, metrics, and token streaming.",p,"Throughput and user latency depend on scheduling as well as kernel speed.")

    p=[]
    p += [box(50,115,180,85,"Question","user intent","warm"),box(285,115,200,85,"Query embedding","vector [D]","box"),box(540,115,200,85,"Retriever","top-k chunks","accent"),box(795,115,175,85,"Reranker","ordered evidence","muted"),box(1025,115,140,85,"Prompt","packed context","warm")]
    for a,b in [(230,285),(485,540),(740,795),(970,1025)]:p.append(arrow(a,157,b,157))
    p += [box(540,330,200,90,"Vector index","IDs + vectors","box"),arrow(640,330,640,200),box(795,330,175,90,"Source store","text + ACL + URI","accent"),arrow(882,330,882,200),box(1025,330,140,90,"Generator","answer + cites","muted"),arrow(1095,200,1095,330),
          label(600,490,"Retrieve → authorize → rerank → pack → generate → verify citations",cls="math"),label(600,530,"Grounding requires entailment from the cited source, not merely retrieved context",cls="small")]
    write("09-rag-pipeline.svg","Retrieval-augmented generation pipeline","A RAG system retrieves authorized chunks, reranks and packs evidence, then generates a cited answer.",p,"Evaluate retrieval recall, answer correctness, citation support, abstention, and latency separately.")

    p=[]
    p += [box(55,120,185,90,"Goal","task + constraints","warm"),box(295,120,185,90,"Planner","bounded steps","box"),box(535,120,185,90,"Tool call","schema args","accent"),box(775,120,185,90,"Executor","auth + idempotency","muted"),box(1015,120,140,90,"Observation","typed result","warm")]
    for a,b in [(240,295),(480,535),(720,775),(960,1015)]:p.append(arrow(a,165,b,165))
    p += [arrow(1085,210,1085,340),box(920,340,235,90,"Validate / stop?","success, retry, abstain","box"),arrow(920,385,390,385),box(295,340,190,90,"Update state","provenance + expiry","accent"),arrow(390,340,390,210),
          label(650,365,"bounded retry",cls="small"),label(600,510,"Policy limits: max steps, max cost, allowed tools, timeout",cls="math"),label(600,550,"A tool result is untrusted input; validate before state mutation",cls="small")]
    write("10-agent-tool-loop.svg","Bounded agent and tool loop","A planner emits validated tool calls, an authorized executor returns observations, and a stop policy bounds retries.",p,"Separate model proposals from validation, authorization, execution, and persistence.")

    p=[]
    p += [box(55,115,180,85,"Question","falsifiable claim","warm"),box(285,115,190,85,"Hypothesis","direction + scope","box"),box(525,115,190,85,"Preregister","metric + budget","accent"),box(765,115,190,85,"Experiment","baseline + controls","muted"),box(1005,115,150,85,"Evidence","data + logs","warm")]
    for a,b in [(235,285),(475,525),(715,765),(955,1005)]:p.append(arrow(a,157,b,157))
    p += [box(165,340,210,95,"Uncertainty","paired CI / variance","box"),box(495,340,210,95,"Ablations","remove one factor","accent"),box(825,340,210,95,"Reproduction","clean environment","muted"),
          arrow(1080,200,930,340),arrow(825,387,705,387),arrow(495,387,375,387),label(600,500,"claim ↔ metric ↔ result ↔ artifact",cls="math"),label(600,540,"Negative results remain informative when the stopping rule was fixed in advance",cls="small")]
    write("11-research-evidence-loop.svg","Research and evidence loop","A falsifiable question becomes a preregistered controlled experiment, uncertainty analysis, ablation, and reproduction artifact.",p,"Conclusions must be no stronger than the evidence and controls that support them.")


if __name__ == "__main__":
    main()
