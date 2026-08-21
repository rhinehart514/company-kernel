---
name: system-integrate
description: Use this skill to integrate Company Kernel into an existing startup or project by inspecting global and project instructions, installed skills, available tools, repository state, and current context; then compile a thin project-specific system layer, minimally route it into the existing instruction system, rationalize capabilities, and initialize or refresh the project model. Use on first installation, major pivots, model or tool changes, skill sprawl, or agent-environment drift. Do not use for routine implementation or to rewrite global settings without explicit authority.
license: MIT
metadata:
  author: Jacob Rhinehart
  version: "0.3.0"
---

# System Integrate

Make the existing model environment right for this project, then compile the project inside it.

Do not stop at an inventory or recommendations unless the user requested an audit. A normal integration leaves behind thin system context, current project context, and a clearer capability environment.

## Modes

Infer the mode from the request:

- **integrate:** inspect, safely write, and produce the first complete environment
- **recompile:** reconcile after a pivot, major model change, new tools, or substantial skill drift
- **audit:** diagnose without writing
- **cleanup:** apply destructive project-local skill or instruction changes only when explicitly authorized

Global instruction, skill, tool, authentication, or permission changes always require explicit authority.

## Load only the judgment needed

Read [references/frontier.md](references/frontier.md) and [references/system-context.md](references/system-context.md) on every run.

Read [references/instructions.md](references/instructions.md) before changing instruction layers.

Read [references/capabilities.md](references/capabilities.md) and [references/tools.md](references/tools.md) before routing or building capability.

Read [references/skill-design.md](references/skill-design.md) only when creating, rewriting, merging, or retiring a skill.

Read [references/project-compilation.md](references/project-compilation.md) before writing project context.

## Inspect before asking

If shell access is available, run:

```sh
python3 scripts/scan_environment.py --root . --json
```

Resolve the script path relative to this skill directory. When it is unavailable, perform equivalent inspection with the host's repository and filesystem tools.

Inspect:

- applicable global, ancestor, and project instruction sources
- installed global and project-local skills
- visible runtime tools and connectors plus on-disk configuration surfaces
- existing `SYSTEM.md`, `.system/*`, `PROJECT.md`, and linked `.project/*`
- repository behavior, recent work, product surfaces, tests, and documentation
- available first-party project evidence
- current external reality only where it could materially change the project

Do not ask the user to inventory information the environment can expose. Do not read or reproduce secrets merely to prove a tool configuration exists.

## Establish the preliminary project model

Understand enough of the project to identify:

- the simplest accurate product or project truth
- the current user, actor, or beneficiary
- the outcome and core loop
- the entry wedge and larger trajectory
- the responsibility and authority boundary
- the current objective and momentum
- the capabilities the project repeatedly needs
- the frontier changes or inherited constraints that matter here

This is working synthesis, not another artifact. It exists so the system layer can be project-specific.

## Compile the system layer first

Create or reconcile root `SYSTEM.md` before finalizing durable project context.

`SYSTEM.md` contains a title and **one to ten non-empty steering lines**. It is additive project-level system context, not a replacement for the host's system prompt or existing repository rules.

Each line must earn permanence by changing what a capable current model notices, values, questions, or refuses for this project.

Create optional `.system/*.md` lenses when a recurring subset of work needs additional judgment that should not occupy every consequential task. Every lens:

- contains a title and one to ten steering lines
- is linked from `SYSTEM.md`
- owns a real tension, scarcity, boundary, or taste
- contains no project facts, task state, or workflow manual

Do not create one lens per department. Several lenses may exist around product or market work while conventional functions with no distinctive judgment have none.

Good candidates include project-specific judgment about product coherence, market power, GTM engineering, agent authority, reliability, adoption, or maintainability. Names should reflect the actual project tension, not an org chart.

Avoid duplicating stronger existing instructions. Rewrite stale system context instead of appending another doctrine layer.

Use [assets/SYSTEM.seed.md](assets/SYSTEM.seed.md) and [assets/LENS.seed.md](assets/LENS.seed.md) as shapes, never boilerplate.

When shell access is available, validate the result:

```sh
python3 scripts/validate_system.py --root .
```

## Integrate the route

When writing is authorized, merge the narrow route in [assets/ROUTE.md](assets/ROUTE.md) into the closest appropriate existing instruction file.

Preserve stronger implementation, safety, permission, coding, and deployment rules.

If no instruction file exists, create the smallest appropriate project-local instruction file. Do not create several client-specific copies unless the project actually uses those clients and the route cannot be shared.

## Rationalize capabilities

Judge the combined environment against this project, not against an imaginary complete company org chart.

For each materially relevant capability, decide whether to:

- **keep:** already strong and properly scoped
- **route:** useful but poorly activated or confused with another capability
- **merge:** genuinely duplicated in trigger, judgment, authority, and result
- **rewrite:** useful but stale, bloated, host-bound, or compensating for an old model weakness
- **retire:** persistent context no longer improves current frontier models
- **build:** a repeated gap deserves a project-local skill, script, adapter, or context surface
- **expose:** the capability exists as a tool or connected source but is not reachable or legible
- **leave missing:** the capability cannot yet be supplied reliably

Do not assume one skill per domain. A project may need several distinct GTM capabilities and no generic GTM skill, several product capabilities and no single product skill, or one capability that crosses conventional functions.

Prefer routing over destructive merging when the distinction is uncertain.

Create `.project/CAPABILITIES.md` only when durable routing materially improves future work. Use [assets/CAPABILITIES.seed.md](assets/CAPABILITIES.seed.md) as a shape.

## Build only what earns persistence

When a real gap survives the base model, existing skills, and available tools, build the smallest durable capability that closes it.

```text
missing project truth         -> project context
missing durable project taste -> thin .system lens
missing non-obvious workflow  -> skill
missing deterministic work    -> script
missing access or current data -> tool, connector, or explicit gap
one-time task                 -> do the task; do not create infrastructure
```

New project-local skills should follow [references/skill-design.md](references/skill-design.md) and may begin from [assets/SKILL.seed.md](assets/SKILL.seed.md).

Do not silently delete or rewrite user-maintained global capabilities.


## Compile the project

After the system layer exists, create or refresh the project model in the same run.

Normally begin with:

```text
PROJECT.md
.project/NOW.md
```

Create additional files only when cadence, authority, audience, ownership, risk, or real size justifies them. Several files may cover one important concern and entire conventional functions may need none.

Keep the user-facing product easier to understand than the internal machinery. Hold the current entry and destination project simultaneously. Rewrite stale truth instead of preserving contradictory eras for archival ambiance.

Use `$project-context` for later project-only refreshes.

## Verify

The integration is successful only when:

- root `SYSTEM.md` and every linked lens contain one to ten high-information lines
- a capable new agent can understand the current project quickly
- product, GTM, onboarding, delivery, and proof describe the same responsibility
- the current wedge visibly unlocks a larger coherent trajectory
- relevant existing skills and tools are easier to use than before
- redundant capability is routed or clearly identified rather than blindly stacked
- newly built capability has a real repeated job
- stronger local rules remain intact
- uncertainty and missing access remain visible

## Return the transformation

Report, in this order:

1. the compiled system context and active lenses
2. the current project truth in one sentence
3. context created, rewritten, merged, or removed
4. capabilities kept, routed, merged, rewritten, retired, built, exposed, or still missing
5. the sharpest product-coherence finding
6. the most consequential frontier unlock
7. the largest remaining uncertainty and next proof
8. any global change deliberately not made without further authority
