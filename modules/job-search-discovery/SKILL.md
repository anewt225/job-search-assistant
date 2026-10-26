---
name: job-search-discovery
description: Self-discovery for job seekers. A short, playful, interactive quiz (multiple choice, this-or-that, ranking, quick scenarios) that surfaces strengths, energizers, must-haves and must-nots, and candidate roles. It then writes a Mnookin-style two-pager, a one-sentence Candidate–Market Fit statement and ranked target roles, and updates the job-search profile so every other module uses them. Use when the user doesn't know what to target, is pivoting, feels stuck, asks "what should I do next", "what am I good at", "what roles fit me", or wants a two-pager, career clarity, or a positioning statement. Grounded in What Color Is Your Parachute, Never Search Alone, Designing Your Life, Pivot, Reverse the Search, The Job Closer and Linked.
---

# Job Search: Self-Discovery

The output is **clarity the market can act on**: a short list of target roles and a sentence that says
what problem you solve and for whom. Everything downstream (LinkedIn, resume, outreach) depends on it.

## Step 0: Context
Read `job-search-profile.md` if it exists (`references/_shared/setup.md` §0). The quiz never needs
connectors. Ask the user to upload anything already written: a resume, an old two-pager, assessment
results (CliftonStrengths, Myers-Briggs, Enneagram), or performance reviews. Mine these first and don't
re-ask what they already answer.

## Step 1: Choose the depth (one question)
- **Quick (~10 min):** 12 questions → candidate roles plus a draft CMF statement.
- **Full (~30 min):** 4 rounds (below) → full two-pager.
- **One exercise:** pick a single exercise from `references/exercises.md` (e.g. the Flower, Odyssey Plans,
  Must-Nots).

## Step 2: Run the quiz (`references/quiz.md`)
- **One question per turn.** Vary the format (multiple choice, this-or-that, rank-3, a quick scenario,
  or a 1-line open answer) so it feels like a game, not a form. Always allow "neither / other".
- **Randomise:** draw questions from the bank in a different order and with different wording each run.
  Never ask the same question twice.
- Every 3–4 questions, **reflect back** one pattern you're seeing ("You keep choosing fixing broken
  systems over building new ones…") and let the user correct it. Corrections outweigh answers.
- Keep a silent tally of the signals in `quiz.md` §Scoring.

## Step 3: Synthesize (`references/outputs.md`)
1. **Top strengths** (3–5), stated in the user's own words where possible, each with one piece of evidence.
2. **Energizers vs. drainers** (loves and hates).
3. **Must-haves / must-nots** (5–7 each).
4. **Candidate roles:** 5–8 titles across 2–3 "lanes", each scored on Well-th (values + strengths +
   market demand) and the one-degree-pivot test (how many variables change at once?). Mark which ones
   need market validation.
5. **Candidate–Market Fit statement**, one sentence: "I help [who] [solve what problem] by [how I'm
   different]."
6. **Experiments:** 3 prototype conversations (people to talk to, via the networking module) and 1 small
   project to test the riskiest assumption.

## Step 4: Save and update context
- Show the draft and accept edits. It's a draft; the listening tour refines it (Terry).
- Save `Two-Pager.<fmt>` to the strategy folder from profile §4.
- **Update profile §1** (positioning, target roles, industries, not-targeting, strengths, proof points)
  after confirming the diff with the user. In a chat app, output the updated profile and remind the user to
  replace the copy in the project's files (`_shared/hosts.md`).
- Next step: "Want to test these with 3 prototype conversations? The networking module can draft the
  outreach."

## Sources
`references/book-notes/` holds the underlying book notes (see `INDEX.md`). Open one only to verify a claim, or when the user asks "what does <book> say?"
