# Job Search Assistant v2: design spec

Status: draft for review, 2026-11-10. Written against v1.1.0.

This is the single design that the open v2 backlog implies. The backlog is 37 items: GitHub issues
#3 to #35, plus four internal items that have no public issue (three decisions and one scoping note).
Every one of them is mapped to a section of this spec in [§9](#9-issue-map). Decisions that are still
open are in [§10](#10-conflicts-and-open-decisions); nothing in the code depends on how they come out.

## 1. Goal

Someone who lands on the site gets a useful answer from the assistant within five minutes, with no
quiz required and no hand-holding.

The evidence is one moderated user test and one install test (Nov 2026). What they showed:

- Installing took too many steps. Chat apps take one skill per upload, so "all eight" meant eight uploads.
- The landing page offered several first actions, and the zips carried a second set of instructions.
- After installing, people did not know what to type.
- Setup asked questions before saying what the assistant does, opened with a choice between two setup
  styles, and proposed six specific apps.
- Setup-first failed the person whose real need was an interview that same day.
- People assumed connecting email was required.

## 2. Design rules

These follow from [`PRINCIPLES.md`](../PRINCIPLES.md) and settle most of the individual issues.

1. **Value before setup.** A concrete request always beats onboarding. Setup is offered, never required.
2. **One flow.** There is one setup, five steps, the same in every app. No "quick" variant, no per-app
   variant. The site wizard, if it stays, is the same five steps in a form ([§7](#7-site-wizard)).
3. **One action at a time.** One primary button per screen on the site. One question per turn in chat.
4. **Say where you are.** Every setup turn starts with "Step N of 5" and the step name.
5. **Suggest, don't prescribe.** Every question has a suggested answer drawn from what the user already
   said and the tools the assistant can actually see. There is no preset app stack.
6. **Nothing has to be connected.** Every ask about a tool says what it enables and offers "no tool".
7. **One place per fact.** Install steps live in `shared/hosts.md`, the site and `docs/QUICKSTART.md`,
   and are changed together. Nothing inside a zip repeats them.

## 3. The path, end to end

```
Site: Get started → pick your app → one install action
        chat apps:      download one zip, upload it once
        coding agents:  copy one prompt, paste it
   ↓
"Installed? Now say this": type / to see the skills + three first messages
   ↓
First message
   ├─ a concrete request, or "I have an interview today with ___"
   │     → the module does it now, asking only what it needs      (urgent path, §5)
   │     → afterwards: one offer to run setup
   └─ "Set up my job search", or nothing specific
         → Welcome turn (no questions)                             (§6.1)
         → Step 1 of 5 · Where you are
         → Step 2 of 5 · How you want to work
         → Step 3 of 5 · Your tools
         → Step 4 of 5 · About you
         → Step 5 of 5 · Review and first task                     (§6.3)
```

## 4. Install in one step

### 4.1 One upload for chat apps
`build.py` emits `job-search-assistant.zip`: a single skill whose `SKILL.md` is a router
(`bundle/SKILL.md`) and whose `references/<module>/` folders hold the eight modules. Each module keeps
its own layout, with its `SKILL.md` renamed `MODULE.md` so that no app reads it as a second skill. The
shared layer and the book notes are stored once at the top level instead of once per module, which is
why the bundle is about half the size of the all-in-one zip. Claude, ChatGPT, Gemini and Grok users
upload this one file.

The per-module zips stay as the advanced option, and `job-search-assistant-all.zip` stays for apps
with a skills folder. Claude Code and Codex keep installing the plugin, which is eight separate skills.

The build ends with checks for the rules the apps enforce: the top-level folder equals the `name:` in
`SKILL.md` (Gemini), names and descriptions are within the Agent Skills limits, every file is plain
text (Gemini rejects binaries), and the router points at every module.

Not settled: whether one router skill triggers as reliably as eight specific ones. See
[§10.4](#104-smaller-conflicts-between-issues).

### 4.2 One primary action on the site
The hero has one button, "Get started", which goes to the app picker. Each app's panel has exactly one
primary action: a download for chat apps, a copy button for coding agents. GitHub moves to the top
right and the footer. "Browse modules" leaves the hero; the modules grid stays lower on the page as
the advanced option. Landing to download is at most three clicks: Get started, your app, download.

### 4.3 Install paths, checked and dated
`shared/hosts.md` gains a column, "Install path last checked live", with a date per app or "not yet".
A path counts as checked only when someone has followed it in the real app. The Claude upload path is
now Settings → Customize → Skills → Add → Upload a skill. The Gemini, Grok, Codex and Antigravity
paths still come from each app's documentation and are marked "not yet".

### 4.4 Install by prompt, only where a prompt installs
Coding agents can run commands, so a pasted prompt can do the whole install: fetch the repository and
copy `plugin/skills/*` into the app's skills folder. The site shows one copy box each for Codex,
Claude Code, Antigravity and Gemini CLI (under "Other"). The README has the short version. Chat apps
do not get a prompt, because a prompt cannot install a skill there. `docs/install.json` states the same
facts for agents: repository, skills path, each app's skills folder, and what to say afterwards.

### 4.5 "Now say this"
Directly under the install step: type `/` to see the skills, then one of three first messages, each
with a copy button. "Set up my job search", "Tailor my resume for this posting: ___", "I have an
interview today with ___". The same three lines are the setup skill's answer to "what can you do?".

### 4.6 No second set of instructions
`QUICKSTART.md` no longer ships inside any zip, and the build fails if it reappears. The file stays in
`docs/` as a reference copy.

### 4.7 "Do I need to connect Gmail?"
No. The site says so in each install panel and in the "now say this" card, the welcome turn says it
before any question, and step 3 offers "no tool" for every job. Still to do: a line per optional
connection on the site saying what it adds.

## 5. Urgent path

Setup never stands between the user and something they need today.

- Triggers: an interview, phone screen or recruiter call within about 48 hours, or any concrete request
  made instead of starting setup.
- The interview module's urgent prep asks once for the company and role, the time, and a resume, and
  starts with whatever arrives. It returns a one-page brief in the same reply: the 30-second version,
  a 60-second "tell me about yourself", the three likeliest questions with answer outlines built only
  from the resume, three questions to ask, and logistics.
- It does not ask for a profile, a persona or a connection, and it does not write to the user's tools.
- Afterwards it offers setup once. A "no" is final for that conversation.

## 6. In-chat setup

The whole flow lives in [`shared/setup.md`](../shared/setup.md). Modules that need a profile field run
the same questions, scoped to what they need.

### 6.1 Welcome turn
The first setup turn asks nothing about the user. In eight lines or fewer: what the assistant does,
that setup is five short steps and about five minutes, that every question has a suggested answer and
can be skipped, that nothing has to be connected, and the urgent path. It ends by asking whether to start.

### 6.2 Turn format
- Progress header: the first line of every setup turn is `Step N of 5 · <step name>`.
- Question pattern: one question per turn; two to five lettered options plus the user's own words;
  exactly one option marked "(suggested)"; at most one line on what the answer enables; "ok", "skip"
  and "back" always work.

### 6.3 The five steps

| Step | Name | What it asks | Why here |
|---|---|---|---|
| 1 | Where you are | Search stage, what would help most this week, what you already have (resume, tracker, notes) | Context first: every later suggestion can use it |
| 2 | How you want to work | Persona (pick or quiz), keep or change the default rules | Sets tone before anything is drafted. Effort preference belongs here later |
| 3 | Your tools | One question per job: tracking, files, email, calendar, tasks, meeting notes | By job, not by app. Suggests what is already connected. "No tool" always offered |
| 4 | About you | Name, one-line positioning, target roles; drafted from the resume if one was shared | Personal detail comes after the user has seen the assistant listen |
| 5 | Review and first task | A five-line summary to confirm or change, then one first task for the stage | Ends with something to do, not a menu |

Removed from v1: the "two ways" opener (Quick or bring-your-own), the six-app Quick stack, the
twelve-component table, and the three-move list at the end. Output format is no longer asked
(Markdown unless the user changes it). Optional extras are no longer asked during setup.

### 6.4 Planned inside the same five steps
These are designed here but not all built yet. None adds a step.

- **Connection states.** Step 3 records each job as connected, not connected or skipped, and the step 5
  summary lists them. The flow describes this; the profile template has no field for the state yet.
- **Value at ask.** Each step 3 question carries one line on what the tool enables. "Value before data"
  then becomes a Respect principle with this as its proof.
- **Module check.** At step 5, and whenever a module is missing, say which modules are installed and
  what is missing. With the one-zip bundle every module is present, so this matters only for
  single-module installs.
- **Stack presets.** If presets return, they are step 3 suggestions ("you said Google for email; use
  Google for calendar and files too?"), never a named default stack.
- **Resume-assisted intake.** Step 4 already drafts from a resume shared in step 1. The site wizard
  cannot read files without leaving the browser, so this is in-chat only.
- **Effort preference.** One question in step 2; it sizes the first task and later suggestions.
- **Interview me.** A voice-friendly way through steps 1, 2 and 4: the same questions, spoken, without
  lettered lists. Step 3 is deferred to text.
- **Test mode.** A sample profile and the sample tracker rows in `templates/tracker-csv/`, entered with
  "try it with sample data". It needs no connection, which keeps it inside "collects nothing".
- **Intake.** v1.1 has no intake step. In v2, steps 1 and 4 are the intake, so the port becomes
  "declare the optional connections in the plugin metadata", not a second flow.

## 7. Site wizard

The wizard is optional and comes after download; no download button depends on it. Whether it stays at
all is an open decision ([§10.3](#103-keep-or-cut-the-site-wizard)), so this branch leaves its code
alone. If it stays, it has to stop being a second setup variant:

- the same five steps in the same order, which moves "About you" to the end and shortens it;
- stage options cut to three clear choices;
- "Quick" removed or redefined so that it means the same thing as in chat, where it no longer exists;
- presets, if any, as suggestions inside "Your tools".

Until then there is a known mismatch: the wizard still offers the Quick six-app stack that chat setup
no longer has. The profile file it produces is unchanged and still works.

## 8. Principles, docs and platform

- **Value before data** goes under Respect in `PRINCIPLES.md`, with §6.4 as its proof.
- **Product philosophy page**: a short "Why it works" page linked from the README and the site.
- **Accessibility audit** of the site against WCAG 2.2 AA. The new install panels and copy buttons are
  part of what gets audited; the app picker is still not a full ARIA tab pattern.
- **Demo video** on the site, 60 to 90 seconds. Host the file in the repository or a release rather
  than embedding a third-party player, so the page keeps collecting nothing.
- **Custom subdomain.** When the site moves, update the homepage URL in the plugin manifests and
  `docs/install.json`, and keep the old address redirecting.
- **Tracker MCP server**: scope only, three or four tools over the CSV tracker. It would be an optional
  connection for the Tracking job in step 3.
- **Not built yet** in `PRINCIPLES.md` (activity log, license) is unchanged by this spec.

## 9. Issue map

"Branch" says what the `v2-overnight` branch does: **done**, **part**, or **no** (designed here only).

| Issue | Title | Spec section | Branch |
|---|---|---|---|
| #3 | One-upload bundle for chat apps | §4.1 | done; triggering eval not run (§10.4) |
| #4 | Hero: one primary action | §4.2 | done |
| #5 | Fix host install paths and test every host live | §4.3 | part: Claude path fixed in all three places, dated column added; no live testing |
| #6 | Stop shipping QUICKSTART.md inside the zips | §4.6 | done |
| #7 | "Now say this" card after install | §4.5 | done |
| #8 | Copy-paste install prompt where it really installs | §4.4 | done; prompts not yet run in each app |
| #9 | Answer "Do I need to connect Gmail?" | §4.7 | part: said in install panels, welcome turn and step 3; per-connection benefits on the site not done |
| #10 | Downloading never requires the quiz | §7 | no (already true; wizard copy untouched) |
| #11 | Fix the "Quick" mismatch | §7, §10.4 | no; mismatch changed shape, see §7 |
| #12 | Cut stage options down to 3 | §7, §10.4 | no |
| #13 | "About you": simplify and move last | §6.3 step 4, §7 | part: last in chat; wizard untouched |
| #14 | Tool-stack presets | §6.4, §7 | no |
| #15 | Resume-assisted intake | §6.4 | part: in-chat drafting from a shared resume |
| #16 | Welcome turn | §6.1 | done |
| #17 | Urgent path: "I have an interview today" | §5 | done |
| #18 | One canonical 5-stage setup flow | §6 | done in chat; the wizard is the remaining variant (§7) |
| #19 | Remove the "two ways" opener and the six-app stack | §6.3 | done in chat, README and quickstart; wizard untouched |
| #20 | Progress header on every setup turn | §6.2 | done |
| #21 | Consistent question pattern | §6.2 | done |
| #22 | Context first | §6.3 step 1 | part: order is in the flow |
| #23 | Map tools by job to be done | §6.3 step 3 | part: step 3 is by job |
| #24 | Show connection states and what each one enables | §6.4 | part: described in the flow; no profile field yet |
| #25 | Module check | §6.4 | no |
| #26 | End setup with a review and a first task | §6.3 step 5 | part: summary and one first task are in the flow |
| #27 | Test mode with sample data | §6.4 | no |
| #28 | Effort preference | §6.4 | no |
| #29 | "Interview me" voice intake | §6.4 | no |
| #30 | Add "Value before data" to PRINCIPLES.md | §8, §6.4 | no |
| #31 | Write the product philosophy page | §8 | no |
| #32 | Audit the site against WCAG 2.2 AA | §8 | no |
| #33 | Add a short demo video to the site | §8 | no |
| #34 | Move the site to a custom subdomain | §8 | no |
| #35 | Add an intake step and declare optional connectors | §6.4 | no |
| internal | Decide: measurement vs "collects nothing" | §10.1 | no; open decision |
| internal | Decide: license | §10.2 | no; open decision |
| internal | Decide: keep or cut the site wizard | §10.3 | no; open decision |
| internal | Scope a tracker MCP server (one page) | §8 | no |

## 10. Conflicts and open decisions

The three decisions below are stated with options and a recommendation. None is decided in code.

### 10.1 Measurement vs "collects nothing"
The principles say the project collects nothing. The goal in §1 is a five-minute path, and there is no
way to see whether people reach it.

| Option | What you learn | Cost |
|---|---|---|
| A. Stay as is: release download counts plus moderated tests | Downloads per asset; depth from tests | None. Small numbers, slow feedback |
| B. Add a cookieless page counter and update the principle | Visits, and which app tab people pick | "Collects nothing" becomes "counts page views, no cookies, no profiles"; the site's "stores nothing on a server" line must change |
| C. A plus an explicit feedback link (an issue form) | What people choose to tell you | A little copy; nothing collected silently |

Recommendation: **A now, with C added, and revisit after the next test round.** Two things to know when
revisiting. First, v2 improves option A for free: the one-zip bundle is a single asset, so its download
count is a clean count of chat-app installs. Second, v2 also opens a blind spot: installs by prompt
(§4.4) clone the repository and never touch a release asset, so they are invisible to option A.

### 10.2 License
`PRINCIPLES.md` says "open, but not for exploitation". The README, the site footer and both plugin
manifests say MIT, which allows resale.

There is also an inconsistency to fix whichever way this goes: the `LICENSE` file on `main` is headed
"MIT License" but its grant no longer includes the words "sublicense, and/or sell". That text is not the
MIT license, so the file and the "MIT" labels currently disagree.

| Option | Effect | Cost |
|---|---|---|
| A. MIT, restored to the standard text | Simple, recognised everywhere, eligible for any plugin directory | The "not for exploitation" principle has to be reworded as a request, not a term |
| B. PolyForm Noncommercial 1.0.0 for code, CC BY-NC-SA 4.0 for the skill text | The license matches the principle | Not "open source" by the OSI definition, so the site's "open source" label goes; some directories and employers exclude noncommercial licenses; v1.0.0 and v1.1.0 stay MIT |
| C. Keep the edited MIT text | None | An ad hoc license nobody recognises, labelled as something it is not |

Recommendation: **do not ship option C. Choose between A and B before the v2 release and make it its own
commit and release note.** If the principle is meant as a promise, B is the option that keeps it. If
adoption and directory listings matter more, take A and reword the principle. This is a recommendation,
not legal advice; `PRINCIPLES.md` already says to get advice before changing the license. The `library/`
notes summarise other authors' books and are not covered by either choice.

### 10.3 Keep or cut the site wizard
The wizard works as a small commitment device, and every step in it adds friction.

| Option | Effect | Cost |
|---|---|---|
| A. Keep it: optional, after download | No change for people who like a form | It is a second setup variant until rebuilt to the five steps (§7); four backlog items (#11, #12, #13, #14) are wizard rework |
| B. Cut it | One setup, in chat, everywhere; those four items close | Loses the only setup path that works before installing anything |
| C. Keep it, frozen, and decide after the next test round | No rework yet | The Quick mismatch stays visible meanwhile |

Recommendation: **C, which is A without the investment: keep it optional and after download, do not
rework it yet, and let the next test round decide.** One dependency to note: with measurement left at
"collects nothing" (§10.1), the only way to learn whether anyone uses the wizard is to watch for it in
moderated tests, so the test plan needs a task that would reveal it.

### 10.4 Smaller conflicts between issues

- **One router skill vs module triggering (#3).** Eight skills each advertise their own triggers; one
  router advertises all of them in a single description. That may make the assistant slower to pick
  the right module, or more reliable because there is one obvious skill. The check is an eval of the
  same prompts with the bundle and with the eight skills. Not run yet. The plugin keeps eight skills
  either way, so only chat apps are affected.
- **"One flow for every host" (#18) vs the wizard (#10 to #14).** Covered in §7 and §10.3.
- **"Quick" (#11) vs removing Quick (#19).** #11 asks for the two Quicks to match; #19 removes one of
  them. After #19 the only way to match is to remove or redefine the wizard's Quick.
- **Three stage options (#12) vs the profile's five.** The profile and the modules use five stages. If
  the wizard goes to three, either the profile goes to three too, or the wizard's three map onto the
  five. This spec keeps five in chat and leaves the mapping to whoever does #12.
- **"About you" last (#13) vs context first (#22).** Resolved by splitting them: situation in step 1,
  identity in step 4.
- **Stack presets (#14) vs no preset stack (#19).** Resolved in §6.4: presets are suggestions, never a
  named default.
- **Install prompts (#8) vs "checked live" (#5).** The prompts and the Gemini CLI and Antigravity
  folders come from documentation. They need the same live check as the upload paths.
- **Demo video (#33) vs "collects nothing".** A third-party video embed loads that party's trackers.
  Self-host the file.
- **Docs in `docs/` are published.** GitHub Pages serves this folder, so this spec and `QUICKSTART.md`
  are public pages once merged. Nothing here is private, but it is worth knowing.

## 11. Release notes for whoever ships this

1. Cut the release from a build of this branch so that `job-search-assistant.zip` exists as a release
   asset **before** the site change goes live. The site and README link to
   `releases/latest/download/job-search-assistant.zip`, which is a 404 until then.
2. Bump the version in `plugin/plugin.json`, `plugin/.claude-plugin/plugin.json` and
   `.claude-plugin/marketplace.json`. This branch leaves them at 1.1.0.
3. Upload the bundle in each chat app and paste each install prompt in each coding agent, then replace
   "not yet" in `shared/hosts.md` with the date.
4. Run the triggering eval from §10.4 before telling existing users to switch to the bundle.
