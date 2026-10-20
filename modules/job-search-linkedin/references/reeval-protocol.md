# Re-Evaluation Protocol

Run when the user returns with an updated profile after a prior audit.

**This is the accountability half of the tool.** Diagnosis is cheap and repeatable; the thing that
actually determines whether a job search improves is whether recommendations get implemented. A tool
that only ever scores is a tool that can be used forever without anything changing.

---

## Prerequisites

- The **prior audit report** (score, dimension breakdown, and the ranked action plan)
- A **new profile export**
- Ideally, **updated analytics** — profile views / 90 days, search appearances / week, post
  impressions. This is the only outcome data available.

If the prior report is missing, this is not a re-eval — run a fresh Score and say so.

---

## 1. Diff, don't re-derive

**Do not re-score from scratch.** Re-scoring everything wastes effort and, worse, introduces drift:
two independent scoring passes on an identical profile will differ by a few points from judgment
noise alone, and that noise will be misread as progress or regression.

Instead:

1. Walk the prior action plan item by item.
2. Compare each against the new profile.
3. Re-score **only criteria whose underlying content changed.**
4. Carry forward unchanged criteria at their prior score, marked `carried`.

State plainly at the top: *"N of 20 criteria re-scored; M carried forward unchanged."*

---

## 2. Classify every prior recommendation

Exactly one of five, per item:

| Status | Meaning |
|---|---|
| ✅ **Shipped** | Implemented substantially as recommended |
| 🟡 **Partial** | Started but incomplete — name precisely what's missing |
| ↔️ **Shipped differently** | Addressed by different means. **Not a failure.** Score the outcome, not the compliance. If the user's version is better, say so. |
| ❌ **Not shipped** | No change |
| ⚪ **Superseded** | No longer applicable — target changed, or the recommendation was wrong |

Then the honest arithmetic:

```
Shipped:            N of M  (NN%)
Points recovered:   +NN.N of +NN.N available
```

**Report the shipped rate without editorializing.** A 3-of-11 rate is information, not an
accusation. The number does the work; commentary on it does not.

---

## 3. Score movement

```
| Dimension | Prior | Now | Δ | Driver |
|---|--:|--:|--:|---|
| A. Discoverability | 24.2 | 28.0 | +3.8 | A5 Open to Work enabled |
```

**Composite: NN → NN (Δ +N.N) · Grade X → Y**

Rules:
- **Attribute every point of movement to a specific criterion.** Unattributed movement is scoring
  drift, and it must be labelled as such rather than counted as progress.
- **A move of ≤4 points in either direction is noise.** The rubric's weights are reasoned, not
  validated. Say so rather than celebrating a 62 → 65.
- If the composite moved but nothing shipped, the difference is drift. Name it.

---

## 4. Did it work in the world?

The score is a proxy. Analytics are the closest available thing to an outcome.

```
| Metric | Prior | Now | Δ |
|---|--:|--:|--:|
| Profile views / 90 days | | | |
| Search appearances / week | | | |
| Post impressions | | | |
| Recruiter InMails | | | |
```

**Caveats that must appear whenever this table does:**
- LinkedIn's indexing lag means changes take **days to weeks** to affect search appearances.
- Seasonal and market variation is large. A single comparison is directional at best.
- Correlation only. Other things changed too.

If analytics moved sharply in the wrong direction after a change, treat that as a genuine signal
worth investigating — not as something to explain away.

---

## 5. The new top three

Recompute the ranked plan against the *current* state. Some prior items will have become cheaper
(the hard part is done), some more expensive, some irrelevant.

**Do not simply re-present the unshipped items in the same order.** If an item has now failed to ship
across two consecutive audits, that is the finding — surface it explicitly:

> ⚠️ **[Item] has now been recommended twice and not shipped.** Either the estimate is wrong, the
> blocker is unstated, or it isn't actually worth doing. Pick one — and if it's the third, delete it
> rather than carrying it into a third audit.

That paragraph is the most valuable output in this entire protocol. A recommendation that survives
two audits unshipped is telling you something the score cannot.

---

## 6. Cross-platform evaluation prompt

Emit a **self-contained prompt** the user can paste into a different AI for an independent,
from-scratch assessment. The point is to check this tool's own suggestions against an evaluator that
shares none of its assumptions or its history with the profile.

Requirements:
- Fully self-contained — no reference to this rubric, this skill, or prior scores
- Includes the target role, locations, and CMF
- Asks for a numeric score **and** its criteria, so the two methodologies can be compared
- Never mentions what was recently changed (that primes the evaluation)

Template:

```
I'm going to share a LinkedIn profile and a target role. Assess the profile as an
experienced technical recruiter would when deciding whether to reach out.

Target role: [TITLE]
Target locations: [LOCATIONS]
Target industry: [INDUSTRY]
What I'm going for: [CMF — the problem I solve and who I solve it for]

Please:
1. Score the profile 0-100 for this specific target, and state the criteria and
   weights you used before giving the number.
2. Name the three things most likely to prevent a recruiter contacting me.
3. Tell me what's genuinely working — be specific, not encouraging.
4. Rewrite the headline and the first 300 characters of the About section.
5. Tell me what you'd want to know that the profile doesn't say.

Be direct. I'd rather have an accurate low score than a kind high one.

PROFILE:
[paste]
```

Then instruct the user to bring the other tool's score back. **A gap larger than ~15 points in either
direction is worth investigating** — it usually means the two are optimizing for different things,
and which one is right is a real question rather than a rhetorical one.

---

## 7. Output

Save as `LinkedIn_ReEval_[Name]_[YYYY-MM-DD].md`, alongside the prior audit.

Structure:
1. Header — prior audit date, prior score, days elapsed
2. Shipped scorecard (§2)
3. Score movement (§3)
4. Analytics (§4)
5. New top three + the twice-unshipped flag (§5)
6. Cross-platform prompt (§6)
7. Next re-eval date — default **6–8 weeks** (Mann's brand-refresh cadence)

---

## Tone

The re-eval is the one place where being soft actively harms the user. If nothing shipped, say
nothing shipped — in one sentence, without a lecture attached. Then ask the useful question:
**what would have to be true for this to get done in the next two weeks?**

Do not moralize about follow-through. Do not congratulate partial completion as though it were
completion. State the arithmetic, name the pattern if there is one, propose the smallest next
action, and stop.
