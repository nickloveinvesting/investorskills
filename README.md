# InvestorSkills — scroll site

A scroll-driven landing page for [InvestorSkills](https://github.com/nickloveinvesting/investor-skills),
a catalog of 46 AI workflow systems for real estate investors and wholesalers.

**One page. Zero raster assets.** Every visual is inline SVG, CSS gradient, or type.
No images, no video, no build step. Two font families are the only external request.

---

## The signature move

Act 4 is a working `max-offer-calculator`, not a mockup. It runs the real deduction
stack from the skill it is selling — selling costs, holding, financing, purchase
closing, rehab, age-scaled contingency, profit — and converges the purchase price
iteratively, because purchase price appears on both sides of the equation.

Leave the fields empty and it refuses:

```
HALTED — required input missing.

Missing: ARV, rehab estimate

I will not return a maximum offer without these. A number produced from a
missing input is the most expensive failure this skill can have —
it looks exactly like a real answer.
```

That refusal is the pitch. Every other AI product page demonstrates output; this
one demonstrates the thing that actually separates a workflow from a prompt.

## Act score

Seven acts, eight device families, no family repeated in adjacent acts.

| # | Act | Act type | Families |
|---|---|---|---|
| 1 | Recognition | `flow` | parallax (4 planes), kinetic |
| 2 | The cost | `pin` | cue sequence |
| 3 | The mechanism | `flow` | reveal, staggered in |
| 4 | **The refusal** | `pin` | pointer, spotlight, live compute |
| 5 | The range | `pan` | lateral travel |
| 6 | The arithmetic | `flow` | count |
| 7 | Commitment | `pin` | magnet |

No `scrub` act: there is no footage, and a generated flythrough would have been
exactly the clay-diorama failure the engine's own guidance warns against.

Full reasoning, feeling curve, and peak definition: [`BRIEF.md`](BRIEF.md).

## Verification

Rendered in headless Chromium at 1440×900, 390×844, and with
`prefers-reduced-motion: reduce`, sampled at every act midpoint:

| Check | Desktop | Mobile | Reduced motion |
|---|---|---|---|
| Acts rendering content | 7 / 7 | 7 / 7 | 7 / 7 |
| Horizontal overflow | none | none | none |
| JS errors | none | none | none |
| Document length | 11,727px | 12,004px | 11,727px |

Frames in [`docs/shots/`](docs/shots/).

## Design floor

| Token | Value | Contrast on canvas |
|---|---|---|
| `--sc-canvas` | `#0a0b0d` | — |
| `--sc-ink` | `#f2efe9` | 17.4:1 |
| `--sc-ink-soft` | `#8b8e96` | 5.9:1 (AA body) |
| `--sc-accent` | `#dfa94a` | 9.2:1 |

Fraunces for display, Inter for text, JetBrains Mono for anything numeric.
Fluid type via `clamp()`, 8-point spacing, 62ch measure on body copy.

## Run it

```bash
python3 -m http.server 8000
```

Then open `http://localhost:8000`. There is nothing to install and nothing to compile.

Deploys to GitHub Pages automatically on push to `main`
(see [`.github/workflows/pages.yml`](.github/workflows/pages.yml)).

## Credits

Built with [scroll-craft](https://github.com/nateherk/scroll-craft) by Nate Herk.
`scrollcraft.js` and `scrollcraft.css` are unmodified engine files, MIT licensed —
see [`ENGINE-LICENSE`](ENGINE-LICENSE). Page design, copy, SVG artwork, and the
calculator are original.

## Licence

Page content and design: © 2026 Nick Love. All rights reserved.
Engine: MIT, Nate Herk.
