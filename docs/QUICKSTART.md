# Job Search Assistant: Quick Start

These skills turn your AI assistant (Claude, ChatGPT, Codex or any app that reads Agent Skills) into a job-search assistant. They're built on proven playbooks: *The 2-Hour Job Search*, *Never Search Alone*, *Reverse the Search* and *Linked*. Each module works on its own. Install one or all of them.

## 1. Install (2 minutes)

**Claude desktop app or claude.ai** (Pro, Max, Team or Enterprise)
1. Settings → **Capabilities** → make sure **Code execution and file creation** is on.
2. Settings → **Capabilities → Skills** → **Upload skill** → choose the `.zip` file. Don't unzip it first.

**ChatGPT** (workspaces with Skills turned on)
- Upload the module from the Skills page, or install the plugin from the ChatGPT desktop app's plugin directory.

**Codex**
- `codex plugin marketplace add anewt225/job-search-assistant`, or unzip into `~/.agents/skills/`.

**Claude Code**
- `/plugin marketplace add anewt225/job-search-assistant`, or unzip into `~/.claude/skills/`.

## 2. Recommended: make a project
Create a **Project** called *Job Search* (Claude and ChatGPT both have them). After setup, add the `job-search-profile.md` file you get to the project's files or knowledge. Every chat in that project will then know your targets, tools and preferences. In Codex or Claude Code, the assistant saves the profile for you.

## 3. Connect your tools (optional, but this is where it gets useful)
Claude calls these **Connectors**, ChatGPT calls them **Apps**, and Codex uses **MCP servers**. Turn on whatever you already use:
- **Email:** Gmail or Outlook
- **Calendar:** Google Calendar or Outlook
- **Files:** Google Drive or OneDrive
- **Tracker:** Notion, Google Sheets or Airtable
- **Tasks:** Todoist, TickTick or others
- **Meeting notes:** Fireflies, Granola or others

Every module also works without them. It falls back to asking you to paste or upload things.

## 4. First run
Start a chat and type something like:

> Set up my job search.

(Or skip setup and just ask for something. Each module asks only for what it needs.)

The assistant runs a short setup. For each part it offers **Quick**, which copies a proven setup; **Bring your own**, a short quiz about the tools you use; or **Skip**. It also asks you to pick an assistant persona: Coach, Strategist, Mentor, Peer, Accountability Partner or Champion. You can also take a 5-question quiz to choose one.

## 5. Things to try
| Module | Say |
|---|---|
| Setup | "Set up my job search" · "Import my tracker" · "Change my persona to Coach" |
| Self-discovery | "Help me figure out what roles fit me" |
| LinkedIn | "Score my LinkedIn for Product Ops Manager" (attach your profile PDF) |
| Resume | "Tailor my resume for <posting URL>" |
| Networking | "Draft a cold email to Priya Shah, Director of Ops at Toast. No connection; I want an informational chat." · "Prep me for this event: <link>" |
| Interviews | "Prep me for my interview with <company>" · "Run a 25-minute mock interview" · "Debrief my interview" |
| Negotiation | "I got an offer. Help me negotiate" |
| Rhythm | "Daily stand-up" · "Run my weekly review" |

## Ground rules it follows
- It only **drafts**. It never sends email or messages for you.
- It never guesses email addresses.
- It writes at most 3 outreach drafts per sitting, because an unsent draft isn't progress.
- It tracks **live conversations per week** (default target: 5) as the metric that matters, not messages or applications.

## Want the full suite?
Other modules cover self-discovery, LinkedIn, resume and cover letter, interviews, negotiation, and the daily brief and weekly review. Setup wizard and downloads: https://anewt225.github.io/job-search-assistant/
