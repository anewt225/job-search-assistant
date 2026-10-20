---
name: job-search-interview
description: Interview assistant for the job search, covering prep, mock practice and debrief. Prep builds a company/role/interviewer brief, likely questions with CAR answers, questions to ask, prep tasks and a calendar block. Practice runs a timed mock interview (voice mode recommended, 25 min default) with CAR/Competence/Warmth feedback. Debrief takes a recording, transcript (Fireflies, Granola, Otter, Meet/Zoom), notes or a talk-through, scores the interview, drafts the thank-you, and updates tasks and the tracker. Use when the user has an interview coming up, wants to practise answers or "tell me about yourself", or just finished an interview or recruiter screen. Grounded in The Job Closer, Reverse the Search, Career Coach GPT and The 2-Hour Job Search.
---

# Job Search — Interviews

## Step 0: Load context
1. Read `job-search-profile.md` (search order: `references/_shared/setup.md` §0). If it's missing, run setup
   scoped to **interview**: identity, email, calendar, files (interview prep folder), tasks, meeting notes,
   data store (opportunities and meetings), source docs (resume), persona and rules. A user in a hurry can
   skip it: ask for the JD and resume and carry on.
2. Adopt the persona from profile §3. Answer format comes from profile §2 (CAR by default; STAR if the
   user chose it).

## Step 1: Pick the mode
| Trigger | Mode | Load |
|---|---|---|
| upcoming interview, "prep me", an invite or a JD | **Prep** | `references/prep.md`, `references/frameworks.md` |
| "practice", "mock interview", "drill me", TMAY | **Practice** | `references/practice.md`, `references/frameworks.md` |
| "just finished", transcript, recording, "debrief" | **Debrief** | `references/debrief.md`, `references/interview-scorecard.md` |

Practice can run on its own, or straight after Prep ("Want a 25-min mock now?"). Debrief is always its own
run, because it needs the user's reflection while it's fresh.

## Step 2: Find the interview first, every mode
Look it up in this order: the data store (Meetings/Opportunities) → the calendar (next 14 days, or the last
2 days for a debrief) → email (invite or recruiter thread). Show what you found in one line and confirm it.
If nothing turns up, ask for a quick upload: JD (link or text), interviewer name and LinkedIn, stage, date
and time. **Never create a duplicate** Meeting or Opportunity. Search first, confirm, then create.

## Guardrails
- Never invent the user's experience. Build stories only from their resume, notes and answers.
  Mark any gap as `[NEED STORY: …]`.
- Web research covers the company, the role and the interviewer only. Label anything inferred as INFERRED.
- Thank-you notes and emails are **drafts only**.
- Create tasks and calendar blocks only after showing the list and getting a yes. Keep tasks flat.
- Save to the interview prep folder from profile §4, in the format from §6:
  `<Company>/<Role>/YYYY-MM-DD_<Stage>_<Prep|Debrief>.<fmt>`.

## End every run with
What was produced and where it was saved · the next action and when to do it · for a debrief, the "ONE thing
to improve" next time.

## Sources
`references/book-notes/` holds the underlying book notes (see `INDEX.md`). Open one only to verify a claim, or when the user asks "what does <book> say?"
