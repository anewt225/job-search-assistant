# AGENTS.md

Instructions for coding agents (Codex, Claude Code, Antigravity, Cursor and others) working in this repo.

## What this is
Eight [Agent Skills](https://agentskills.io) (`SKILL.md` folders) for a job search, plus a setup
wizard site. The skills are written to run in any host that reads Agent Skills: Claude, ChatGPT,
Gemini, Grok, Codex, Antigravity, Claude Code and others. Chat apps (Claude, ChatGPT, Gemini, Grok) take
one skill per upload, so they get `job-search-assistant.zip`: a router `SKILL.md` (`bundle/`) with every
module under `references/<module>/`. The per-module zips use the same format: one top-level folder named
after the skill, `SKILL.md` inside.

## Layout
- `modules/<module>/`: source of truth for each skill (`SKILL.md`, `references/`, `agents/openai.yaml`).
- `bundle/`: the router `SKILL.md` for the one-upload zip. Add a row there when you add a module.
- `shared/`: setup, personas, profile template, data schema and `hosts.md`. Copied into every module's
  `references/_shared/` at build time. Never edit the copies.
- `library/`: book notes, copied into `references/book-notes/` per module at build time.
- `plugin/`: generated. One folder serves both hosts: `.claude-plugin/plugin.json` (Claude Code) and
  `plugin.json` (portable manifest, read by ChatGPT and Codex).
- `.claude-plugin/marketplace.json` and `.agents/plugins/marketplace.json`: Claude and OpenAI
  marketplaces, both pointing at `./plugin`.
- `docs/`: GitHub Pages site and setup wizard (a single static `index.html`), `install.json` (install
  facts for agents; keep it in step with `shared/hosts.md`) and `V2-SPEC.md` (the v2 design).

## Build
```
uv run --no-project build.py
```
Writes `dist/*.zip` (the one-upload bundle, one per module, and an all-in-one), regenerates
`plugin/skills/`, then runs the packaging checks (folder name equals `name:`, plain-text files only, no
second set of install steps inside a zip). A failed check exits non-zero. There is no other test suite.

## Rules for edits
- Follow [`PRINCIPLES.md`](PRINCIPLES.md). If a change conflicts with a principle, flag it instead of
  working around it.
- Keep skills host-neutral. Anything app-specific (menu paths, where files live, scheduling, voice)
  goes in `shared/hosts.md` only; modules point to it. Say "the assistant", not a product name.
- Setup is one flow: `shared/setup.md` (welcome turn, urgent path, five steps, one question per turn).
  Don't add a second variant in a module or on the site; change the flow there.
- Install steps live in `shared/hosts.md`, `docs/index.html` and `docs/QUICKSTART.md`. Change all three
  together, and never ship install steps inside a zip.
- Keep `SKILL.md` files short; put detail in `references/` so it loads only when needed.
- Ground rules are product features: drafts only, never send; never guess email addresses; at most
  3 outreach drafts per run.
- Keep module files plain text (`.md`, `.csv`, `.json`, `.py`, `.yaml`). The Gemini app rejects binary
  files such as `.docx` and `.xlsx`, and its scripts can't reach the internet, so no script may depend on
  a network call.
- Keep each skill's folder name equal to its `name:` frontmatter (Gemini requires it).
- `private/` is personal material and is gitignored. Never publish from it.
