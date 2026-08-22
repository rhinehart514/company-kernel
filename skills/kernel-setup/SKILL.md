---
name: kernel-setup
description: Install, migrate, reconcile, or audit Company Kernel 0.7 across the shared system and one active project. Use for first setup, version migration, broken routing, model or tool changes, capability sprawl, or context topology changes. Do not use for routine project work or silent global cleanup.
license: MIT
metadata:
  author: Jacob Rhinehart
  version: "0.7.0"
---

# Kernel Setup

Make the machine and one active project legible to a frontier model without making normal work carry the whole operating system.

## Modes

- **setup:** install the system and initialize the project
- **migrate:** replace Company Kernel-owned 0.6 structure with 0.7
- **reconcile:** repair stale routes, system files, capabilities, or project shape
- **audit:** inspect and make the calls without writing

## Inspect before asking

Use `scripts/scan.py` from the source repository or `<kernel-home>/bin/scan.py` after installation.

Inspect:

- global and project instruction files
- existing Company Kernel files and routes
- installed skills and exact duplicates
- tool configuration paths and connected capabilities
- `COMPANY.md`, `PROJECT.md`, and `.kernel/` context
- legacy 0.6 context
- Git state and recent repository behavior
- first-party product, technical, market, and customer evidence

Do not ask the user to inventory what the environment can show. Do not read or print secrets because a config path exists.

## Install the system

Use `COMPANY_KERNEL_HOME` when set. Otherwise use `~/.company-kernel`.

Install the twelve canonical runtime files:

```text
KERNEL.md
CONTEXT.md
STRATEGY.md
PRODUCT.md
SOFTWARE.md
DESIGN.md
GTM.md
CUSTOMER.md
RESEARCH.md
OPERATING.md
CAPABILITIES.md
REVIEW.md
```

Also install `templates/`, `bin/init.py`, and `bin/scan.py`.

Use `scripts/install.py --user` from source for portable installation. Use `--force` only after comparing changed installed files with the canonical version and preserving stronger user-authored work.

Delete stale Company Kernel duplication instead of stacking another route or doctrine layer.

Never rewrite unrelated global rules, authentication, permissions, tool configuration, or user-owned skills.

## Initialize the project

Run `scripts/init.py` from source or `<kernel-home>/bin/init.py` after installation.

The smallest complete local model is:

```text
AGENTS.md             thin route, preserving existing rules
COMPANY.md            cross-project company truth
PROJECT.md            project-specific truth
.kernel/NOW.md        fast-moving state
```

Create optional files only when durable truth earns them:

```text
.kernel/company/<DOMAIN>.md
.kernel/project/<DOMAIN>.md
```

Do not create all domains for symmetry. Do not invent company truth from code. Use repository evidence to prefill what it can prove and leave consequential unknowns explicit.

## Migrate 0.6 safely

Recognized project moves are:

```text
.kernel/CODING.md  -> .kernel/project/SOFTWARE.md
.kernel/PRODUCT.md -> .kernel/project/PRODUCT.md
.kernel/GTM.md     -> .kernel/project/GTM.md
```

Preserve content exactly during the mechanical move. Then use `$project-update` to rewrite it into the stronger system, company, and project model.

Do not mechanically copy old system standards into company or project truth.

Preserve ambiguous legacy files for review rather than deleting them.

## Compile current truth

After installation, inspect the company and project as they actually exist.

Use this test for durable context:

- a capable model cannot safely infer it
- the model would likely infer it incorrectly
- rediscovery would waste meaningful time
- it constrains future decisions
- it preserves hidden intent, authority, responsibility, or evidence

State enough of the world behind an important conclusion that a cold model can extend it. Do not preserve only the final slogan. Do not turn the file into a conversation archive.

## Reconcile capabilities

Judge the model, context, skills, tools, connectors, scripts, and evidence together.

For each material repeated need, make one call:

- model-owned
- instruction-owned
- skill-owned
- tool-owned
- script-owned
- human-owned
- missing
- duplicated
- unclear

Do not infer duplication from names. Do not build a skill for one-time work. Record only useful routing and material gaps in `CAPABILITIES.md`.

## Finish

Report:

1. installed system and version
2. route added, replaced, or withheld
3. preserved and migrated context
4. company and project truth created or withheld
5. optional domain files created and why each earned existence
6. capability routing, duplicates, and gaps
7. contradictions and unresolved authority
8. next proof
9. changed files and withheld global changes

A successful setup lets the user return to normal work immediately. It should not require a ceremony before every task.
