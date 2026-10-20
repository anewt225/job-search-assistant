# Setup / Onboarding

Goal: produce a filled `job-search-profile.md` (template: `profile-template.md`) in as few turns as
possible. **Modules call setup scoped to what they need**; only the full `/setup` walks every component.

## 0. Find an existing profile first
Look, in order: files attached to this Project/conversation → `./job-search-profile.md` →
`~/.claude/job-search/job-search-profile.md` → the user's files root (search the filename). If found, read
it and only fill gaps the current module needs. Never re-ask what's already there.

## 1. Open with one choice
> "I can set you up two ways, per component: **Quick** — copy a proven setup (Gmail · Google Calendar ·
> Google Drive · Notion template · TickTick · Fireflies), I just ask for names/links. **Bring your own** —
> a short quiz to point me at the tools you already use. Or **Skip** a component — features that need it
> stay off. Want Quick for everything, or go component by component?"

Ask one component at a time, multiple choice, with "skip" always available. Before asking about a
connector, **check whether its tools are actually available in this session**; if not, say which
connector to enable (claude.ai: Settings → Connectors; Claude Code: `/mcp` or a plugin) and offer
"skip for now" or a manual fallback (paste / upload).

## 2. Components

| # | Component | Quick (proven setup) | BYO quiz question | Manual fallback | Used by |
|---|---|---|---|---|---|
| 1 | **Identity & targets** | — (always asked) | Name, 1-line positioning, 1–5 target roles, industries, not-targeting, stage. Offer the self-discovery module if they don't know yet | — | all |
| 2 | **Email** | Gmail | "Where do outreach, recruiter and interview emails live?" Gmail · Outlook · other | paste threads | networking, interview, daily |
| 3 | **Calendar** | Google Calendar + a dedicated **"Career"** calendar for job-search events | "Which calendar shows your real availability? Which one should job-search events go on?" | I give .ics text / times to add | events, interview, weekly |
| 4 | **Files** | Google Drive folder `Job Search/` with `Resumes/ Cover Letters/ Applications/<Company>/<Role>/ Networking/<YYYY-MM-DD Event>/ Interview Prep/ Strategy/` | "Where should I read and save files?" Drive · OneDrive · Dropbox · local folder · this Project only | I output files for you to save | all |
| 5 | **Tasks** | TickTick list "Job Search" (flat tasks) | "Where do your to-dos live?" TickTick · Todoist · Google Tasks · Notion · Things · none | tasks listed in chat | all |
| 6 | **Meeting notes** | Fireflies | "How do you capture calls?" Fireflies · Granola · Otter · Meet/Zoom transcripts · Notion AI · manual notes · nothing | upload/paste | interview debrief, events |
| 7 | **Data store** | Duplicate the Notion template (see README link) | "Where do you track companies/contacts/applications today?" Notion · Sheets · Excel · Airtable · Obsidian · spreadsheet-ish mess · nothing yet → see `data-schema.md` §Import | CSV files I create for you | all |
| 8 | **Source docs** | — | "Upload or point me to: master resume, any recent tailored resume/cover letter, LinkedIn PDF." | upload | resume, linkedin, interview |
| 9 | **Output format** | Markdown | md · docx · pdf · Google Doc | — | all |
| 10 | **Persona** | Accountability Partner | Quiz in `personas.md` or pick from the table | — | all |
| 11 | **Rules** | 5 live conversations/wk · ≤5 apps/wk each with a named human · CAR · drafts only · ≤3 drafts/run | "Keep these defaults or change any?" | — | all |
| 12 | **Extras** (optional) | — | Contact enrichment (Hunter/Apollo), Readwise, LinkedIn Connections.csv, existing Claude Project instructions to merge | — | networking, events |

**Module scopes** (ask only these when a module runs setup):
| Module | Components |
|---|---|
| setup | all |
| discovery | 1, 4 (strategy folder), 9, 10 |
| linkedin | 1, 4, 5, 8 (resume, LinkedIn), 10 |
| resume | 1, 4 (resumes, cover letters, applications), 7 (opportunities), 8, 9, 10, 11 |
| networking | 1 (lite: name, positioning, targets), 2, 3, 4 (networking folder), 5, 7 (contacts, companies, meetings), 10, 11 |
| interview | 1, 2, 3, 4 (interview prep), 5, 6, 7 (opportunities, meetings), 8, 10, 11 |
| negotiation | 1 (+ must-haves, comp floor), 10 |
| rhythm | 1, 2, 3, 5, 7, 10, 11 |

## 3. Importing what they already have
If the user shares an existing tracker, Claude Project instructions, a CLAUDE.md, a "about me" doc or
past outputs: read them, extract into profile fields, show the diff, confirm. For trackers follow
`data-schema.md` §Import.

## 4. Save + confirm
- Write `job-search-profile.md`. Where: the files root's `Strategy/` folder if one is set; Claude Code
  default `~/.claude/job-search/`; on claude.ai, output the file and tell the user to **add it to the
  Project's knowledge** (or paste into Project instructions) so every chat sees it.
- End with a 5-line summary: persona, data store, connected tools, skipped tools, and the one command
  to try next.

## 5. Cost note to show once
"Quick setup with the Notion template costs ~nothing. Having me build databases or import a large
tracker uses more of your usage — I'll batch it and tell you before anything big."
