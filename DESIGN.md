# DESIGN.md — InvestorSkills

Written at finish, from the built page. The world is the 1900 Du Bois data
portraits, chosen by the user over the assigned direction (The Settlement
Statement) and over the appraisal comp grid. Seed key `51a9f55c`.

Everything drawn on this page is inline SVG. There is no raster asset, no photo,
no video, no gradient, no shadow, and no blur anywhere in the shipped file.

---

## Ground and inks

Flat, hand-laid colour. Nothing is tinted, faded, or softened; a field is either
the ink or it is the board.

| Token | Value | Role | Contrast on board |
|---|---|---|---|
| `--board` | `#EBDCC4` | aged board, the page ground | — |
| `--board-deep` | `#E0CDAE` | banded rows, sunk panels | — |
| `--ink` | `#17130E` | body, display, the ninth category | 13.8:1 |
| `--crimson` | `#B3242A` | rules, refusal, primary action, first category | 6.1:1 |
| `--gold` | `#C98A12` | second category, secondary action, rehab lines | 3.6:1 |
| `--emerald` | `#1C5B44` | third category, drawn/valid state, free skills | 6.0:1 |
| `--indigo` | `#2C5480` | fourth category | 5.4:1 |

**Gold is a fill and a large-type colour only.** At 3.6:1 it clears AA for large
text and UI but not for body, and it is never used for body copy.

**Nine categories from four inks.** The plates extend a limited palette with
hatch rather than with new hues. Categories 1–4 are solid, 5–8 are the same four
inks at 45° hatch over board, and the ninth is ink. Any future category takes a
hatch variant, never a new colour.

## Faces

Both self-hosted as variable woff2 in `fonts/`. There is no external font
request, and no system face is used as a display voice.

| Face | Files | Role |
|---|---|---|
| Big Shoulders Display | `fonts/bsd-latin.woff2`, `-latinext` | all headings, every figure, the drawn numerals inside SVG |
| Public Sans | `fonts/ps-latin.woff2`, `-latinext` | body, captions, controls, the register |

Headings: 900 weight, uppercase, `line-height:.92`, `letter-spacing:.004em`.
Body: 1.62 leading, measure capped at 68ch, `.lede` at 58ch.
Every numeral on the page is tabular; `font-variant-numeric:tabular-nums` is set
on `body`, so figures never jitter when the assay redraws.

**Caps are for labels, not for sentences.** `.cap` is a label voice at .73rem
with .17em tracking. Anything that reads as a sentence is sentence case at .86–.9rem.
The only uppercase running text is `.claim`, a display statement held to 16ch.

**11px floor.** No functional text — link, button, label, table cell, or caption —
renders below 11px at any breakpoint.

## Plates

Seven numbered plates. The number is not decoration: it is the wayfinding the
page is built on, and it appears in the masthead index, in each plate head, and
in the ledger line numbers.

| Plate | Question | Form it invents |
|---|---|---|
| I | What is the catalog? | A coiled ribbon of 46 arc segments, banded by category, that unrolls into bars |
| II | What does one bad number cost? | Two squares drawn to area, $197 against $24,000 |
| III | Prompt or skill? | Wrapped bars — one breaks and restarts, one runs long enough to wrap |
| IV | Will it answer? | The plate that cannot be drawn |
| V | What is in it? | A ruled register of all 46, filterable from the key |
| VI | What does it cost? | Three tier bars against the $972 reference |
| VII | What now? | One action |

No two plates share a form. That is the rule the world is built on, and it is
what replaced the same-size-card scaffold this page used before.

## Motion

**Parallax is the plate's own colour separations.** Three planes travel at
different rates through each plate's passage across the viewport: the rule bed at
+54px, the ink geometry at −20px, the lettering at −6px. The effect is a plate
assembling from its separations as you descend it, and it is a property of every
plate rather than an effect on one.

Reveal is **position-checked, never observer-gated**. Elements carry `.rv`, and a
scroll sweep adds `.in` once the element passes 94% of the viewport height. An
earlier build of this site shipped a hero that was invisible under
`prefers-reduced-motion` because a callback never fired; the sweep, the
already-visible `.rv` default, and a `try/catch` that unhides everything on a
boot error close that failure class three ways.

Under `prefers-reduced-motion: reduce`: every plane is pinned, every reveal is
resolved, and scroll behaviour is instant. Nothing is hidden.

## The signature interaction

Two fields in Plate IV drive the whole surface. Empty, the plate refuses to draw
and stamps INSUFFICIENT DATA across an unruled sheet. Filled, it draws the
deduction band, prints the numbered ledger (100 / 201–204 / 301–302 / 401 / 1400),
runs two sensitivity solves, names the input the deal is most sensitive to — and
restates Plate VI's claim in terms of the deal the visitor just typed.

The calculator is the real deduction stack from `max-offer-calculator`, converged
iteratively because purchase price appears on both sides. It is not a mock.

## Browser surfaces

Themed from the palette, not left to the browser: selection (crimson on board),
caret (crimson in the assay fields), scrollbar (crimson thumb on deep board),
focus ring (3px crimson, 3px offset), underline offset, and tabular numerals.

## Known remainder

The mechanical detector reports 11 `cramped-padding` findings against
`.grid-bed`, the decorative rule layer behind each plate. It is `aria-hidden`,
`pointer-events:none`, and bears no text; ruled board running edge to edge is the
artifact being drawn. Two `tight-leading` and three `all-caps-body` findings
remain against `.claim`, the uppercase display statement, held to 16 characters
per line at 1.14 leading. Both are the committed world overriding the general
floor, and both are deliberate.

## What must not drift

- Every visual stays SVG. A raster asset entering this page breaks the world.
- No gradient, no shadow, no blur, no rounded corner. Flat ink or board.
- No two plates share a chart form.
- Gold never carries body text.
- Legibility never depends on a reveal firing.
- No invented proof. Real figures only: 46, 9, 10 free, 5 authored, 15 reference
  documents, $27/$67/$197, $972.
