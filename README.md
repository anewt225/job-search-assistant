# Job Search Assistant

**Eight small AI skills that cover the whole job search**, from figuring out what to target to
negotiating the offer. They're grounded in proven playbooks (*The 2-Hour Job Search*, *Never Search
Alone*, *Reverse the Search*, *Linked*, *The Job Closer*, *Career Coach GPT*), wired to whatever tools you
already use, and tuned to the kind of coach you want. They're standard [Agent Skills](https://agentskills.io)
(`SKILL.md` folders), so they run in **Claude, ChatGPT, Codex, Claude Code** and other apps that read them.

### ▶ **[Start here: interactive setup & downloads](https://anewt225.github.io/job-search-assistant/)**

---

## Modules

Each module is a standalone skill. Install one, or all of them.

| Module | What it does | Try saying | Download |
|---|---|---|---|
| **Setup & hub** | Onboarding (Quick or bring-your-own, per tool), persona, tracker import, "where do I start?" | "Set up my job search" | [zip](https://github.com/anewt225/job-search-assistant/releases/latest/download/job-search-setup.zip) |
| **Self-discovery** | A playful quiz → strengths, must-haves, target roles, two-pager, Candidate–Market Fit statement | "Help me figure out what roles fit me" | [zip](https://github.com/anewt225/job-search-assistant/releases/latest/download/job-search-discovery.zip) |
| **LinkedIn** | 100-point score + 7-advisor panel, rewrites in your voice, exportable to-dos, re-check | "Score my LinkedIn for Product Ops Manager" | [zip](https://github.com/anewt225/job-search-assistant/releases/latest/download/job-search-linkedin.zip) |
| **Resume & cover letter** | Score against a JD, tailor with GLORY + Pareto, before/after delta | "Tailor my resume for <posting URL>" | [zip](https://github.com/anewt225/job-search-assistant/releases/latest/download/job-search-resume.zip) |
| **Networking & events** | 6-Point cold emails, warm reconnects, referral asks, follow-ups, contact triage, event briefs + calendar blocks | "Draft outreach to Priya at Lumen, no connection" | [zip](https://github.com/anewt225/job-search-assistant/releases/latest/download/job-search-networking.zip) |
| **Interviews** | Prep brief, 25-min voice mock interview, debrief + thank-you + tasks | "Prep me for my interview with Northwind" | [zip](https://github.com/anewt225/job-search-assistant/releases/latest/download/job-search-interview.zip) |
| **Negotiation** | Comp research, offer comparison, counter scripts, recruiter role-play | "I got an offer. Help me negotiate" | [zip](https://github.com/anewt225/job-search-assistant/releases/latest/download/job-search-negotiation.zip) |
| **Daily & weekly rhythm** | 2-min stand-up; weekly retro → week-ahead with time blocks; can be scheduled | "Run my weekly review" | [zip](https://github.com/anewt225/job-search-assistant/releases/latest/download/job-search-rhythm.zip) |

**[Download all 8 →](https://github.com/anewt225/job-search-assistant/releases/latest/download/job-search-assistant-all.zip)**

## Install

**Claude desktop app or claude.ai** (Pro, Max, Team or Enterprise)
1. Settings → **Capabilities** → turn on *Code execution and file creation*.
2. Settings → Capabilities → **Skills** → *Upload skill* → choose a module's `.zip` (don't unzip it).
3. Create a **Project** called "Job Search" and add your `job-search-profile.md` to its knowledge.

**ChatGPT** (workspaces with Skills turned on)
1. Upload a module from the Skills page, or install the plugin from the ChatGPT desktop app's plugin directory
   (after adding the marketplace below).
2. Create a **Project** called "Job Search" and add your `job-search-profile.md` to its files.

**Codex**
```
codex plugin marketplace add anewt225/job-search-assistant
```
Or unzip modules into `~/.agents/skills/`.

**Claude Code**
```
/plugin marketplace add anewt225/job-search-assistant
/plugin install job-search-assistant@job-search-assistant
```
Or unzip modules into `~/.claude/skills/`.

You get `job-search-profile.md` from [the setup wizard](https://anewt225.github.io/job-search-assistant/#wizard),
or by saying "set up my job search". Optional: connect Gmail/Outlook, Google/Outlook Calendar, Drive/OneDrive,
Notion/Sheets/Airtable, Todoist/TickTick, Fireflies/Granola. Claude calls these *Connectors*, ChatGPT calls
them *Apps*, and Codex uses *MCP servers*. Per-app details: [`shared/hosts.md`](shared/hosts.md).

## How it fits together

```
job-search-profile.md   ← written once by setup; read first by every module (small = cheap)
        │
        ├── your tools (optional): email · calendar · files · tasks · meeting notes
        └── your tracker: Companies ← Contacts ← Meetings → Opportunities, plus Tasks
```

- **One profile, many modules.** Your targets, rules, persona and tool locations live in one short
  file. Modules read it instead of re-asking you, and only load their reference files for the mode you use.
- **Bring your own tools, per component.** For each piece (email, calendar, files, tasks, meeting notes,
  tracker), setup offers *Quick* (a proven Gmail · Google Calendar · Drive · Notion · TickTick · Fireflies
  stack), *your own tool*, or *Skip*. Everything works with no connectors at all (paste and upload).
- **Personas.** Coach · Strategist · Mentor · Peer · Accountability Partner · Champion. Pick one, or take
  the 5-question quiz.
- **Ground rules.** Drafts only, never sends. Never guesses email addresses. At most 3 outreach drafts
  per sitting. Success is measured in **live conversations per week**, not applications.

<a id="tracker"></a>
## Tracker templates

Five tables, 12 fields or fewer each, with sample data showing how they connect: **Companies** (with
LAMP scoring) · **Contacts** · **Opportunities** · **Meetings** (only *live* ones count toward your weekly
target) · **Tasks**.
- **Notion:** [duplicate the template](https://alexnewton.notion.site/job-search-assistant-template?source=github_asst), then share it with Claude's Notion connector. Or let setup build the databases for you.
- **Google Sheets, Excel, Airtable, Obsidian:** import [`templates/tracker-csv/`](templates/tracker-csv).
- **Already have a tracker?** Say "import my tracker". Claude maps your columns to the schema and dedupes.

Schema: [`shared/data-schema.md`](shared/data-schema.md)

## Repo layout

```
modules/<module>/       SKILL.md + references/ + agents/openai.yaml (source of truth for each skill)
shared/                 setup, personas, profile template, data schema, hosts.md (bundled into every module)
library/                book notes the modules cite (bundled per module, loaded only on demand)
templates/tracker-csv/  tracker templates with sample data
plugin/                 one plugin for Claude Code, ChatGPT and Codex (generated by build.py)
.agents/plugins/        OpenAI marketplace · .claude-plugin/ Claude marketplace
AGENTS.md               instructions for coding agents working on this repo
docs/                   GitHub Pages site + setup wizard
build.py                uv run --no-project build.py → dist/*.zip + plugin/skills/
```

## Credits & license

Frameworks belong to their authors: Steve Dalton, Phyl Terry, Madeline Mann, Omar Garriott & Jeremy
Schifeling, Bill Burnett & Dave Evans, Jenny Blake, Richard Bolles, Reid Hoffman & Ben Casnocha, and
others. The `library/` notes are personal study notes that cite those works. Please buy the books.
Code and original text: MIT. Not affiliated with Anthropic or OpenAI.

Built by [Alex Newton](https://github.com/anewt225).
