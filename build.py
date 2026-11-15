"""Bundle each module with the shared layer + its book notes, zip it, and assemble the plugin.

Usage: uv run --no-project build.py [module-name ...]   (default: every folder in modules/)
Outputs:
  dist/job-search-assistant.zip     ONE skill for chat apps (Claude, ChatGPT, Gemini, Grok): a router SKILL.md
                                    plus every module under references/<module>/. One upload installs everything.
  dist/<module>.zip                 advanced: a single module as its own skill (top-level folder = module, SKILL.md inside)
  dist/job-search-assistant-all.zip every module as a separate skill folder (unzip into ~/.claude/skills/ or ~/.agents/skills/)
  plugin/skills/<module>/           one plugin for every host: .claude-plugin/plugin.json (Claude Code) and
                                    plugin.json (portable manifest for ChatGPT / Codex), served by
                                    .claude-plugin/marketplace.json and .agents/plugins/marketplace.json

Every run ends with check(): the packaging rules the hosts enforce (see AGENTS.md). A failed check exits non-zero.
"""

import json
import re
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
BUNDLE_SRC = ROOT / "bundle"
BUNDLE_NAME = "job-search-assistant"
INSTALL_JSON = ROOT / "docs" / "install.json"

# The Gemini app rejects binary files, so skills ship plain text only.
TEXT_SUFFIXES = {".md", ".csv", ".json", ".py", ".yaml", ".yml", ".txt"}
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")

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
BOOK_NOTES_INDEX = ["# Book notes (source excerpts)\n", "Open one only to verify a claim or when the user asks what a book says.\n"]


def write_book_notes(dest: Path, notes: list[str]) -> None:
    dest.mkdir(parents=True)
    lines = list(BOOK_NOTES_INDEX)
    for rel in notes:
        src = LIBRARY / rel
        shutil.copy2(src, dest / src.name)
        lines.append(f"- `{src.name}`")
    (dest / "INDEX.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def stage(module: Path) -> None:
    refs = module / "references"
    for name in ("_shared", "book-notes"):
        if (refs / name).exists():
            shutil.rmtree(refs / name)
    shutil.copytree(SHARED, refs / "_shared")
    notes = BOOK_NOTES.get(module.name, [])
    if notes:
        write_book_notes(refs / "book-notes", notes)


def zip_dir(zf: zipfile.ZipFile, folder: Path) -> None:
    for f in sorted(folder.rglob("*")):
        if f.is_file():
            zf.write(f, Path(folder.name) / f.relative_to(folder))


def frontmatter(text: str) -> tuple[dict[str, str], str]:
    """Return (top-level key: value pairs, body) of a SKILL.md."""
    m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n?(.*)$", text, re.S)
    if not m:
        return {}, text
    fields = {}
    for line in m.group(1).splitlines():
        key, sep, value = line.partition(":")
        if sep and not line.startswith((" ", "\t")):
            fields[key.strip()] = value.strip()
    return fields, m.group(2)


def build_bundle(all_modules: list[Path]) -> Path:
    """One skill for chat apps: bundle/SKILL.md routes to references/<module>/MODULE.md.

    Each module keeps its own folder layout, so the paths written inside a module still resolve
    relative to that module's folder. The shared layer and the book notes are stored once, at the
    bundle's top-level references/, instead of once per module.
    """
    work = DIST / "_bundle" / BUNDLE_NAME
    if work.parent.exists():
        shutil.rmtree(work.parent)
    shutil.copytree(BUNDLE_SRC, work)
    refs = work / "references"
    shutil.copytree(SHARED, refs / "_shared")
    notes = sorted({rel for m in all_modules for rel in BOOK_NOTES.get(m.name, [])})
    write_book_notes(refs / "book-notes", notes)
    skip = shutil.ignore_patterns("_shared", "book-notes", "agents")
    for module in all_modules:
        dest = refs / module.name
        shutil.copytree(module, dest, ignore=skip)
        fields, body = frontmatter((dest / "SKILL.md").read_text(encoding="utf-8"))
        (dest / "SKILL.md").unlink()  # a nested SKILL.md could be read as a second skill
        header = f"<!-- Module {module.name}. {fields.get('description', '')} -->\n\n"
        (dest / "MODULE.md").write_text(header + body.lstrip(), encoding="utf-8")
    out = DIST / f"{BUNDLE_NAME}.zip"
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
        zip_dir(zf, work)
    shutil.rmtree(work.parent)
    return out


def check(all_modules: list[Path], built: list[str]) -> None:
    """Packaging rules that hosts enforce. Collect every failure, then exit non-zero if there is one."""
    errors: list[str] = []
    names = [m.name for m in all_modules]

    def check_skill(label: str, folder: str, text: str) -> None:
        fields, _ = frontmatter(text)
        name, desc = fields.get("name", ""), fields.get("description", "")
        if name != folder:
            errors.append(f"{label}: folder '{folder}' must equal frontmatter name '{name}' (Gemini rule)")
        if not NAME_RE.match(name) or len(name) > 64:
            errors.append(f"{label}: name '{name}' must be lowercase letters, digits and hyphens, 64 chars max")
        if not desc or len(desc) > 1024:
            errors.append(f"{label}: description must be 1 to 1024 characters (is {len(desc)})")

    def check_zip(path: Path, skill_folders: list[str]) -> zipfile.ZipFile | None:
        if not path.exists():
            errors.append(f"{path.name}: not built")
            return None
        zf = zipfile.ZipFile(path)
        members = zf.namelist()
        tops = sorted({n.split("/")[0] for n in members})
        if tops != sorted(skill_folders):
            errors.append(f"{path.name}: top-level folders {tops}, expected {sorted(skill_folders)}")
        for n in members:
            if Path(n).name == "QUICKSTART.md":
                errors.append(f"{path.name}: ships {n}; install steps live on the site and in hosts.md only")
            if Path(n).suffix not in TEXT_SUFFIXES:
                errors.append(f"{path.name}: {n} is not a plain-text file (the Gemini app rejects binaries)")
        skills = [n for n in members if Path(n).name == "SKILL.md"]
        expected = sorted(f"{f}/SKILL.md" for f in skill_folders)
        if sorted(skills) != expected:
            errors.append(f"{path.name}: SKILL.md files {sorted(skills)}, expected {expected}")
        for folder in skill_folders:
            if f"{folder}/SKILL.md" in members:
                check_skill(f"{path.name}:{folder}", folder, zf.read(f"{folder}/SKILL.md").decode("utf-8"))
        return zf

    for name in built:
        check_zip(DIST / f"{name}.zip", [name])
    check_zip(DIST / "job-search-assistant-all.zip", names)

    zf = check_zip(DIST / f"{BUNDLE_NAME}.zip", [BUNDLE_NAME])
    if zf:
        members = set(zf.namelist())
        router = zf.read(f"{BUNDLE_NAME}/SKILL.md").decode("utf-8") if f"{BUNDLE_NAME}/SKILL.md" in members else ""
        for name in names:
            if f"{BUNDLE_NAME}/references/{name}/MODULE.md" not in members:
                errors.append(f"bundle: references/{name}/MODULE.md is missing")
            if f"references/{name}/MODULE.md" not in router:
                errors.append(f"bundle: the router SKILL.md never points to references/{name}/MODULE.md")
        for shared in SHARED.iterdir():
            if f"{BUNDLE_NAME}/references/_shared/{shared.name}" not in members:
                errors.append(f"bundle: references/_shared/{shared.name} is missing")

    if INSTALL_JSON.exists():
        listed = json.loads(INSTALL_JSON.read_text(encoding="utf-8")).get("skills", [])
        if sorted(listed) != sorted(names):
            errors.append(f"docs/install.json: skills {sorted(listed)} do not match modules/ {sorted(names)}")

    if errors:
        raise SystemExit("check failed:\n  " + "\n  ".join(errors))
    print(f"check ok  {len(built) + 2} zips, {len(names)} modules")


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
    for module in all_modules:
        if module.name not in names:
            stage(module)  # the all-in-one zip, the bundle and the plugin need every module staged
    out = DIST / "job-search-assistant-all.zip"
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
        for module in all_modules:
            zip_dir(zf, module)
    print(f"{out.relative_to(ROOT)}  {out.stat().st_size / 1024:.0f} KB")

    out = build_bundle(all_modules)
    print(f"{out.relative_to(ROOT)}  {out.stat().st_size / 1024:.0f} KB")

    if PLUGIN_SKILLS.exists():
        shutil.rmtree(PLUGIN_SKILLS)
    for module in all_modules:
        shutil.copytree(module, PLUGIN_SKILLS / module.name)
    print(f"plugin/skills  {len(all_modules)} skills")

    check(all_modules, names)


if __name__ == "__main__":
    main()
