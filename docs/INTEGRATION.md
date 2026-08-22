# Integration

`$kernel-integrate` builds the shared kernel above projects, then initializes the active project.

## Shared home

Use `COMPANY_KERNEL_HOME` when set. Otherwise use:

```text
~/.company-kernel
```

## Inspect first

The integrator inspects applicable global and project instructions, installed skills, available tools, tool configuration paths, existing kernel files, project context, repository behavior, Git state, and first-party evidence.

It reads metadata, not secrets. A configuration path does not prove a tool is active in the current session.

## Reconcile rather than stack

Preserve stronger user-authored instructions. Remove stale Company Kernel duplication. Do not rewrite unrelated global rules, skills, authentication, permissions, or tool configuration.

## Install the shared kernel

Create or reconcile:

```text
KERNEL.md
CAPABILITIES.md
standards/*
reviews/*
```

System standards are active runtime judgment. Review files are cold-path references.

## Map capabilities

For each repeated need, decide whether it is already owned by the model, an instruction, a skill, a tool, a connector, a script, or nothing reliable yet.

Do not infer duplication from names. Do not build a new skill for one-time work. Keep project-local changes as the default proving ground.

## Add routes

Add one small route to the global instruction file the active client reads and one project route when needed. Preserve all stronger local rules.

## Initialize the project

Create `PROJECT.md`, `.kernel/NOW.md`, and only the domain models supported by the repository and current work.

Do not create Coding, Product, and GTM files merely for symmetry.
