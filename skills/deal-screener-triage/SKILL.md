---
name: deal-screener-triage
description: >
  Screen an inbound residential deal in under a minute and return one of three
  verdicts: dead, park, or work today. Built to kill deals fast so acquisition
  time goes to the few that can close. Use for: Wholesaler, First-Deal Investor.
  Category: Deal Analysis & Underwriting.
triggers:
  - screen this deal
  - is this deal worth it
  - quick deal analysis
  - deal triage
  - should I look at this
  - lead qualification
category: deal-analysis
price_usd: 0
tier: free
status: authored
version: 1.0.0
---

# 60-Second Deal Screener

> Kill bad deals in under a minute so you spend your day on the three that can actually close.

## Overview

Most acquisition time is wasted on deals that were never going to close. Not
because they were analyzed wrong, but because they were analyzed at all. A deal
with a seller who has no motivation and no equity does not need an ARV pull.

This skill applies four gates in order and stops at the first failure. It is
deliberately harsh. The cost of a false negative is one lost deal. The cost of a
false positive is a week.

## When to use this skill

- On every inbound lead before any research effort
- When a wholesaler sends you a deal and you need a verdict, not a courtesy call
- When your pipeline has more deals than you have hours

## Inputs required

Accept whatever the user has. Do not demand a full data set. This skill runs on
partial information by design and reports its own confidence.

| Input | Weight |
|---|---|
| Asking price | high |
| Rough condition | high |
| Seller's stated reason for selling | high |
| Timeline / urgency | high |
| Est. ARV or neighborhood price band | medium |
| Occupancy status | medium |
| Existing loan balance | medium |
| Address / submarket | low |

## Workflow

Run gates in order. **Stop at the first hard fail and report immediately.** Do not
complete later gates for a deal already dead. Speed is the product.

### Gate 1 - Motivation

Look for a reason the seller must transact, not a reason they would like to.

- **Hard motivation:** foreclosure timeline, probate with multiple heirs, divorce
  decree, out-of-state landlord with a vacancy, tax lien, relocation with a date,
  condition beyond the owner's means to fix
- **Soft motivation:** testing the market, "if I get my price", curiosity, an
  agent's suggestion

Soft motivation with no other pressure is a **hard fail**. Report: dead, no
motivation. A seller with no reason to move will not accept an investor price.

### Gate 2 - Spread possibility

Compute a crude ceiling: `(ARV or price band) x 0.72 - rough rehab`.
Compare to asking price.

- Asking price **below** the ceiling: pass
- Asking price **within 10% above**: pass with a note that it needs negotiation
- Asking price **more than 10% above**: hard fail unless Gate 1 returned hard
  motivation, in which case downgrade to park

Use 0.72 here rather than a full MAO build. This gate is a filter, not a valuation.
Anything that passes gets a real number later from `max-offer-calculator`.

### Gate 3 - Equity and payoff

If a loan balance is known, compare it to the crude ceiling.

- Balance above the ceiling: the seller cannot sell at your price without bringing
  cash or a short sale. **Hard fail** unless the user works subject-to or short
  sales, in which case route to `creative-finance-pitch` and mark park.
- Balance unknown: proceed, flag as the top unknown.

### Gate 4 - Timeline and control

- Seller wants to close in under 45 days and has authority to sign: pass
- Multiple decision makers not yet aligned (heirs, ex-spouses, partners): park,
  not dead. These close, just later.
- Property already listed with an agent at a retail price and less than 60 days on
  market: park. Revisit at day 90.

## Output format

Keep it to nine lines. Anything longer defeats the purpose.

```
VERDICT: [DEAD | PARK | WORK TODAY]
Reason: [one sentence, the gate that decided it]

Motivation:  [hard | soft | unknown]
Spread:      [pass | tight | fail]  crude ceiling ~$XXX,XXX
Equity:      [pass | fail | unknown]
Timeline:    [pass | park | unknown]

Top unknown: [the one thing to find out next]
Next action: [specific, e.g. "call and ask for the payoff" | "add to 90-day drip" | "drive it today"]
Confidence:  [high | medium | low] - based on N of 8 inputs present
```

## Decision rules

- **DEAD** - any hard fail. Move on. Do not soften this to keep a lead warm.
- **PARK** - the deal is real but the timing, the decision makers, or the price
  expectation are not. Route to `seller-followup-engine` with a revisit date.
- **WORK TODAY** - all four gates pass. Escalate to `arv-comp-selector` then
  `max-offer-calculator`.

If fewer than 4 of the 8 inputs are present, report confidence low and make the
next action "gather" rather than "decide".

## Failure modes

**Being polite.** The most common failure is returning PARK when the answer is
DEAD, because DEAD feels harsh. A pipeline full of parked dead deals is the exact
problem this skill exists to solve. If motivation is soft and there is no other
pressure, say dead.

**Analyzing past the first fail.** Completing all four gates on a dead deal wastes
the minute the skill was built to save.

**Treating unknown as fail.** Unknown is not fail. Unknown becomes the top unknown
and the next action. Only a known bad answer kills a deal.

**Confusing distress with motivation.** An ugly house owned by someone comfortable
is not a deal. A clean house owned by someone in a divorce is.

## Notes

Written for Wholesaler, First-Deal Investor.

Pairs with: `max-offer-calculator`, `seller-call-script`, `seller-followup-engine`.
