# Instruction judgment

Instruction systems already have authority, scope, and precedence. Discover those before adding another layer.

## Classify before changing

For each instruction, decide whether to:

- **keep:** distinctive, current, and in the right scope
- **move:** valuable but belongs in a skill, project context, test, or narrower directory
- **compress:** several lines restate one useful steering belief
- **resolve:** it conflicts with a stronger or closer instruction
- **retire:** the current model, repository, or project no longer benefits from it

Do not judge by age or length alone. A single precise deployment rule may matter more than a page of generic reasoning advice.

## Put each kind of context in the right layer

```text
durable project taste and priors -> SYSTEM.md or a thin .system lens
current project truth            -> PROJECT.md or .project/*
fast-changing objective          -> .project/NOW.md
repeatable non-obvious work      -> skill
implementation and safety rules  -> existing AGENTS/CLAUDE/GEMINI/etc.
deterministic enforcement        -> code, tests, CI, policy, or permissions
one-time intent                  -> current task
```

Do not copy the same rule into every client-specific file merely to make it feel installed.

## Authority

Treat global and shared user instructions as read-only unless the user explicitly delegates changes at that scope.

For project-local integration, preserve stronger safety, permission, implementation, deployment, and approval rules. Add only the narrow route required to make system and project context discoverable.

When precedence is uncertain, report the conflict rather than declaring one worldview victorious through filesystem enthusiasm.

## Thinness

Remove generic reminders that capable current models already perform reliably unless an eval shows the reminder materially changes behavior.

A permanent instruction must earn its context cost through distinctive taste, project truth, a recurring failure, an authority boundary, or a proven operational constraint.
