---
name: max-offer-calculator
description: >
  Produce a defensible maximum allowable offer for a residential deal by building
  the number from actual cost lines instead of applying a percentage rule. Returns
  a walk-away number, the assumptions behind it, and the two inputs most likely to
  be wrong. Use for: Wholesaler, Fix-and-Flipper, First-Deal Investor.
  Category: Deal Analysis & Underwriting.
triggers:
  - max allowable offer
  - MAO
  - what should I offer
  - offer price
  - 70 percent rule
  - walk away number
  - deal spread
category: deal-analysis
price_usd: 0
tier: free
status: authored
version: 1.0.0
---

# Max Allowable Offer Builder

> Get a walk-away number backed by real spread math instead of a 70% rule you cannot defend to a seller.

## Overview

The 70% rule is a screening heuristic that got promoted to an underwriting method.
It bundles profit, holding costs, financing, and closing costs into one percentage
and hides all four. That is fine at 6am on a driving-for-dollars list. It is not
fine when you are about to sign.

This skill rebuilds the offer from the cost lines up. Every dollar between ARV and
offer is named. When a seller asks why the number is what it is, you can answer.

## When to use this skill

- Before submitting any written offer on a residential deal
- When a deal "works on the 70% rule" but your gut says the margin is thin
- When you need to show a partner or lender how you arrived at a price
- When you are deciding whether to counter or walk

Do not use it for: multifamily 5+ units (use `multifamily-underwriting`),
raw land, or new construction.

## Inputs required

| Input | Required | If missing |
|---|---|---|
| ARV | yes | Stop. Ask for it. Do not estimate from list price. |
| Rehab estimate | yes | Stop. A guess here invalidates the whole output. |
| Exit strategy | yes | Ask: wholesale, flip, or hold. The math differs. |
| Holding period (months) | no | Default 5 for flip, 1 for wholesale. State the default used. |
| Financing terms | no | Default hard money at 11% + 2 points, 85% LTC. State it. |
| Assignment fee target | wholesale only | Default $10,000. State it. |
| Market | no | Affects closing cost defaults. Default DFW Texas. |

**Refusal rule:** if ARV or rehab is absent, do not produce a number. Producing a
confident MAO from a missing input is the single most expensive failure this skill
can have. Ask for the missing input and stop.

## Workflow

### Step 1 - Intake and refusal check

Confirm ARV, rehab, and exit strategy are present. Restate all three back to the
user with their source ("ARV $285,000, from three closed comps within 0.4 miles").
If a value arrived without a source, flag it as unverified in the final output.

### Step 2 - Build the deduction stack

Work down from ARV. Name every line. Never combine two lines into one percentage.

**Selling costs** (paid at exit)
- Agent commission: 5% of ARV, or 0 if selling to a known cash buyer
- Seller-side closing costs: 1.5% of ARV
- Concessions allowance: 1% of ARV in a buyer's market, 0 in a seller's market

**Holding costs** (per month x holding period)
- Property taxes: annual tax bill / 12. In Texas, use the actual assessed rate,
  typically 2.1% to 2.7% of assessed value annually. Do not use a national average.
- Insurance (vacant/builder's risk): $180/mo default
- Utilities: $150/mo default
- Lawn and security: $100/mo default

**Financing costs**
- Points: points % x loan amount, charged once
- Interest: rate/12 x loan amount x holding period
- Loan amount: LTC% x (purchase + rehab), capped at the lender's ARV constraint

**Purchase-side closing**
- Title, escrow, recording: 1.2% of purchase price, or $2,500 minimum

**Rehab**
- The line-item estimate provided
- Contingency: 10% if built after 1990, 15% if 1970-1989, 20% if before 1970

**Profit**
- Flip: the greater of 12% of ARV or $30,000
- Wholesale: the assignment fee target
- Hold: skip profit, solve for DSCR >= 1.25 instead and report the max price
  that clears it

### Step 3 - Solve

Purchase price appears on both sides (it drives loan amount and purchase closing
costs), so solve iteratively: start with a purchase estimate of 65% of ARV,
compute the stack, adjust, repeat until the delta is under $500. Three passes is
normally enough. Show the converged number, not the iterations.

### Step 4 - Sensitivity

Recompute MAO at:
- Rehab 20% over estimate
- ARV 5% under estimate
- Holding period 2 months longer

Report each result. Then name the **single input the deal is most sensitive to** -
the one where a 10% error moves MAO the most. That is the input to go verify
before offering.

### Step 5 - Output

## Output format

```
MAX ALLOWABLE OFFER: $XXX,XXX
Exit strategy: [flip | wholesale | hold]

DEDUCTION STACK
  ARV                              $XXX,XXX   [source]
  - Selling costs                  ($XX,XXX)  [commission, closing, concessions]
  - Holding costs (N months)       ($X,XXX)   [tax, ins, util, maint]
  - Financing (points + interest)  ($X,XXX)   [terms]
  - Purchase closing               ($X,XXX)
  - Rehab                          ($XX,XXX)  [estimate + N% contingency]
  - Profit                         ($XX,XXX)  [basis]
  = MAX ALLOWABLE OFFER            $XXX,XXX

SENSITIVITY
  Rehab +20%          MAO $XXX,XXX  (-$X,XXX)
  ARV -5%             MAO $XXX,XXX  (-$X,XXX)
  Holding +2 months   MAO $XXX,XXX  (-$X,XXX)

MOST SENSITIVE INPUT: [name]. Verify this before offering.

UNVERIFIED ASSUMPTIONS
  - [any input that arrived without a source]

WALK-AWAY: Do not go above $XXX,XXX. Above that the deal returns less than
[profit basis] and you are working for free.
```

## Decision rules

- If MAO comes out **below 45% of ARV**, the rehab is likely mis-scoped or the ARV
  is inflated. Say so rather than reporting an absurd number.
- If MAO comes out **above 85% of ARV**, either the rehab is trivial or a cost line
  is missing. Re-check before reporting.
- If sensitivity shows **any single 10% input error swinging MAO by more than 15%**,
  label the deal fragile and recommend verifying before writing an offer.
- If the exit is hold and DSCR cannot reach 1.25 at any price above $0, say the
  deal does not work as a rental and stop.

## Failure modes

**Anchoring to list price.** If the user supplies a list price, ignore it entirely
until the MAO is computed. Then compare. Never let list price influence ARV.

**Silent defaults.** Every default used must appear in the output. A user who does
not know a 5-month hold was assumed will be surprised at month seven.

**False precision.** Round MAO down to the nearest $500. A number like $187,342
implies an accuracy the inputs do not support.

**Rehab optimism.** If the rehab estimate arrived as a single round number with no
line items, flag it. A $40,000 rehab with no scope behind it is a wish.

## Notes

Texas-specific defaults: property tax rates are high and assessed values reset on
sale, so a purchase at a price well below assessed value does not lower the tax
bill until protested. Budget the current bill, not a hoped-for reduction.

Written for Wholesaler, Fix-and-Flipper, First-Deal Investor.

Pairs with: `arv-comp-selector`, `rehab-cost-estimator`, `deal-screener-triage`.
