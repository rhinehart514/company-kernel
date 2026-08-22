---
name: kernel-integrate
description: Install or reconcile Company Kernel 0.5, map capabilities, add thin routes, and initialize the active project. Use for first setup, migration, major environment changes, or a broken kernel. Do not use for routine project work or silent global cleanup.
license: MIT
metadata:
  author: Jacob Rhinehart
  version: "0.5.0"
---

# Kernel integrate

Build the shared kernel first. Build the project second.

## Modes

- **install:** create the 0.5 kernel and initialize the active project
- **reconcile:** repair drift, duplication, routing, or capability changes
- **audit:** inspect and make calls without writing
- **migrate:** recompile a 0.4 installation into the 0.5 topology

## Inspect before asking

Run the scanner when shell access exists:

```sh
python3 scripts/scan_environment.py --root . --json
```

Inspect applicable global and project instructions, installed skills, available tools, tool configuration paths, existing Company Kernel files, repository behavior, Git state, and first-party evidence.

Do not ask the user to inventory what the environment can show. Do not print secrets.

## Reconcile the shared kernel

Use `COMPANY_KERNEL_HOME` when set. Otherwise use `~/.company-kernel`.

Create or reconcile the packaged files under `assets/system/`:

```text
KERNEL.md
CAPABILITIES.md
standards/*
reviews/*
```

Preserve stronger user-authored judgment. Remove stale Company Kernel duplication rather than stacking another layer. Do not rewrite unrelated global rules, skills, authentication, permissions, or tool configuration.

## Map capabilities

For every material repeated need, make one call: model-owned, instruction-owned, skill-owned, tool-owned, script-owned, missing, duplicated, or unclear.

Write only useful routing and material gaps to `CAPABILITIES.md`. Do not turn it into an inventory dump. Do not build a skill for one-time work.

## Add routes

Add the smallest route to the global instruction file the active client already reads. Add a project route only when needed.

Use `assets/GLOBAL-ROUTE.md` and `assets/PROJECT-ROUTE.md` as shapes. Replace `<SYSTEM_HOME>` with the real path. Preserve stronger rules.

## Initialize the active project

Create `PROJECT.md`, `.kernel/NOW.md`, and only the domain models the repository needs. Use the project assets bundled with `$project-model` when available.

Do not create Coding, Product, and GTM files for symmetry. Do not invent missing company truth from code.

## Report

Lead with:

1. the installed topology
2. the domain calls
3. the project truth
4. capability routing and gaps
5. unknowns and next proof
6. changed files and withheld global changes
