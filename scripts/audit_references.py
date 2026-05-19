"""Inventory chapter references and build a human-readable consolidated index."""
from pathlib import Path
import json, re, sys

ROOT = Path(__file__).resolve().parents[1]
URL = re.compile(r"https?://[^\s)>]+")
REF_HEADING = re.compile(r"^#{2,3}\s+(?:Primary\s+)?References\s*$", re.I | re.M)

def main():
    chapters = json.loads((ROOT / "curriculum/chapters.json").read_text())
    errors, inventory, sections = [], [], []
    for chapter in chapters:
        path = ROOT / chapter["path"]
        text = path.read_text()
        matches = list(REF_HEADING.finditer(text))
        if len(matches) != 1:
            errors.append(f"{chapter['id']}: expected one reference section, found {len(matches)}")
            continue
        tail = text[matches[0].end():]
        next_heading = re.search(r"^#{1,3}\s+", tail, re.M)
        block = tail[:next_heading.start()] if next_heading else tail
        entries = [line.strip()[2:].strip() for line in block.splitlines() if line.strip().startswith("- ")]
        if not entries:
            errors.append(f"{chapter['id']}: empty reference section")
        urls = [u.rstrip(".,;") for u in URL.findall(block)]
        for url in urls:
            if "example.com" in url or "TODO" in url.upper():
                errors.append(f"{chapter['id']}: placeholder URL {url}")
        inventory.append({"chapter": chapter["id"], "title": chapter["title"], "entries": len(entries), "urls": urls})
        sections.append(f"## {chapter['number']}. {chapter['title']}\n\n" + ("\n".join(f"- {e}" for e in entries) or "- No formatted entries") + "\n")

    report = {
        "result": "FAIL" if errors else "PASS",
        "chapters": len(chapters),
        "reference_entries": sum(x["entries"] for x in inventory),
        "linked_sources": sum(len(x["urls"]) for x in inventory),
        "chapters_with_links": sum(bool(x["urls"]) for x in inventory),
        "errors": errors,
        "inventory": inventory,
    }
    (ROOT / "build").mkdir(exist_ok=True)
    (ROOT / "build/reference-audit.json").write_text(json.dumps(report, indent=2) + "\n")
    header = "# Consolidated chapter references\n\nGenerated from the canonical chapter reference sections. Entries remain grouped by chapter because repeated sources may support different claims. Software documentation is version-sensitive; access dates in the chapters are authoritative.\n\n"
    (ROOT / "REFERENCES.md").write_text(header + "\n".join(sections))
    print(json.dumps({k: v for k, v in report.items() if k != "inventory"}, indent=2))
    raise SystemExit(bool(errors))

if __name__ == "__main__":
    main()
