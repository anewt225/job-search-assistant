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
| **Other Agent Skills hosts** (Cursor, Copilot, Gemini CLI …) | The host's skills folder (`SKILL.md` folders, per its docs) | `./job-search-profile.md` in the working folder | The host's MCP config | if it has a shell | the OS scheduler, or on demand | — |

**Words differ by host.** "Connector" (Claude), "app" (ChatGPT) and "MCP server" (Codex, Claude Code)
mean the same thing here: a tool that reaches the user's email, calendar, files, tasks or tracker. Use
the host's word when talking to the user.

**No tool, no problem.** Every feature has a manual fallback (paste, upload, or a file the user saves).
Never block a run because a connector is missing; say which one would help and carry on.
