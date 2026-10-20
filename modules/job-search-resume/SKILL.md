---
name: job-search-resume
description: Resume and cover letter assistant. It scores a resume or cover letter against a job description (weighted 100-point rubric, keyword gap, ATS check) and tailors both to a specific role using GLORY, the 3 Ns and the Pareto cover letter, with before/after scores. Use when the user wants to tailor, assess, score, rewrite or proofread a resume or cover letter, check fit or keyword match for a job posting, or asks "how competitive am I for this role" or "is this ready to send". Works from the user's own resume and past applications; it falls back to built-in templates when there are none. Grounded in Reverse the Search, Career Coach GPT, The Job Closer and Linked.
---

# Job Search: Resume & Cover Letter

## Step 0: Context
1. Read `job-search-profile.md` (`references/_shared/setup.md` §0). If it's missing, run setup scoped to
   **resume**: identity, files (resumes, cover letters, applications), source docs, data store
   (opportunities), output format, persona and rules. In a hurry? Ask only for the resume and the JD.
2. **Source material, best first:** the master resume plus recent tailored versions (profile §6) → whatever
   the user uploads → nothing (offer to build a starter resume from a LinkedIn PDF or a 10-minute
   interview, using `references/templates.md`).
3. **Formatting reference:** match the user's most recently *submitted* resume or cover letter. If there
   isn't one, use `references/templates.md`. Example outputs, if bundled, live in `examples/`; use them
   only for structure, never for content.

## Step 1: Pick the mode
| Trigger | Mode |
|---|---|
| "score / assess / check / is this ready" | **Assess** → `references/resume-rubric.md` or `references/cover-letter-rubric.md`, plus `references/report-template.md` |
| "tailor / customize / write a cover letter for" | **Tailor** → Assess (before) → tailor → Assess (after) → delta |

## Assess
1. Get the JD (a URL to fetch, the Opportunity record, or pasted text). Without a JD, scoring is
   meaningless, so ask for one.
2. Detect the document type (resume: dated roles and sections; cover letter: salutation and paragraphs).
3. Extract JD keywords: hard skills, soft skills, industry terms, action verbs, requirements and
   responsibilities.
4. Score every rubric dimension, one line of reasoning each, then compute the composite exactly as the
   rubric specifies.
5. In chat: composite, dimension table, top 3 strengths, top 3 gaps, and the single highest-value fix.
   Save the full report if the user wants it.
6. Next step by score: <60 tailor substantially · 60–75 close the gaps · 75–85 targeted tweaks · >85 ready.

## Tailor (GLORY, from Mann)
1. **Before score** (Assess).
2. **G**ather keywords → **L**ist tasks: map the user's real experience to each requirement →
   **O**bserve the story: the narrative arc to this role → **R**efine accomplishments: every bullet gets
   at least one of the 3 Ns (Numbers, Names, Notables) → **Y**es statements: each bullet answers a JD
   requirement.
3. Mirror the JD's terminology. Put the strongest material in the **top third** of page one (the
   6-second scan). Aim for about **50%+ fit**; don't stretch for 100%.
4. **Cover letter (Pareto):** a strong reusable base with ~20% customised. 250–350 words. Open with a
   company-specific hook about something recent and real, add 2–3 proof points, and close with a clear
   call to action. Use a referral opening if a human is attached.
5. Produce files in the profile's format (docx via the docx skill if available, otherwise md or pdf),
   named `<Company>_<Role>_Resume` and `<Company>_<Role>_CoverLetter`, saved to
   `applications/<Company>/<Role>/`.
6. **After score** and the delta table (per-dimension change and keywords added), plus any gaps that
   remain.
7. Flag the **96-hour window** if the posting is less than 4 days old. Remind the user about the
   application rule in profile §2 (a named human attached). Offer to log the Opportunity (Status = Applied)
   and a follow-up task for 7 days out.

## Guardrails
- **Never fabricate** employers, titles, dates, metrics or tools. If a bullet needs a number the user
  hasn't given, write `[X%?]` and ask.
- Keep the user's voice. Show what changed; don't silently rewrite whole sections.
- Strip AI tells: no "spearheaded synergies", no em-dash chains, no "passionate about".

## Sources
`references/book-notes/` holds the underlying book notes (see `INDEX.md`). Open one only to verify a claim, or when the user asks "what does <book> say?"
