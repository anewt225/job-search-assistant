# Hosts: the only app-specific file

Modules never assume which AI app they run in. When a step depends on the app (connecting a tool,
saving the profile, scheduling, voice), look up the current host's row here. **Check capabilities by
the tools you actually have** (can you run code? is there a calendar tool?), not by the host's name.
If you can't tell the host and it matters, ask once and record it in profile §4 `host app`.

| Host | Install the skills | Where the profile lives | Connect tools | Run code | Schedule | Voice |
|---|---|---|---|---|---|---|
| **Claude app / claude.ai** | Settings → Capabilities → Skills → upload a module `.zip` | Project knowledge (Project "Job Search") | Settings → Connectors | Settings → Capabilities → *Code execution and file creation* | Scheduled tasks (desktop app, Cowork) | Voice mode button |
| **Claude Code** | `/plugin marketplace add anewt225/job-search-assistant`, or unzip into `~/.claude/skills/` | `~/.claude/job-search/` | `/mcp`, or a plugin | yes (shell) | `/schedule` | — |
| **ChatGPT** | Skills (when enabled for the workspace) → upload, or install the plugin | Project files (Project "Job Search") | Settings → Apps (formerly connectors) | yes, when code/data analysis is on | Tasks (scheduled) | Voice mode |
| **Codex** (CLI, IDE, app) | `codex plugin marketplace add anewt225/job-search-assistant`, or unzip into `~/.agents/skills/` | `~/.agents/job-search/` | MCP servers in `~/.codex/config.toml`, or a plugin | yes (shell) | Codex app automations, if available; otherwise on demand | — |
| **Gemini app** (web, Mac, mobile) | Settings → Skills → Upload → a module `.zip` (web or Mac; personal Google account, 18+) | Attach `job-search-profile.md` at the start of a chat, or paste it | Settings → Apps (Gmail, Calendar, Drive, Keep, Tasks are built in) | yes, but scripts can't reach the internet | Scheduled actions (paid plans) | Gemini Live |
| **Gemini Gems** (being retired; use skills) | No skills folder. Paste a module's `SKILL.md` into the Gem's instructions; add its `references/` files as knowledge (10 files max) | The Gem's knowledge files | Same as the Gemini app | same as the Gemini app | — | Gemini Live |
| **Antigravity** (IDE and `agy` CLI) | Copy the modules into `~/.gemini/config/skills/` (all workspaces) or `<workspace>/.agents/skills/` | `~/.agents/job-search/` or `./job-search-profile.md` | MCP servers (the IDE's MCP settings, or a plugin's `mcp_config.json`) | yes (terminal) | on demand | — |
| **Grok** (grok.com, apps) | Skills → upload a module `.zip` | Project files, or attach the profile | Connectors, where available | yes | Tasks (scheduled) | Voice mode |
| **Other Agent Skills hosts** (GitHub Copilot, Cursor, Gemini CLI, Muse Code, Perplexity Computer …) | The host's skills folder or upload (`SKILL.md` folders, per its docs); many read `.agents/skills/` | `./job-search-profile.md` in the working folder | The host's MCP config | if it has a shell | the OS scheduler, or on demand | — |

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
