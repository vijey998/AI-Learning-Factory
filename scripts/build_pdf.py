"""Build the working book PDF from canonical Markdown with Pandoc/XeLaTeX."""
from pathlib import Path
import json,re,subprocess,sys
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'output/pdf';TMP=ROOT/'tmp/pdfs';OUT.mkdir(parents=True,exist_ok=True);TMP.mkdir(parents=True,exist_ok=True)
chapters=json.loads((ROOT/'curriculum/chapters.json').read_text());parts=json.loads((ROOT/'curriculum/parts.json').read_text())
figure_after={
    'CH-01':('01-end-to-end-llm-flow.svg','End-to-end language-model flow.'),
    'CH-05':('02-tensor-shape-ledger.svg','Tensor-shape ledger through the model.'),
    'CH-18':('03-scaled-dot-product-attention.svg','Scaled dot-product attention.'),
    'CH-21':('04-transformer-block.svg','Pre-normalized Transformer block.'),
    'CH-26':('05-training-loop.svg','Training and reproducibility loop.'),
    'CH-50':('06-kv-cache-lifecycle.svg','KV-cache lifecycle during prefill and decode.'),
    'CH-57':('07-distributed-parallelism.svg','Distributed parallelism and communication boundaries.'),
    'CH-61':('08-inference-serving.svg','Production inference request path.'),
    'CH-69':('09-rag-pipeline.svg','Retrieval-augmented generation pipeline.'),
    'CH-71':('10-agent-tool-loop.svg','Bounded agent and tool-execution loop.'),
    'CH-79':('11-research-evidence-loop.svg','Research evidence and reproduction loop.'),
}
print_figures=TMP/'figures';print_figures.mkdir(exist_ok=True)
for filename,_ in figure_after.values():
    source=ROOT/'figures'/filename
    target=print_figures/(Path(filename).stem+'.pdf')
    subprocess.run(['inkscape',str(source),'--export-type=pdf',f'--export-filename={target}'],check=True,capture_output=True,text=True)
chunks=[]
for name in ('edition-notice.md','preface.md','how-to-use-this-book.md'):
    chunks.append((ROOT/'frontmatter'/name).read_text()+'\n\n')
for part in parts:
    chunks += [f"# Part {part['id']}: {part['title']} {{-}}\n"]
    for c in chapters:
        if c['part']!=part['id']:continue
        s=(ROOT/c['path']).read_text()
        s=re.sub(r'^#\s+\d+\.\s+', '# ', s, count=1, flags=re.M)
        # Coverage anchors are required by the HTML/audit build, but standalone
        # Pandoc heading attributes render as literal text in the print edition.
        s=re.sub(r'<a id="[^"]+"></a>\s*', '', s)
        if c['id'] in figure_after:
            filename,caption=figure_after[c['id']]
            print_path=print_figures/(Path(filename).stem+'.pdf')
            figure=f'![{caption}]({print_path.as_posix()}){{width=96%}}'
            s=re.sub(r'(?m)^(#{2,3}\s+(?:Primary\s+)?References\s*)$',figure+r'\n\n\1',s,count=1)
        chunks.append(s+'\n\n')
chunks += ['\\appendix\n', (ROOT/'appendices/exercise-solutions.md').read_text()+'\n\n', (ROOT/'GLOSSARY.md').read_text()+'\n\n']
if (ROOT/'REFERENCES.md').exists():chunks.append((ROOT/'REFERENCES.md').read_text()+'\n')
body=TMP/'manuscript.md';body.write_text('\n'.join(chunks))
header=TMP/'header.tex';header.write_text(r'''\usepackage{microtype}
\usepackage{fancyhdr}
\usepackage{xcolor}
\definecolor{bookteal}{HTML}{146D70}
\usepackage{titlesec}
\titleformat{\chapter}[display]{\normalfont\huge\bfseries\color{bookteal}\raggedright}{\chaptertitlename\ \thechapter}{20pt}{\Huge}
\hyphenpenalty=700
\exhyphenpenalty=700
\pagestyle{fancy}\fancyhf{}\fancyhead[LE]{\small\leftmark}\fancyhead[RO]{\small\rightmark}\fancyfoot[C]{\thepage}
\setlength{\headheight}{15pt}
''')
pdf=OUT/'inside-the-llm-working-edition.pdf'
cmd=['pandoc',str(body),'--from=markdown+tex_math_dollars+tex_math_single_backslash+raw_tex+fenced_code_blocks+pipe_tables','--pdf-engine=xelatex','--top-level-division=chapter','--toc','--toc-depth=2','--number-sections','--include-in-header',str(header),'-V','documentclass=book','-V','classoption=openany','-V','geometry:margin=0.85in','-V','mainfont=DejaVu Serif','-V','sansfont=DejaVu Sans','-V','monofont=DejaVu Sans Mono','-V','fontsize=10pt','-V','colorlinks=true','-V','linkcolor=bookteal','-V','urlcolor=bookteal','-M','title=Inside the LLM','-M','subtitle=From Tokens to Systems to Research','-M','author=Vijey Shrivathsan Vasudevan and Shri Venkatakrishnan Vasudevan','-M','date=Publication Candidate - September 2026','-o',str(pdf)]
proc=subprocess.run(cmd,cwd=ROOT,text=True,capture_output=True)
if proc.returncode:
 print(proc.stdout);print(proc.stderr,file=sys.stderr);raise SystemExit(proc.returncode)
print(pdf)
