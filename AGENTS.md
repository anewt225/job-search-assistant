# AGENTS.md

Instructions for coding agents (Codex, Claude Code, Cursor and others) working in this repo.

## What this is
Eight [Agent Skills](https://agentskills.io) (`SKILL.md` folders) for a job search, plus a setup
wizard site. The skills are written to run in any host that reads Agent Skills: Claude, ChatGPT,
Codex, Claude Code and others.

## Layout
- `modules/<module>/`: source of truth for each skill (`SKILL.md`, `references/`, `agents/openai.yaml`).
- `shared/`: setup, personas, profile template, data schema and `hosts.md`. Copied into every module's
  `references/_shared/` at build time. Never edit the copies.
- `library/`: book notes, copied into `references/book-notes/` per module at build time.
- `plugin/`: generated. One folder serves both hosts: `.claude-plugin/plugin.json` (Claude Code) and
  `plugin.json` (portable manifest, read by ChatGPT and Codex).
- `.claude-plugin/marketplace.json` and `.agents/plugins/marketplace.json`: Claude and OpenAI
  marketplaces, both pointing at `./plugin`.
- `docs/`: GitHub Pages site and setup wizard (a single static `index.html`).

## Build
```
uv run --no-project build.py
```
Writes `dist/*.zip` (one per module plus an all-in-one) and regenerates `plugin/skills/`.

## Rules for edits
- Keep skills host-neutral. Anything app-specific (menu paths, where files live, scheduling, voice)
  goes in `shared/hosts.md` only; modules point to it. Say "the assistant", not a product name.
- Keep `SKILL.md` files short; put detail in `references/` so it loads only when needed.
- Ground rules are product features: drafts only, never send; never guess email addresses; at most
  3 outreach drafts per run.
- `private/` is personal material and is gitignored. Never publish from it.
