---
version: 1
slug: "index-html"
primary_target: "index.html"
related_targets: []
---

## Scope

`index.html` — the single public surface for InvestorSkills. Visitor mode: **Persuade**.

Audience: wholesalers, fix-and-flippers, small multifamily investors, agent-investors,
first-deal investors. Job: decide whether these skills are worth $27–$197.
Action: take the free ten, or buy the toolkit.
Proof available: 46 skills, 9 categories, 10 free, 15 reference documents on the
flagship, the price ladder, the $972 individual-purchase comparison, and the live
max-offer calculator. No testimonials, no customer counts — none exist.

## Direction contract

**THESIS.** Every number on this page is a drawn quantity, and the one number the
product will not draw is the one it lacks an input for. The page refuses the dark
proptech product page and refuses the warm scrolly-telling landing page equally:
this is a bound set of statistical plates, and the visitor reads it the way an
underwriter reads a comp package.

**OWN-WORLD.** The 1900 Du Bois data portraits. Aged board ground; flat saturated
crimson, gold, emerald and ink laid down without gradient, halo, or shadow; hairline
crimson rules banding the sheet; heavy condensed display caps against small tracked
caption caps. Every chart invents the form its question needs — coiled spiral, wrapped
bar, stepped square grid, area block — and no two plates share a form. All geometry is
inline SVG. Depth is the plate's own colour separations: rule grid, ink geometry, and
lettering ride at different rates, so the plate assembles as you descend it.

**STORY.** The visitor understands that a general model answers every question
including the ones it has no data for; believes that a workflow which halts is worth
more than one which guesses; and takes the free ten or the $197 toolkit.

**FIRST VIEWPORT.** Board ground. Left two-thirds: the wordmark block over a
three-line condensed headline at display scale, a two-line statement beneath it, and
the primary action as a filled crimson block beside a gold-ruled secondary. Right
third: PLATE I, a coiled spiral of 46 arc segments banded by category, drawn in the
four inks — the catalog as one object. Under both, a full-width plate index in
hand-lettered caps with a drawn glyph per plate, which is the page's navigation.
No image, no gradient, nothing soft.

**FORM.** Du Bois data portraits, challenger card, chosen by the user over the
assigned direction (The Settlement Statement) and over Impeccable's pick (The
Appraisal Comp Grid). Seed key 51a9f55c, direction scope, persuade mode, assigned
index 4. Raise carried in from the variable-font specimen challenger: one control
drives the whole surface — the ARV field remaps every drawn quantity on the page
live. Raise carried in from the settlement statement: every deduction is a named,
numbered line, nothing bundled into a percentage.

**FINISH.** unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance

## Constraints

- Every visual is SVG. No raster in the shipped page.
- Parallax is a required property of the page, not a section effect.
- Legibility may never depend on a reveal firing (a prior build shipped an
  invisible hero under `prefers-reduced-motion`).
- No invented proof of any kind.
- Static HTML/CSS/JS, no build step, GitHub Pages.

## Unresolved

- `agent-investor` pack holds 3 paid skills at $67; saves the buyer $14. Fix or cut.
- 41 of 46 skills are scaffolds; the page must not imply a finished catalog.
