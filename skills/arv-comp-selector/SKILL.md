---
name: arv-comp-selector
description: >
  Turn a raw comp pull into a defensible after-repair value with every adjustment
  shown, every rejected comp explained, and a confidence band instead of a single
  false-precision number. Use for: Fix-and-Flipper, Wholesaler, First-Deal Investor.
  Category: Deal Analysis & Underwriting.
triggers:
  - ARV
  - after repair value
  - comps
  - comparable sales
  - what is this worth
  - comp analysis
  - appraisal estimate
category: deal-analysis
price_usd: 27
tier: paid
status: authored
version: 1.0.0
---

# ARV & Comp Selector

> Turn a raw comp pull into a defensible ARV with every adjustment shown and every bad comp thrown out on the record.

## Overview

ARV is the input every other number depends on. A 5% ARV error moves the max offer
by more than a 20% rehab error. Most investors spend an hour on rehab and four
minutes on ARV.

The failure is rarely arithmetic. It is comp selection. Pull twelve sales, keep the
six that support the number you want, and the math is flawless and the answer is
wrong. This skill forces rejection to be explicit, so the bias has to happen where
you can see it.

## When to use this skill

- Before computing a max offer on any residential deal
- When an appraisal came in low and you need to know whether to dispute
- When a wholesaler's ARV claim needs verification
- When two comps disagree and you need a defensible tiebreak

## Inputs required

| Input | Required | If missing |
|---|---|---|
| Subject address | yes | Stop. |
| Subject beds/baths/sqft/year built/lot | yes | Stop. These drive every adjustment. |
| Comp list with sale price, date, and same attributes | yes | Stop. Do not estimate from Zestimate or list prices. |
| Subject's post-rehab condition target | yes | Ask: rent-ready, retail-standard, or high-finish. |
| Photos of comps | no | Improves condition adjustment confidence |

**Refusal rule:** never produce an ARV from list prices, pending sales, or
automated valuation estimates alone. Closed sales only. If the user supplies only
actives, say what the number would be worth and ask for closed data.

## Workflow

### Step 1 - Qualify each comp

Score every comp against the subject. A comp must pass all five to be included.

| Test | Standard | Loosen only if |
|---|---|---|
| Distance | within 0.5 mi | rural, then 1.0 mi |
| Recency | closed within 90 days | slow market, then 180 days with a market adjustment |
| Size | within 20% of subject sqft | fewer than 4 comps qualify |
| Type | same story count, same beds +/- 1 | never loosen bed count by more than 1 |
| Boundary | same school attendance zone and no crossing of a major arterial, rail line, or subdivision boundary | never loosen |

The boundary test is the one most often skipped and the one that most often
explains a bad number. Two houses 0.3 miles apart on opposite sides of a highway
are not comparable.

### Step 2 - Reject explicitly

For every rejected comp, record the comp and the single test it failed. This list
appears in the output. It is the difference between an ARV and an opinion.

If fewer than three comps survive, say so. Report the number as low confidence and
name what additional data would fix it. Do not loosen every standard at once to
manufacture a fifth comp.

### Step 3 - Adjust

Adjust each surviving comp toward the subject. Direction: if the comp is superior,
adjust the comp's price **down**.

Default adjustment values, DFW residential. State them in the output and let the
user override.

| Feature | Adjustment |
|---|---|
| Living area | $65/sqft of difference |
| Full bath | $6,000 |
| Half bath | $3,500 |
| Garage bay | $7,500 |
| Lot size | $2.00/sqft of difference, capped at $15,000 |
| Pool | $18,000 |
| Age | $500 per year of difference, capped at $12,000 |
| Condition vs. subject's target | see below |
| Market movement | monthly appreciation rate x months since close |

**Condition adjustment.** Compare each comp's condition at sale to the subject's
post-rehab target, not to its current state.
- Comp sold in similar finish to target: $0
- Comp sold one tier below target (e.g. rent-ready vs retail): +4% of comp price
- Comp sold one tier above: -4%
- Comp sold as a distressed or as-is sale: exclude entirely, it is not a retail comp

**Adjustment cap.** If total gross adjustments on a comp exceed 15% of its sale
price, the comp is too dissimilar. Drop it and note why. A heavily adjusted comp is
a guess wearing a table.

### Step 4 - Reconcile

Do not average. Weight.

- Weight by inverse total adjustment: the least-adjusted comp carries the most.
- Compute the weighted value and the unweighted range.
- Report ARV as the weighted number, rounded to the nearest $1,000.
- Report a confidence band: the spread between the highest and lowest adjusted
  comp values.

### Step 5 - Stress the number

- If the band is **wider than 8% of ARV**, the comp set is inconsistent. Say so.
- Identify the single comp whose removal moves ARV the most. Name it. That is the
  comp an appraiser is most likely to disagree about.

## Output format

```
ARV: $XXX,000
Confidence band: $XXX,000 - $XXX,000  (spread X.X% of ARV)
Confidence: [high | medium | low]  (N comps used, N rejected)

COMPS USED
  Address            Sold      Price      Gross Adj    Adjusted    Weight
  ...                MM/DD     $XXX,XXX   $XX,XXX      $XXX,XXX    XX%

ADJUSTMENT DETAIL
  [per comp: each adjustment line, value, direction]

COMPS REJECTED
  Address            Failed: [the single test]

MOST LOAD-BEARING COMP: [address]. Removing it moves ARV to $XXX,000.

ADJUSTMENT VALUES USED
  [the table actually applied, so it can be challenged]

CAVEATS
  - [any loosened standard and why]
```

## Decision rules

- Fewer than 3 qualified comps: confidence low, and the ARV is a placeholder.
- Band wider than 8%: recommend an appraisal or a broker price opinion before
  committing earnest money.
- Any comp requiring more than 15% gross adjustment: excluded, always.
- Distressed sales: never used as retail comps, but count them separately and
  report the distressed-to-retail ratio. It is useful for the wholesale exit.

## Failure modes

**Selecting to the answer.** The most common and most expensive failure. The
rejection list is the control: if every rejected comp happens to be a low sale,
the selection is biased.

**Using list prices.** A list price is a wish. It enters this skill nowhere.

**Ignoring boundaries.** Distance is a proxy for comparability, and it is a bad one
across a highway, a school zone line, or a subdivision edge.

**Over-adjusting to rescue a comp.** If it needs that much help, it is not a comp.

**False precision.** Reporting $287,340 implies accuracy the method does not have.
Round to $1,000 and publish the band.

## Notes

DFW-specific: school attendance zones move price more than distance across much of
Collin and Denton county. Verify the zone, not just the district.

Written for Fix-and-Flipper, Wholesaler, First-Deal Investor.

Pairs with: `max-offer-calculator`, `flip-profit-model`, `rehab-cost-estimator`.
