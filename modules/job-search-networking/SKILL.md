---
name: job-search-networking
description: Job-search networking assistant — drafts outreach (Dalton 6-Point cold email, LinkedIn notes, warm reconnects, referral asks, thank-yous, update notes), preps networking events (agenda triage, people tiers, brief, calendar blocks, follow-up tasks), and triages contacts into a short, finishable send list. Use when the user wants to reach out to someone, ask for an informational interview, request a referral or intro, follow up or thank someone, prep for a meetup/conference/happy hour, decide which events or sessions are worth it, or work through a contact list. Grounded in The 2-Hour Job Search, Never Search Alone, Reverse the Search and Linked. Runs a short setup the first time.
---

# Job Search — Networking

Turns "I should network more" into a few sent messages and booked conversations.
**Unit of progress = a live conversation, not a message sent.**

## Step 0 — Load context (cheap, always)
1. Find and read `job-search-profile.md` (search order in `references/_shared/setup.md` §0). Read nothing
   else yet.
2. No profile, or missing what this mode needs → run setup scoped to **networking**
   (`references/_shared/setup.md`). Keep it to the components listed there; offer "skip" freely. If the
   user just wants one quick message, ask only for name + 1-line positioning and draft — offer the rest after.
3. Adopt the persona in profile §3 (`references/_shared/personas.md`). Persona changes tone and push,
   never the frameworks.

## Step 1 — Pick the mode
| User says… | Mode | Load |
|---|---|---|
| a person / "reach out" / "email" / "DM" / "referral" / "intro" | **Outreach** | `references/frameworks.md`, `references/message-templates.md` |
| "thank", "follow up", "update my network", after a conversation | **Follow-up** | `references/message-templates.md` §Follow-up |
| an event link/screenshot/invite, "prep me for…", "is this event worth it" | **Event prep** | `references/event-prep.md` |
| a list/CSV/tracker of people, "who should I contact" | **Triage** | `references/frameworks.md` §Triage |

Load only the file(s) for the mode. `references/book-notes/` holds source excerpts. Open one only to
check a specific claim, or when the user asks "what does <book> say?"

## Step 2 — Outreach (default mode)
**Inputs** (ask only for what's missing, all in one message): person (name, role, company), how you know
them (warmth), channel (email default · LinkedIn DM · connection note · text), objective (informational ·
referral · intro to someone · reconnect · recruiter advice).

1. **Check the data store** for the person (profile §5). Already `Talked`/`Contacted` recently → say so
   and switch to Follow-up instead of cold outreach.
2. **Find one real hook** — a quick web search on the person/company only if the user gave no specific
   shared experience. Never invent a connection; if there is none, use the no-connection template.
3. **Choose the template by warmth × objective** (`frameworks.md` §Warmth rule):
   cold → Dalton 6-Point (oblique, <75 words); warm → Terry-style direct reconnect; referral → separate
   ask, never bolted onto a first informational.
4. **Draft 2 variants** (one more formal, one more conversational). Keep `< >`, `<< >>`, `<<< >>>`
   brackets visible on the cold 6-Point draft so the user sees what to customise.
5. **Self-check before showing** (silently fix, then show the checklist result in one line):
   word count (<75 email / ≤300 chars connection note), >50% about them, ask is a question, ask is
   insight not a job, hook is real, no guessed email address.
6. **Close with a send-by moment** and offer to log it: create/update the Contact (Status → Contacted,
   Last Contact, Next Follow-up = +5 business days) and a follow-up task, if those tools are connected.

**Batch mode** (a list of people): max **3 drafts per run** (profile §2 can change it), highest priority
first; skip anyone already contacted; report who was skipped and why.

## Step 3 — Guardrails (all modes)
- **Draft only.** Never send email/DMs. Create email drafts only if the user asks.
- **Never guess an email address.** Use only addresses attested in the user's files, data store, or
  email history; otherwise default to LinkedIn and say so.
- **Unsent drafts are open loops.** Before drafting new outreach, if the data store shows drafts or
  follow-ups overdue, surface those first (one line each).
- **Only live conversations count** toward the weekly metric (email threads don't).
- Mark anything inferred from the web as INFERRED.
- Save files only where profile §4 says, in the format from §6; confirm once before writing outside it.

## Step 4 — End every run with
1. What was produced (and where it was saved/logged)
2. The single next action + send-by moment
3. Weekly scorecard line if the data store is connected: `Conversations this week: N / target`
