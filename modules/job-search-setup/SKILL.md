---
name: job-search-setup
description: Onboarding and hub for the Job Search Assistant suite. Runs the full setup, either Quick (copy a proven Gmail, Google Calendar, Drive, Notion, TickTick and Fireflies stack) or bring-your-own (a short quiz per component), picks an assistant persona, creates or imports the tracker (Notion, Google Sheets, Excel, Airtable, CSV, Obsidian), merges existing Claude Project instructions or notes, and writes job-search-profile.md, which every module reads. Also answers "what can you do / where do I start" and routes to the right module. Use for "set up my job search", "onboard me", "change my settings or persona", "import my tracker", "connect my tools", or "help with my job search" with no specific task.
---

# Job Search: Setup & Hub

## Run setup
Follow `references/_shared/setup.md` fully (all 12 components). Use `references/_shared/personas.md` for
the persona step, `references/_shared/data-schema.md` for the data store and imports, and
`references/_shared/profile-template.md` for the output.

Order: identity → persona → data store (biggest decision) → files → email → calendar → tasks → meeting
notes → source docs → output format → rules → extras. Offer to bundle: "Quick for the rest?"

**Data store paths**
- **Notion template (fastest):** give the template link from the README. The user duplicates it, then
  shares the page with the Notion connector. Fetch it and record the 5 database IDs in the profile.
- **Build for me:** create the 5 tables in the chosen backend from `data-schema.md`. Warn once that this
  costs more usage than duplicating the template.
- **Import / merge:** follow `data-schema.md` §Import.
- **Nothing yet:** start with CSV files in the files root, and migrate later.

**Merge existing context:** if the user pastes Claude Project instructions, a CLAUDE.md, an "about me" doc
or old prompts, extract the durable facts into the profile (positioning, rules, tone). Put anything that
doesn't fit into §7 "Notes for Claude". Show the result before saving.

## After setup
1. Save the profile (setup.md §4) and print the 5-line summary.
2. Suggest the **first 3 moves** based on the search stage:
   - exploring → **discovery** quiz
   - targets known but no traction → **linkedin** score + **networking** triage of the warm list
   - actively applying → **resume** tailor for the top posting + **networking** referral ask
   - interviewing → **interview** prep or practice
   - offer in hand → **negotiation**
   - everyone → **rhythm** weekly retro on Sunday
3. Offer to schedule the daily and weekly rhythm runs.

## Hub: what each module does
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
