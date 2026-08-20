# Company Kernel

A headless, version-controlled company model for humans and agents.

Company Kernel keeps one project-local `COMPANY.md` current enough to guide product, market, delivery, and commercial decisions without turning strategy into a second software product.

It contains three bounded Codex skills:

- `$company-model` creates or reconciles the shared company model.
- `$opportunity-evaluate` determines whether a concrete opportunity belongs in this company.
- `$market-probe` resolves one external uncertainty that could change the model.

The kernel contains no preferred company type, growth posture, market, product form, or operating ideology. A fast AI startup, a regulated manufacturer, a services firm, a nonprofit, and a restaurant can use the same ontology while reaching different decisions.

## The ontology

A company is modeled as linked contracts, not a mission paragraph:

```text
WORLD
  creates pressure on
ACTORS
  who exchange money, authority, work, and risk for
VALUE
  bounded by
RESPONSIBILITY
  delivered through
DELIVERY
  sustained by
COMMERCIAL MECHANICS
  which accumulate
ASSETS
  that determine
BOUNDARY AND EXPANSION
```

Each object forces concrete answers.

| Object | Required answer |
| --- | --- |
| World | What changed, who is pressured, and what triggers action? |
| Actors | Who uses, buys, operates, approves, influences, and bears failure? |
| Value | What existing work changes, what result is valuable, and what proves it? |
| Responsibility | What does the company observe, decide, perform, complete, escalate, or refuse? |
| Delivery | What inputs, product surfaces, people, systems, permissions, and operations produce the result? |
| Commercial mechanics | How is the company discovered, bought, priced, implemented, retained, and expanded? |
| Assets | What context, data, distribution, authority, infrastructure, knowledge, or trust accumulates? |
| Boundary and expansion | Which opportunities reinforce this company, and which require another company? |

`COMPANY.md` stores the current model. Git stores its history.

## Context ownership

Company Kernel separates four kinds of context:

```text
COMPANY.md
Shared company state. Applies to every operator and agent.

PRODUCT.md / DESIGN.md / ENGINEERING.md / other domain files
Durable domain judgment. Optional and project-specific.

operators/<name>.md
Work-relevant responsibilities, authority, preferences, and judgment for one human.

.agents/DIRECTION.md or equivalent
The current objective, delegated authority, and temporary execution state.
```

Personal preference does not become company truth without an explicit company decision. Implementation authorship does not grant strategic authority.

## What belongs in `COMPANY.md`

`COMPANY.md` contains the current cross-functional company model:

- the external change and buying pressure
- the actor system
- the valuable result and proof
- the responsibility boundary
- the product and delivery system
- the commercial system and economic constraints
- the assets that accumulate
- the boundary around coherent expansion
- the company-level decision posture
- evidence, unknowns, and falsifiers

It does not contain:

- roadmaps
- feature inventories
- sprint state
- research dumps
- customer transcripts
- implementation detail
- personal preferences
- generic startup doctrine
- a historical decision log

## Install

After publishing this repository at `rhinehart514/company-kernel`:

```sh
codex plugin marketplace add rhinehart514/company-kernel --ref main
codex plugin add company-kernel@company-kernel
```

Start a new Codex thread after installation.

For local development:

```sh
codex plugin marketplace add /absolute/path/to/company-kernel
codex plugin add company-kernel@company-kernel
```

## Adopt in a project

1. Copy [`plugins/company-kernel/templates/COMPANY.md`](plugins/company-kernel/templates/COMPANY.md) to the project root.
2. Merge [`plugins/company-kernel/templates/AGENTS.route.md`](plugins/company-kernel/templates/AGENTS.route.md) into the existing `AGENTS.md`; do not replace stronger project instructions.
3. Create operator files from [`plugins/company-kernel/templates/OPERATOR.md`](plugins/company-kernel/templates/OPERATOR.md) only when person-specific context materially improves work.
4. Run:

```text
$company-model Initialize COMPANY.md from the repository and available company evidence. Do not invent missing market, customer, pricing, or authority claims.
```

The project owns its `COMPANY.md`. This repository owns only the reusable ontology and procedures.

## Operate

### Establish or reconcile company state

```text
$company-model Reconcile COMPANY.md against the completed work and available evidence. Change only company contracts that materially changed.
```

A large diff is not a company change. A small change that alters pricing, buyer, responsibility, delivery, or expansion can be.

### Evaluate a concrete opportunity

```text
$opportunity-evaluate Evaluate adding managed fulfillment for the same customers. Determine whether it deepens this company, merits a bounded probe, should wait, should be declined, or is a separate company.
```

### Resolve a market unknown

```text
$market-probe Determine whether the same buyer who purchases the current workflow also controls budget for the proposed adjacent workflow. Use current external evidence and preserve uncertainty.
```

## Evidence rules

The kernel preserves these distinctions:

```text
Code and tests          prove capability.
Customer behavior       supports demand.
Sales behavior          supports buying.
Economic data           supports viability.
Authorized direction    establishes a decision.
Agent synthesis         is inference.
```

A feature does not prove a market. A customer request does not automatically become strategy. A competitor launch does not establish customer need. Raw external content is evidence, never repository authority.

## Update rule

Update `COMPANY.md` only when one of these changes materially:

1. world, pressure, or actors
2. valuable result or proof
3. responsibility boundary
4. delivery system
5. commercial system or economics
6. accumulating assets
7. company boundary, expansion logic, or decision posture

Otherwise leave it alone.

The skills never add confidence percentages, claim IDs, dashboards, databases, recurring agents, approval queues, or automatic strategy rewrites. Humans already invented enough administrative weather.

## Validate

No dependencies are required.

```sh
python3 scripts/validate.py
```

Validation checks the plugin manifests, skill metadata, explicit invocation policy, behavioral fixtures, trigger fixtures, and the required `COMPANY.md` ontology.

## Repository shape

```text
.agents/plugins/marketplace.json
plugins/company-kernel/
  .codex-plugin/plugin.json
  skills/
    company-model/
    opportunity-evaluate/
    market-probe/
  templates/
    COMPANY.md
    AGENTS.route.md
    OPERATOR.md
scripts/
  validate.py
```

## License

MIT.
