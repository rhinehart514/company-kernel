---
name: project-model
description: Create, refresh, audit, or restructure Company Kernel project models after material changes to technical truth, product responsibility, market position, evidence, bets, constraints, or direction. Do not use for routine implementation or shared-system changes.
license: MIT
metadata:
  author: Jacob Rhinehart
  version: "0.5.0"
---

# Project model

Keep one project true enough for a capable agent to move without founder re-briefing.

## Modes

- **initialize:** create the first project model
- **refresh:** update durable truth after material evidence
- **audit:** identify stale, missing, duplicated, or unsupported context without writing
- **restructure:** split, merge, rename, or remove context that no longer earns its place

## Read the kernel

Locate `KERNEL.md` through the active route, `COMPANY_KERNEL_HOME`, or `~/.company-kernel`.

Read the kernel route, then only the system standards relevant to this project change. Do not load review files unless the task is actually a review.

Read [model judgment](references/model.md), [evidence](references/evidence.md), and [writing](references/writing.md).

## Inspect before asking

Run:

```sh
python3 scripts/scan_project.py --root . --json
```

Inspect applicable instructions, repository behavior, recent changes, product surfaces, tests, docs, current project models, and first-party evidence.

Do not ask the user to inventory what the repository already shows. Code proves capability, not complete company truth.

## Build only what earns a place

Start with:

```text
PROJECT.md
.kernel/NOW.md
```

Create `.kernel/CODING.md`, `.kernel/PRODUCT.md`, or `.kernel/GTM.md` only when that domain materially affects work and the project has truth worth preserving.

Use the assets as shapes, not forms. Omit empty sections. Several files may cover one domain when content changes at different speeds or belongs to different authority, but do not reward symmetry.

## Update from evidence

Rewrite invalidated truth. Delete dead context. Preserve deliberate decisions and hidden constraints. Mark assumptions and contradictions. Add dates or provenance only where freshness changes judgment.

Observed reality outranks stale files. Do not edit shared system standards. Route a credible standards challenge to `$kernel-review`.

## Finish

A capable new agent should be able to explain the project, select relevant system standards, identify valid choices and boundaries, understand current bets, and name the next evidence that should change direction.

Report the calls, model deltas, unsupported claims removed, remaining unknowns, and next proof.
