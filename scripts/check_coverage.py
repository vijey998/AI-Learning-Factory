"""Validate curriculum structure; --release additionally requires verified evidence.
A structural pass is not a semantic or technical completeness certificate.
"""
import argparse,json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
STATES=['planned','drafted','technically_reviewed','integrated','complete']
def validate(root=ROOT,release=False):
    errors=[]
    def read(name):return json.loads((root/'curriculum'/name).read_text())
    chapters=read('chapters.json');topics=read('topics.json');sources=read('source_inventory.json');parts=read('parts.json')
    def unique(rows,label):
        ids=[r['id'] for r in rows]
        if len(ids)!=len(set(ids)):errors.append(f'Duplicate {label} ID')
    for rows,label in [(chapters,'chapter'),(topics,'topic'),(sources,'source'),(parts,'part')]:unique(rows,label)
    by_c={c['id']:c for c in chapters};by_t={t['id']:t for t in topics}
    if len(chapters)!=80:errors.append('Expected 80 chapters in the accepted architecture')
    if len(parts)!=20:errors.append('Expected 20 parts')
    v1_expected={f'V1-{n:03d}' for n in range(1,162)}
    if {s['id'] for s in sources if s['id'].startswith('V1-')}!=v1_expected:errors.append('V1 source inventory must retain all 161 original topics')
    expected={f'V2-{n:03d}' for n in range(1,207)}
    if {s['id'] for s in sources if s['id'].startswith('V2-')}!=expected:errors.append('V2 source inventory must retain all 206 headings')
    if {s['id'] for s in sources if s['id'].startswith('AUDIT-')}!={f'AUDIT-{n:03d}' for n in range(1,55)}:errors.append('Audit inventory must retain all 54 correction groups')
    texts={}
    for c in chapters:
        if c['status'] not in STATES:errors.append(f"Invalid chapter status: {c['id']}")
        p=root/c['path']
        if not p.is_file():errors.append(f'Missing chapter: {p}');continue
        texts[c['id']]=p.read_text()
        if c['part'] not in {p['id'] for p in parts}:errors.append(f"Unknown part: {c['id']}")
        if not c['topics']:errors.append(f"Chapter has no requirements: {c['id']}")
        for tid in c['topics']:
            if tid not in by_t or by_t[tid]['chapter']!=c['id']:errors.append(f'Invalid chapter-topic mapping: {tid}')
        for dep in c['prerequisites']:
            if dep not in by_c:errors.append(f'Unknown prerequisite: {dep}')
            elif by_c[dep]['number']>=c['number']:errors.append(f"Forward prerequisite: {c['id']} -> {dep}")
    visiting=set();visited=set()
    def walk(cid):
        if cid in visiting:errors.append(f'Prerequisite cycle: {cid}');return
        if cid in visited or cid not in by_c:return
        visiting.add(cid)
        for dep in by_c[cid]['prerequisites']:walk(dep)
        visiting.remove(cid);visited.add(cid)
    for cid in by_c:walk(cid)
    for t in topics:
        cid=t['chapter'];state=t['status']
        if state not in STATES:errors.append(f"Invalid topic status: {t['id']}")
        if cid not in by_c or t['id'] not in by_c.get(cid,{}).get('topics',[]):errors.append(f"Orphan topic: {t['id']}")
        if f'id="{t["anchor"]}"' not in texts.get(cid,''):errors.append(f"Missing section anchor: {t['id']}")
        if state!='planned':
            if not t['evidence']:errors.append(f"Missing evidence: {t['id']}")
            for e in t['evidence']:
                p,sep,a=e.partition('#')
                if not (root/p).is_file():errors.append(f'Missing evidence file: {e}')
                elif sep and f'id="{a}"' not in (root/p).read_text():errors.append(f'Missing evidence anchor: {e}')
        if release and state!='complete':errors.append(f"Unfinished topic: {t['id']}")
        if release and not t.get('review_record'):errors.append(f"Missing review record: {t['id']}")
    for s in sources:
        if s['chapter'] not in by_c:errors.append(f"Unmapped source: {s['id']}")
        if not s['topic'].strip():errors.append(f"Empty source obligation: {s['id']}")
    audit=json.loads((root/'curriculum/provenance.json').read_text())
    if release and not audit['original_v1_verified']:errors.append('Original V1 has not been independently reconciled')
    if release:
        for c in chapters:
            if c['status']!='complete':errors.append(f"Unfinished chapter: {c['id']}")
    return errors,{'chapters':len(chapters),'topics':len(topics),'source_requirements':len(sources),'drafted_topics':sum(t['status']=='drafted' for t in topics),'complete_topics':sum(t['status']=='complete' for t in topics)}
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--release',action='store_true');args=parser.parse_args()
    errors,stats=validate(release=args.release)
    print(json.dumps({'mode':'release' if args.release else 'structure','result':'FAIL' if errors else 'PASS',**stats,'errors':errors},indent=2))
    sys.exit(bool(errors))
