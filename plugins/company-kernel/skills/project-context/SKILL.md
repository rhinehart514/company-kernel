---
name: project-context
description: Create, audit, restructure, or refresh one project under the shared system. Use when project truth changes. Preserve local rules and write only the project files the repository needs. Do not use for routine implementation or whole-machine cleanup.
license: MIT
metadata:
  author: Jacob Rhinehart
  version: "0.4.0"
---

# Project context

Keep one project true and legible as it moves.

## Modes

- **initialize:** create the first project model
- **refresh:** rewrite stale truth after a material change
- **audit:** make calls without editing
- **restructure:** split, merge, rename, or remove context that no longer reads well

## Read the shared system

Locate the system from the active instruction route, `COMPANY_KERNEL_HOME`, or `~/.company-kernel`.

Read `SYSTEM.md`, then only the lenses relevant to this project and task. The system shapes judgment. It does not provide project facts.

If the shared system itself is stale or missing, report it and use `$system-integrate`. Do not create a project-local `SYSTEM.md`.

Read [context shape](references/context.md), [evidence](references/evidence.md), [project types](references/project-types.md), and [writing](references/writing.md).

## Inspect the project

Run the scanner when shell access exists:

```sh
python3 scripts/scan_context.py --root . --json
```

Read applicable instructions, repository behavior, recent changes, product surfaces, tests, docs, existing context, and first-party evidence.

Do not ask the user to inventory what the repository already shows. Code is evidence of capability, not complete company truth.

## Build the model

Establish only what current evidence supports:

- the simplest accurate project truth
- the outcome and why now
- actors, users, buyers, operators, systems, or beneficiaries
- the core loop that creates and proves value
- the responsibility and authority boundary
- the entry wedge and larger trajectory
- what the project refuses to become
- current evidence, contradiction, uncertainty, and momentum
- what compounds through use or operation

For a startup, keep the current entry and destination company distinct.

For another project type, pursue the largest coherent consequence supported by its purpose.

## Write the smallest useful set

Start with:

```text
PROJECT.md
.project/NOW.md
```

Add a file only when its content changes at a different speed, belongs to a different authority, or has become too large to stay useful.

Several files may cover one important concern. Entire conventional functions may need none.

Use [PROJECT.seed.md](assets/PROJECT.seed.md) and [NOW.seed.md](assets/NOW.seed.md) as shapes, not forms.

Rewrite invalidated truth. Delete dead context. Keep uncertainty visible. Add dates or provenance when freshness matters.

## Finish

Check that a capable new agent can explain the project, the product remains simpler than its machinery, product and GTM make the same promise, the current objective is current, and the entry visibly earns the trajectory.

Report the project truth, calls made, files changed, remaining unknowns, and next proof.
