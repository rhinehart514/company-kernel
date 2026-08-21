# Architecture

## The layers

Company Kernel separates five things that are routinely mixed together:

```text
PRIORS
Distinctive beliefs and taste.

SKILLS
Repeatable verbs for compiling and researching context.

PROJECT CONTEXT
Current truth for one project.

HOST INSTRUCTIONS
The user's existing rules, permissions, conventions, and tool policy.

REALITY
Repository state, users, market evidence, operations, analytics, and external change.
```

The portable system has soft authority over judgment. It has no right to erase stronger local rules.

## Why multiple files

A moving project contains truths that change at different speeds.

One giant file becomes stale because durable identity, current objective, technical detail, market evidence, and active bets are edited for different reasons. One file per business function is not better; it imports an org chart the project may not have.

Company Kernel splits context when one of four boundaries is real:

- **cadence:** durable truth versus fast-moving state
- **authority:** authorized direction versus evidence, inference, or personal preference
- **audience:** context every agent needs versus context only one class of work needs
- **size:** a concern has become too large to remain legible inside the root file

A fast-moving project normally gets `PROJECT.md` and `.project/NOW.md`. Everything else must earn existence.

## `PROJECT.md`

The root file is a compressed model and route, not a business plan.

It usually carries:

- the simplest accurate product or project truth
- what must become true
- why this is possible or important now
- the actors and user mental model
- the core value loop
- current responsibility and boundary
- entry wedge and larger trajectory
- links to supporting project context
- an `as of` date

It should remain short enough that consequential work can load it cheaply.

## `.project/NOW.md`

`NOW.md` is deliberately disposable.

It carries:

- the current objective
- momentum
- active bets
- constraints
- decisions in motion
- contradictions
- the next evidence that matters

It is rewritten, not archived. Git already has a hobby.

## Additional context

The skill can create any additional Markdown files that improve judgment. Examples include `PRODUCT.md`, `MARKET.md`, `DELIVERY.md`, `ECONOMICS.md`, `EVIDENCE.md`, or project-specific names.

The rule is not one file per domain. A product with several genuinely distinct surfaces may need `PRODUCT.md`, `USER-LOOP.md`, and `AGENT-AUTHORITY.md`. A research project may need no market file at all.

## The project compiler

`$project-context` is a compiler in the loose but useful sense:

```text
existing instructions
repository and product
recent changes
available company evidence
current external reality
founder direction
        ↓
inspect, reconcile, judge, compress
        ↓
PROJECT.md + linked adaptive context
```

It should not merely document the company a founder described. It should notice where current capabilities, market structure, evidence, or product behavior imply a different boundary.

It must also resist founder and model fantasy by preserving contradiction and uncertainty.

## Persistent steering

The skills carry a small frontier lens:

- intelligence and software production are increasingly abundant
- judgment, coherence, trust, distribution, attention, and reality remain scarce
- the current product should be easy to understand even when the destination company is enormous
- cheap implementation removes a natural governor on feature sprawl
- company and product boundaries inherited from expensive intelligence deserve reconsideration
- strong evidence can kill attractive beliefs
- context itself accumulates debt

These are priors, not compulsory conclusions.

## Tool use

The skills are tool-agnostic. They use the host's repository access, browser, search, connectors, code execution, or other capabilities when those materially improve the project model.

The research obligation is framed around evidence, not a ritual number of calls or sources.

One capable agent is the default. Parallel work is useful only when the research divides into independent, high-value streams.

## Updates

Context is refreshed after a material project-model change, not after every implementation change.

Material changes include:

- product truth
- user or buyer
- responsibility boundary
- current wedge
- market motion
- pricing or economics
- delivery model
- accumulating advantage
- major evidence or contradiction
- current objective

A large diff may change none of these. A one-line pricing decision may change several.
