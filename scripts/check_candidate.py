"""Checks required for the internally reviewed publication candidate."""
from pathlib import Path
import json, re, sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
errors=[]

review_files=[ROOT/'reviews'/f'parts-{a:02d}-{b:02d}.md' for a,b in ((1,5),(6,10),(11,15),(16,20))]
for path in review_files:
    if not path.is_file(): errors.append(f'missing review record: {path.relative_to(ROOT)}')
    elif 'ai-assisted internal' not in path.read_text().lower(): errors.append(f'unlabeled review record: {path.relative_to(ROOT)}')

figures=sorted((ROOT/'figures').glob('*.svg'))
if len(figures)<10:errors.append(f'figures: expected at least 10, found {len(figures)}')
for path in figures:
    try:
        root=ET.parse(path).getroot()
        tags={x.tag.split('}')[-1] for x in root}
        if not {'title','desc'}<=tags:errors.append(f'figure accessibility metadata: {path.name}')
    except ET.ParseError as exc:errors.append(f'figure XML: {path.name}: {exc}')

solutions=(ROOT/'appendices/exercise-solutions.md')
if not solutions.is_file():errors.append('missing exercise solutions appendix')
else:
    nums=[int(x) for x in re.findall(r'^###\s+(\d+)\.',solutions.read_text(),re.M)]
    if nums!=list(range(1,81)):errors.append('exercise solution keys are not exactly 1..80')

lab_record=ROOT/'build/milestone-labs.json'
if not lab_record.is_file():errors.append('missing milestone lab experiment record')
else:
    data=json.loads(lab_record.read_text())
    if not isinstance(data,list) or [x.get('lab') for x in data]!=[f'{i:02d}' for i in range(1,16)]:
        errors.append('milestone lab record does not contain labs 01..15')
    for item in data if isinstance(data,list) else []:
        if item.get('status')!='reference-complete':errors.append(f"lab {item.get('lab')}: incomplete reference")

required=[ROOT/'COPYRIGHT.md',ROOT/'frontmatter/preface.md',ROOT/'frontmatter/how-to-use-this-book.md',ROOT/'REFERENCES.md']
for path in required:
    if not path.is_file() or not path.read_text().strip():errors.append(f'missing publication component: {path.relative_to(ROOT)}')

print(json.dumps({'result':'FAIL' if errors else 'PASS','review_records':len(review_files),'figures':len(figures),'labs':15,'exercise_solutions':80,'errors':errors},indent=2))
raise SystemExit(bool(errors))
