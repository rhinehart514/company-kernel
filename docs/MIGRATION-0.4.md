# Migration from 0.4

Version 0.4 separated shared system context from project context. Version 0.5 makes the operating topology explicit.

## Replaced

```text
SYSTEM.md + LENSES.md + many thin lenses
```

becomes:

```text
KERNEL.md
standards/CODING.md
standards/PRODUCT.md
standards/GTM.md
reviews/*
```

The old lens library mixed domain judgment, cross-domain capabilities, and external reconsideration. Version 0.5 gives each a distinct job.

## Project layout

```text
PROJECT.md
.project/NOW.md
.project/*
```

becomes:

```text
PROJECT.md
.kernel/NOW.md
.kernel/CODING.md
.kernel/PRODUCT.md
.kernel/GTM.md
```

Only relevant domain files are created.

## Skills

- `$system-integrate` becomes `$kernel-integrate`
- `$project-context` becomes `$project-model`
- `$project-research` is replaced by `$kernel-review` for standards and model reconsideration

Ordinary research should use the best available research capability in the environment. It no longer needs a mandatory Company Kernel wrapper.

## Migration rule

Do not copy old prose into new files mechanically. Recompile current judgment and project truth against repository reality. Preserve stronger user-authored rules and useful evidence.
