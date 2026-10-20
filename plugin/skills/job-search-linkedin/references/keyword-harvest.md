# Keyword Harvest

Run this **before** scoring B5, and before drafting any rewrite. The rubric needs a target to measure against; the rewrite needs vocabulary to borrow. Both come from here.

The method is adapted from Tamara Adlin's Dream Job Spreadsheet and the peer-profile comparison in the *Never Search Alone* LinkedIn Rehab exercise. The insight behind it: **you are not inventing language, you are collecting it.** Employers have already written down exactly what they want, in their own words, in public. Use theirs.

---

## Step 1 — Gather sources

Collect, at minimum:

- **5–8 real job descriptions** for the target role. Not summaries — full postings. Include at least two that feel like a *reach*, since those carry the vocabulary of the level above.
- **3–5 peer profiles**: people who currently hold the job the user wants. Not aspirational celebrities — working practitioners one step ahead.
- **2–3 target company career pages**, for house vocabulary and values language.

If the user supplies fewer than 3 JDs, say so and note in the report that coverage confidence is low. Do not silently proceed — a keyword gap computed from one posting is noise.

---

## Step 2 — Extract and categorize

From every source, pull:

| Category | What to look for |
|---|---|
| **Hard skills** | Tools, platforms, methods, certifications |
| **Domain terms** | Industry vocabulary, segment names, regulatory language |
| **Role verbs** | What the job *does* — leads, implements, forecasts, migrates |
| **Scope markers** | Team size, budget, geography, stage — the words that encode level |
| **Outcome language** | How this field describes winning — retention, uptime, pipeline, adoption |
| **Requirements** | Years, degrees, credentials |

Record the **exact string**, not a paraphrase. "Go-to-market strategy" and "GTM" are different tokens and may be indexed differently. Capture both when both appear.

Count frequency across sources. A term in 6 of 8 postings is a requirement; a term in 1 of 8 is that company's dialect.

---

## Step 3 — The three-bucket gap

This is the core artifact. Place every harvested term into exactly one bucket by where it appears **on the user's profile**:

### 🔴 Missing — absent from the profile entirely
The highest-value bucket and the reason to run this exercise. These are terms recruiters search for that currently return nothing for this person.

### 🟡 Tags only — present in the Skills section, absent from prose
The most commonly overlooked bucket. Skill tags are weaker signal than the same term used in context in the headline, About, or an experience bullet — and under semantic matching, a term used in a sentence that demonstrates the capability substantially outperforms the same term sitting in a list. **Surfacing a term from 🟡 to prose is usually the cheapest score improvement available.**

### 🟢 Present in prose — already working
Confirm and leave alone. Listing these matters: it prevents the user from rewriting things that already work, which is a real failure mode.

Output as a three-column table, ordered within each bucket by frequency across source JDs.

---

## Step 4 — Honesty filter

Before anything moves from 🔴 to a draft, test each term:

1. **Can the user substantiate it?** If asked "tell me about a time you did this" in an interview, is there an answer? If not, the term does not go on the profile. A keyword that wins the search and loses the interview is worse than no keyword.
2. **Is it a translation or a fabrication?** Renaming real work in the market's vocabulary is legitimate and necessary — an "impact-measurement methodology" *is* a "customer analytics framework" if that is what it did. Claiming unbuilt experience is not.
3. **Would a practitioner wince?** Terms used slightly wrong are worse than terms omitted; they signal outsider status precisely to the expert reader you are trying to impress.

Flag anything that fails as **stretch** in the report, and handle it under the 50% Rule below rather than dropping it in silently.

---

## Step 5 — The reach columns

Terms the user cannot yet claim are not waste — they are the development plan. Sort the honesty-filter failures:

| Bucket | Meaning |
|---|---|
| **Close enough** | Has the substance, lacks the exact term or the stated year count. **Use it.** |
| **2 weeks & 2 books** | Genuinely learnable before the search concludes. Name the specific resource. |
| **4–6 months** | Would be true after landing the job. Do not claim; prepare to address. |
| **A year or two** | Real gap. Useful for a development plan, not this profile. |
| **Not interested** | Present in the JD, unwanted by the user. Explicitly excluded — often a signal the role is mis-targeted. |

**The 50% Rule** (Schifeling): candidates meeting roughly half of stated requirements convert to interview at the highest rate, and the rate *declines* past that. Do not treat gaps as disqualifying, and tell the user where they sit against the threshold. A profile engineered to appear 100% qualified frequently reads as overqualified or fabricated.

---

## Step 6 — Peer profile diff

For each peer profile, capture:

- Their **headline** construction — literal pattern, e.g. `[Title] at [Company] | [Domain] | [Credential]`
- How they describe **the same work the user has done** — this is the highest-value output of the whole exercise
- What they include that the user omits, and vice versa
- Their **top 3 pinned skills**

Then answer explicitly: **what does this peer say that the user cannot yet say, and what can the user say that this peer cannot?** The second half is the differentiation the positioning should be built on. A profile that merely converges on peer language is findable but interchangeable.

---

## Output

Produce:

1. The three-bucket table
2. The reach-column table with the 50% Rule assessment
3. A ranked **"words in"** list — 10–15 terms to introduce, ordered by (JD frequency × ease of honest substantiation)
4. A **"words out"** list — internal jargon, invented titles, dated terminology, and anything that failed the practitioner-wince test
5. Peer headline patterns, verbatim

Hand all five to `rewrite-playbook.md`.
