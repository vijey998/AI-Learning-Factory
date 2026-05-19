"""Editorial floor checks. Passing does not establish technical correctness."""
import json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
MIN_WORDS=400
BOILERPLATE=('Planned chapter specification','Planned: explain the mechanism')
TEX_COMMAND=re.compile(r'\\(?:mathbb|mathrm|operatorname|times|ell|mu|beta|gamma|Delta|nabla|partial|qquad|quad|cdot|sum|sqrt|log|exp|infty|leq|geq|frac|sigma|top|odot|approx|in)(?![A-Za-z])')

def tex_outside_math(text):
    """Return line numbers containing TeX commands outside code or math spans."""
    hits=[];in_fence=False;in_display=False;in_bracket_math=False
    for lineno,line in enumerate(text.splitlines(),1):
        if line.lstrip().startswith('```'):
            in_fence=not in_fence;continue
        if in_fence:continue
        cleaned=[];i=0;inline=False
        while i<len(line):
            if line.startswith('\\[',i):
                in_bracket_math=True;i+=2;continue
            if line.startswith('\\]',i):
                in_bracket_math=False;i+=2;continue
            if not in_display and line.startswith('\\(',i):
                inline=True;i+=2;continue
            if not in_display and line.startswith('\\)',i):
                inline=False;i+=2;continue
            if line.startswith('$$',i):
                in_display=not in_display;i+=2;continue
            if not in_display and line[i]=='$':
                inline=not inline;i+=1;continue
            if not in_display and not in_bracket_math and not inline:cleaned.append(line[i])
            i+=1
        if TEX_COMMAND.search(''.join(cleaned)):hits.append(lineno)
    return hits
def check(root=ROOT):
    chapters=json.loads((root/'curriculum/chapters.json').read_text())
    topics=json.loads((root/'curriculum/topics.json').read_text())
    errors=[];stats=[]
    by_chapter={c['id']:[] for c in chapters}
    for t in topics:by_chapter[t['chapter']].append(t['anchor'])
    for c in chapters:
        p=root/c['path']
        if not p.is_file():errors.append(f"missing:{c['id']}");continue
        s=p.read_text();words=len(re.findall(r"\b[\w'-]+\b",s))
        anchors=re.findall(r'<a id="([a-z0-9-]+)"></a>',s)
        expected=by_chapter[c['id']]
        if anchors!=expected:errors.append(f"anchors:{c['id']} expected {expected} got {anchors}")
        if words<MIN_WORDS:errors.append(f"length:{c['id']} {words}<{MIN_WORDS}")
        for phrase in BOILERPLATE:
            if phrase in s:errors.append(f"boilerplate:{c['id']}:{phrase}")
        bad=[ord(x) for x in s if ord(x)<32 and x not in '\n\r']
        if bad:errors.append(f"control:{c['id']}:{bad[:5]}")
        if 'Status: **Draft' not in s:errors.append(f"status-line:{c['id']}")
        if bad_math:=tex_outside_math(s):errors.append(f"math-delimiters:{c['id']}:{bad_math}")
        stats.append({'chapter':c['id'],'words':words,'anchors':len(anchors)})
    return errors,stats
if __name__=='__main__':
    errors,stats=check();print(json.dumps({'result':'FAIL' if errors else 'PASS','chapters':len(stats),'total_words':sum(x['words'] for x in stats),'minimum_words':min((x['words'] for x in stats),default=0),'errors':errors},indent=2));sys.exit(bool(errors))
