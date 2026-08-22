---
name: project-update
description: Create, refresh, audit, restructure, or graduate Company Kernel context after material changes to company truth, project truth, evidence, direction, boundaries, architecture, product, market, customer outcomes, or operating state. Do not use for routine implementation or unapproved shared-system changes.
license: MIT
metadata:
  author: Jacob Rhinehart
  version: "0.7.0"
---

# Project Update

Make the next capable agent start from what this company and project already earned.

Do not make it relive the whole history. Do not hand it only the final twenty percent of the conclusion.

## Modes

- **initialize:** compile the first accurate company and project model
- **refresh:** update durable truth after material evidence or decisions
- **audit:** find stale, missing, duplicated, unsupported, or misplaced context without writing
- **restructure:** split, merge, move, rename, or remove context that no longer earns its place
- **graduate:** move a learning upward to the narrowest level where it remains true

## Load the right context

Locate `KERNEL.md` through the active route, `COMPANY_KERNEL_HOME`, or `~/.company-kernel`.

Read the router, then only the system domains relevant to the change.

Read:

```text
COMPANY.md
PROJECT.md
.kernel/NOW.md
.kernel/company/<relevant domain>.md
.kernel/project/<relevant domain>.md
```

Do not load `REVIEW.md` unless the task challenges durable context rather than updating it from accepted evidence.

## Inspect before asking

Inspect applicable instructions, repository behavior, recent changes, product surfaces, tests, runtime evidence, docs, existing context, connected first-party sources, market outcomes, and customer outcomes available to the session.

Do not ask the user to inventory what the environment already shows.

Code proves capability and implementation. It does not prove the company thesis, market, promise, or authority.

## Classify every durable truth

Use the narrowest scope where the statement remains true:

**Now**

Fast-moving state that should survive the current session but may expire soon.

**Project**

Truth specific to this repository, product surface, implementation, campaign, or bounded outcome.

**Company**

Truth that should guide several projects: thesis, market position, product model, operating boundary, evidence, or cross-project decision.

**System review**

Evidence challenges transferable judgment in the shared kernel. Do not edit the system here. Route it to `$kernel-review`.

A project success does not automatically prove a universal principle.

A company decision should not be hidden in one project's technical file.

## Decide what deserves context

Store an item only when at least one is true:

- a capable model cannot safely infer it
- the model would likely infer it incorrectly
- rediscovering it would waste meaningful time
- it constrains future decisions
- it preserves hidden intent, authority, responsibility, or failure conditions
- evidence materially changed the current model
- the reasoning behind a compressed call is necessary for the call to transfer

Do not store ordinary implementation detail, generated summaries, task history, meeting chronology, or facts cheaper to retrieve from the source.

## Write the smallest complete model

Core files:

```text
COMPANY.md
PROJECT.md
.kernel/NOW.md
```

Optional domain files:

```text
.kernel/company/STRATEGY.md
.kernel/company/PRODUCT.md
.kernel/company/SOFTWARE.md
.kernel/company/DESIGN.md
.kernel/company/GTM.md
.kernel/company/CUSTOMER.md
.kernel/company/RESEARCH.md
.kernel/company/OPERATING.md

.kernel/project/<same domains>.md
```

Use `<kernel-home>/templates/DOMAIN.md` as a shape, not a questionnaire.

Create a domain file only when its absence can change future judgment. Omit empty sections. Split a file only when content changes at a different speed, belongs to different authority, or has become too large to steer work.

## Transfer the earned worldview

A strong context file should let a cold model understand:

- what is true
- why the truth matters
- what observation or decision produced it
- what distinction prevents a generic interpretation
- what it changes
- where it stops
- what evidence should reopen it

Use compressed concepts when they buy thought, not when they merely sound clever.

Every important section should leave the model able to make a decision it was less likely to make before reading it.

Assume intelligence. Never assume context.

## Update from evidence

Separate observation, inference, assumption, contradiction, and unknown.

Rewrite invalidated truth. Delete dead context. Preserve deliberate decisions and hidden constraints. Add dates or provenance only where freshness changes judgment.

Observed reality outranks stale files.

When evidence applies across projects, graduate it to company context. When it applies only here, keep it in the project. When it is still an active hypothesis, keep it in `NOW.md` or mark the bet explicitly.

Do not move a finding upward because it sounds important.

## Preserve authority

Update project context only when the active workflow grants project write authority.

Update company context only when the active workflow grants authority to change company truth.

Do not edit shared system files. Use `$kernel-review` for a qualified challenge.

Surface contradictions between explicit human direction, company truth, project truth, and observed reality rather than silently choosing the most convenient source.

## Finish

A capable new agent should be able to explain:

- what the company believes and is trying to become
- what this project owns
- where responsibility and authority stop
- how value is created and proved
- what is true in the relevant domains
- what is being tested now
- what evidence should change direction
- which learning graduated and why

Report context deltas, moved truth, unsupported claims removed, contradictions, remaining unknowns, and next proof.
