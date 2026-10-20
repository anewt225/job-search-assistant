# Sources & Provenance

> **v2 note.** This file is now the short-form attribution table. The full research
> aggregation — every source's contribution, the documented conflicts, verified 2026 platform
> behavior with dates, and the synthesis that justifies the rubric weights — lives in
> **`methodology_LinkedIn.md`**. Read that first; this file is the index.

Every criterion in the rubric traces to a named source. Where sources conflict, the conflict
is documented rather than resolved silently.

---

## Primary sources

| Work | Author(s) | What it contributes |
|---|---|---|
| **Linked: Conquer LinkedIn. Get Your Dream Job.** | Omar Garriott & Jeremy Schifeling | The backbone. "How to Win LinkedIn Recruiter in 12 Steps," the three search rules, recruiter filter mechanics, the About/Experience structure. |
| **Career Coach GPT** | Jeremy Schifeling | Headline and About construction, the 50% Rule, the Profile Holy Trinity (headline / location / photo), the 3 Ns, Top Third Rule. |
| **The Job Closer** | Steve Dalton | The objective-information position on headlines, error-free as a floor condition, recruiter risk-aversion, the 6-second scan. |
| **The 2-Hour Job Search** | Steve Dalton | LAMP list for generating the target-company set that feeds the harvest. |
| **Reverse the Search** | Madeline Mann | GLORY framework, keyword-to-expertise association, network scale (2,000+), the 6–8 week brand-refresh cadence. |
| **Never Search Alone** | Phyl Terry | Candidate–Market Fit as the anchor for all scoring; the LinkedIn Rehab group exercise; the CMF announcement post. |
| **Job Hunting in the AI Era** | Brossman, Gower, Rose & O'Connor | AI/ATS screening behavior, LinkedIn-as-first-impression, publishing cadence, Shape Profile (I/T/Pi/X). |
| **Fire Me I Beg You** | Robbie Abed & James Altucher | Social proof as an interview pre-condition, narrative consistency across sections, buzzword elimination, first-person voice. |
| **The Start-Up of You** | Reid Hoffman & Ben Casnocha | Professional identity independent of employer — the basis for custom URL, Featured, and publishing criteria. |
| **Switchers** | Dawn Graham | Similarity attracts; the translation burden sits with the writer; name the bridge asset; address the objection before it's raised. *Added v2.* |
| **Stand Out / Reinventing You** | Dorie Clark | The known-for test; hireable vs. sought-out; proof of a pivot beats announcement of it. *Added v2.* |
| **Expect to Win** | Carla Harris | Performance currency vs. relationship currency; sponsor vs. mentor; state the ask. *Added v2.* |
| **So Good They Can't Ignore You / Deep Work** | Cal Newport | Career capital over passion. Used as a subtractive editing filter, not a generator. *Added v2.* |
| **Pivot** | Jenny Blake | The one-degree pivot — how many variables is the reader being asked to accept at once. *Added v2.* |
| **What Color Is Your Parachute?** | Richard Bolles | Transferable-skills inventory; name skills in the market's vocabulary. *Added v2.* |
| **LinkedIn Recruiter Cheatsheet** | The Job InSiders | The seven recruiter filters, used to set dimension weights. |

Framework attributions inside the rubric name the source at point of use.

---

## 2026 platform research

Book guidance predates LinkedIn's current matching stack. Where they conflict, current
platform behavior wins, and the rubric says so.

**What changed:**

- **Semantic matching replaced keyword matching.** LinkedIn's candidate search now ranks by
  LLM-based semantic relevance rather than literal term overlap, evaluating profiles as
  whole documents. Consequence: prose that *demonstrates* a capability outperforms a list
  that *names* it, and keyword stuffing now actively degrades match quality. This is the
  single largest departure from the books, all of which optimize for term density.
- **Headline weighting.** The headline remains the most heavily indexed field — reported at
  roughly 5× other fields — which reinforces rather than contradicts the books.
- **Skills weighting.** Skills carry heavy search weight; endorsement counts remain largely
  invisible in LinkedIn Recruiter. The books' "skills yes, endorsements no" guidance holds.
- **AI-assisted sourcing.** LinkedIn's Hiring Assistant (GA since late 2025) builds sourcing
  strategies from role context rather than Boolean strings, and reduces the number of
  profiles a recruiter reviews per role. Consequence: fewer profiles get seen, so the
  semantic fit of those that surface matters more.
- **Content favoring.** Teaching/insight posts are surfaced; promotional posts are
  suppressed. Reflected in E2.

**Corrected character limits.** Several sources cite outdated caps. Current values, used
throughout:

| Field | Books say | Actual (2026) |
|---|---|---|
| Headline | 120 (*Linked*) / 220 (*Career Coach GPT*) | **220** |
| About | 2,000 (*Linked*) | **2,600** |
| Experience description | — | **2,000** |

---

## Documented conflict: headline posture

The most substantive disagreement between primary sources. Not resolvable by evidence —
both positions are internally coherent and rest on different assumptions about what a
headline signals.

**Aspirational** — *Linked*, *Career Coach GPT*
> Put the desired job title in the headline. LinkedIn is "experience + aspiration."
> "Aspiring/Future [role]" is acceptable. Rests on: the algorithm can only match tokens
> that are present.

**Objective** — *The Job Closer*
> Aspirational headlines "don't effectively convey confidence." Use objective experience —
> current title and employer, under ~15 words. Rests on: recruiters are risk-averse and
> read hedging as weakness.

**How the rubric handles it:** the user picks a posture, or the tool applies a synthesis —
lead with the most target-adjacent title claimable *truthfully*, without hedging language.
This satisfies the algorithmic constraint (token present) and Dalton's objection (no
"aspiring"). The report always states which way it scored.

A rubric that hid this would be more confident and less honest. Contested criteria are
marked as contested.

---

## Known limitations

- **Weights are reasoned, not empirically validated.** They derive from documented recruiter
  filter order and the gate-vs-gradient argument, not from outcome data. They are a
  defensible prior, not a measurement. Treat a 4-point difference between two profiles as
  noise.
- **No access to live LinkedIn.** Scores what the user supplies. Cannot verify search
  ranking, actual impressions, or how the profile renders to a recruiter.
- **US/English-centric.** Recruiter behavior, title conventions, and photo norms vary by
  market. Photo criteria in particular do not transfer to markets where photos are
  discouraged or prohibited.
- **Platform behavior moves.** The 2026 research has a shelf life. Re-verify before relying
  on the semantic-matching claims in a later year.
- **Optimizes for recruiter discovery.** That is the stated goal, but it is not the only way
  to find work — referrals and direct outreach frequently outperform inbound, and a high
  score is not a substitute for talking to people.


---

## Deliberately excluded

**Marc Cosentino, *Case in Point*** — case-interview methodology has no LinkedIn-profile
implication. Recorded so the omission reads as a decision rather than an oversight. Belongs in
`methodology_Interviewing.md` when that file exists.
