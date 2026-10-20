---
name: job-search-linkedin
description: LinkedIn profile review for job seekers. Scores a profile against a specific target role on a weighted 100-point rubric plus a 7-advisor panel, harvests the keyword gap, drafts 3–5 alternatives per section in the user's voice, exports a ranked action plan (Todoist, TickTick, Asana, CSV, Markdown), and re-checks the profile later to see what shipped. Accepts a PDF, screenshots, an HTML save or a full LinkedIn data export. Refreshes its platform research with a quick web search when it's stale. Use when the user mentions their LinkedIn profile, headline, About section, recruiter visibility, "score/review/optimize my LinkedIn", or "why am I not getting recruiter interest". Grounded in Linked, Career Coach GPT, The Job Closer, Reverse the Search and Never Search Alone.
---

# Job Search: LinkedIn Profile Review

A LinkedIn profile has one job: get the user into the small set of candidates a recruiter actually
contacts. Recruiters look for reasons to say no, and discoverability is a gate: a profile that never
shows up in search scores zero on everything else. Profile work fails at the *shipping* step, so every
run ends ranked and finishable.

## Step 0: Context
1. Read `job-search-profile.md` (`references/_shared/setup.md` §0). If it's missing, run setup scoped to
   **linkedin**: identity and targets, files, tasks, source docs (resume, LinkedIn), persona.
2. **Target first.** Get the exact target title(s), locations, 5–15 target companies or company type,
   the Candidate–Market Fit statement if there is one, and 3+ real JDs. With no target, stop and help
   define one (or suggest the discovery module). Fewer than 3 JDs → proceed, but state that confidence in
   the keyword gap is low.

## Step 1: Get the profile (most to least complete; never scrape LinkedIn)
1. **Full data export.** Settings → Data privacy → Get a copy of your data. Includes Profile, Positions,
   Skills and Recommendations CSVs; read only those files.
2. **HTML save** of the profile page (File → Save page as).
3. **PDF.** Profile → Resources/More → Save to PDF. This is the fastest option, but it omits Featured,
   activity and the banner.
4. **Screenshots** of each section.
Any section not supplied is marked **Not assessed** and excluded from the denominator. Never score what
you haven't seen.

## Step 2: Pick the mode
| Trigger | Mode | Load |
|---|---|---|
| "score / review / audit" | **Score** | refresh check → `keyword-harvest.md` → `profile-rubric.md` → `advisory-panel.md` → `report-template.md` |
| "rewrite my headline / About / …" | **Rewrite** | `rewrite-playbook.md` (plus the harvest if one exists) |
| "I updated it, check again" | **Re-eval** | `reeval-protocol.md` and the prior report |
| "make a to-do list / export" | **Export** | `scripts/make_todos.py` |
`methodology_LinkedIn.md` justifies the rubric. Read only its §4 (2026 platform behavior) and
§Refresh protocol during a Score run. `sources.md` is the citation index.

## Score workflow
0. **Refresh check.** If `methodology_LinkedIn.md` **Swept** is more than 90 days old and web search is
   available, run its §Refresh protocol first (2–4 searches). If not, note the sweep date.
1. **Harvest** the vocabulary gap (3 buckets) and peer headline patterns. Do this before scoring.
2. **Score** all 20 criteria, 0–4 each, weighted to 100. One sentence of reasoning per criterion. Don't
   round up.
3. **Panel.** Seven advisor verdicts, unscored. If a panel finding seems big enough to move the score,
   log it as a rubric gap; don't adjust by feel.
4. **Report.** In chat: composite, 5 dimension scores, the 3 fixes with the most **points recoverable
   per minute**, the projected composite after those fixes, and **one stop rule**. Save the full report
   if the user wants it.
5. Offer Rewrite for the top-3 sections and Export for the action plan.

## Export
Build the action JSON (schema: `python3 scripts/make_todos.py --example`), then run
`python3 scripts/make_todos.py actions.json -o ./out`. This produces generic, Todoist, Asana and TickTick
CSVs plus `tasks.md` and `tasks.json`. If code execution isn't available, give a markdown checklist. If a
task connector is configured (profile §4), offer to create the top tasks directly, as flat tasks. Add a
recurring **"LinkedIn brand refresh"** task every 6–8 weeks (Mann).

## Non-negotiables
- Never fabricate experience. Reframe and translate only.
- Score against the target, not the person. Distinguish "scored 0" from "not assessed".
- Preserve the user's voice. Show character counts. Flag stretch claims.
- Name the contested criterion (headline posture: aspirational vs. objective) and say which way you scored.
- Cite the criterion for every recommendation.
- Be direct and warm, and lead with what already works. An honest 54 beats an inflated 70.

## Sources
`references/book-notes/` holds the underlying book notes (see `INDEX.md`). Open one only to verify a claim, or when the user asks "what does <book> say?"
