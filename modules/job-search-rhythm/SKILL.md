---
name: job-search-rhythm
description: Lightweight operating rhythm for a job search. A 2-minute daily stand-up (done yesterday, plan today, blockers, suggested time blocks) and a weekly retro followed by week-ahead planning (wins, time vs. priorities, one lesson to apply → intention, top 5 priorities, 5 secondary objectives, dated events and loose tasks → suggested calendar blocks). Optionally pulls data first from connected email, calendar, tasks and tracker, or just talks it through. Can be scheduled. Use for "daily brief", "stand-up", "what should I do today", "plan my week", "weekly review", "retro", "how did my week go", or the job-search scorecard.
---

# Job Search: Daily Stand-up & Weekly Retro

Designed to be **cheap**: short outputs and minimal tool calls. Never dump raw data. Summarize to the few
items that change a decision.

## Step 0: Context
Read `job-search-profile.md` (`references/_shared/setup.md` §0) for targets, rules (weekly conversation
target, application cap), persona and connected tools. If it's missing, ask for the 2–3 things needed
(targets, task tool, calendar) and carry on.

## Step 1: Sync or talk? (ask once per run; remember a stated default in profile §7)
> "Want me to **sync first** (pull <the connected tools listed>), or just **talk it through**?"
- **Sync (light):** calendar (today, or next 7 days for the week) · tasks due or overdue · tracker
  records changed since the last run (Meetings this week, Opportunities with a Next Step Date ≤ today,
  Contacts with Next Follow-up ≤ today) · email: search only for recruiter, interview and reply threads
  from the last 1–7 days (subjects and senders, not bodies). Cap each source at about 10 items.
- **Talk:** ask the questions below and suggest from what you already know (profile, prior outputs in
  this Project).

## Daily stand-up (≤ 15 lines of output)
Ask in one message (pre-filled from the sync when available; the user corrects it):
1. **Done yesterday?** 2. **Plan for today?** 3. **Blockers?**
Then output:
```
✅ Yesterday: …
🎯 Today (top 3, conversations first): 1) … 2) … 3) …
🚧 Blockers → suggested unblock: …
🗓 Suggested schedule: 09:00–09:45 outreach (send the 3 drafts) · 13:00–13:30 interview prep · …  (fits around calendar events)
📊 Week so far: conversations N/target · applications N/cap · follow-ups overdue N
```
Prioritise in this order: time-sensitive items (thank-yous due, follow-ups, interviews within 48 hours,
postings inside the 96-hour window) → conversations and warm outreach → targeted applications →
maintenance. If a draft is sitting unsent, it goes first.

## Weekly: retro first, then week-ahead (two phases; don't start phase 2 until phase 1 is submitted)
**Phase 1, retro** (ask together, pre-filled from the sync):
1. What went well and what got done? (include the scorecard: conversations, applications, interviews,
   follow-ups sent)
2. Did time spent match your priorities and goals? (if the calendar is synced, show a rough split by
   category)
3. One small way to apply a lesson or productivity tweak next week?
Output ≤ 8 lines: wins · scorecard against targets · alignment verdict · the one change.

**Phase 2, week ahead** (prompt only after the retro is submitted):
1. Intention for the week (one phrase)
2. Top 5 priorities
3. 5 secondary objectives
4. Dated or timed events (pre-filled from the calendar) plus loose tasks
Output:
- A week table: each top-5 priority → suggested time block(s) (day, time, duration) placed around
  existing events, conversations first, deep work in the user's best hours if known.
- Offer: a) create the calendar blocks (on the job-search calendar, as Busy) · b) create or update the
  tasks (flat) · c) save `Weekly/YYYY-Www.md` to the strategy folder.
Create nothing without a yes.

## Scheduling (optional)
If the user wants it automatic: suggest a weekday-morning daily stand-up and a Sunday-evening (or Friday
afternoon) weekly run, using whatever scheduling the app offers (scheduled tasks in the Claude app or
Cowork, `/schedule` in Claude Code). A scheduled run defaults to **sync** mode and produces the output
only. It never creates events or tasks without the user being present to confirm.
