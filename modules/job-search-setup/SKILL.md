---
name: job-search-setup
description: Onboarding and hub for the Job Search Assistant suite. Opens with a short welcome (what the assistant does, what setup involves, how long it takes), then runs one 5-step setup, one question at a time with a suggested answer - where you are, how you want to work (persona), your tools by job (tracking, files, email, calendar, tasks, meeting notes; none required), about you, review and first task - and writes job-search-profile.md, which every module reads. Skips setup when the user needs help right now, such as an interview today. Creates or imports the tracker (Notion, Google Sheets, Excel, Airtable, CSV, Obsidian) and merges existing project instructions or notes. Also answers "what can you do / where do I start" and routes to the right module. Use for "set up my job search", "onboard me", "change my settings or persona", "import my tracker", "connect my tools", or "help with my job search" with no specific task.
---

# Job Search: Setup & Hub

## Run setup
Follow `references/_shared/setup.md`. It is the single setup flow for every app:

1. **Welcome turn first** (setup.md §1). Say what the assistant does, that setup is 5 short steps and
   about 5 minutes, and that nothing has to be connected. Ask nothing about the user yet.
2. **Urgent path** (setup.md §2). If the user has an interview in the next day or two, or asks for
   something concrete instead of starting, skip setup and help now. Offer setup once afterwards.
3. **Five steps** (setup.md §4): Where you are → How you want to work → Your tools → About you →
   Review and first task.
4. **Every setup turn** starts with the progress header, `**Step N of 5 · <step name>**`, and asks one
   question with lettered options and one suggested answer (setup.md §3).

Use `references/_shared/hosts.md` for anything app-specific, `references/_shared/personas.md` for the
persona question, `references/_shared/data-schema.md` for the tracker and imports, and
`references/_shared/profile-template.md` for the output. There is no preset tool stack and no second
"quick" variant: suggestions come from what the user said in step 1 and from the tools you can actually
see connected.

**Tracker paths** (step 3, Tracking)
- **Notion template:** give the template link from the README. The user duplicates it, then shares the
  page with the host's Notion connection. Fetch it and record the 5 database IDs in the profile.
- **Build for me:** create the 5 tables in the chosen backend from `data-schema.md`. Warn once that this
  costs more usage than duplicating the template.
- **Import / merge:** follow `data-schema.md` §Import.
- **Nothing yet:** start with CSV files in the files root, and migrate later.

**Merge existing context:** if the user pastes project instructions, a custom GPT's instructions, a CLAUDE.md or AGENTS.md, an "about me" doc
or old prompts, extract the durable facts into the profile (positioning, rules, tone). Put anything that
doesn't fit into §7 "Notes for the assistant". Show the result before saving.

## After setup (step 5)
1. Show the 5-line summary (setup.md §8), ask "save, or change something?", then save the profile.
2. Give **one first task** for the user's stage (setup.md §4), not a list.
3. Say how to reach everything else: type `/` to see the skills in apps that list them, or just say
   what you need. Mention that the daily and weekly rhythm can be scheduled later.

## Hub: what to say
When the user asks "what can you do?" or "where do I start?", answer with three first messages by
situation, then the table:
- Just starting: "Set up my job search"
- Applying now: "Tailor my resume for <posting link>"
- Interview coming up: "I have an interview today with <company>"

| Module | Say something like |
|---|---|
| job-search-discovery | "Help me figure out what roles fit me" |
| job-search-linkedin | "Score my LinkedIn for <role>" |
| job-search-resume | "Tailor my resume for <posting URL>" |
| job-search-networking | "Draft outreach to <person>" · "Prep me for <event>" |
| job-search-interview | "Prep me for my interview with <company>" · "Mock interview" · "Debrief my interview" |
| job-search-negotiation | "I got an offer. Help me negotiate" |
| job-search-rhythm | "Daily stand-up" · "Weekly review" |

If a module isn't installed, say so and point to the README's download links. If the user asks for a
quick one-off anyway, give a lighter version inline.

## Changing settings later
"Change my persona", "switch my tracker to Sheets", "I'm now interviewing": edit only the affected
profile section, show the diff, and save.
