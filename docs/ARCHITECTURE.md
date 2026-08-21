# Architecture

Company Kernel separates what should stay shared from what changes inside one project.

```text
SYSTEM
shared beliefs, taste, judgment, capability routing
        ↓
PROJECT
current truth for one repository
        ↓
TASK
what must happen now
        ↓
REALITY
what proves us right or wrong
```

## System

The system sits above projects. The default home is:

```text
~/.company-kernel/
  SYSTEM.md
  LENSES.md
  lenses/
  CAPABILITIES.md
```

`SYSTEM.md` contains one to ten lines that should shape consequential work across projects.

`lenses/*` contains optional one-to-ten-line judgment for product, market, software, research, design, operations, and other recurring work.

`CAPABILITIES.md` explains which skills, tools, and sources own which jobs. It is a map, not a prompt.

The system may coexist with `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, Cursor rules, Copilot instructions, and other user context. It adds a thin operating worldview. It does not replace safety, permissions, coding conventions, or personal preferences.

## Project

Each repository owns its current truth:

```text
PROJECT.md
.project/NOW.md
.project/*
```

`PROJECT.md` is the short model every consequential task should understand.

`.project/NOW.md` changes faster. It holds the objective, momentum, bets, constraints, contradictions, and next proof.

Additional files exist only when content changes at a different speed, belongs to a different authority, or has become too large to stay useful.

## Skills, tools, and rules

```text
system lens     durable judgment
project context current truth
skill           repeated non-obvious capability
tool            access or external action
script          deterministic work
rule            implementation, safety, or permission boundary
task            current intent
```

Do not solve missing data with prose. Do not solve one-time work with a permanent skill. Do not put current project facts into the shared system.

## Order of work

The first integration runs in this order:

1. inspect existing global and project context
2. build or reconcile the shared system
3. clean up skill and tool routing
4. add the smallest routes to existing instructions
5. build or refresh the current project model
6. report the calls, changes, unknowns, and next proof

System first. Project second. Reality last and always authoritative.
