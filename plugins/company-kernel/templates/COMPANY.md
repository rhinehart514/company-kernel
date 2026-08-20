# Company

> Canonical shared company state. Keep this file compact. It does not contain tasks, roadmaps, feature inventories, research dumps, personal preferences, implementation detail, or historical logs.

## Current model

**Company claim:** [Company] creates [valuable result] for [beneficiary or user] when [trigger], authorized or funded by [buyer, funder, or authority], through [product and delivery form].

**Why this can become a company:** [Name the accumulating asset or control point that makes later customers, workflows, products, or transactions easier.]

**Current boundary:** [State what belongs inside this company now and what does not.]

Do not state unresolved beliefs here as facts. Put them under **Evidence and unknowns**.

## 1. World and pressure

- **External change:** What changed in technology, regulation, behavior, cost, supply, distribution, or capability?
- **Pressured actor:** Who now faces a consequence?
- **Trigger:** What event makes the actor act rather than tolerate the status quo?
- **Cost of no action:** What money, time, risk, revenue, quality, or opportunity is lost?
- **Why existing options fail:** What is missing, too expensive, too fragmented, too slow, or structurally misaligned?

## 2. Actor system

Delete roles that do not exist. Add rows when several actor classes exist. Do not merge different roles merely to make the model look simpler.

| Role | Specific actor | Controls | Wants | Bears which failure |
| --- | --- | --- | --- | --- |
| User |  |  |  |  |
| Buyer |  |  |  |  |
| Operator |  |  |  |  |
| Approver or gatekeeper |  |  |  |  |
| Affected party |  |  |  |  |
| Channel or partner |  |  |  |  |

## 3. Value contract

- **Existing work:** What happens today, step by step, before this company intervenes?
- **Valuable result:** What changed state does the customer value?
- **Unit of value:** Task, case, transaction, workflow, decision, location, outcome, access, or another explicit unit.
- **Frequency and volume:** How often and at what scale does the work occur?
- **Proof:** What observable evidence demonstrates completion or value?
- **Current alternative:** Person, vendor, software, manual process, delay, or doing nothing.
- **Existing spend or labor:** What budget, headcount, fees, risk, or opportunity cost already supports the work?

## 4. Responsibility contract

- **Company observes:** What information or events can the company see?
- **Company decides:** Which judgments can the company make?
- **Company performs:** Which actions can the company take?
- **Company completes:** Which result does the company own through a terminal state?
- **Human or customer decides:** Which judgment, consent, approval, or authority remains human?
- **Terminal state:** What exact condition means the work is complete?
- **Exception state:** What condition requires escalation or a different path?
- **Cutoff state:** When must the company stop rather than continue?
- **Failure owner:** Who bears the consequence when the result is wrong, late, incomplete, or unsafe?

## 5. Delivery system

- **Inputs:** Data, requests, inventory, access, physical inputs, or context required.
- **Product surface:** Interface, API, device, document, location, or channel the customer uses.
- **Execution layer:** Software, agents, people, machinery, partners, or procedures that perform the work.
- **Human or service layer:** Ongoing work the company must perform outside the product.
- **Integrations and authority:** Systems, permissions, approvals, or physical access required.
- **Onboarding:** What must happen before the first real result?
- **Ongoing operation:** What must continue after onboarding?
- **Time to first value:** The first observable result and what must precede it.
- **Cost drivers:** What makes delivery more expensive as customers, volume, scope, or risk increase?

## 6. Commercial system

- **Entry wedge:** The smallest valuable commitment that establishes a customer relationship or control point.
- **Discovery:** How the buyer learns this company exists.
- **Sale:** Self-serve, founder-led, sales-led, partner-led, procurement, tender, storefront, referral, or another explicit motion.
- **Buyer commitment:** Money, data, access, workflow change, implementation time, authority, or risk transferred.
- **Pricing unit:** Seat, usage, transaction, location, project, retainer, outcome, take rate, product, grant, or another explicit unit.
- **Implementation burden:** Work required from the company, customer, and partners.
- **Retention mechanism:** Why the customer continues paying, returning, or participating.
- **Expansion event:** What observed event creates a credible next sale or larger responsibility.
- **Economic failure condition:** Which delivery cost, acquisition cost, margin, cycle time, risk, or concentration would make the model fail?

## 7. Accumulating assets

Include only assets that persist and make later work easier. Features are not automatically assets.

| Asset | How it is acquired | What it makes easier | Constraint or decay |
| --- | --- | --- | --- |
|  |  |  |  |

Possible asset classes include customer context, workflow authority, proprietary data, distribution, installed infrastructure, system-of-record position, transaction access, reusable delivery knowledge, trust, brand, network density, supply, and regulatory approval.

## 8. Boundary and expansion

- **Current territory:** The work, customer, transaction, or control point the company presently owns.
- **Adjacent territory:** Opportunities made cheaper or more likely by current assets.
- **Same company when:** Conditions under which a new opportunity reinforces the current actors, value, delivery, commercial system, or assets.
- **Separate company when:** Conditions that require a different buyer, brand, sales motion, product core, operating organization, risk regime, or supply system.
- **Absorption rule:** How a successful experiment becomes part of the core rather than a permanent side product.
- **Stop condition:** Evidence that should end expansion, narrow the model, or kill the company thesis.

## 9. Decision posture

This is company policy, not an operator preference.

- **Primary optimization:** Speed, safety, margin, reach, reliability, mission outcome, learning, control, or another explicit priority.
- **Evidence threshold:** What must be known before reversible and irreversible actions?
- **Reversibility:** Which decisions may be made quickly because they are cheap to undo?
- **Risk constraints:** Legal, financial, physical, reputational, trust, privacy, or safety boundaries.
- **Parallel bets:** How many materially different bets may run, and what must they share?
- **Consequence of waiting:** When delay is safer, and when delay is itself the greater risk.

## 10. Current company decisions

Keep only decisions that materially constrain several functions. Git preserves prior versions.

- **Decision:**  
  **Authority:**  
  **Consequence:**

## 11. Evidence and unknowns

### Evidence relied upon

Reference canonical sources rather than pasting full research.

- **Claim supported:**  
  **Observed evidence:**  
  **Source and date:**

### Unknowns and falsifiers

- **Current belief:**  
  **Why it matters:**  
  **Evidence missing:**  
  **Cheapest valid test:**  
  **Would strengthen:**  
  **Would falsify or reshape:**

## Change contract

Update this file only when one of these changes materially:

1. world, pressure, or actors
2. valuable result or proof
3. responsibility boundary
4. delivery system
5. commercial system or economics
6. accumulating assets
7. company boundary, expansion logic, or decision posture

A large code change may require no update. A small change to buyer, pricing, authority, completion, onboarding, or delivery may require one.

Evidence rules:

- Code and tests prove capability.
- Customer behavior supports demand.
- Sales behavior supports buying.
- Economic data supports viability.
- Authorized human direction establishes a decision.
- Agent synthesis is inference.

Before accepting the model, verify:

- the payer or authority can grant the commitment delivery requires
- the valuable result has observable proof
- the responsibility boundary has matching access, authority, terminal, exception, and cutoff states
- delivery burden can fit the commercial and economic system
- named assets actually accumulate from normal operation
- expansion reuses or creates those assets instead of hiding a second company

Make the smallest defensible diff. Do not update timestamps, rewrite stable language for freshness, or turn an implication into company truth.
