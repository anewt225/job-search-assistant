# Job Search Assistant

**Eight small AI skills that cover the whole job search**, from figuring out what to target to
negotiating the offer. They're grounded in proven playbooks (*The 2-Hour Job Search*, *Never Search
Alone*, *Reverse the Search*, *Linked*, *The Job Closer*, *Career Coach GPT*), wired to whatever tools you
already use, and tuned to the kind of coach you want. They're standard [Agent Skills](https://agentskills.io)
(`SKILL.md` folders), so they run in **Claude, ChatGPT, Gemini, Grok, Codex, Antigravity, Claude Code** and other apps that
read them.

### ▶ **[Start here: interactive setup & downloads](https://anewt225.github.io/job-search-assistant/)**

---

## Modules

Each module is a standalone skill. Install one, or all of them.

| Module | What it does | Try saying | Download |
|---|---|---|---|
| **Setup & hub** | A welcome, then one 5-step setup (about 5 minutes), persona, tracker import, "where do I start?" | "Set up my job search" | [zip](https://github.com/anewt225/job-search-assistant/releases/latest/download/job-search-setup.zip) |
| **Self-discovery** | A playful quiz → strengths, must-haves, target roles, two-pager, Candidate–Market Fit statement | "Help me figure out what roles fit me" | [zip](https://github.com/anewt225/job-search-assistant/releases/latest/download/job-search-discovery.zip) |
| **LinkedIn** | 100-point score + 7-advisor panel, rewrites in your voice, exportable to-dos, re-check | "Score my LinkedIn for Product Ops Manager" | [zip](https://github.com/anewt225/job-search-assistant/releases/latest/download/job-search-linkedin.zip) |
| **Resume & cover letter** | Score against a JD, tailor with GLORY + Pareto, before/after delta | "Tailor my resume for <posting URL>" | [zip](https://github.com/anewt225/job-search-assistant/releases/latest/download/job-search-resume.zip) |
| **Networking & events** | 6-Point cold emails, warm reconnects, referral asks, follow-ups, contact triage, event briefs + calendar blocks | "Draft outreach to Priya at Lumen, no connection" | [zip](https://github.com/anewt225/job-search-assistant/releases/latest/download/job-search-networking.zip) |
| **Interviews** | Prep brief, 25-min voice mock interview, debrief + thank-you + tasks | "Prep me for my interview with Northwind" | [zip](https://github.com/anewt225/job-search-assistant/releases/latest/download/job-search-interview.zip) |
| **Negotiation** | Comp research, offer comparison, counter scripts, recruiter role-play | "I got an offer. Help me negotiate" | [zip](https://github.com/anewt225/job-search-assistant/releases/latest/download/job-search-negotiation.zip) |
| **Daily & weekly rhythm** | 2-min stand-up; weekly retro → week-ahead with time blocks; can be scheduled | "Run my weekly review" | [zip](https://github.com/anewt225/job-search-assistant/releases/latest/download/job-search-rhythm.zip) |

**Chat apps (Claude, ChatGPT, Gemini, Grok): [one zip, one upload →](https://github.com/anewt225/job-search-assistant/releases/latest/download/job-search-assistant.zip)** · Skills folders: [all 8 as separate skills →](https://github.com/anewt225/job-search-assistant/releases/latest/download/job-search-assistant-all.zip)

## Install

**Claude desktop app or claude.ai** (Pro, Max, Team or Enterprise)
1. Settings → **Capabilities** → turn on *Code execution and file creation*.
2. Settings → **Customize** → **Skills** → *Add* → *Upload a skill* → choose `job-search-assistant.zip` (don't unzip it).
3. Create a **Project** called "Job Search" and add your `job-search-profile.md` to its knowledge.

**ChatGPT** (workspaces with Skills turned on)
1. Upload `job-search-assistant.zip` from the Skills page, or install the plugin from the ChatGPT desktop app's plugin directory
   (after adding the marketplace with the Codex command below).
2. Create a **Project** called "Job Search" and add your `job-search-profile.md` to its files.

**Gemini app** (personal Google account; web or Mac app; skills need *Keep Activity* on, so Google keeps your chats)
1. Settings → **Skills** → *Upload* → choose `job-search-assistant.zip`. Pick the skill with `/` in any chat.
2. Gemini has no projects, so attach your `job-search-profile.md` at the start of a job-search chat.
3. Optional: Settings → **Apps** → turn on Gmail, Calendar, Drive and Tasks.

Gems are being replaced by skills (personal accounts from November 2026), so use skills rather than a Gem.

**Grok**
1. **Skills** → upload `job-search-assistant.zip`.
2. Add your `job-search-profile.md` to a Project's files, or attach it to the chat.

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

**Antigravity** (IDE or `agy` CLI)
Unzip the modules into `~/.gemini/config/skills/` (every workspace) or `<workspace>/.agents/skills/`.

**Anything else that reads Agent Skills** (GitHub Copilot, Cursor, Gemini CLI, Muse Code, Perplexity
Computer …): put the module folders wherever that app loads skills from. Many read `.agents/skills/`.

### Install by prompt (coding agents)
In an app that can run commands for you (Claude Code, Codex, Antigravity, Gemini CLI), paste this and
swap in your app's skills folder: `~/.claude/skills/` · `~/.agents/skills/` (Codex) ·
`~/.gemini/config/skills/` (Antigravity) · `~/.gemini/skills/` (Gemini CLI).

```
Install the Job Search Assistant skills for me.
1. Get https://github.com/anewt225/job-search-assistant (git clone --depth 1 into a temporary folder, or download the main branch).
2. Copy every folder inside its plugin/skills/ directory into ~/.claude/skills/ (create it if it doesn't exist). Replace older copies of the same job-search-* folders and touch nothing else.
3. Delete the temporary folder.
4. List the skills you installed, then tell me to start a new session and say: Set up my job search
```

Chat apps can't install from a prompt; they need the upload above. Agents: the same facts are in
[`docs/install.json`](docs/install.json).

### After installing: say this
Type `/` to see the skills, then say one of:
- "Set up my job search" (5 short steps, about 5 minutes, all optional)
- "Tailor my resume for <posting link>"
- "I have an interview today with <company>" (skips setup and preps you now)

You get `job-search-profile.md` by saying "set up my job search", or from
[the optional setup wizard](https://anewt225.github.io/job-search-assistant/#wizard). No connection is required. Optional: connect Gmail/Outlook, Google/Outlook Calendar, Drive/OneDrive,
Notion/Sheets/Airtable, Todoist/TickTick, Fireflies/Granola. Claude and Grok call these *Connectors*, ChatGPT and
Gemini call them *Apps*, and Codex, Claude Code and Antigravity use *MCP servers*. Per-app details: [`shared/hosts.md`](shared/hosts.md).

## How it fits together

```
job-search-profile.md   ← written once by setup; read first by every module (small = cheap)
        │
        ├── your tools (optional): email · calendar · files · tasks · meeting notes
        └── your tracker: Companies ← Contacts ← Meetings → Opportunities, plus Tasks
```

- **One profile, many modules.** Your targets, rules, persona and tool locations live in one short
  file. Modules read it instead of re-asking you, and only load their reference files for the mode you use.
- **One setup, five steps.** Where you are → how you want to work → your tools → about you → review and
  first task. One question at a time, each with a suggested answer. Need help today? Say so and setup waits.
- **Bring your own tools, by job.** For tracking, files, email, calendar, tasks and meeting notes, setup
  asks what you already use, suggests whatever it can see connected, and always offers "no tool".
  Everything works with no connectors at all (paste and upload).
- **Personas.** Coach · Strategist · Mentor · Peer · Accountability Partner · Champion. Pick one, or take
  the 5-question quiz.
- **Ground rules.** Drafts only, never sends. Never guesses email addresses. At most 3 outreach drafts
  per sitting. Success is measured in **live conversations per week**, not applications.

<a id="tracker"></a>
## Tracker templates

Five tables, 12 fields or fewer each, with sample data showing how they connect: **Companies** (with
LAMP scoring) · **Contacts** · **Opportunities** · **Meetings** (only *live* ones count toward your weekly
target) · **Tasks**.
- **Notion:** [duplicate the template](https://alexnewton.notion.site/job-search-assistant-template?source=github_asst), then share it with your assistant's Notion connector. Or let setup build the databases for you.
- **Google Sheets, Excel, Airtable, Obsidian:** import [`templates/tracker-csv/`](templates/tracker-csv).
- **Already have a tracker?** Say "import my tracker". The assistant maps your columns to the schema and dedupes.

Schema: [`shared/data-schema.md`](shared/data-schema.md)

## Repo layout

```
modules/<module>/       SKILL.md + references/ + agents/openai.yaml (source of truth for each skill)
bundle/                 router SKILL.md for the one-upload zip (modules are added under references/ at build time)
shared/                 setup, personas, profile template, data schema, hosts.md (bundled into every module)
library/                book notes the modules cite (bundled per module, loaded only on demand)
templates/tracker-csv/  tracker templates with sample data
plugin/                 one plugin for Claude Code, ChatGPT and Codex (generated by build.py)
.agents/plugins/        OpenAI marketplace · .claude-plugin/ Claude marketplace
AGENTS.md               instructions for coding agents working on this repo
docs/                   GitHub Pages site + setup wizard, install.json (install facts for agents), V2-SPEC.md
build.py                uv run --no-project build.py → dist/*.zip + plugin/skills/, then checks the packaging rules
```

## Principles

Platform-agnostic, portable, minimal data, a human approves anything that reaches another person.
The full list, each linked to where the product keeps it, is in [`PRINCIPLES.md`](PRINCIPLES.md).

## Credits & license

Frameworks belong to their authors: Steve Dalton, Phyl Terry, Madeline Mann, Omar Garriott & Jeremy
Schifeling, Bill Burnett & Dave Evans, Jenny Blake, Richard Bolles, Reid Hoffman & Ben Casnocha, and
others. The `library/` notes are personal study notes that cite those works. Please buy the books.
Code and original text: MIT. Not affiliated with Anthropic, OpenAI, Google or xAI.

Built by [Alex Newton](https://github.com/anewt225).
