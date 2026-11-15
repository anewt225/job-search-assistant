# Hosts: the only app-specific file

Modules never assume which AI app they run in. When a step depends on the app (connecting a tool,
saving the profile, scheduling, voice), look up the current host's row here. **Check capabilities by
the tools you actually have** (can you run code? is there a calendar tool?), not by the host's name.
If you can't tell the host and it matters, ask once and record it in profile §4 `host app`.

| Host | Install the skills | Install path last checked live | Where the profile lives | Connect tools | Run code | Schedule | Voice |
|---|---|---|---|---|---|---|---|
| **Claude app / claude.ai** | Settings → Customize → Skills → Add → Upload a skill → `job-search-assistant.zip` (one upload, don't unzip) | 2026-11, upload path only (the code-execution toggle was not re-checked) | Project knowledge (Project "Job Search") | Settings → Connectors | Settings → Capabilities → *Code execution and file creation* | Scheduled tasks (desktop app, Cowork) | Voice mode button |
| **Claude Code** | `/plugin marketplace add anewt225/job-search-assistant`, or unzip into `~/.claude/skills/` | not yet | `~/.claude/job-search/` | `/mcp`, or a plugin | yes (shell) | `/schedule` | — |
| **ChatGPT** | Skills (when enabled for the workspace) → upload `job-search-assistant.zip`, or install the plugin | not yet | Project files (Project "Job Search") | Settings → Apps (formerly connectors) | yes, when code/data analysis is on | Tasks (scheduled) | Voice mode |
| **Codex** (CLI, IDE, app) | `codex plugin marketplace add anewt225/job-search-assistant`, or unzip into `~/.agents/skills/` | not yet | `~/.agents/job-search/` | MCP servers in `~/.codex/config.toml`, or a plugin | yes (shell) | Codex app automations, if available; otherwise on demand | — |
| **Gemini app** (web, Mac, mobile) | Settings → Skills → Upload → `job-search-assistant.zip` (web or Mac; personal Google account, 18+) | not yet | Attach `job-search-profile.md` at the start of a chat, or paste it | Settings → Apps (Gmail, Calendar, Drive, Keep, Tasks are built in) | yes, but scripts can't reach the internet | Scheduled actions (paid plans) | Gemini Live |
| **Gemini Gems** (being retired; use skills) | No skills folder. Paste a module's `SKILL.md` into the Gem's instructions; add its `references/` files as knowledge (10 files max) | not yet | The Gem's knowledge files | Same as the Gemini app | same as the Gemini app | — | Gemini Live |
| **Antigravity** (IDE and `agy` CLI) | Copy the modules into `~/.gemini/config/skills/` (all workspaces) or `<workspace>/.agents/skills/` | not yet | `~/.agents/job-search/` or `./job-search-profile.md` | MCP servers (the IDE's MCP settings, or a plugin's `mcp_config.json`) | yes (terminal) | on demand | — |
| **Grok** (grok.com, apps) | Skills → upload `job-search-assistant.zip` | not yet | Project files, or attach the profile | Connectors, where available | yes | Tasks (scheduled) | Voice mode |
| **Other Agent Skills hosts** (GitHub Copilot, Cursor, Gemini CLI, Muse Code, Perplexity Computer …) | The host's skills folder or upload (`SKILL.md` folders, per its docs); many read `.agents/skills/`. Gemini CLI: `~/.gemini/skills/` | not yet | `./job-search-profile.md` in the working folder | The host's MCP config | if it has a shell | the OS scheduler, or on demand | — |

**One zip or eight.** Chat apps (Claude, ChatGPT, Gemini, Grok) take one skill per upload, so they get
`job-search-assistant.zip`: every module in a single skill. The per-module zips are the advanced option.
Apps with a skills folder or a plugin system (Claude Code, Codex, Antigravity, Gemini CLI) install the
eight modules as separate skills.

**Checked live** means someone followed the path in the real app and it worked, on that date. "Not yet"
paths come from each app's documentation. Re-check a path before changing it, and update the date here,
on the site (`docs/index.html`) and in `docs/QUICKSTART.md` together.

**Words differ by host.** "Connector" (Claude, Grok), "app" (ChatGPT, Gemini) and "MCP server" (Codex,
Claude Code, Antigravity) mean the same thing here: a tool that reaches the user's email, calendar,
files, tasks or tracker. Use the host's word when talking to the user.

**Gemini specifics.** A Gemini skill can't fetch web pages from a script, and Drive files can't be
bundled into a skill yet. Use Gemini's own Google apps (Gmail, Drive, Calendar) for live data instead,
and ask the user to attach or paste anything else. In the app, `/` (soon `@`) picks a skill by name.
Skills only work with *Keep Activity* on, which means Google keeps the user's Gemini chats. Say so
once during setup, before the user adds personal data, and point them to Gemini's activity settings.

**No tool, no problem.** Every feature has a manual fallback (paste, upload, or a file the user saves).
Never block a run because a connector is missing; say which one would help and carry on.
