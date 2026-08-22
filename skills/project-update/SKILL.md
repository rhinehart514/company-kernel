---
name: project-update
description: Create, refresh, audit, or restructure Company Kernel project models after material changes to technical truth, product responsibility, market position, evidence, bets, constraints, or direction. Do not use for routine implementation or shared-system changes.
license: MIT
metadata:
  author: Jacob Rhinehart
  version: "0.6.0"
---

# Project Update

Keep one project true enough that a capable new agent can move without founder re-briefing.

## Modes

- **initialize:** create the first project model
- **refresh:** update durable truth after material evidence
- **audit:** find stale, missing, duplicated, or unsupported context without writing
- **restructure:** split, merge, rename, or remove context that no longer earns its place

## Load the right context

Locate `KERNEL.md` through the active route, `COMPANY_KERNEL_HOME`, or `~/.company-kernel`.

Read the shared kernel and only the system standards relevant to the project change. Do not load review files unless the task is actually a review.

## Inspect before asking

Inspect applicable instructions, repository behavior, recent changes, product surfaces, tests, docs, existing project files, connected first-party evidence, and real market or customer outcomes available to the session.

Do not ask the user to inventory what the repository already shows. Code proves capability, not complete company truth.

## Decide what deserves durable context

Store an item only when at least one is true:

- a capable model cannot safely infer it
- the model would likely infer it incorrectly
- rediscovering it would waste meaningful time
- it constrains future decisions
- it preserves hidden intent, authority, or responsibility
- evidence materially changed the current model

Do not store ordinary implementation detail, generated summaries, task history, or facts cheaper to retrieve from the source.

## Write the smallest complete model

Start with:

```text
PROJECT.md
.kernel/NOW.md
```

Create domain files only when earned:

- `.kernel/CODING.md` for Technical Truth
- `.kernel/PRODUCT.md` for Product Model
- `.kernel/GTM.md` for Market Position

Use `templates/` as shapes, not questionnaires. Omit empty sections. Split a domain only when content changes at a different speed, belongs to different authority, or has become too large to steer judgment.

## Update from evidence

Separate observation, inference, assumption, contradiction, and unknown.

Rewrite invalidated truth. Delete dead context. Preserve deliberate decisions and hidden constraints. Add dates or provenance only where freshness changes judgment.

Observed reality outranks stale files. Do not edit shared system standards. Route a credible standards challenge to `$kernel-review`.

## Finish

A capable new agent should be able to explain:

- what the project is
- what outcome it owns
- where responsibility stops
- how value is created and proved
- what is true in the relevant domains
- what is being tested now
- what evidence should change direction

Report model deltas, unsupported claims removed, contradictions, remaining unknowns, and next proof.
