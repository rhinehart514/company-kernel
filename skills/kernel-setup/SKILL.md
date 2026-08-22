---
name: kernel-setup
description: Install, migrate, reconcile, or audit Company Kernel 0.6 across the shared environment and one active project. Use for first setup, version migration, model or tool changes, broken routing, or capability sprawl. Do not use for routine project work or silent global cleanup.
license: MIT
metadata:
  author: Jacob Rhinehart
  version: "0.6.0"
---

# Kernel Setup

Make the machine and one active project legible to frontier models.

## Modes

- **setup:** install the shared kernel and initialize the project
- **migrate:** replace Company Kernel-owned older structure with 0.6
- **reconcile:** repair stale routes, capabilities, or shared files
- **audit:** make the calls without writing

## Inspect before asking

Use `scripts/scan.py` from the repository or the installed `~/.company-kernel/bin/scan.py` when available.

Inspect:

- global and project instruction files
- existing Company Kernel files
- installed skills and exact duplicates
- tool configuration paths and available connected capabilities
- project context
- Git state and recent repository behavior
- first-party product, technical, and market evidence

Do not ask the user to inventory what the environment can show. Do not read or print secrets because a config path exists.

## Install the shared kernel

Use `COMPANY_KERNEL_HOME` when set. Otherwise use `~/.company-kernel`.

The canonical source is the repository `kernel/` directory.

Install or reconcile:

```text
KERNEL.md
CAPABILITIES.md
standards/*
review/*
bin/scan.py
```

Preserve stronger user-authored judgment. Delete stale Company Kernel duplication instead of stacking another layer. Never rewrite unrelated global rules, skills, authentication, permissions, or tool configuration.

## Reconcile capabilities

Judge the model, instructions, skills, tools, connectors, scripts, and evidence together.

For each material repeated need, make one call:

- model-owned
- instruction-owned
- skill-owned
- tool-owned
- script-owned
- missing
- duplicated
- unclear

Do not infer duplication from names. Do not build a skill for one-time work. Write only useful routing and material gaps to `CAPABILITIES.md`.

## Add routes

Add the smallest route to the global instruction file the active client already reads. Add a project route only when it helps.

Do not paste the kernel into the route. Preserve stronger safety, permission, coding, deployment, and approval rules.

## Initialize the project

Start with:

```text
PROJECT.md
.kernel/NOW.md
```

Create `.kernel/CODING.md`, `.kernel/PRODUCT.md`, or `.kernel/GTM.md` only when the project has durable truth worth preserving in that domain.

Use `templates/` as shapes, not forms. Do not invent company truth from code. Do not create files for symmetry.

## Finish

Report:

1. installed topology
2. preserved and removed context
3. domain files created or withheld
4. capability routing and gaps
5. project truth and contradictions
6. next proof
7. changed files and withheld global changes
