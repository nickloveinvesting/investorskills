#!/usr/bin/env python3
"""Generate repo scaffold from catalog.json. Safe to re-run: never overwrites
a SKILL.md whose body has been hand-authored (marked status: authored)."""
import json, os, re, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
CAT = json.load(open(ROOT / "internal" / "catalog.json"))
P = CAT["pricing"]

def price(s):
    return 0 if s["free"] else P["single"]

def frontmatter(s):
    cat = CAT["categories"][s["cat"]]
    personas = ", ".join(CAT["personas"][p] for p in s["personas"])
    trig = sorted(set(re.findall(r"[a-z]{4,}", s["name"].lower() + " " + s["slug"].replace("-", " "))))
    lines = [
        "---",
        f"name: {s['slug']}",
        "description: >",
        f"  {s['promise']}",
        f"  Use for: {personas}. Category: {cat}.",
        "triggers:",
    ]
    lines += [f"  - {t}" for t in trig[:10]]
    lines += [
        f"category: {s['cat']}",
        f"price_usd: {price(s)}",
        f"tier: {'free' if s['free'] else 'paid'}",
        "status: scaffold",
        "version: 0.1.0",
        "---",
    ]
    return "\n".join(lines)

SKELETON = """
# {name}

> {promise}

## Overview

{promise}

This skill is a workflow, not a prompt. It defines the sequence, the inputs it
refuses to proceed without, the decision rules, and the shape of the output.

## When to use this skill

- {p0}
- When you need a repeatable answer rather than a one-off opinion
- When the output has to be defensible to a lender, partner, or seller

## Inputs required

| Input | Required | Notes |
|---|---|---|
| _TBD_ | yes | |

## Workflow

### Step 1 - Intake and refusal check
_TBD: what must be present before the model does anything._

### Step 2 - Analysis
_TBD._

### Step 3 - Decision rules
_TBD._

### Step 4 - Output
_TBD._

## Output format

_TBD._

## Failure modes

_TBD: how this skill goes wrong and what it should do instead._

## Notes

Written for {personas}.
"""

README = """# {name}

{promise}

- **Category:** {cat}
- **Price:** {pricestr}
- **Built for:** {personas}

## Install

**Claude Projects** - add `SKILL.md` to project knowledge.
**Claude Code** - copy the folder into `.claude/skills/{slug}/`.
**ChatGPT** - paste `SKILL.md` into a Project's instructions.
**Cursor** - append `SKILL.md` to `.cursorrules`.

Full guide: [`docs/installation.md`](../../docs/installation.md)

## Files

| File | Purpose |
|---|---|
| `SKILL.md` | Core instructions |
| `README.md` | This file |
| `EXAMPLE.md` | One worked example, start to finish |
"""

EXAMPLE = """# {name} - Worked Example

## Scenario

_TBD: a concrete deal, with real numbers._

## Input given

_TBD._

## Output produced

_TBD._

## Why the output is right

_TBD: the reasoning a reviewer would check._
"""

def main():
    made = skipped = 0
    for s in CAT["skills"]:
        d = ROOT / "skills" / s["slug"]
        d.mkdir(parents=True, exist_ok=True)
        ctx = dict(
            name=s["name"], promise=s["promise"], slug=s["slug"],
            cat=CAT["categories"][s["cat"]],
            personas=", ".join(CAT["personas"][p] for p in s["personas"]),
            p0=f"When you are working a {CAT['personas'][s['personas'][0]].lower()} deal and need this step done consistently",
            pricestr="Free" if s["free"] else f"${P['single']}",
        )
        sk = d / "SKILL.md"
        if sk.exists() and "status: authored" in sk.read_text():
            skipped += 1
        else:
            sk.write_text(frontmatter(s) + SKELETON.format(**ctx))
            made += 1
        (d / "README.md").write_text(README.format(**ctx))
        if not (d / "EXAMPLE.md").exists():
            (d / "EXAMPLE.md").write_text(EXAMPLE.format(**ctx))

    # packs
    for p in CAT["packs"]:
        if p["persona"]:
            items = [s for s in CAT["skills"] if p["persona"] in s["personas"]]
        else:
            items = [s for s in CAT["skills"] if not s["free"]]
        paid = [s for s in items if not s["free"]]
        full = len(paid) * P["single"]
        pr = P["complete"] if p["persona"] is None else P["pack"]
        body = [f"# {p['name']}", "", f"**Price:** ${pr}  ",
                f"**Includes:** {len(paid)} paid skills" + (f" + {len(items)-len(paid)} free" if len(items)-len(paid) else "") + "  ",
                f"**Value if bought individually:** ${full}  ",
                f"**You save:** ${full - pr}", "", "## Included", ""]
        for s in sorted(items, key=lambda x: x["name"]):
            body.append(f"- **{s['name']}** - {s['promise']}")
        (ROOT / "packs" / f"{p['slug']}.md").write_text("\n".join(body) + "\n")

    print(f"skills scaffolded={made} preserved={skipped} packs={len(CAT['packs'])}")

if __name__ == "__main__":
    main()
