# Data Schema — minimal job-search tracker

Five tables, ≤12 fields each. Same names in every backend so modules read/write without translation.
**Required** fields are bold; everything else is optional. Relations become a name/ID text column in
spreadsheets/CSV.

## Companies
| Field | Type | Notes |
|---|---|---|
| **Name** | title | |
| Website | url | careers page if possible |
| Industry | select | |
| Priority | select | High · Medium · Low · Paused |
| LAMP-A (Advocacy) | number 0–3 | 0 none · 1 2nd-degree · 2 alum/affinity · 3 1st-degree contact |
| LAMP-M (Motivation) | number 1–3 | |
| LAMP-P (Posting) | number 0–3 | 0 none · 1 adjacent · 2 relevant · 3 ideal |
| LAMP Score | formula | A×100 + M×10 + P — sort descending (Dalton) |
| Notes | text | |
| Contacts / Opportunities | relation | back-links |

## Contacts
| Field | Type | Notes |
|---|---|---|
| **Name** | title | |
| **Company** | relation | |
| Title | text | |
| Email | email | only attested addresses — never guessed |
| LinkedIn | url | |
| **Status** | select | New lead · Contacted · Scheduled · Talked · Nurture · Dormant |
| Warmth | select | Warm · Lukewarm · Cold |
| Segment | select | Booster · Obligate · Curmudgeon · Unknown (Dalton) |
| Source | select | Event · Referral · LinkedIn · Alumni · Former colleague · Cold |
| Last Contact | date | |
| Next Follow-up | date | |
| Notes | text | hooks, "Met at: <event> (<date>)", what they said |
| Opportunities / Meetings | relation | back-links |

## Opportunities
| Field | Type | Notes |
|---|---|---|
| **Role** | title | |
| **Company** | relation | |
| **Status** | select | Interested · Applied · Screening · Interviewing · Offer · Won · Lost · Withdrawn |
| Priority | select | High · Medium · Low |
| Fit | number 1–5 | |
| Posting URL | url | |
| Date Applied | date | |
| Human attached | relation → Contacts | referrer / hiring manager / recruiter |
| Comp range | text | |
| Next Step | text | |
| Next Step Date | date | |
| Notes | text | |

## Meetings  (informationals, networking events, screens, interviews — one table)
| Field | Type | Notes |
|---|---|---|
| **Title** | title | `[Type] — <Person/Event> — <Company>` |
| **Type** | select | Informational · Event · Recruiter screen · Interview · Follow-up |
| **Date** | date | |
| Live? | checkbox | counts toward the weekly conversation metric only if live (call/video/in person) |
| Contacts | relation | |
| Opportunity | relation | |
| Status | select | Scheduled · Prepped · Done · Thank-you sent |
| Self-rating | number 1–5 | |
| Notes / transcript | url | |
| Lessons learned | text | |
| Next steps | text | |

## Tasks  (skip if the user has a task app)
| Field | Type | Notes |
|---|---|---|
| **Task** | title | verb-first |
| **Status** | select | To do · Doing · Done · Dropped |
| Due | date | |
| Priority | select | High · Medium · Low |
| Category | select | Networking · Applications · Interview prep · Brand · Admin |
| Contact | relation | |
| Opportunity | relation | |

Flat tasks only — many task apps don't sync subtasks.

---

## Import / merge (BYO data)

Accept: Google Sheets, Excel/CSV, Notion DB or template, Airtable base/CSV export, Obsidian (Bases or
folder of notes with frontmatter), LinkedIn `Connections.csv`, pasted tables.

1. **Profile the source** — list its columns/properties + row count. Never read more than ~50 rows
   inline; for big files (e.g. Connections.csv) filter with code first.
2. **Propose a mapping** source → schema field, as a table. Unmapped source fields → `Notes` (or keep
   as extra columns if the user wants). Missing required fields → ask once for a default.
3. **Dedupe** on Name + Company (contacts), Role + Company (opportunities). Show conflicts; never
   overwrite silently.
4. **Confirm, then write** in batches. Report counts written / skipped / conflicts.
5. If the user keeps their own schema, record the field-name overrides in profile §5 instead of
   migrating.

## Backend notes
- **Notion** — create a parent page "Job Search", 5 databases with the relations above. Or duplicate
  the published template (link in README) — fastest, no tokens spent building.
- **Google Sheets / Excel** — one workbook, one tab per table, header row = field names.
- **Airtable** — one base, five tables; linked-record fields for relations.
- **CSV folder / Obsidian** — `companies.csv` … or one note per record with YAML frontmatter using the
  field names; relations as `[[wikilinks]]`.
