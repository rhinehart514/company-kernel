---
name: opportunity-evaluate
description: "Evaluate a concrete product, market, service, channel, pricing, integration, workflow, or business-model opportunity against the current company when explicitly invoked. Return pursue, probe, defer, decline, separate company, or insufficient evidence. Do not use for unconstrained brainstorming or generic market reports."
---

# Opportunity Evaluate

Determine whether a concrete opportunity should be pursued by this company, tested cheaply, delayed, declined, or treated as a separate company.

Do not reward narrowness or breadth by default. Apply the company's decision posture from `COMPANY.md`.

## Define the opportunity

Before judging it, make the proposal explicit:

- target actor
- trigger
- existing work or failure
- valuable result
- responsibility the company would take
- product and delivery form
- buyer and budget
- distribution and sale
- pricing or economic unit
- required authority, trust, supply, regulation, or implementation
- evidence already available
- cost and time of the cheapest valid test

If these cannot be resolved from available context, identify exactly what remains unknown. Do not fill gaps with category clichés.

## Compare it to the company

Read `COMPANY.md` and test:

### World and actors

- Does the opportunity arise from the same external change or pressure?
- Does it serve the same buyer, user, operator, gatekeeper, or affected party?
- Can the existing customer relationship carry the new commitment?

### Value and responsibility

- Does it deepen the current result, own adjacent work, or introduce a different value transaction?
- Does it require new judgment, liability, completion states, exceptions, or failure ownership?

### Delivery and commercial mechanics

- Can existing product, people, partners, integrations, permissions, supply, onboarding, and operations deliver it?
- Does current distribution reach the buyer?
- Does the current sales motion and pricing logic fit?
- Does it create a contradictory margin, cycle time, risk, support, or implementation model?

### Assets and absorption

- Which existing assets does it reuse?
- Which durable assets would success add?
- Would those assets make later work easier?
- Can a successful probe be absorbed into the current company and product?
- Would it remain a permanent side product with its own buyer, brand, motion, support, and organization?

### Timing and posture

- What is the consequence of acting now?
- What is the consequence of waiting?
- Is the action reversible?
- What evidence threshold and risk constraint does the company require?
- What existing work would be displaced?

## Verdict

Choose one:

- **Pursue:** Evidence and fit justify committing meaningful resources now.
- **Probe:** A bounded, reversible market action can resolve the decisive uncertainty cheaply.
- **Defer:** It may fit, but timing, capacity, dependency, or opportunity cost makes waiting correct.
- **Decline:** Expected value or strategic leverage is too weak for this company.
- **Separate company:** The opportunity may be valuable but requires a materially different actor system, value contract, delivery system, commercial system, risk regime, or accumulating core.
- **Insufficient evidence:** No honest verdict is available and no responsible test has yet been defined.

Do not use a numeric score. A score conceals the decisive tradeoff with arithmetic cosplay.

## Required output

```text
Opportunity:
<one concrete sentence>

Verdict:
<pursue | probe | defer | decline | separate company | insufficient evidence>

Decisive reasons:
- <reason grounded in company structure or evidence>
- <reason>
- <reason>

Reused assets:
- <asset, or none>

New complexity:
- <buyer, product, delivery, commercial, operating, risk, or supply complexity>

Cheapest valid market action:
<build, sell, interview, price, deploy, partner, observe, or other real action>

Evidence that changes the verdict:
- <strengthening evidence>
- <falsifying evidence>

Company-model implication:
<none, possible unknown, or specific contract to reconcile if the test succeeds>
```

## Failure

Failure includes:

- a list of generic pros and cons
- assuming cheap code means cheap distribution, trust, delivery, regulation, or support
- calling an opportunity adjacent because both use AI
- rejecting an opportunity merely because it is outside the current feature set
- approving breadth without a shared asset or absorption path
- recommending more research when a bounded market action can answer the question
- silently changing `COMPANY.md`
