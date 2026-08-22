# Codebase map

The layout is the architecture.

```text
.
├── kernel/
│   ├── KERNEL.md
│   ├── CONTEXT.md
│   ├── STRATEGY.md
│   ├── PRODUCT.md
│   ├── SOFTWARE.md
│   ├── DESIGN.md
│   ├── GTM.md
│   ├── CUSTOMER.md
│   ├── RESEARCH.md
│   ├── OPERATING.md
│   ├── CAPABILITIES.md
│   └── REVIEW.md
├── templates/
│   ├── COMPANY.md
│   ├── PROJECT.md
│   ├── DOMAIN.md
│   └── .kernel/
│       └── NOW.md
├── skills/
│   ├── kernel-setup/
│   ├── project-update/
│   └── kernel-review/
├── scripts/
│   ├── install.py
│   ├── init.py
│   ├── scan.py
│   └── validate.py
└── examples/startup/
    ├── AGENTS.md
    ├── COMPANY.md
    ├── PROJECT.md
    └── .kernel/
        ├── NOW.md
        ├── company/
        └── project/
```

## Two axes

Company Kernel separates context by level and judgment by domain.

```text
LEVEL
SYSTEM -> COMPANY -> PROJECT -> WORK

DOMAIN
STRATEGY | PRODUCT | SOFTWARE | DESIGN | GTM | CUSTOMER | RESEARCH | OPERATING
```

The system domain teaches reusable judgment.

A company domain stores current truth that should guide several projects.

A project domain stores current truth local to one project.

The immediate request owns temporary task detail.

## Runtime ownership

### `kernel/KERNEL.md`

Owns routing, inheritance, precedence, hot-path loading, conflict resolution, and context graduation.

It must remain small enough to load for consequential work.

### `kernel/CONTEXT.md`

Owns the operating environment behind every domain: what changed by 2026, what remains scarce, which YC truths survive, and which historical cost assumptions should not govern automatically.

### `kernel/<DOMAIN>.md`

Owns reusable judgment in one domain.

A domain file should:

- install enough context for the important calls to stand cold
- sharpen decisions rather than list good behavior
- contain language a capable model can extend
- reject obsolete assumptions explicitly
- preserve human authority around consequential decisions
- define what completion means at the level of the claim

Domain files never contain the strategy, product, stack, market, customers, or state of a particular company.

### `kernel/CAPABILITIES.md`

Owns routing across model, instruction, skill, tool, connector, script, and human capability.

It is not a machine inventory.

### `kernel/REVIEW.md`

Owns the cold path for qualifying and applying durable context changes.

It is not normal runtime context.

## Local context ownership

### `COMPANY.md`

Owns company identity, thesis, arena, promise, boundary, compounding path, direction, and strongest evidence.

It should remain useful across several projects.

### `PROJECT.md`

Owns one project's outcome, responsibility, product model, core loop, direction, evidence, fixed decisions, constraints, and non-goals.

### `.kernel/NOW.md`

Owns fast-moving state that should survive the current session: current outcome, active bets, evidence, unknowns, blocks, and next proof.

It is not a transcript or backlog.

### `.kernel/company/<DOMAIN>.md`

Owns durable company truth in one domain.

Create one only when missing cross-project context can change future decisions.

### `.kernel/project/<DOMAIN>.md`

Owns durable project truth in one domain.

Create one only when repository inspection cannot safely reconstruct the truth or hidden intent.

## Skills

### `kernel-setup`

Owns installation, migration, route reconciliation, capability audit, and first initialization.

### `project-update`

Owns compiling, refreshing, restructuring, and graduating company or project context.

### `kernel-review`

Owns qualified challenges to system, company, or project context and applies only authorized changes.

Skills inspect, decide, and write. They do not become a second doctrine library.

## Scripts

### `install.py`

Copies the canonical system, skills, templates, scanner, and initializer. It may initialize one project after installation.

### `init.py`

Creates the three core local context files, adds one marked route without replacing existing `AGENTS.md`, and optionally moves recognized 0.6 project files.

### `scan.py`

Inspects routes, context surfaces, installed skills, duplicate skills, tool configuration paths, legacy context, and Git state without reading secret values.

### `validate.py`

Proves repository shape, system coverage, bounded context weight, plugin metadata, skill shape, installation, initialization, idempotence, migration, scanning, examples, and local links.

Scripts own deterministic mechanics only. They do not invent company truth.

## Canonical source

`kernel/` is the only canonical system.

`templates/` is the only canonical local shape.

The repository root is the Codex plugin.

There is no mirrored generated plugin tree and no second copy of system judgment inside project templates.

## How to change the system

A system change may touch:

1. one or more `kernel/*.md` files
2. `KERNEL.md` when routing or precedence changes
3. templates when the local ownership model changes
4. skills when repeated operating behavior changes
5. scripts and validation when deterministic mechanics change
6. examples when the correct inheritance path changes
7. documentation when installation or ownership changes

Do not add a domain because a company has another department.

Add one only when it owns a distinct class of transferable judgment and local truth that the existing domains cannot carry safely.

## The writing test

A strong model should finish a system file able to think a useful thought it was less likely to think before reading it.

If the file only restates common knowledge, it does not earn runtime context.

See [Writing system context](WRITING.md).
