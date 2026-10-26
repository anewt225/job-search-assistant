# Principles

What the Job Search Assistant promises the people who use it. Each principle links to where the
product keeps that promise, so you can check it instead of taking our word for it. Promises the product
doesn't keep yet are listed under [Not built yet](#not-built-yet). When two principles pull in different
directions, the user's freedom and control win.

**Freedom · Respect · Control · Craft**

## Freedom: yours to take anywhere

**Vendor independence.** It runs in the AI app you already use, and no feature depends on one vendor.
*Proof:* standard `SKILL.md` folders; the same zip installs in Claude, ChatGPT, Gemini and Grok; every
app-specific step lives in one table, [`shared/hosts.md`](shared/hosts.md).

**Open formats.** Your profile, tracker and documents stay readable without this project.
*Proof:* the profile is Markdown ([`profile-template.md`](shared/profile-template.md)); the tracker uses
the same field names in Notion, Sheets, Airtable, CSV and Obsidian ([`data-schema.md`](shared/data-schema.md));
LinkedIn to-dos export to CSV and JSON ([`make_todos.py`](modules/job-search-linkedin/scripts/make_todos.py)).

**Freedom to exit.** Leaving is free and takes nothing with it.
*Proof:* there is no account, server or subscription. Your data already lives in your own tools.

**Open, but not for exploitation.** Published for individuals, coaches and communities to use and
improve, not for others to copy and resell. *Not yet reflected in the license; see
[Not built yet](#not-built-yet).*

## Respect: your data, your call

**Minimal data.** Hold as little as possible, read only what the task needs.
*Proof:* this project hosts nothing, and the setup wizard keeps your answers only in your browser. The
daily stand-up reads email subjects and senders, not bodies, about 10 items per source
([`rhythm`](modules/job-search-rhythm/SKILL.md)).

**No training, no selling.** The project collects nothing, so it has nothing to train on or sell.
The AI app you run it in has its own terms, and the assistant tells you when they matter (for example,
Gemini's *Keep Activity* requirement in [`hosts.md`](shared/hosts.md)).

**Transparent scoring and sources.** Every claim shows where it came from.
*Proof:* anything inferred is labelled `INFERRED`; missing experience becomes `[NEED STORY: …]`, never
invented ([`interview`](modules/job-search-interview/SKILL.md)); every score gives one line of reasoning per
criterion ([`linkedin`](modules/job-search-linkedin/SKILL.md), [`resume`](modules/job-search-resume/SKILL.md));
pay ranges come with sources and dates ([`negotiation`](modules/job-search-negotiation/SKILL.md)).

**Care for third parties.** Contacts and interviewers never agreed to anything.
*Proof:* never guess an email address ([`networking`](modules/job-search-networking/SKILL.md)); research
covers only the company, role and interviewer; LinkedIn is never scraped.

## Control: a human decides

**Approval for anything that reaches another person.** Nothing is sent, posted or shared for you.
*Proof:* every module writes drafts only, creates email drafts only when asked, and writes at most 3
outreach drafts per run ([`networking`](modules/job-search-networking/SKILL.md)).

**Ask before changing your tools.** You see what will change before it does.
*Proof:* tasks and calendar blocks are created only after you approve the list
([`interview`](modules/job-search-interview/SKILL.md), [`rhythm`](modules/job-search-rhythm/SKILL.md));
profile updates and tracker imports show a diff or counts first ([`setup.md`](shared/setup.md),
[`data-schema.md`](shared/data-schema.md) §Import).

**Secure by default.** Connect only what you choose, and nothing goes out without your approval.
*Proof:* every connector is optional and every feature has a paste or upload fallback
([`hosts.md`](shared/hosts.md)).

## Craft: simple, not simplified

**Easy to start, deep when you want it.** Respect the user's time: plain language, one question at a
time, sensible defaults.
*Proof:* Quick setup takes six questions; modules read your profile instead of asking again
([`setup.md`](shared/setup.md) §0); mock interviews ask one question at a time
([`practice.md`](modules/job-search-interview/references/practice.md)).

**Accessible.** Usable by voice, on a phone and with a screen reader.
*Proof so far:* mock interviews and negotiation role-play are built for voice mode; the site works at
phone width and in light and dark themes. A full audit is [not built yet](#not-built-yet).

**Honest about AI.** No inflated claims; say what the assistant can't do.
*Proof:* success is measured in live conversations per week, not applications sent; mock interviews
estimate answer length from word count rather than pretend to time you
([`practice.md`](modules/job-search-interview/references/practice.md)).

## Not built yet

- **An activity log** showing what the assistant read and wrote in each run.
- **An accessibility audit** of the site against WCAG 2.2 AA, with the fixes.
- **A license that matches "not for exploitation."** MIT lets anyone, including companies, copy and
  sell the work. Options: PolyForm Noncommercial 1.0.0 for code plus CC BY-NC-SA 4.0 for the skill text,
  or keep the skills noncommercial and license any hosted platform separately. Noncommercial licenses are
  "source-available," not "open source" by the OSI definition, and releases already published under MIT
  stay MIT. Get advice before changing it.
- **If a hosted or paid version ever exists:** it keeps only account and billing data, encrypted;
  cancelling is as easy as signing up; your data leaves with you.

## Using these principles

New module or feature? Check it against all four groups in the pull request, and add a *Proof:* link
when it keeps a promise. If a principle blocks something useful, open an issue instead of working around it.

Influences: Cory Doctorow on interoperability and the freedom to exit; Ink & Switch, *Local-first
software*; Privacy by Design; Microsoft's *Guidelines for Human-AI Interaction*; CISA *Secure by Design*.
