# Principles

How the Job Search Assistant is designed, and what it promises the people who use it. Every module,
feature and contribution should follow these. When two pull in different directions, the user's
freedom and control win.

Four groups, easy to remember: **Freedom · Respect · Control · Craft**.

---

## 1. Freedom: yours to take anywhere

**1.1 Vendor independence.** The assistant runs wherever you already work: Claude, ChatGPT, Codex,
Gemini, or the next thing. No AI vendor, tool vendor or partner owns the experience, and no feature
depends on one vendor when an open alternative exists.
*How:* skills use the open SKILL.md format; vendor-specific setup lives in one host table in
`shared/setup.md`, never inside module logic.

**1.2 Interoperability.** Built on open standards (SKILL.md, MCP, Markdown, CSV) so other tools can read,
write and build around it.
*How:* one data schema (`shared/data-schema.md`) with the same field names in every backend.

**1.3 Data portability.** Your profile, tracker and documents are always available in open formats
you can open without us.
*How:* the profile is a Markdown file; the tracker exports to CSV; nothing is stored in a format only
this project can read.

**1.4 Freedom to exit.** Leaving is free and painless. No lock-in, no penalty for leaving, no dark
patterns to keep you. If there is ever a paid version, cancelling will be as easy as signing up, and
your data leaves with you.

**1.5 Open, but not for exploitation.** The methodology and skills are published so individuals,
coaches and communities can use, learn from and improve them. They are not published so a third
party can copy the product piece for piece and resell it, or so large companies can profit from work
given away for free.
*How:* see [Licensing note](#licensing-note) below.

## 2. Respect: your data, your call

**2.1 Minimal data hosting.** Hold as little as possible, for as short a time as possible. Data that
isn't held can't be exposed, and what is held is easier to secure. By default your job-search data
lives in your own tools (Notion, Sheets, Drive, a local folder); any hosted service keeps only what it
needs to work (for example account and billing details), encrypted.

**2.2 No training, no selling, no sharing.** Your data is never used to train models, never sold, and
never shared with third parties beyond the services needed to do what you asked, under terms that
forbid them from keeping or training on it.

**2.3 Data transparency.** You can always see what is stored, where, and what the assistant did with
it: which tools it read, what it wrote, what it created.

**2.4 Fairness through transparency.** We don't collect demographic data to audit you, because that
would mean collecting more about you. Instead the assistant is open about how it works: it labels
anything inferred (`INFERRED`), never invents experience (`[NEED STORY: …]`), shows the criteria
behind every score, and says where its advice comes from.

**2.5 Care for third parties.** Contacts, interviewers and recruiters never agreed to anything. Keep
notes about them minimal and relevant, never guess email addresses, and never collect more about them
than the task needs.

## 3. Control: a human decides

**3.1 Mandatory approval for anything that reaches another person.** The assistant never sends,
posts, books or shares anything on your behalf without your explicit approval. Before you approve,
you see an accurate preview of the exact content, or a direct link to the draft in the app where it
will be sent (for example the Gmail draft or calendar invite). Drafts only, by default.

**3.2 Soft approval for work on your own things.** For changes that only affect your own files, code
or website, the assistant can move faster: it shows what it changed and makes it easy to review and
undo. You can tighten this to "ask first" at any time.

**3.3 Secure by default.** Safe settings out of the box: least privilege for every connection,
nothing outbound without approval (3.1), and no setting that trades your safety for convenience
without telling you.

## 4. Craft: simple, not simplified

**4.1 Intuitive and simple, not simplified.** Easy to start ("Quick for everything"), with depth when
you want it. Respect the user's time and intelligence: plain language, one question at a time,
sensible defaults, no busywork.

**4.2 Accessible by default.** The most intuitive design is also accessible: readable, keyboard and
screen-reader friendly, voice-friendly, with any adjustments easy to switch on. We treat WCAG 2.2 AA
as the floor, not the goal.

**4.3 Honest about AI.** No inflated outcome claims. Say clearly what the assistant can't do, what it
inferred, and when a human (or a book) knows better.

---

## Licensing note

Principle 1.5 is not compatible with the current MIT license, which allows anyone, including
companies, to copy and sell the work. Options under consideration:

- **PolyForm Noncommercial 1.0.0** for code, plus **CC BY-NC-SA 4.0** for the skill and methodology
  text: free for personal, educational and non-profit use, with commercial use only by permission.
- **Open core:** keep the skills under a noncommercial license; license any hosted platform separately.

Noncommercial licenses are "source-available," not "open source" by the Open Source Initiative's
definition. Versions already released under MIT stay MIT for whoever downloaded them; a new license
applies from the release that adopts it. Get advice before changing it.

## Using these principles

- New module or feature? Check it against all four groups in the pull request description.
- A principle blocks something useful? Open an issue to discuss changing the principle; don't quietly
  work around it.
- Influences: Cory Doctorow (*The Internet Con*, *Enshittification*) on interoperability and the
  freedom to exit; Ink & Switch, *Local-first software*; Privacy by Design (GDPR Art. 25);
  Microsoft's *Guidelines for Human-AI Interaction*; CISA *Secure by Design*.
