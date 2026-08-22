# Company Kernel 0.6

**Stop re-briefing the model. Give it a company operating system.**

Frontier models already know how to code, write, research, and sell. That is not the problem.

The problem is that they still default to old software economics, generic startup advice, and whatever they can infer from one repository. Company Kernel fixes that before the task starts.

0.6 gives the model three things:

1. a current startup prior for 2026
2. strong domain judgment for Coding, Product, and GTM
3. current project truth it cannot safely invent

Then it gets out of the way.

## The whole system

```text
KERNEL
current operating environment + routing
        ↓
SYSTEM STANDARD + PROJECT MODEL
how to decide       what is true here
        ↓
WORK
        ↓
EVIDENCE
   ├── update project truth
   └── qualify external review
```

Normal work stays lean. Review stays outside the hot path.

## Repository map

```text
kernel/                 canonical shared system
  KERNEL.md              2026 startup prior + runtime route
  standards/             Coding, Product, GTM judgment
  review/                cold-path review protocol + triggers

templates/              exact project file shapes
  PROJECT.md
  .kernel/
    NOW.md
    CODING.md
    PRODUCT.md
    GTM.md

skills/                 three explicit operating skills
  kernel-setup/
  project-update/
  kernel-review/

scripts/                install, inspect, validate
examples/startup/       one complete example
```

Nothing important is buried in a generated plugin subtree. The repository root is the plugin.

## What gets installed

Shared system:

```text
~/.company-kernel/
  KERNEL.md
  CAPABILITIES.md
  standards/
    CODING.md
    PRODUCT.md
    GTM.md
  review/
    REVIEW.md
    CODING.md
    PRODUCT.md
    GTM.md
  templates/
    PROJECT.md
    .kernel/*
  bin/scan.py
```

One project:

```text
PROJECT.md
.kernel/
  NOW.md
  CODING.md      # only when the project needs durable technical truth
  PRODUCT.md     # only when the project needs a durable product model
  GTM.md         # only when the project needs a durable market position
```

Do not create files because a diagram has boxes. Create them because missing context would change the decision.

## The three skills

### `$kernel-setup`

Install, migrate, reconcile, or audit the shared kernel and its routes. It inspects existing rules and capabilities before touching anything.

### `$project-update`

Create or refresh the current project model after architecture, product, market, evidence, bets, constraints, or direction materially change.

### `$kernel-review`

Question a system standard or project model only after a real signal earns the interruption. It can research and propose. Humans approve shared-standard changes.

## Install

Codex plugin:

```sh
codex plugin marketplace add rhinehart514/company-kernel --ref main
codex plugin add company-kernel@company-kernel
```

Portable install:

```sh
python3 scripts/install.py --user
```

Then run from a real project:

```text
$kernel-setup Set up Company Kernel 0.6 on this machine and initialize this repository.
Inspect existing global rules, skills, tools, and project context first.
Preserve stronger work. Install the shared kernel, add the smallest routes,
and create only the project models this repository actually needs.
```

## What 0.6 refuses to build

- no dashboard
- no context database
- no permanent reflection agent
- no automatic standards mutation
- no one-skill-per-department bureaucracy
- no giant prompt that loads every domain
- no fake project truth generated from code

The scarce thing is judgment, not Markdown production.

## Read next

- [Codebase map](docs/CODEBASE.md)
- [Install and first run](docs/INSTALL.md)
- [Migrate from 0.5](docs/MIGRATE-0.5.md)

## Validate

```sh
python3 scripts/validate.py
```

MIT.
