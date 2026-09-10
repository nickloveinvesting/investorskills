# CreatorSkills Architecture Blueprint

Structural teardown of creatorskills.co, reduced to the reusable mechanics.
No source copy is reproduced here. Everything below is structure, taxonomy, and
commercial logic, which is not protectable.

Captured: 2026-09-10. Site last modified 2026-08-31. Site launched ~2026-02-26.

---

## 1. Site skeleton (447 indexed URLs)

| Segment | Count | Job |
|---|---|---|
| `/blog/*` | 220 | Programmatic SEO surface. One post per skill plus category round-ups. |
| `/skills/*` | 94 | Product detail pages. The money pages. |
| `/create/*` | 56 | Free interactive applet per skill. Top-of-funnel + product demo. |
| `/tags/*` | 28 | Faceted browse. Internal link mesh. |
| `/categories/*` | 14 | Primary taxonomy browse. |
| `/packs/*` | 10 | Bundles. The real conversion unit. |
| `/workflows/*` | 6 | Persona hubs. Entry point per buyer type. |
| `/platforms/*`, `/platform/*` | 7 | Compatibility landing pages (Claude, ChatGPT, Cursor, Claude Code). |
| `/docs/*` | 2 | Install guide. Reduces refund risk. |
| `/llms.txt`, `/llms-full.txt` | 2 | AI-search visibility layer. |
| Legal, about, pricing, free, for-developers | 6 | Trust and conversion support. |

The ratio is the lesson: **2.3 blog posts per product, and a free applet for 60% of the catalog.**
Content is not a side channel here. It is the entire acquisition engine.

---

## 2. Price ladder

Three rungs, one-time only, no subscription.

- **$7** — single skill
- **$19** — themed pack, 5 to 28 skills
- **$49** — complete catalog, 51 paid skills, includes future additions

Mechanics worth copying:

1. **Anchor by count, not by value.** Every pack shows "save $107" computed as
   (skills x $7) minus $19. The discount is manufactured by the unit price.
2. **The pack upsell sits on the product page**, below the buy button, showing the
   same skill inside a pack for the same or lower effective cost. The $7 SKU
   exists mainly to make $19 look free.
3. **Free tier is 17 skills**, browsable by bottleneck. Free is a catalog slice,
   not a stripped sample.
4. **Lifetime + future updates** on the top rung. Removes the "will this go stale"
   objection at the exact moment it fires.

---

## 3. Product page template

Fixed section order on every `/skills/*` page:

1. H1 name + one-line outcome promise
2. Trust strip: maker, hours-saved-per-month figure, last-updated date, category, platform badges, pack membership
3. About this Skill (expanded promise)
4. Tags
5. Who this is for (3 bullets, each a buyer self-identification statement)
6. Purchase-proof line ("one of N skills bought together in a single bundle checkout, DATE")
7. Founder pull-quote on why the skill exists
8. What's Included (file manifest, typically 3 files: SKILL.md, README.md, EXAMPLE.md)
9. What You Get (3 reassurance tiles: quick install, made by practitioners, pay once)
10. How to Install
11. Pack upsell block with savings math
12. Skill Preview (partial SKILL.md, System Role section only)
13. Popular Skills / Platforms / Resources
14. Reviews + refund guarantee
15. FAQ (6 questions, identical across pages)
16. Works Great With (cross-sell)
17. Background reading (links to 5-6 blog posts)

Sections 6, 7 and 12 are the differentiators. Preview builds confidence,
the founder quote supplies a human, the purchase-proof line manufactures
social proof without needing reviews.

---

## 4. Delivery format

Each product is a small folder of markdown, not an app:

```
skill-name/
  SKILL.md      # core instructions, YAML frontmatter + body
  README.md     # install and usage
  EXAMPLE.md    # one worked example end to end
```

Install paths marketed per platform: Claude Projects, ChatGPT Custom
Instructions, Cursor `.cursorrules`, Claude Code `CLAUDE.md`. Same files,
four framings. This is a positioning move, not an engineering one.

---

## 5. Taxonomy

**14 categories:** analytics-optimization, community-engagement,
content-repurposing, course-creation, email-newsletter, freelance-client,
image-generation-thumbnails, podcasting, product-creation, scripts-outlines,
sponsor-brand-deals, titles-thumbnails, other.

**5 persona workflow hubs:** YouTube creator, streamer, newsletter creator,
course creator, freelancer. Each hub prescribes a canonical path:
land on hub -> compare one named pack against two named individual skills.
That is a scripted buyer journey, not a browse page.

**28 tags** for faceting. Heaviest: youtube (16), monetization (8),
analytics (8), podcast (7), linkedin (7).

---

## 6. AI-search layer

`llms.txt` (46KB) and `llms-full.txt` (86KB) are the most deliberate thing on
the site. Contents:

- Entity declaration (name, domain, founder, category)
- "Best starting points" with an explicit reason to pick each
- Full catalog with price and tags per item, inline
- Every pack with its complete skill manifest
- **Brand disambiguation** ("we are NOT creator.co")
- **Named competitor comparisons** (PromptBase, God of Prompt, awesomeskill.ai, Custom GPTs)
- FAQ block written as clean question/answer pairs

This is written to be quoted by an LLM verbatim. The disambiguation and
comparison blocks exist so that a model answering "best AI skills marketplace"
has pre-chewed differentiation to repeat.

---

## 7. Blog pattern

Two repeating templates:

- **`{skill-name}-skill-guide-2026`** — one per product, 60+ instances. Bottom-of-funnel, converts search for the exact tool.
- **`best-ai-{thing}-for-{persona}-2026` / `top-10-{x}`** — category round-ups that list its own products. Top-of-funnel, captures comparison intent.

Year is hardcoded in the slug. Cheap freshness signal, annual rewrite cost.

---

## 8. Cracks in the execution

Reusable as a checklist of what to do better.

1. **Counts contradict across pages.** Homepage says 89+, llms.txt says 80+, pricing says 51 in the toolkit, sitemap has 94 skill URLs. Reads as generated, not maintained.
2. **Refund terms contradict.** Pricing page says 7-day. Product pages say 30-day. That is a real liability, not a typo.
3. **Social proof is nearly absent.** One product carries one rating. The synthetic "bought together in a bundle checkout" line is doing all the work.
4. **The GitHub repo cited in llms-full.txt returns 404.** A dead citation inside the file built specifically to be trusted by AI crawlers.
5. **No seller side.** It calls itself a marketplace but is single-vendor, so no supply flywheel and no catalog growth beyond one person's output.
6. **Depth is thin.** Products are single-file prompt systems dressed as workflows. Nothing carries a reference library.

---

## 9. What transfers to a real estate catalog

Copy: the three-rung ladder, the pack-savings math, the product page section
order, the free tier as catalog slice, the persona hub with a scripted path,
`llms.txt` with disambiguation and named comparisons, one blog post per product.

Do not copy: the $7 price point (calibrated to creators, not investors),
the single-file shallowness, the fake-count sloppiness, the absent seller side.
