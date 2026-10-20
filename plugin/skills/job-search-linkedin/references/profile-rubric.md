# LinkedIn Profile Rubric

**v2 — 2026-08-05.** Criteria, weights, and anchors are **unchanged from v1 by design**, so scores
stay comparable across audits (42 -> 63 -> ...). What v2 adds is an **advisor annotation** on each
criterion naming whose framework governs it. Full frameworks: `advisory-panel.md`. Justification for
the weights: `methodology_LinkedIn.md`.

> **This rubric is Layer 1.** After scoring, run **Layer 2 - the Advisory Panel**
> (`advisory-panel.md`). The panel is unscored: it explains the score rather than adding to it. If a
> panel finding seems severe enough to change the number, that is evidence the rubric is missing a
> criterion - log it for the next methodology refresh. **Never adjust the composite by feel.**

Score every criterion. Do not skip any. Show your reasoning for each score in one short sentence, then give the number.

## How to score

Each criterion is scored **0–4** against the anchors below, then scaled to its point weight:

```
points_earned = (score / 4) × weight
```

| Score | Anchor |
|---|---|
| **0** | Absent. The field is empty, disabled, or actively counterproductive. |
| **1** | Present but ineffective. Exists, does not serve the target role. |
| **2** | Adequate. Does the minimum; a recruiter would not ding it, nor be moved by it. |
| **3** | Strong. Clearly serves the target role; a recruiter would take it seriously. |
| **4** | Exemplary. Would be used as a teaching example. |

**Never award a 4 by default.** A 4 requires a specific, quotable reason. If you cannot name it, the score is a 3.

**Anchor to the target, not to the person.** Every score is "relative to the roles named in the Candidate–Market Fit," never "relative to the average LinkedIn user." A brilliant profile for the wrong job scores low.

---

## Weight summary

| Dimension | Points | What it answers |
|---|---:|---|
| **A. Discoverability** | 32 | Do you appear in the search at all? |
| **B. Relevance & Semantic Depth** | 26 | Once found, do you match? |
| **C. Credibility & Proof** | 22 | Is the claim believable? |
| **D. Human Filter** | 12 | Does a tired human click? |
| **E. Engagement Signals** | 8 | Are you worth an InMail? |
| **Total** | **100** | |

Discoverability carries the most weight because it is a gate, not a gradient: a profile that never surfaces in a recruiter search scores zero on everything downstream in the real world, regardless of how well written it is. Dalton's framing is the one to keep in mind — recruiters must reject 99%+ of applicants, so they are scanning for reasons to say *No*.

---

## A. Discoverability — 32 points

### A1. Headline: target job title — **10 pts**

*Advisors: **Schifeling** (headline is the most heavily weighted field; Holy Trinity) - **Dalton** (objective posture, <=15 words) - **Mann** (translate internal titles; target the role you want). This is the contested criterion - see below.*

The single highest-leverage field on the profile. LinkedIn indexes the headline far above other fields, recruiters begin nearly every search with a job title, and the 220-character cap makes it hard to game — which is precisely why the algorithm trusts it.

- **0** — Default headline (current title auto-filled and irrelevant to target), or empty.
- **1** — Vague personal branding with no job title ("Lifelong learner | Problem solver | Coffee enthusiast").
- **2** — Contains *a* job title, but not one a recruiter would search for the target role.
- **3** — Contains the target job title verbatim, as a recruiter would type it.
- **4** — Target title verbatim **plus** a credible qualifier, and it reads like a human wrote it.

> **Check the exact string.** Search the target title on LinkedIn Jobs and use the most common phrasing. "Strategy & Operations" and "Strategic Operations" are not the same token. Internal or invented titles ("Growth Ninja," "Member of Technical Staff") must be translated to the market-recognized equivalent.

### A2. Headline: qualifiers and readability — **4 pts**

*Advisors: **Schifeling** (Holy Trinity) - **Dalton** (6-second scan).*

- **0** — Keyword soup, pipe-delimited to the character limit, unreadable.
- **2** — Title plus one or two supporting terms; serviceable.
- **4** — Title, industry/domain, and one differentiating credential, ordered so the first ~70 characters carry the meaning (that is all that renders in mobile search results).

### A3. Location — **6 pts**

*Advisor: **Schifeling** - "update your Location to where you want to be found, not where you're sitting right now." A binary filter, not a dial.*

An on/off switch, not a dial. If the target market is Chicago and the profile says Boise, the profile is invisible to that search — remote-friendly era included, because recruiters still filter on it to preserve in-office optionality.

- **0** — Blank, or a location with no relationship to the target market.
- **2** — Correct metro but imprecise (country- or state-level only).
- **4** — Set to the specific target metro, matching how the market names it.

### A4. Skills section — **6 pts**

*Advisors: **Schifeling** (top-20 skills from real JDs; skills yes, endorsements no) - **Mann** (combined top-5 keyword method).*

Skills appear in LinkedIn Recruiter; endorsements largely do not. Optimize for presence and accuracy, not for endorsement counts.

- **0** — Fewer than 5 skills, or none relevant to the target.
- **1** — Present but generic (Microsoft Office, Teamwork).
- **2** — 10–25 relevant skills; top 3 not deliberately chosen.
- **3** — 25+ relevant skills drawn from real job descriptions; top 3 pinned and on-target.
- **4** — The above, plus every skill named in the target JDs is present, and the top 3 are the three a recruiter would filter on first.

### A5. Open to Work — **4 pts**

*Advisor: **Schifeling** - "the one step every job-seeker should leverage." See methodology SS4.4 for the 2026 public-vs-private evidence. Recruiters-only is NOT penalized.*

Binary in effect. Recruiters filter for it to avoid wasting limited InMail credits; leaving it off removes you from those searches by default.

- **0** — Not enabled.
- **2** — Enabled but under-configured (fewer than 3 titles, or a single location).
- **4** — Enabled with ~5 target titles and multiple target locations. Recruiters-only is a legitimate choice and is **not** penalized — score visibility scope on intent, not on bravery.

### A6. Public visibility and custom URL — **2 pts**

*Advisors: **Garriott & Schifeling** (custom URL as a brand component) - **Hoffman** (identity independent of employer).*

- **0** — Profile not public, or default numeric URL.
- **2** — Public, custom URL claimed, name (or name + expertise) in the slug.

---

## B. Relevance & Semantic Depth — 26 points

> **2026 note.** LinkedIn's candidate matching now runs on semantic/LLM relevance rather than literal keyword overlap. Prose that demonstrates a capability in context now outperforms a keyword list that merely names it. Score depth of demonstrated meaning, not term frequency — and penalize keyword stuffing under B2, since it now actively degrades match quality rather than merely reading badly.

### B1. About — the billboard — **7 pts**

*Advisors: **Graham** (the target frame must lead; never make the reader translate) - **Mann** (value-add over history) - **Clark** (a point of view, or only a summary?).*

Only ~300 characters render on desktop (~200 on mobile) before "…see more." Nearly everyone wastes them.

- **0** — About section empty.
- **1** — Opens with a personality throat-clear ("Equal parts lifelong learner and productivity nerd") — zero target signal above the fold.
- **2** — States what the person does, but flatly and without target framing.
- **3** — Target role and domain are unmistakable within the first two lines.
- **4** — The above, and the opening line makes a reader want to keep reading — a specific point of view, not a summary.

### B2. About — the body — **7 pts**

*Advisors: **Newport** (strike every line asserting passion; keep what demonstrates capability) - **Harris** (state the ask, give a contact method) - **Mann** (specialties line from the keyword method).*

Full cap is 2,600 characters. Score the whole section for: narrative arc, 2–3 concrete proof points, a natural specialties/skills line, and an explicit call to action with a contact method.

- **0** — Empty or a single sentence.
- **1** — A wall of adjectives, or a keyword dump with no story. *Cap at 1 if the section is visibly stuffed* — semantic matching penalizes it and humans stop reading.
- **2** — Coherent summary, but no numbers and no ask.
- **3** — Clear arc, at least two quantified proof points, skills line, and a CTA.
- **4** — All of the above, in an unmistakably individual voice, with an explicit statement of what the person is looking for and how to reach them.

### B3. Experience — current/most recent role — **6 pts**

*Advisors: **Schifeling** (3 Ns; Keyword + Impact) - **Dalton** (effort tier: objective info, select bullets, or full replication).*

The single most common catastrophic gap: a strong résumé bullet set that exists nowhere on LinkedIn. Skill tags alone render as an empty role to a recruiter.

- **0** — No description. Title and dates only.
- **1** — One line, or a copy-paste of a formal internal job description.
- **2** — 2–4 bullets describing responsibilities.
- **3** — 3–5 bullets combining target keywords with stated impact.
- **4** — The above, every bullet quantified, and scope legible to an outsider without insider context.

### B4. Experience — prior roles — **3 pts**

*Advisor: **Graham** - the highest-stakes criterion for a career-changer. Score translation, not similarity. Supported by **Bolles** (transferable skills in the market's vocabulary) and **Mann** (the role you want, not the roles you've had).*

- **0** — Titles and dates only throughout.
- **2** — Most roles have some description; relevance to the target is inconsistent.
- **4** — Every role carries 1–5 bullets, and earlier roles are deliberately framed toward the target rather than left as historical artifacts.

> Career-changers: score how well prior roles are **translated**, not how closely they match. A restaurant GM who reframed operations work as systems implementation scores 4; one who left it as restaurant duties scores 1, even with identical underlying experience.

### B5. Keyword coverage against target JDs — **3 pts**

*Advisors: **Mann** (keyword-to-expertise association) - 2026 semantic matching (methodology SS4.1): cover the related-term cluster, never repeat the token.*

Run the three-bucket gap from `keyword-harvest.md` first, then score.

- **0** — Fewer than 25% of target-JD terms appear anywhere.
- **2** — 50–70% coverage; most live only in skill tags.
- **4** — 80%+ coverage, and the high-value terms appear in *prose* (headline, About, experience), not only as tags.

---

## C. Credibility & Proof — 22 points

### C1. Quantified achievement — **8 pts**

*Advisors: **Schifeling** (3 Ns) - **Harris** (performance currency - note where it saturates) - **Newport** (demonstrated, not claimed).*

Apply the **3 Ns**: every bullet should carry a **Number**, a **Name** (recognizable org, client, tool, or brand), or a **Notable** (something beyond the job description).

- **0** — No bullets anywhere, or zero contain any of the 3 Ns.
- **1** — Purely responsibility statements ("Responsible for managing...").
- **2** — Roughly a third carry at least one N.
- **3** — Most bullets carry at least one N; the strongest role is well quantified.
- **4** — Nearly every bullet carries at least one N, and the numbers convey *scale* the reader can situate (denominator included: "40% faster" beats "improved efficiency," and "40% faster across 19 business units" beats both).

### C2. Recommendations — **6 pts**

*Advisor: **Harris** - relationship currency, and the sponsor question: is anyone visible here who would spend capital on this person? Usually the cheapest large win on the board. Also **Abed & Altucher** (social proof as precondition).*

Third-party validation. Dalton's risk-aversion point applies: recommendations lower perceived hiring risk in a way self-authored copy cannot.

- **0** — None.
- **1** — 1–2, all older than 5 years or from peers only.
- **2** — 2–3, mixed recency.
- **3** — 3+, at least one from a manager, at least one within 3 years.
- **4** — 3+ recent, at least one from a senior person in or adjacent to the target domain, each speaking to specific attributes rather than generic praise.

### C3. Featured / media / work samples — **4 pts**

*Advisors: **Clark** (proof of the new positioning, not announcement of it) - **Hoffman** (portable professional identity).*

- **0** — Featured section absent.
- **2** — Present, but the items don't support the target positioning.
- **4** — 2+ items that directly evidence target-role capability (writing, deck, project, talk, press).

### C4. Education and certifications — **4 pts**

*Advisor: **Dalton** - objective information, and it must be error-free. An expired or mis-dated credential is a free reason to say No.*

- **0** — Missing entirely.
- **2** — Listed, bare.
- **3** — Listed with credential IDs where applicable; relevant coursework or achievements noted.
- **4** — The above, and certifications visibly relevant to the target role, treated like experience entries with evidence of application.

---

## D. Human Filter — 12 points

### D1. Profile photo — **5 pts**

*Advisors: **Schifeling** (Holy Trinity; Duchenne smile; dress for the tribe you want to enter) - **Abed & Altucher** (pay for it) - **Dalton** (approachable, not formal).*

Profiles with photos are viewed dramatically more often. Score three things: dress, expression, crop.

- **0** — No photo.
- **1** — Present but disqualifying: group shot, heavy filter, unclear which person is the subject, obviously casual for the target field.
- **2** — Acceptable but flat — stiff, poorly lit, or dressed off-register for the target.
- **3** — Well lit, cropped to head and shoulders, dressed for the target field, genuine expression.
- **4** — The above with a true Duchenne smile (eyes engaged, not just mouth) and evident warmth. Warmth outperforms polish.

### D2. Background banner — **2 pts**

*Advisor: **Schifeling** - the cover photo occupies more real estate than the headshot.*

- **0** — Default blue.
- **1** — A photo, but no signal about industry or positioning.
- **2** — Reinforces target domain or geography.

### D3. Error-free and narratively consistent — **5 pts**

*Advisors: **Dalton** - the floor condition, and the one criterion where absence of defect outweighs presence of brilliance - **Abed & Altucher** (every section telling the same story).*

Dalton's floor condition: this is the one criterion where the absence of defects matters more than the presence of brilliance. A typo is a free reason to say No.

- **0** — Multiple typos, broken dates, contradictory titles.
- **2** — Clean but inconsistent — headline promises one thing, experience shows another.
- **4** — Zero errors, and headline, About, experience, skills, and recommendations all tell the same story.

---

## E. Engagement Signals — 8 points

### E1. Network and company connections — **4 pts**

*Advisors: **Mann** (2,000+ at 10+ years) - **Hoffman** (network as a deliberately built asset) - **Garriott & Schifeling** (weak ties, ~80% of jobs).*

Recruiters filter for candidates already connected inside their company — a connected candidate is a warmer, cheaper approach.

- **0** — Under 150 connections.
- **2** — 500+.
- **3** — 1,000+ with real presence in the target industry.
- **4** — 2,000+, deliberately built, with first-degree connections at named target companies.

### E2. Following targets and activity — **4 pts**

*Advisors: **Clark** (any reason to follow absent an open role?) - **Brossman et al.** (publish to be visible) - 2026 ranking (methodology SS4.3: dark profiles lose visibility even when perfectly optimized). Plus **Schifeling**'s invisible signal - InMail responsiveness is itself a ranking input.*

- **0** — Follows no target companies; no activity in 12 months.
- **2** — Follows some targets; occasional reactions.
- **3** — Follows most target companies; comments substantively; posts occasionally.
- **4** — The above plus original posts demonstrating domain thinking. Teaching content is favored by the algorithm; promotional and "open to work" broadcast posts are suppressed — score the former, not the latter.

---

## Contested criterion: headline posture

The sources genuinely disagree, and the rubric refuses to hide it.

| Position | Source | Claim |
|---|---|---|
| **Aspirational** | *Linked* (Garriott & Schifeling); *Career Coach GPT* (Schifeling) | Put the **desired** job title in the headline. LinkedIn is experience *plus aspiration*. "Aspiring/Future [role]" is acceptable. |
| **Objective** | *The Job Closer* (Dalton) | Aspirational headlines "don't effectively convey confidence." Use objective experience — current title and employer. Keep it under ~15 words. |

**How to handle it:** ask the user which posture they want before scoring A1, or infer it and state the assumption explicitly in the report.

- **Aspirational posture** — score A1 against the *target* title. Best when the person is changing fields and their current title actively misleads.
- **Objective posture** — score A1 against the most senior, market-legible title they have actually held. Best when current experience already reads as adjacent to the target.

A defensible synthesis, and the default when the user expresses no preference: **lead with the most target-adjacent title the person can claim truthfully, without the word "aspiring."** This satisfies the algorithm (the token is present) and Dalton's confidence objection (no hedging language). Say in the report that this is a contested call and note which way you scored it.

---

## Layer 2 - run the Advisory Panel

Scoring is not finished until the panel has run. Read `advisory-panel.md` and produce the seven
verdicts, the split, and the collective read. The panel is where posture, differentiation, and voice
get examined - none of which a weighted composite can see.

Order matters: **score first, panel second, rewrites third.** Running the panel before the score
produces impressions dressed as analysis; running it after the rewrites is too late to shape them.

---

## Composite and grade

```
composite = Σ (score_i / 4) × weight_i
```

| Score | Grade | Reading |
|---:|:--|---|
| 90–100 | A | Ready. Remaining gaps are cosmetic. |
| 85–89 | A− | Strong. One or two targeted fixes. |
| 80–84 | B+ | Working profile with a clear next lever. |
| 75–79 | B | Solid base; one dimension is dragging. |
| 70–74 | B− | Findable but not persuasive. |
| 65–69 | C+ | Real gaps in a high-weight dimension. |
| 60–64 | C | Discoverable or credible, rarely both. |
| 50–59 | D | Structurally incomplete for the target. |
| < 50 | F | Effectively invisible for this target. |

Report the composite, each dimension as `earned / possible`, and the three highest **point-recovery** items — not the lowest raw scores. A 0 on a 2-point criterion is cosmetic; a 2 on a 10-point criterion is the actual problem. **Rank fixes by points recoverable per minute of effort.**
