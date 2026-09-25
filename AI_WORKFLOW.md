# AI-assisted authoring and verification

## Purpose

The book uses AI assistance to draft, reorganize, and review technical material. The authors remain responsible for claims, code, diagrams, references, and publication decisions. The canonical content is in `chapters/`, `code/`, `labs/`, and `curriculum/`.

## Method

1. Define each chapter's outcome and source obligations in the curriculum data.
2. Draft an explanation tied to executable examples and cited sources.
3. Run the manuscript, coverage, reference, lab, and unit-test checks in `scripts/release_check.py`.
4. Record internal AI-assisted review in `reviews/` and leave unresolved work visible in `STATUS.md` and `RESEARCH_QUEUE.md`.
5. Require independent human review and target-hardware validation before claiming a final publication release.

AI-assisted internal review is evidence of an editorial pass, not independent verification. Reproduction claims should identify the exact lab, environment, and output. Hypotheses in the research queue are proposals, not established results. `BOOK_PLAN.md` is the master plan; `COVERAGE_MATRIX.md` and `DEPENDENCY_GRAPH.md` are generated control documents.
