"""Regenerate project control documents and a dependency-free offline HTML reader."""
from pathlib import Path
import json,re,html
from check_coverage import validate
R=Path(__file__).resolve().parents[1]
def read(n):return json.loads((R/'curriculum'/n).read_text())
def inline(s):
    s=html.escape(s)
    s=re.sub(r'`([^`]+)`',r'<code>\1</code>',s)
    s=re.sub(r'\*\*([^*]+)\*\*',r'<strong>\1</strong>',s)
    s=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',r'<a href="\2">\1</a>',s)
    return s

def markdown(text):
    # Deliberate subset: headings, paragraphs, fenced code, flat lists and tables.
    out=[];paragraph=[];code=None;table=False;listing=False
    def flush():
        if paragraph:out.append('<p>'+inline(' '.join(paragraph))+'</p>');paragraph.clear()
    def close_structures():
        nonlocal table,listing
        if table:out.append('</tbody></table></div>');table=False
        if listing:out.append('</ul>');listing=False
    for line in text.splitlines():
        if line.startswith('```'):
            flush();close_structures()
            if code is None:code=[]
            else:out.append('<pre><code>'+html.escape('\n'.join(code))+'</code></pre>');code=None
            continue
        if code is not None:code.append(line);continue
        if re.fullmatch(r'<a id="[a-z0-9-]+"></a>',line):flush();close_structures();out.append(line);continue
        if line.startswith('|'):
            flush()
            cells=[x.strip() for x in line.strip('|').split('|')]
            if all(re.fullmatch(r':?-+:?',x) for x in cells):continue
            if not table:close_structures();out.append('<div class="table"><table><tbody>');table=True
            out.append('<tr>'+''.join('<td>'+inline(c)+'</td>' for c in cells)+'</tr>');continue
        close_structures() if table else None
        match=re.match(r'^(#{1,6}) (.*)',line)
        if match:flush();close_structures();n=len(match[1]);out.append(f'<h{n}>{inline(match[2])}</h{n}>');continue
        if re.match(r'^(- |\d+\. )',line):
            flush()
            if not listing:out.append('<ul>');listing=True
            out.append('<li>'+inline(re.sub(r'^(- |\d+\. )','',line))+'</li>');continue
        if listing:close_structures()
        if not line.strip():flush()
        else:paragraph.append(line)
    flush();close_structures()
    return '\n'.join(out)

def main():
    errors,stats=validate()
    if errors:raise SystemExit('\n'.join(errors))
    cs=read('chapters.json');ts=read('topics.json');ss=read('source_inventory.json');parts=read('parts.json')
    by_c={c['id']:c for c in cs}
    plan=['# Book plan','', 'Working title: **Inside the LLM: From Tokens to Systems to Research**.','',
    'Twenty parts, 80 substantial chapters. Each chapter below has a concrete exit artifact. The 206 V2 headings are subsections, not 206 chapters. The consolidated inventory also retains the explicit V1 audit corrections.','',
    '## Ordering rationale','',
    'Start with an end-to-end mental model, then introduce shapes and resource accounting before neural networks. Build gradients, tokenization, attention and a tiny GPT before large-model architectures. Basic held-out evaluation and sampling are introduced when needed for training; their rigorous treatments follow. Hardware, kernels and compilers precede advanced inference optimization. Distributed systems precede production serving. Interpretability and frontier experiments come after the reader can account for both tensors and execution costs.','',
    'The four perspectives recur throughout: information (token), learning (gradient), hardware (byte), and service execution (request). A chapter may explain that a perspective is inapplicable rather than invent a gradient or hardware claim.','',
    '## Intended depth','',
    'Main chapters explain mechanisms, equations and representative code. Companion labs hold full implementations and measurements. Total word count is an editorial planning variable, not a completion criterion. Topic evidence and learner outcomes determine completeness.','']
    for p in parts:
        plan += [f"## Part {p['id']:02d} — {p['title']}",'']
        for c in cs:
            if c['part']==p['id']:plan += [f"### {c['number']:02d}. [{c['title']}]({c['path']})",'',f"**Exit artifact:** {c['outcome']}.",'',f"**Required scope:** "+'; '.join(t['title'] for t in ts if t['chapter']==c['id'])+'.','']
    plan += ['## Milestone projects','','See [labs/README.md](labs/README.md) for fifteen implementation milestones and their hardware/acceptance conditions. Multi-GPU measurements require suitable hardware; CPU simulations do not fulfill that gate.','']
    (R/'BOOK_PLAN.md').write_text('\n'.join(plan))
    matrix=['# Coverage matrix','','Generated from `curriculum/*.json`. A destination means planned coverage, not substantive completion.','',
    f"- {len(cs)} chapters; {len(ts)} atomic teaching requirements.",f'- {len(ss)} source obligations: 161 original V1 topics, 206 V2 headings, 54 audit correction groups, and 20 framework/milestone obligations.',
    f"- {stats['drafted_topics']} drafted topics; {stats['complete_topics']} complete topics.",'- The original 161-topic V1 outline is reconciled item by item in the source inventory.','','## Source reconciliation','','| Source ID | Obligation | Destination | Chapter status |','| --- | --- | --- | --- |']
    for s in ss:
        c=by_c[s['chapter']];matrix.append(f"| {s['id']} | {s['topic']} | [{c['id']}]({c['path']}) | {c['status']} |")
    matrix+=['','## Atomic topic requirements','','| Topic ID | Topic | Destination | Status | Evidence |','| --- | --- | --- | --- | --- |']
    for t in ts:
        c=by_c[t['chapter']];ev=', '.join(f'[section]({e})' for e in t['evidence']) or '—'
        matrix.append(f"| {t['id']} | {t['title']} | [{c['id']}]({c['path']}#{t['anchor']}) | {t['status']} | {ev} |")
    (R/'COVERAGE_MATRIX.md').write_text('\n'.join(matrix)+'\n')
    dep=['# Prerequisites and reading paths','','The default path is sequential, with explicit cross-part prerequisites listed below. This conservative order is deliberate for a novice-to-research curriculum. Experienced readers may use the paths below, but should verify each chapter outcome before skipping it.','','| Path | Chapters | Purpose |','| --- | --- | --- |','| Model construction | 1–28 | Implement and train a tiny decoder |','| Systems | 1–8, 17–24, 29–36, 41–68 | Explain execution, memory and service behavior |','| Adaptation and applications | 1–40, 49–52, 69–72 | Understand post-training and agent workflows |','| Research | Core foundations plus 73–80 | Design controlled representation and efficiency experiments |','','An overview can name a mechanism before its formal treatment. It must not require unexplained mathematics. Examples: basic sampling appears in Chapter 1; the full policy treatment is Chapter 51. Basic held-out evaluation appears before Part IX.','','| Chapter | Prerequisites |','| --- | --- |']
    for c in cs:dep.append(f"| [{c['id']}: {c['title']}]({c['path']}) | "+', '.join(c['prerequisites'])+' |')
    (R/'DEPENDENCY_GRAPH.md').write_text('\n'.join(dep)+'\n')
    (R/'STATUS.md').write_text(f'''# Manuscript status

## Publication candidate

- 20 parts and 80 substantive chapter drafts.
- {len(ts)} atomic topics and {len(ss)} source obligations have explicit destinations; all topics have draft evidence anchors.
- Runnable artifacts include the original focused examples plus deterministic reference implementations for all fifteen milestone labs.
- Eleven accessible technical figures, solutions for all eighty chapter exit checks, generated control documents, and HTML/PDF editions accompany the Markdown source.

## Editorial state

All chapters have completed an AI-assisted internal technical/editorial pass recorded in `reviews/`. Reference, manuscript, candidate, test, and rendered-publication checks are automated. This is not equivalent to independent human review, and the curriculum status remains drafted until that external gate is satisfied.

## Release blockers

- Independent human technical and semantic review, including the V1/V2 mappings.
- Target-hardware measurements for the labs explicitly marked as CPU simulations, especially Triton and multi-GPU execution.
- Legal/ISBN/distribution decisions and final author approval of the public-release files.
- Authenticated push and tagged release in the private GitHub repository.

## Next pass

Resolve external-review findings, run the hardware-dependent experiments, and record both in dated review/experiment records. The candidate gate may pass before the independent release gate; do not promote topics merely to make a dashboard green.
''')
    nav=[];articles=[]
    for p in parts:
        nav.append(f'<h3>Part {p["id"]}: {html.escape(p["title"])}</h3>')
        for c in cs:
            if c['part']!=p['id']:continue
            nav.append(f'<a class="entry" href="#{c["id"]}">{c["number"]:02d}. {html.escape(c["title"])}</a>')
            articles.append(f'<article id="{c["id"]}"><span class="badge">{html.escape(c["status"].upper())}</span>'+markdown((R/c['path']).read_text())+'</article>')
    style='''[hidden]{display:none!important}body{margin:0;background:#f6f5f0;color:#24313d;font:17px/1.75 Georgia,serif}nav{position:fixed;width:265px;top:0;bottom:0;overflow:auto;background:#142b39;color:#e7eff0;padding:24px;box-sizing:border-box;font:13px/1.5 system-ui}nav h2{font-size:22px}nav h3{margin-top:25px;font-size:13px;color:#8bcfc6}nav a{display:block;color:#dce6e9;text-decoration:none;padding:5px 0}input{box-sizing:border-box;width:100%;padding:10px;border:0;border-radius:5px}main{margin-left:265px;max-width:850px;padding:50px 55px}h1,h2,h3,.badge{font-family:system-ui;line-height:1.3}h1{font-size:36px}h2{font-size:23px;margin-top:38px}h3{font-size:19px}.badge{font-size:12px;background:#d9eae6;padding:6px 10px;border-radius:5px}article{padding:35px 0 65px;border-bottom:2px solid #ccd6d7;scroll-margin-top:20px}pre{overflow:auto;background:#142b39;color:#e8f3ef;padding:20px;border-radius:8px;line-height:1.5}code{font:14px/1.5 monospace}p code{background:#e4e9e7;padding:2px 4px}.table{overflow:auto}table{border-collapse:collapse;width:100%;font-size:15px}td{border-bottom:1px solid #cbd4d5;padding:9px;text-align:left}tr:first-child{font-weight:bold;background:#e2ebe8}a{color:#146d70}.notice{background:#e2ebe8;padding:22px;border-left:4px solid #297e77}button{padding:8px;margin-bottom:5px;cursor:pointer}@media(max-width:800px){nav{position:static;width:100%;max-height:300px}main{margin:0;padding:25px}h1{font-size:29px}}@media print{nav,button{display:none}main{margin:0;padding:0}article{break-before:page}pre{white-space:pre-wrap}}'''
    page='<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Inside the LLM — Publication Candidate</title><style>'+style+'</style></head><body><nav><h2>Inside the LLM</h2><input id="search" aria-label="Filter chapter titles" placeholder="Find a chapter…">'+''.join(nav)+'</nav><main><h1>From tokens to systems to research</h1><p><strong>Vijey Shrivathsan Vasudevan and Shri Venkatakrishnan Vasudevan</strong></p><div class="notice"><strong>Publication candidate · 20 parts · 80 internally reviewed chapters</strong><p>All chapters contain substantive teaching content and an AI-assisted internal review record. Independent human technical review remains pending. This preview is generated from the canonical Markdown source and works offline.</p></div>'+''.join(articles)+'</main><script>document.getElementById("search").addEventListener("input",function(){const q=this.value.toLowerCase();document.querySelectorAll(".entry").forEach(a=>a.hidden=!a.textContent.toLowerCase().includes(q));});</script></body></html>'
    (R/'build').mkdir(exist_ok=True);(R/'build/reading-preview.html').write_text(page)
    print(f'Generated book plan, coverage matrix, prerequisites, status and offline reader ({len(page):,} characters).')
if __name__=='__main__':main()
