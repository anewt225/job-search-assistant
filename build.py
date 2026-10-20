"""Bundle each module with the shared layer + its book notes, zip it, and assemble the Claude Code plugin.

Usage: uv run --no-project build.py [module-name ...]   (default: every folder in modules/)
Outputs:
  dist/<module>.zip                 claude.ai skill upload format (top-level folder = module, SKILL.md inside)
  dist/job-search-assistant-all.zip every module in one zip (unzip into ~/.claude/skills/)
  plugin/skills/<module>/           Claude Code plugin served by .claude-plugin/marketplace.json
"""

import shutil
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).parent
MODULES = ROOT / "modules"
SHARED = ROOT / "shared"
LIBRARY = ROOT / "library"
DIST = ROOT / "dist"
PLUGIN_SKILLS = ROOT / "plugin" / "skills"
QUICKSTART = ROOT / "docs" / "QUICKSTART.md"

# Book notes each module ships with (paths relative to library/). Loaded lazily by the skills.
BOOK_NOTES = {
    "job-search-networking": [
        "the-2-hour-job-search.md",
        "reverse-the-search.md",
        "linked.md",
        "never-search-alone/outreach-thank-you-and-follow-up-notes.md",
        "never-search-alone/golden-question-interview-template.md",
        "never-search-alone/reverse-exit-interview-template.md",
    ],
    "job-search-interview": ["the-job-closer.md", "career-coach-gpt.md", "reverse-the-search.md"],
    "job-search-resume": ["career-coach-gpt.md", "reverse-the-search.md", "linked.md", "the-job-closer.md"],
    "job-search-linkedin": ["linked.md", "career-coach-gpt.md", "reverse-the-search.md"],
    "job-search-discovery": [
        "designing-your-life.md",
        "pivot.md",
        "the-start-up-of-you.md",
        "great-at-work.md",
        "fire-me-i-beg-you.md",
    ],
    "job-search-negotiation": [
        "career-coach-gpt.md",
        "reverse-the-search.md",
        "never-search-alone/job-mission-with-okrs-examples.md",
    ],
}


def stage(module: Path) -> None:
    refs = module / "references"
    for name in ("_shared", "book-notes"):
        if (refs / name).exists():
            shutil.rmtree(refs / name)
    shutil.copytree(SHARED, refs / "_shared")
    notes = BOOK_NOTES.get(module.name, [])
    if notes:
        dest = refs / "book-notes"
        dest.mkdir(parents=True)
        lines = ["# Book notes (source excerpts)\n", "Open one only to verify a claim or when the user asks what a book says.\n"]
        for rel in notes:
            src = LIBRARY / rel
            shutil.copy2(src, dest / src.name)
            lines.append(f"- `{src.name}`")
        (dest / "INDEX.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def zip_dir(zf: zipfile.ZipFile, module: Path) -> None:
    for f in sorted(module.rglob("*")):
        if f.is_file():
            zf.write(f, Path(module.name) / f.relative_to(module))
    if QUICKSTART.exists():
        zf.write(QUICKSTART, Path(module.name) / "QUICKSTART.md")


def main() -> None:
    names = sys.argv[1:] or sorted(p.name for p in MODULES.iterdir() if p.is_dir())
    DIST.mkdir(exist_ok=True)
    for name in names:
        module = MODULES / name
        if not (module / "SKILL.md").exists():
            raise SystemExit(f"{name}: missing SKILL.md")
        stage(module)
        out = DIST / f"{name}.zip"
        with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
            zip_dir(zf, module)
        print(f"{out.relative_to(ROOT)}  {out.stat().st_size / 1024:.0f} KB")

    all_modules = sorted(p for p in MODULES.iterdir() if (p / "SKILL.md").exists())
    out = DIST / "job-search-assistant-all.zip"
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
        for module in all_modules:
            zip_dir(zf, module)
    print(f"{out.relative_to(ROOT)}  {out.stat().st_size / 1024:.0f} KB")

    if PLUGIN_SKILLS.exists():
        shutil.rmtree(PLUGIN_SKILLS)
    for module in all_modules:
        shutil.copytree(module, PLUGIN_SKILLS / module.name)
    print(f"plugin/skills  {len(all_modules)} skills")


if __name__ == "__main__":
    main()
