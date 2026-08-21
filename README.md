# Company Kernel

**Build the system once. Keep every project current.**

Company Kernel gives frontier models two things they usually lack:

1. a small shared system of beliefs, taste, and judgment above every project
2. a current project model inside each repository

It also inspects the skills, tools, and rules already on the machine. It keeps what helps, fixes routing, exposes missing access, and builds new capability only when the model and existing environment cannot already do the job.

[Start here](START-HERE.md)

## The shape

```text
~/.company-kernel/
  SYSTEM.md
  LENSES.md
  lenses/
  CAPABILITIES.md

project/
  PROJECT.md
  .project/
    NOW.md
    ...only what this project needs
```

The shared system is not copied into every project. Projects inherit it through one small route in the agent instructions they already use.

## First run

```text
$system-integrate Build or reconcile the shared Company Kernel system above my projects.
Inspect my existing global rules, installed skills, and available tools.
Keep stronger rules. Write a readable 1-10 line SYSTEM.md and only useful lenses
under ~/.company-kernel, create a clear capability map, then initialize this repository
with PROJECT.md and .project/NOW.md. Do not delete or rewrite unrelated global work.
```

A good first run should make the company more obvious, the product more coherent, and the agent environment easier to use.

## What the system contains

`SYSTEM.md` holds the few beliefs that should shape consequential work everywhere.

Optional lenses add thin judgment for recurring work. The source library includes several lenses around product and market work because one generic `PRODUCT.md` or `GTM.md` would be mush:

```text
FRONTIER.md
STRATEGY.md
PRODUCT-COHERENCE.md
OUTCOME-OWNERSHIP.md
MARKET-POWER.md
GTM-ENGINEERING.md
PROOF.md
RESEARCH.md
WRITING.md
DESIGN.md
SOFTWARE.md
CUSTOMER-OUTCOMES.md
ECONOMICS.md
OPERATIONS.md
AGENT-SYSTEMS.md
```

Each active system file contains one to ten lines. The integrator keeps only what adds value beside the user's existing rules.

## What a project contains

Every active project normally starts with:

```text
PROJECT.md
.project/NOW.md
```

`PROJECT.md` explains what the project is, what it owns, why it matters now, where it enters, and what winning unlocks.

`.project/NOW.md` holds the current objective, momentum, bets, constraints, contradictions, and next proof.

More files appear only when the truth is too large or changes at a different speed:

```text
.project/PRODUCT.md
.project/PRODUCT-SURFACES.md
.project/USER-LOOP.md
.project/MARKET.md
.project/ACCOUNT-SIGNALS.md
.project/SALES-MOTION.md
.project/DISTRIBUTION.md
.project/DELIVERY.md
.project/AGENT-AUTHORITY.md
.project/ECONOMICS.md
.project/EVIDENCE.md
.project/CAPABILITIES.md
```

There may be four files around GTM and none around strategy. The system does not reward symmetry.

## The skills

### `$system-integrate`

Build or refresh the shared system, clean up capability routing, then initialize the current project.

Use it for first setup, model upgrades, tool changes, skill sprawl, major pivots, or a system that no longer feels coherent.

### `$project-context`

Refresh one project's truth after the customer, product, market, responsibility, economics, evidence, or current objective changes.

### `$project-research`

Resolve one uncertainty that can change a real decision. Research should update a belief, narrow a test, or show that nothing should change.

## Install

Codex:

```sh
codex plugin marketplace add rhinehart514/company-kernel --ref main
codex plugin add company-kernel@company-kernel
```

Portable Agent Skills:

```sh
python3 scripts/install.py --user
```

Project-local skills:

```sh
python3 scripts/install.py --project /path/to/project
```

The installer copies skills. The integrator inspects before it writes system or project context.

## Read next

- [What gets built](docs/WHAT-GETS-BUILT.md)
- [First run](docs/FIRST-RUN.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Writing](docs/WRITING.md)
- [Integration](docs/INTEGRATION.md)
- [Evaluation](docs/EVALUATION.md)

## Validate

```sh
python3 scripts/validate.py
```

MIT.
