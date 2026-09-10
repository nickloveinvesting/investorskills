# PRODUCT.md — InvestorSkills

## What it is

A catalog of 46 AI workflow systems for real estate investors and wholesalers. Each
skill is a folder of markdown (`SKILL.md`, `README.md`, `EXAMPLE.md`, sometimes a
`references/` library) that installs into Claude, ChatGPT, Cursor, or Claude Code and
turns that model into a specialist for one step of a transaction.

Not a course. Not coaching. Not a CRM, a lead-list vendor, or a deal-analysis SaaS.

## Mechanism

The differentiator is **refusal**. A prompt answers whatever it is given, including
nothing. Every skill here declares its required inputs and halts without them, prints
every default it applied, holds fixed decision thresholds so the same deal produces
the same verdict twice, and names the single input the deal is most sensitive to.

The one-sentence version: *a number produced from a missing input is the most
expensive thing an AI can hand a real estate investor, and these skills would rather
stop than produce one.*

## Users and their scene

Five personas, each with its own catalog slice:

| Persona | Scene |
|---|---|
| Wholesaler | Working a list, on the phone, needs a verdict in under a minute |
| Fix-and-flipper | Standing in a house with a contractor, scoping and pricing |
| Small multifamily investor | 5-50 units, pre-1990s, reading a broker package that is built to flatter |
| Agent-investor | Licensed, invests on the side, needs deal flow without losing retail clients |
| First-deal investor | Has capital and no framework, working toward one close |

They are not designers or developers. They read spreadsheets, contracts, and MLS
printouts all day. Screen time is on a laptop at a desk or a phone in a truck.

## Catalog structure

- 46 skills across 9 categories: deal analysis, lead generation, seller negotiation,
  rehab scoping, disposition, funding, transaction ops, marketing, business systems
- 10 free, 36 paid
- 5 authored and shippable today; the flagship `multifamily-underwriting` carries 15
  reference documents (~800KB) and is deeper than most competing catalogs entire
- 41 scaffolded from `internal/catalog.json`; `internal/generate.py` rebuilds them
  and never touches a file marked `status: authored`

## Pricing

$27 per skill · $67 per persona pack · $197 for the complete toolkit (36 paid skills,
plus everything added later). One-time. No subscription. 10 skills free.
Individually the toolkit's skills total $972.

Chosen deliberately against the creator-tools convention of $7/$19/$49: a wholesaler
nets five figures on an assignment and reads $7 as a toy.

## Constraints that must survive any redesign

- **Market defaults are DFW Texas** because that is where the underlying deals were
  done. Every default must be stated in output so another market can override it.
- **No invented proof.** No testimonials, no customer counts, no case studies, no
  revenue claims. None exist yet. Real numbers only: 46 skills, 9 categories, 10
  free, 15 reference documents, the price ladder, the $972 comparison.
- **The live calculator must stay live.** The page ships a working
  `max-offer-calculator` running the real deduction stack. It is the proof.
- **Reduced motion is load-bearing.** A previous build shipped a hero that was
  entirely invisible under `prefers-reduced-motion`. Legibility may never depend on
  a reveal firing.
- **Accessibility:** WCAG AA contrast minimum on all text.

## Voice

Direct, forensic, unhyped. Short sentences. Specific numbers over adjectives. Never
coaching-speak, never hype, never exclamation. The product's own register is a
terminal printing a refusal, and the page should not be warmer than the product.

## Platform

`web`. Static, no framework, no build step. Deployed on GitHub Pages.

## Stack

Decided by the incumbent and confirmed for this rebuild: plain static HTML, CSS, and
vanilla JS in a single page, no build step. Deploy target is GitHub Pages, which
constrains it to files servable as-is.

## Brand commitments (user-pinned, this session)

- **Every visual is SVG.** No raster assets anywhere in the shipped page. No photos,
  no video, no generated imagery.
- **Parallax throughout.** Depth via differential motion is a required property of
  the page, not an effect applied to one section.
- **SVG used systematically, not illustratively** — as diagram, chart, measurement,
  and structural rule. The register is an instrument, not an environment.
- **One repository.** Site and catalog ship together, public.

## Open decisions

- Whether the `agent-investor` pack survives: it holds 3 paid skills against a $67
  price, so it saves the buyer $14. Needs more skills or removal.
- 41 of 46 skills are scaffolds. The catalog is real but not finished, and the page
  must not imply otherwise.
