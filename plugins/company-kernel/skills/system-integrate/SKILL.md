---
name: system-integrate
description: Build the shared system above projects, clean up rules, skills, and tools, then initialize the active repository. Use for first setup or major environment change. Do not use for routine project updates or silent global cleanup.
license: MIT
metadata:
  author: Jacob Rhinehart
  version: "0.4.0"
---

# System integrate

Build the shared system first. Build the project second.

## Modes

- **integrate:** create or reconcile the shared system, then initialize the project
- **recompile:** refresh the system after a material model, tool, rule, or capability change
- **audit:** inspect and make calls without writing
- **cleanup:** apply destructive shared changes only when the user clearly authorized them

## Read

Read [the system model](references/system.md), [capability judgment](references/capabilities.md), [skill judgment](references/skills.md), [tool judgment](references/tools.md), and [writing](references/writing.md).

Use the packaged [system source](references/system/SYSTEM.md) and [lens index](references/system/LENSES.md) as starting judgment, not boilerplate.

## Inspect before asking

Run the scanner when shell access exists:

```sh
python3 scripts/scan_environment.py --root . --json
```

Inspect applicable global and project instructions, installed skills, runtime tools, tool configuration paths, existing shared system context, project context, repository behavior, recent changes, and available first-party evidence.

Do not ask the user to inventory what the environment can show. Do not read or print secrets just because a configuration path exists.

## Build the shared system

Use `COMPANY_KERNEL_HOME` when set. Otherwise use `~/.company-kernel`.

Create or reconcile:

```text
SYSTEM.md
LENSES.md
lenses/*
CAPABILITIES.md
```

`SYSTEM.md` and every active lens contain one to ten non-empty steering lines. They express durable beliefs, taste, tensions, and boundaries that can help across projects.

Do not put project facts, current priorities, feature state, or procedures in the shared system.

Compare the source library with the user's existing rules. Keep only what adds value. Preserve strong user-authored judgment. Rewrite stale duplication instead of stacking another layer.

Validate the result when possible:

```sh
python3 scripts/validate_system.py --system-home ~/.company-kernel
```

## Reconcile capabilities

Judge the model, instructions, skills, tools, scripts, and connected evidence together.

For each relevant capability, make a call: keep, route, combine, rewrite, retire, build, expose, or leave missing.

Do not infer duplication from names. Do not force one skill per department. Several GTM or product capabilities may remain separate when they own different jobs.

Build project-local first. Shared global skills, instructions, tools, authentication, and permissions stay unchanged unless the user clearly authorized that scope.

Write the useful routing and known gaps to `CAPABILITIES.md`. Do not turn it into an inventory dump.

## Add routes

When authorized, add one small route to the global instruction file the active client already reads. Add one small project route when the repository needs it.

Use [GLOBAL-ROUTE.md](assets/GLOBAL-ROUTE.md) and [PROJECT-ROUTE.md](assets/PROJECT-ROUTE.md) as shapes. Replace the system path with the real path.

Keep existing safety, permissions, coding, deployment, and approval rules intact.

## Build the project

After the shared system is ready, follow [project compilation](references/project.md) and create or refresh:

```text
PROJECT.md
.project/NOW.md
```

Add more project files or project-local capabilities only when the work earns them.

## Report the result

Lead with judgment, not filesystem telemetry:

1. **Project truth**
2. **The calls**
3. **Product coherence**
4. **Frontier unlock**
5. **Trajectory**
6. **Shared system**
7. **Capability changes**
8. **Next proof**

Put changed files and withheld global changes last.
