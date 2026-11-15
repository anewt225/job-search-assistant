# Setup / Onboarding

Goal: produce a filled `job-search-profile.md` (template: `profile-template.md`) in about five minutes.
There is **one flow, five steps, the same in every app**. Anything app-specific comes from `hosts.md`.
**Modules call setup scoped to what they need** (§7); only a full "set up my job search" walks all five steps.

## 0. Find an existing profile first
Look, in order: files attached to this project/conversation → `./job-search-profile.md` →
`~/.agents/job-search/` → `~/.claude/job-search/` → the user's files root (search the filename). If found, read
it and only fill gaps the current module needs. Never re-ask what's already there.

## 1. Welcome turn (before any question)
The first setup turn asks nothing about the user. In eight lines or fewer it says what the assistant
does, what setup involves, how long it takes, and that nothing has to be connected:

> **Job Search Assistant**
> I help with the whole search: working out what to target, LinkedIn, resumes, outreach, interview prep
> and practice, negotiation, and a weekly rhythm. I only draft. You decide what gets sent.
>
> **Setup is 5 short steps, about 5 minutes:** 1 Where you are · 2 How you want to work · 3 Your tools ·
> 4 About you · 5 Review and first task. One question at a time, each with a suggested answer, and you
> can skip any of them. Nothing has to be connected: everything works with paste or upload.
>
> **Interview today or tomorrow?** Say "I have an interview today with ___" and we'll skip setup and prep now.
>
> Ready to start? Say "go", or tell me what you need help with first.

If a profile already exists (§0), don't restart: say what is already set, name the gaps, and ask whether
to fill them now. If the user answers the welcome with a task instead of "go", do the task (§2).

## 2. Urgent path: help now, set up later
Setup never stands between the user and something they need today.
- **Triggers:** an interview, phone screen or recruiter call within about 48 hours, or any concrete
  request made instead of starting setup ("just tailor this resume").
- **Do:** skip setup. Hand over to the matching module; for an interview that is the interview module's
  urgent prep (`prep.md` §Urgent). Ask only for what that task needs. If the module isn't installed,
  give the lighter inline version and say which module would do it fully.
- **After the task:** offer setup once, in one line ("Want to do the 5-minute setup so I remember this
  next time?"). If they decline, don't offer again in this conversation.

## 3. Turn format (every setup turn after the welcome)
**Progress header.** The first line of every setup turn is the step and its name, exactly as in §4:

`**Step 3 of 5 · Your tools**`

**Question pattern.**
- One question per turn. Never two.
- Two to five lettered options, plus the user's own words. Mark exactly one **(suggested)**: the answer
  that fits what you already know (earlier answers, tools you can see connected), otherwise the default
  in §4 and §5.
- At most one line on what the answer enables. No recap paragraphs between questions.
- Always accept: a letter, free text, "ok" (takes the suggested answer), "skip" or "back".
- Open questions (name, target roles) follow the same shape: one at a time, with an example, skippable.
- Confirm the answer in a few words, then ask the next question in the same turn.

```
**Step 3 of 5 · Your tools**
Where do you keep track of companies and applications? It lets me remember who you've talked to.
a) A spreadsheet (Google Sheets or Excel)
b) Notion
c) Nothing yet: start me with simple CSV files (suggested)
d) Something else
Reply with a letter, your own words, "skip" or "back".
```

## 4. The five steps
| Step | Name (use verbatim) | Ask, one at a time | Suggested when nothing is known | Writes to profile |
|---|---|---|---|---|
| 1 | **Where you are** | Search stage · what would help most this week · what you already have (resume, LinkedIn export, a tracker, old notes or instructions) | stage: exploring | §1 search stage, §6, §7 |
| 2 | **How you want to work** | Persona (pick one, or take the quiz in `personas.md`) · keep the default rules or change one | Accountability Partner · keep the defaults | §3, §2 |
| 3 | **Your tools** | One question per job in §5, tracker first | no tool: paste and upload | §4, §5 |
| 4 | **About you** | Name · one-line positioning · target roles. If a resume was shared in step 1, draft all three from it and ask for corrections instead | skip; the self-discovery module can fill these later | §1 |
| 5 | **Review and first task** | Show the summary (§8) and ask: save, or change something? Then give one first task | save | whole file |

Notes:
- Step 1 comes first so that every later suggestion can use it. Someone who is interviewing should not
  be asked about tools before they have been asked about the interview.
- Steps 2 to 4 only ask what the profile is still missing.
- Output format defaults to Markdown and isn't asked; say so in the review.
- Step 5 ends with **one** first task for the stage: exploring → the self-discovery quick quiz ·
  listening tour → one outreach draft · actively applying → tailor the resume for the top posting ·
  interviewing → interview prep · negotiating → the negotiation module. Add one line on how to reach the
  rest: "type `/` to see every skill, or just say what you need."

## 5. Step 3 detail: tools by job
Ask about the job, not the app. There is no preset stack. **Before asking about a job, check which
tools are actually available in this session.** If one is, name it and make it the suggested answer
("I can see a calendar connected. Use it?"). If none is, the suggested answer is the no-tool fallback,
and you say once which connection would help, using the host's own steps and word for it (`hosts.md`).
Record each job as *connected*, *not connected* or *skipped* (§8).

| Job | Question | What it enables | Common answers (examples, not a recommendation) | No tool (always offered) | Used by |
|---|---|---|---|---|---|
| **Tracking** | "Where do you keep track of companies, contacts and applications?" | remembering who you've talked to and what's next | a spreadsheet · Notion (template link in the README) · Airtable · Obsidian · an existing tracker to import (`data-schema.md` §Import) | CSV files I create for you | all |
| **Files** | "Where should I read and save documents?" | saved resumes, briefs and notes you can find again | a cloud drive folder · a local folder · this AI project's files | I output files for you to save | all |
| **Email** | "Where do recruiter and outreach emails live?" | finding threads and creating drafts (never sending) | the mail app you already use | paste the thread | networking, interview, rhythm |
| **Calendar** | "Which calendar shows your real availability?" | prep blocks and follow-up reminders you approve first | the calendar you already use; optionally a separate one for job-search events | I give you times to add | networking, interview, rhythm |
| **Tasks** | "Where do your to-dos live?" | follow-ups that don't get lost | your to-do app · the tracker's Tasks table | tasks listed in chat | all |
| **Meeting notes** | "How do you capture calls and interviews?" | debriefs from what was actually said | a notetaker app · call transcripts · your own notes | upload or paste | interview, networking |

If the user picks **Tracking → Notion**, give the template link from the README, or offer to build the
five tables (warn once that building costs more usage than duplicating). For **nothing yet**, start with
CSV files in the files root and migrate later.

## 6. Importing what they already have
If the user shares an existing tracker, project instructions (Claude, ChatGPT, a custom GPT, a Gemini Gem), a CLAUDE.md or AGENTS.md, an "about me" doc or
past outputs: read them, extract into profile fields, show the diff, confirm. For trackers follow
`data-schema.md` §Import. Optional extras (contact enrichment, reading highlights, a LinkedIn
connections export) are never asked during setup; add them when the user brings them up.

## 7. Module scopes
When a module runs setup because the profile is missing something, it uses the same turn format (§3)
and asks only these items, in step order. The progress header is for a full setup only.

| Module | Ask only |
|---|---|
| setup | everything (all five steps) |
| discovery | stage · persona · files (strategy folder) |
| linkedin | stage · persona · files · tasks · documents (resume, LinkedIn export) · name and targets |
| resume | stage · persona · rules · tracking (opportunities) · files · documents · name and targets |
| networking | persona · rules · tracking (contacts, companies, meetings) · files · email · calendar · tasks · name, positioning and targets |
| interview | persona · rules · tracking (opportunities, meetings) · files · email · calendar · tasks · meeting notes · documents (resume) |
| negotiation | persona · name and targets, plus must-haves and comp floor |
| rhythm | persona · rules · tracking · email · calendar · tasks |

## 8. Save + confirm
- Write `job-search-profile.md`. Where: the files root's `Strategy/` folder if one is set; otherwise the
  host's location from `hosts.md`. In a chat app (Claude, ChatGPT, Gemini, Grok), output the file and tell
  the user to **add it to the project's files/knowledge** (or paste it into project instructions) so every
  chat sees it. Where the app has no projects (Gemini), tell them to keep the file and attach it at the
  start of each job-search chat.
- The step 5 summary is five lines: stage and first task · persona · tracker · each tool job with its
  state (connected, not connected, skipped) · where the profile was saved.

## 9. Cost note to show once
"Duplicating the Notion template or starting with CSV files costs almost nothing. Having me build
databases or import a large tracker uses more of your usage. I'll batch it and tell you before anything big."
