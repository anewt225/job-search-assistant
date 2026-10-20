#!/usr/bin/env python3
"""
make_todos.py — turn a LinkedIn Rehab action plan into portable task lists.

Input:  a JSON action plan (see actions.schema.json / --example)
Output: generic.csv, todoist.csv, asana.csv, ticktick.csv, tasks.md, tasks.json

    python3 make_todos.py actions.json -o ./out
    python3 make_todos.py --example > actions.json

No third-party dependencies. Python 3.8+.
"""

import argparse
import datetime as _dt
import csv
import json
import os
import sys
from datetime import date, timedelta

# --- priority mapping -------------------------------------------------------
# Internal scale is 1 (highest) .. 4 (lowest), matching Todoist's CSV values.
PRIORITY_LABEL = {1: "Critical", 2: "High", 3: "Medium", 4: "Low"}
CRITICALITY_TO_PRIORITY = {"critical": 1, "high": 2, "medium": 3, "low": 4}

EXAMPLE = {
    "profile": "Example Candidate",
    "target_role": "Strategy & Operations",
    "generated": "2026-07-30",
    "composite_before": 59,
    "composite_projected": 79,
    "actions": [
        {
            "title": "Turn on Open to Work (recruiters only)",
            "notes": "Profile > Open to > Finding a new job. Add 5 target titles and 4 locations.",
            "criterion": "A5",
            "points": 4.0,
            "minutes": 2,
            "criticality": "critical",
        },
        {
            "title": "Publish rewritten About section",
            "notes": "Use the billboard variant chosen in the report. 25-minute timer; save when it beeps.",
            "criterion": "B1,B2",
            "points": 8.75,
            "minutes": 25,
            "criticality": "critical",
        },
        {
            "title": "Add bullets to current role",
            "notes": "Paste the top 4 resume bullets. Do not wordsmith.",
            "criterion": "B3,C1",
            "points": 7.5,
            "minutes": 15,
            "criticality": "critical",
        },
    ],
}


def compute_schedule(actions, start=None, per_day_minutes=45):
    """Assign due dates by packing actions into ~45-minute daily blocks."""
    start = start or date.today()
    day_offset, used = 0, 0
    for a in actions:
        mins = int(a.get("minutes", 15))
        if used and used + mins > per_day_minutes:
            day_offset += 1
            used = 0
        used += mins
        a["_due"] = start + timedelta(days=day_offset)
    return actions


def roi(a):
    """Points recovered per minute — the ranking that actually matters."""
    mins = max(int(a.get("minutes", 15)), 1)
    return float(a.get("points", 0)) / mins


def prepare(plan, start=None):
    actions = list(plan.get("actions", []))
    for a in actions:
        a["_priority"] = CRITICALITY_TO_PRIORITY.get(
            str(a.get("criticality", "medium")).lower(), 3
        )
        a["_roi"] = roi(a)
    # Critical first, then best points-per-minute.
    actions.sort(key=lambda a: (a["_priority"], -a["_roi"]))
    return compute_schedule(actions, start)


# --- writers ----------------------------------------------------------------

def write_generic(actions, plan, path):
    """Widely compatible. Imports into Notion, ClickUp, Airtable, Sheets, Excel,
    Monday, and most trackers that accept an arbitrary CSV."""
    cols = ["Task", "Notes", "Priority", "Due Date", "Estimate (min)",
            "Section", "Status", "Tags"]
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(cols)
        for a in actions:
            w.writerow([
                a["title"],
                a.get("notes", ""),
                PRIORITY_LABEL[a["_priority"]],
                a["_due"].isoformat(),               # YYYY-MM-DD
                a.get("minutes", ""),
                "LinkedIn Rehab",
                "Not started",
                f"linkedin,{a.get('criterion','')}",
            ])


def write_todoist(actions, plan, path):
    """Todoist's importer is strict: exact header, lowercase 'task' in TYPE,
    priority 1 (highest) .. 4 (lowest)."""
    cols = ["TYPE", "CONTENT", "DESCRIPTION", "PRIORITY", "INDENT", "AUTHOR",
            "RESPONSIBLE", "DATE", "DATE_LANG", "TIMEZONE"]
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(cols)
        for a in actions:
            w.writerow([
                "task",
                a["title"],
                a.get("notes", ""),
                a["_priority"],
                1, "", "",
                a["_due"].isoformat(),
                "en", "",
            ])
        # Trailing blank row keeps Todoist from swallowing the final task.
        w.writerow(["", "", "", "", "", "", "", "", "", ""])


def write_ticktick(actions, plan, path):
    """TickTick CSV importer.

    Two hard constraints, both learned the painful way:

    1. TickTick expects six header lines of metadata before the column row. Without
       them the importer silently produces an empty list rather than an error.
    2. Tasks are written FLAT - no parent/child nesting. Subtasks do not survive a
       Notion<->TickTick sync, so a nested plan silently loses its children on the
       next sync. Phase is carried in the folder/list column instead.

    Priority: 5 = high, 3 = medium, 1 = low, 0 = none.
    """
    tt_priority = {1: 5, 2: 3, 3: 1, 4: 0}
    with open(path, "w", newline="", encoding="utf-8") as f:
        f.write('"Date": %s\n' % _dt.date.today().isoformat())
        f.write('"Version": "6.1"\n')
        f.write('"Status": "0 Normal 1 Completed 2 Archived"\n')
        f.write('"Kind": "TASK"\n')
        f.write('"Timezone": "America/New_York"\n')
        f.write('\n')
        w = csv.writer(f)
        w.writerow(["Folder Name", "List Name", "Title", "Kind", "Tags",
                    "Content", "Is Check list", "Start Date", "Due Date",
                    "Reminder", "Repeat", "Priority", "Status",
                    "Created Time", "Completed Time", "Order", "Timezone",
                    "Is All Day", "Is Floating", "Column Name", "Column Order",
                    "View Mode", "taskId", "parentId"])
        for i, a in enumerate(actions):
            due = a["_due"].isoformat() + "T09:00:00+0000"
            w.writerow([
                "Job Search",
                "LinkedIn Rehab",
                a["title"],
                "TEXT",
                "linkedin,%s" % a.get("criterion", ""),
                a.get("notes", ""),
                "N",                      # never a checklist - keep it flat
                "", due, "", "",
                tt_priority.get(a["_priority"], 0),
                "0",
                "", "", -i, "America/New_York",
                "false", "false", "", "", "list", "", "",   # parentId always blank
            ])


def write_asana(actions, plan, path):
    """Asana CSV importer. Dates must be month/day/year."""
    cols = ["Name", "Notes", "Due Date", "Section/Column", "Priority", "Tags"]
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(cols)
        for a in actions:
            w.writerow([
                a["title"],
                a.get("notes", ""),
                a["_due"].strftime("%m/%d/%Y"),      # Asana wants MM/DD/YYYY
                "LinkedIn Rehab",
                PRIORITY_LABEL[a["_priority"]],
                f"linkedin {a.get('criterion','')}".strip(),
            ])


def write_markdown(actions, plan, path):
    """Fallback that works everywhere: Obsidian, Bear, GitHub, TickTick,
    Apple Reminders (paste), Google Tasks (paste)."""
    total_pts = sum(float(a.get("points", 0)) for a in actions)
    total_min = sum(int(a.get("minutes", 0)) for a in actions)
    lines = [
        f"# LinkedIn Rehab — Action Plan",
        "",
        f"**Target role:** {plan.get('target_role','—')}  ",
        f"**Generated:** {plan.get('generated','—')}  ",
        f"**Score:** {plan.get('composite_before','—')} → "
        f"{plan.get('composite_projected','—')} projected  ",
        f"**Total effort:** {total_min} min for {total_pts:.1f} points",
        "",
        "Ordered by criticality, then by points recovered per minute.",
        "",
    ]
    current = None
    for a in actions:
        band = PRIORITY_LABEL[a["_priority"]]
        if band != current:
            lines += ["", f"## {band}", ""]
            current = band
        pts = float(a.get("points", 0))
        lines.append(
            f"- [ ] **{a['title']}** "
            f"`{a.get('minutes','?')} min` `+{pts:.1f} pts` "
            f"`{a.get('criterion','')}` — due {a['_due'].isoformat()}"
        )
        if a.get("notes"):
            lines.append(f"  - {a['notes']}")
    lines += ["", "---", "",
              "*Stop rule: when the timer ends, close LinkedIn and go do outreach. "
              "The profile isn't the goal — the conversations it enables are.*", ""]
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def write_json(actions, plan, path):
    out = dict(plan)
    out["actions"] = [
        {k: v for k, v in a.items() if not k.startswith("_")} | {
            "priority": a["_priority"],
            "due": a["_due"].isoformat(),
            "points_per_minute": round(a["_roi"], 3),
        }
        for a in actions
    ]
    with open(path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)


WRITERS = [
    ("generic.csv", write_generic),
    ("todoist.csv", write_todoist),
    ("asana.csv", write_asana),
    ("ticktick.csv", write_ticktick),
    ("tasks.md", write_markdown),
    ("tasks.json", write_json),
]


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("plan", nargs="?", help="Path to the action-plan JSON")
    p.add_argument("-o", "--out", default=".", help="Output directory")
    p.add_argument("--start", help="First due date, YYYY-MM-DD (default: today)")
    p.add_argument("--example", action="store_true",
                   help="Print an example action-plan JSON and exit")
    args = p.parse_args()

    if args.example:
        print(json.dumps(EXAMPLE, indent=2))
        return 0
    if not args.plan:
        p.error("provide a plan file, or use --example")

    with open(args.plan, encoding="utf-8") as f:
        plan = json.load(f)

    if not plan.get("actions"):
        print("error: plan contains no actions", file=sys.stderr)
        return 1

    start = date.fromisoformat(args.start) if args.start else None
    actions = prepare(plan, start)

    os.makedirs(args.out, exist_ok=True)
    for name, fn in WRITERS:
        fn(actions, plan, os.path.join(args.out, name))
        print(f"wrote {os.path.join(args.out, name)}")

    print(f"\n{len(actions)} actions | "
          f"{sum(int(a.get('minutes',0)) for a in actions)} min | "
          f"{sum(float(a.get('points',0)) for a in actions):.1f} pts recoverable")
    return 0


if __name__ == "__main__":
    sys.exit(main())
