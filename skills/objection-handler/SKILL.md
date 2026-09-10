---
name: objection-handler
description: >
  Answer the objections that end seller calls, using responses that keep the
  conversation open instead of winning the point. Covers price, trust, timing,
  agent comparison, and stalling. Use for: Wholesaler, First-Deal Investor.
  Category: Seller Outreach & Negotiation.
triggers:
  - seller objection
  - seller said no
  - handle objection
  - lowball response
  - seller pushback
  - what do I say when
category: seller-negotiation
price_usd: 0
tier: free
status: authored
version: 1.0.0
---

# Seller Objection Handler

> Answer the nine objections that end most seller calls, in language that keeps the conversation alive.

## Overview

Most objection training teaches rebuttals. A rebuttal wins an argument with
someone who was about to sell you their house. That is a bad trade.

Every objection below is answered the same structural way: acknowledge the
objection as reasonable, supply the missing information that caused it, then
return a question that hands control back to the seller. The goal is never to
close on the call. It is to still be talking.

## When to use this skill

- Live, mid-call, when a seller says something that stops you
- In prep, to rehearse the objections a specific lead is likely to raise
- After a lost call, to work out what should have been said

## Inputs required

| Input | Required | Notes |
|---|---|---|
| The objection, in the seller's own words | yes | Exact wording matters. "That's too low" and "I need more than that" are different objections. |
| Deal context | no | Motivation, condition, timeline if known |
| Where in the call it happened | no | Early objections are usually trust, late ones are usually price |

## The response structure

Every answer follows the same three moves. Never skip the first.

1. **Acknowledge** - state the objection back as reasonable. Not "I understand,
   but". The word *but* deletes everything before it. Use a period instead.
2. **Inform** - supply the one piece of information the seller does not have that
   makes your position make sense.
3. **Return** - end on an open question. Never end on your own statement. Whoever
   speaks last owns the silence, and the silence should be theirs.

## The nine objections

### 1. "That's way too low."

**Acknowledge:** It is a lot lower than what the house would sell for fixed up.
That is a fair reaction.
**Inform:** The number covers the repairs, the six months of carrying it, the
agent commissions on the back end, and a margin. Explain any line they ask about.
**Return:** Can I walk you through how I got there? If a line is wrong, I would
rather know now.

### 2. "I can get more from an agent."

**Acknowledge:** You probably can. On price, a listing usually beats a cash offer.
**Inform:** The trade is that a listing means repairs before photos, showings,
30 to 45 days after an offer, and commissions. What I offer is speed and certainty.
**Return:** Which of those matters more for you right now, the top number or the
timeline?

### 3. "I need to think about it."

**Acknowledge:** You should. This is not a decision to make on a phone call.
**Inform:** State that the offer holds for a specific window and why.
**Return:** What is the part you want to think through most? I might be able to
answer it now so you are thinking about the real question.

### 4. "I have to talk to my [spouse / kids / brother]."

**Acknowledge:** Of course.
**Inform:** Note that the person not on the call always hears a worse version of
the offer than the one you made.
**Return:** Would it be easier if I got on a call with both of you so you are not
the one having to defend my number?

### 5. "How do I know you'll actually close?"

**Acknowledge:** You do not, yet. And you have probably heard from people who did
not.
**Inform:** Offer proof of funds, the title company you use, and two recent
closings the seller can verify.
**Return:** What would you need to see to feel comfortable? I would rather send it
than ask you to take my word.

### 6. "Another investor offered more."

**Acknowledge:** Then take it, if they close.
**Inform:** Note that a higher number that gets renegotiated at day 20 is worth
less than a lower number that funds. Ask what their earnest money is and whether
it goes hard.
**Return:** If that offer falls through, can I be the call you make?

### 7. "I'm not in a hurry."

**Acknowledge:** No reason to be.
**Inform:** Do not manufacture urgency. Do not invent a deadline. This one is
answered by leaving cleanly.
**Return:** Then let me get out of your way. Can I check back in 90 days in case
anything changes?

### 8. "Why do you want my house?"

**Acknowledge:** Fair question.
**Inform:** Answer honestly. You buy at a discount, fix, and resell or rent. Say
the actual business model. Any evasion here costs the deal.
**Return:** Does that change how you feel about talking?

### 9. "I owe more than that."

**Acknowledge:** That happens more than people think.
**Inform:** Explain that there may still be structures that work: subject-to,
seller carry, or a short sale, depending on the lender.
**Return:** Would you be open to me looking at whether one of those fits? It may
not, but it costs you nothing to find out.

## Decision rules

- If the seller raises **the same objection three times**, it is not the real
  objection. Stop answering it and ask directly: "What is actually making you
  hesitate?"
- If the objection is **price and motivation is soft**, do not raise the offer.
  Move to follow-up. Chasing a soft seller with a higher number trains them.
- If the objection is **trust**, never answer with more enthusiasm. Answer with
  documents.
- If the seller becomes hostile, exit warmly and immediately. Note the date and
  route to `seller-followup-engine`. Hostile sellers call back.

## Failure modes

**Using "but".** It deletes the acknowledgment and signals the whole thing was a
setup for the rebuttal.

**Raising the offer to end an objection.** This teaches the seller that objecting
raises the price, and it will happen again at closing.

**Manufacturing false urgency.** "This offer expires tonight" on a house that has
sat for two years is not credible and it costs trust permanently.

**Winning.** If the seller feels beaten, they will not sign, or they will sign and
back out. The objective is agreement, not victory.

## Notes

Written for Wholesaler, First-Deal Investor.

Pairs with: `seller-call-script`, `offer-presentation`, `seller-followup-engine`,
`creative-finance-pitch`.
