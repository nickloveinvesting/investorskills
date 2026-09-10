# InvestorSkills

Forty-six AI workflow systems for real estate investors and wholesalers, and the
site that sells them. One repository.

- **Live:** https://nickloveinvesting.github.io/investorskills/
- **The catalog:** [`CATALOG.md`](CATALOG.md) · skills in [`skills/`](skills/) · bundles in [`packs/`](packs/)
- **The site:** [`index.html`](index.html) — one file, no build step

## The product

Each skill is a folder of markdown that installs into Claude, ChatGPT, Cursor, or
Claude Code and turns that model into a specialist for one step of a transaction.

The differentiator is refusal. A prompt answers whatever it is given, including
nothing. These declare their required inputs and halt without them, print every
default they applied, hold fixed decision thresholds so the same deal produces the
same verdict twice, and name the single input the deal is most sensitive to.

46 skills across 9 categories. 10 free, 36 paid. $27 a skill, $67 a strategy pack,
$197 for everything. One-time, no subscription.

Five are authored and shippable; `multifamily-underwriting` carries 15 reference
documents. The remaining 41 are scaffolded from `internal/catalog.json` —
`python3 internal/generate.py` rebuilds them and never touches a file marked
`status: authored`.

## The site

A single HTML file. **Every visual on it is inline SVG** — no image, no video, no
gradient, no shadow. Seven numbered plates, each inventing the chart form its own
question needs, after the 1900 W.E.B. Du Bois data portraits.

Plate IV is a working `max-offer-calculator` running the real deduction stack.
Leave the fields empty and it stamps INSUFFICIENT DATA across a sheet it refuses
to draw. Fill them and it draws the deduction band, prints a numbered ledger, runs
two sensitivity solves, and restates the pricing plate in terms of your deal.

Design system: [`DESIGN.md`](DESIGN.md). Product truth: [`PRODUCT.md`](PRODUCT.md).

```bash
python3 -m http.server 8000     # then open http://localhost:8000
```

Deploys to GitHub Pages on push to `main`.

## Licence

Proprietary — see [`LICENSE`](LICENSE). Plates drawn after W.E.B. Du Bois,
Paris 1900 (public domain).
