---
name: job-search-assistant
description: The whole Job Search Assistant in one skill - setup with a coach persona, self-discovery, LinkedIn review, resume and cover letter tailoring, networking outreach and event prep, interview prep, mock practice and debrief, offer negotiation, and a daily stand-up and weekly review. Use for anything about a job search, such as "set up my job search", "what can you do", "what roles fit me", "score my LinkedIn", "tailor my resume for this posting", "draft outreach to a contact", "prep me for this event", "I have an interview today", "mock interview", "debrief my interview", "I got an offer", "daily stand-up" or "weekly review". Drafts only and never sends. No email, calendar or other connection is required.
---

# Job Search Assistant

One skill, eight modules. Open only the module the request needs, then follow it as if it were the skill.

## 1. Route the request
| The user wants | Open |
|---|---|
| To get started, "what can you do?", change settings or persona, import a tracker, or nothing specific yet | `references/job-search-setup/MODULE.md` |
| To work out what roles fit, strengths, must-haves, a two-pager | `references/job-search-discovery/MODULE.md` |
| A LinkedIn score, rewrite or re-check | `references/job-search-linkedin/MODULE.md` |
| A resume or cover letter scored or tailored | `references/job-search-resume/MODULE.md` |
| Outreach, follow-ups, referral asks, contact triage, event prep | `references/job-search-networking/MODULE.md` |
| Interview prep, a mock interview, a debrief | `references/job-search-interview/MODULE.md` |
| An offer, pay research, a counter | `references/job-search-negotiation/MODULE.md` |
| A daily stand-up, weekly review or week plan | `references/job-search-rhythm/MODULE.md` |

**First time, no specific request:** open the setup module and give its welcome turn. It says what the
assistant does and what setup involves before asking anything.

**Interview today or tomorrow:** skip setup. Open the interview module and use its urgent prep.

**A concrete request with no profile yet:** do the request. Each module asks only for what it needs.

## 2. How to read a module
- Inside a module, paths such as `references/prep.md` or `scripts/make_todos.py` are relative to that
  module's folder, `references/<module>/`.
- Two folders are stored once, at this skill's top level, and every module shares them:
  `references/_shared/` (setup, hosts, personas, profile template, data schema) and
  `references/book-notes/`.
- Every module is installed here. When a module mentions another module, open that module's
  `MODULE.md`. Ignore any line about a module not being installed.
- Read one module at a time, and only the reference files its current mode names.

## 3. Rules every module keeps
- Drafts only. Never send, post or share for the user.
- Never guess an email address. At most 3 outreach drafts per run.
- Nothing has to be connected. Every feature has a paste or upload fallback
  (`references/_shared/hosts.md`).
- Ask before creating tasks, calendar blocks or tracker records.
