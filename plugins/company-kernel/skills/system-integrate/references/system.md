# Shared system

The system sits above projects. It should help across repositories without knowing the facts of any one of them.

## Home

Use `COMPANY_KERNEL_HOME` when set. Otherwise use:

```text
~/.company-kernel
```

The shared home contains:

```text
SYSTEM.md       the few beliefs used across consequential work
LENSES.md       a readable index
lenses/*        optional one-to-ten-line judgment
CAPABILITIES.md useful skill, tool, and access routing
```

## What belongs

A system line earns permanence when it changes what a capable current model notices, values, questions, or refuses across projects.

Good subjects include the changing capability frontier, product coherence, outcome ownership, market power, proof, writing, software quality, customer responsibility, economics, operations, and agent-system design.

## What does not belong

Keep project facts in `PROJECT.md`, current priorities in `.project/NOW.md`, procedures in skills, implementation rules in existing agent files, and mechanical enforcement in code or CI.

The system should get smaller as models improve. Delete lines that no longer change behavior.
