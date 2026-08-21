---
name: project-context
description: Use this skill to create, audit, reorganize, or refresh durable context for a startup or project after the agent environment is already integrated, especially when the repository is moving quickly, product or market direction changed, or agents lack a coherent current model. Read SYSTEM.md when present, preserve stronger local instructions, and create the smallest adaptive set of PROJECT.md plus linked project context files. Use $system-integrate instead when rules, skills, tools, or the project-level system context also need recompilation. Do not use for routine implementation, bug fixes, or ordinary documentation.
license: MIT
metadata:
  author: Jacob Rhinehart
  version: "0.3.0"
---

# Project Context

Keep the project model that a capable agent needs now.

This skill owns project compilation. It does not own the entire agent environment, replace local rules, or turn every uncertainty into a research program.

## Modes

Infer the mode from the request:

- **initialize:** create the first coherent project context when full environment integration is unnecessary
- **refresh:** reconcile existing context against current reality and rewrite stale truth
- **audit:** diagnose context quality without editing unless asked
- **restructure:** split, merge, rename, or remove context files when their current shape is hurting use

## Read upstream context

Read `SYSTEM.md` when it exists, then only the linked `.system/*.md` lenses relevant to the task. Treat them as the project's thin judgment layer and do not duplicate their lines in project facts.

If `SYSTEM.md` is absent and the task also involves instruction layers, installed skills, tools, or full first-run integration, use `$system-integrate` instead.

Read [references/frontier.md](references/frontier.md) on every run.

Read [references/context-shape.md](references/context-shape.md) before creating or restructuring files.

For a user-facing product, read [references/product-coherence.md](references/product-coherence.md).

For a commercial project or active market motion, read [references/market-power.md](references/market-power.md).

Read [references/project-types.md](references/project-types.md) when the project is not clearly a venture startup.

Read [references/evidence.md](references/evidence.md) when claims are uncertain, current external facts matter, or research may be required.

## Begin with the project

Inspect before asking the user to inventory it.

If shell access is available, run:

```sh
python3 scripts/scan_context.py --root .
```

Resolve the path relative to this skill directory, or use equivalent repository inspection when the script is unavailable.

Find and respect existing instruction sources and project context.

Read the repository, recent changes, product surfaces, tests, examples, and available first-party evidence that can materially improve the model.

Do not mistake code for complete company truth. Do not ignore code when prose disagrees with what the product actually does.

## Compile the model

Establish only what current evidence supports:

- the simplest accurate project or product truth
- what must become true
- why this is possible or important now
- actors, users, buyers, operators, systems, or other participants
- the core loop that creates and proves value
- the current responsibility and authority boundary
- the entry wedge
- the larger trajectory unlocked by winning it
- what the project refuses to become
- current evidence, contradiction, and uncertainty
- momentum, constraints, bets, and the present objective
- what compounds through use or operation

For a startup, hold the current wedge and destination company at the same time. Do not blur them into vague positioning.

For another project type, pursue the largest coherent consequence supported by its purpose rather than forcing venture language onto it.

## Choose the context set

Always optimize for use, not completeness.

A moving integrated project normally has:

```text
SYSTEM.md
.system/          optional thin lenses
PROJECT.md
.project/NOW.md
```

This skill normally writes `PROJECT.md` and `.project/*`. It may flag `SYSTEM.md` as stale, but should not rewrite the system layer unless the user explicitly includes it or invokes `$system-integrate`.

Create additional linked Markdown files only when cadence, authority, audience, ownership, risk, or real size justifies the split.

There is no required one-file-per-domain set. Several files may cover one important concern. Entire conventional functions may need no file.

Keep `PROJECT.md` short enough to load for consequential work. It should route to supporting context rather than absorb everything.

Do not create empty placeholders, speculative roadmaps, generic doctrine, or a second task tracker.

Use the seeds in [assets/PROJECT.seed.md](assets/PROJECT.seed.md) and [assets/NOW.seed.md](assets/NOW.seed.md) as starting shapes, not mandatory forms.

## Preserve truth quality

Distinguish:

- authorized direction
- observed evidence
- inference
- active bet
- unknown

Add dates or provenance to dynamic claims when staleness would matter.

Search or use connected evidence when a current fact could materially change the project model. Do not research by ritual. Use `$project-research` when a bounded uncertainty deserves a dedicated pass.

Rewrite invalidated truth. Do not append a newer contradiction beneath an older claim and call that memory.

Delete context that no longer improves decisions.

## Integrate carefully

Do not overwrite an existing instruction system.

Only modify an instruction file when the request explicitly asks to integrate or route project context.

Use the narrow route in [assets/ROUTE.md](assets/ROUTE.md), adapted to the host and existing file. If no `SYSTEM.md` exists, omit that clause rather than create a broken route.

## Finish

Verify that:

- a new capable agent can understand the project quickly
- `SYSTEM.md`, linked `.system` lenses, and project truth do not contradict each other
- the user-facing product remains simpler than the internal machinery
- GTM, product, onboarding, delivery, and proof describe the same promise
- the current objective is actually current
- the entry wedge visibly connects to a larger coherent trajectory
- uncertainty remains visible
- every created file earns its existence
- links resolve
- existing rules remain intact

Report:

1. what was created, changed, merged, or removed
2. the current project truth in one sentence
3. the most consequential remaining unknowns
4. any stale system line or instruction conflict the user should resolve
5. the next natural prompt for operating the project
