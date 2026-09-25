# AI Learning Factory

**Inside the LLM: From Tokens to Systems to Research**

Authors: **Vijey Shrivathsan Vasudevan** and **Shri Venkatakrishnan Vasudevan**

A Markdown-first book and implementation companion, organized into 20 parts and 80 substantial chapters. The working method follows the token, gradient, byte and request through the same system.

## Start here

- [Book plan](BOOK_PLAN.md): ordering, all 80 chapter outcomes and milestones.
- [Coverage matrix](COVERAGE_MATRIX.md): explicit requirements and source reconciliation.
- [Dependency graph](DEPENDENCY_GRAPH.md): prerequisites and reading paths.
- [Complete manuscript](chapters/part-01/01-the-llm-in-one-picture.md): begin the 80-chapter draft with Chapter 1.
- [Status](STATUS.md): exactly what has been implemented and what remains.
- Open `build/reading-preview.html` locally for a single-file offline reading preview.

## Run

Use Python 3.10 or newer. The manuscript tooling uses the standard library; implementation labs and their tests require NumPy. No API key, paid service, or GPU is needed. Install the one package dependency first: `python -m pip install -r requirements.txt`.

```bash
python scripts/check_coverage.py
python scripts/check_manuscript.py
python -m unittest discover -s tests -v
python code/resource_lab.py
python scripts/build.py
python scripts/build_pdf.py
```

Run the complete reproducible working-edition gate with:

```bash
python scripts/release_check.py
```

This runs manuscript and source coverage checks, the consolidated reference audit, all fifteen lab references, the publication-candidate gate, the full unit-test suite, and the HTML/PDF builds.

The release gate intentionally fails while the manuscript is unfinished:

```bash
python scripts/check_coverage.py --release
```

## Source of truth

Chapter prose lives in `chapters/`; executable examples in `code/`; lab specifications in `labs/`. `curriculum/*.json` defines stable IDs, topic destinations, status and source obligations. `scripts/build.py` regenerates the plan, matrix, dependency document and HTML preview. Edit the JSON or chapter files, not generated control documents. The HTML exporter supports the limited Markdown syntax used here; it is a starter reader, not a publication typesetter.

## Completeness promise and limit

All 206 supplied V2 headings and the explicit V1 audit corrections are retained. The original 161-topic V1 outline is mapped item by item alongside V2 and the later audit. The publication candidate contains 80 substantive chapters, AI-assisted internal review records, 238 linked chapter references, 15 executable lab references, 11 accessible diagrams, and 80 keyed exercise solutions. Independent human review and target-hardware validation remain open.

## Output strategy

Markdown is canonical. The included HTML reader and typeset PDF are generated locally and visually verified. No website is published. The package can be built without GitHub access.

## Working conventions

See [AUTHORING.md](AUTHORING.md) and [templates/chapter.md](templates/chapter.md). Do not delete agreed requirements while consolidating chapters. Move their destinations while retaining IDs. Research ideas such as neural handoff are hypotheses to test, not established performance claims.

## Research and AI workflow

The [book plan](BOOK_PLAN.md), [research queue](RESEARCH_QUEUE.md), and [AI-assisted workflow](AI_WORKFLOW.md) document scope, verification, and unresolved questions.

## License

Original code in `code/`, `scripts/`, and `tests/` is [MIT licensed](LICENSE-CODE.md). The coauthored manuscript, figures, lab prose, and generated books remain [all rights reserved](COPYRIGHT.md).
