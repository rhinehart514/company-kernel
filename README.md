# Company Kernel 0.5

**System judgment. Project truth. Work that learns.**

Company Kernel gives frontier models the context they cannot safely invent:

1. compact, reusable judgment above projects
2. current technical, product, and market models inside each project
3. an external review path for questioning those models without bloating normal work

It is headless, file-based, version-controlled, and designed for 2026 model capability. It does not add an orchestrator, database, dashboard, recurring agent, or permanent reflection loop.

## Runtime shape

```text
SYSTEM STANDARD ──┐
                   ├──→ WORK ──→ EVIDENCE
PROJECT MODEL ─────┘               │
                                   ├──→ update project truth
                                   └──→ trigger external review
```

The external review layer is cold-path intelligence. It is not loaded during ordinary work.

## Installed layout

```text
~/.company-kernel/
  KERNEL.md
  CAPABILITIES.md
  standards/
    CODING.md
    PRODUCT.md
    GTM.md
  reviews/
    PROTOCOL.md
    CODING.md
    PRODUCT.md
    GTM.md

project/
  PROJECT.md
  .kernel/
    NOW.md
    CODING.md      # only when relevant
    PRODUCT.md     # only when relevant
    GTM.md         # only when relevant
```

`KERNEL.md` routes work. System standards define how to decide. Project files define what is true here. Review files define when those beliefs deserve reconsideration.

## Domains in 0.5

- **Coding:** Engineering Judgment + Technical Truth
- **Product:** Product Judgment + Product Model
- **GTM:** Market Judgment + Market Position

Strategy remains reserved until it proves it owns company-level decisions that Product and GTM cannot safely own.

## Skills

### `$kernel-integrate`

Install or reconcile the shared kernel, inspect existing rules and capabilities, add thin routes, and initialize the active project.

### `$project-model`

Create, refresh, split, merge, or remove project models as reality changes.

### `$kernel-review`

Qualify a meaningful signal, inspect internal and external evidence, and propose the smallest justified system or project delta. System changes require human approval.

## First run

```text
$kernel-integrate Install Company Kernel 0.5 above my projects. Inspect current rules, skills, tools, and this repository. Preserve stronger instructions, create only needed project models, add thin routes, and report unknowns.
```

## Install

Codex:

```sh
codex plugin marketplace add rhinehart514/company-kernel --ref main
codex plugin add company-kernel@company-kernel
```

Portable skills:

```sh
python3 scripts/install.py --user
```

Project-local skills:

```sh
python3 scripts/install.py --project /path/to/project
```

## Read next

- [Start here](START-HERE.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Domain contracts](docs/DOMAIN-CONTRACTS.md)
- [Integration](docs/INTEGRATION.md)
- [Migration from 0.4](docs/MIGRATION-0.4.md)

## Validate

```sh
python3 scripts/validate.py
```

MIT.
