---
name: project-context
description: Use this skill to create, audit, reorganize, or refresh durable context for a startup or project, especially when a repository is moving quickly, product or market direction changed, multiple instruction files exist, or agents lack a coherent current model. Inspect existing rules and evidence, preserve stronger local instructions, and create the smallest adaptive set of PROJECT.md plus linked project context files. Do not use for routine implementation, bug fixes, or ordinary documentation.
license: MIT
metadata:
  author: Jacob Rhinehart
  version: "0.2.0"
---

# Project Context

Build the project model that a capable agent needs now.

This skill owns context compilation. It does not own the project, replace local rules, or turn every uncertainty into a research program.

## Modes

Infer the mode from the request:

- **initialize:** create the first coherent context set
- **refresh:** reconcile existing context against current reality and rewrite stale truth
- **audit:** diagnose context quality without editing unless asked
- **restructure:** split, merge, rename, or remove context files when their current shape is hurting use

## Load the right lenses

Read [references/frontier.md](references/frontier.md) on every run.

Read [references/context-shape.md](references/context-shape.md) before creating or restructuring files.

For a user-facing product, read [references/product-coherence.md](references/product-coherence.md).

For a commercial project or active market motion, read [references/market-power.md](references/market-power.md).

Read [references/project-types.md](references/project-types.md) when the project is not clearly a venture startup.

Read [references/evidence.md](references/evidence.md) when claims are uncertain, current external facts matter, or research may be required.

## Begin with the environment

Inspect before asking the user to inventory the project.

If shell access is available, run:

```sh
python3 scripts/scan_context.py --root .
```

Resolve the path relative to this skill directory, or use equivalent repository inspection when the script is unavailable.

Find and respect existing instruction sources, including relevant `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, Copilot instructions, Cursor rules, skills, and project documentation.

Read the repository, recent changes, product surfaces, tests, examples, and any available first-party project evidence that can materially improve the model.

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

A moving project normally needs:

```text
PROJECT.md
.project/NOW.md
```

Create additional linked Markdown files only when cadence, authority, audience, or real size justifies the split.

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

Only modify an instruction file when the request explicitly asks to integrate or route the project context.

Use the narrow route in [assets/ROUTE.md](assets/ROUTE.md), adapted to the host and existing file. Merge it without weakening stronger rules.

If no instruction file exists and integration was requested, create the smallest appropriate one.

## Finish

Verify that:

- a new capable agent can understand the project quickly
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
4. any instruction conflict the user should resolve
5. the next natural prompt for operating the project
