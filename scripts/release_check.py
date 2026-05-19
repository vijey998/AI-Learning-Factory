"""Rebuild and validate every machine-checkable working-edition artifact."""
from pathlib import Path
import json, subprocess, sys

ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "output/pdf/inside-the-llm-working-edition.pdf"

def run(*cmd, quiet=False):
    print("+", " ".join(cmd), flush=True)
    subprocess.run(cmd, cwd=ROOT, check=True, stdout=subprocess.DEVNULL if quiet else None)

run(sys.executable, "scripts/check_coverage.py")
run(sys.executable, "scripts/check_manuscript.py")
run(sys.executable, "scripts/audit_references.py")
run(sys.executable, "code/milestone_labs.py", "--lab", "all", "--output", "build/milestone-labs.json", quiet=True)
run(sys.executable, "scripts/check_candidate.py")
run(sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v")
run(sys.executable, "scripts/build.py")
run(sys.executable, "scripts/build_pdf.py")

info = subprocess.run(["pdfinfo", str(PDF)], text=True, capture_output=True, check=True).stdout
text = subprocess.run(["pdftotext", str(PDF), "-"], text=True, capture_output=True, check=True).stdout
errors = []
if "Pages:" not in info:
    errors.append("pdfinfo did not report a page count")
if "{#t-" in text or '<a id="t-' in text:
    errors.append("internal topic anchors leaked into the PDF")
if "Contents" not in text or "Chapter 80" not in text:
    errors.append("PDF is missing expected front or end matter")
report = {
    "result": "FAIL" if errors else "PASS",
    "pdf": str(PDF.relative_to(ROOT)),
    "bytes": PDF.stat().st_size,
    "errors": errors,
}
(ROOT / "build/validation-report.json").write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps(report, indent=2))
raise SystemExit(bool(errors))
