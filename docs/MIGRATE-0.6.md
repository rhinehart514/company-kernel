# Migrate from 0.6

0.6 separated shared standards from project models.

0.7 keeps that distinction and finishes the hierarchy:

```text
SYSTEM -> COMPANY -> PROJECT -> WORK
```

It also expands the system from Coding, Product, and GTM to eight complete domains while making the normal runtime more selective.

## What changed

### Shared system

0.6:

```text
kernel/KERNEL.md
kernel/standards/
kernel/review/
```

0.7:

```text
kernel/KERNEL.md
kernel/CONTEXT.md
kernel/STRATEGY.md
kernel/PRODUCT.md
kernel/SOFTWARE.md
kernel/DESIGN.md
kernel/GTM.md
kernel/CUSTOMER.md
kernel/RESEARCH.md
kernel/OPERATING.md
kernel/CAPABILITIES.md
kernel/REVIEW.md
```

The flat system is easier to route, inspect, install, and change. `REVIEW.md` remains cold-path context.

### Local context

0.6:

```text
PROJECT.md
.kernel/NOW.md
.kernel/CODING.md
.kernel/PRODUCT.md
.kernel/GTM.md
```

0.7:

```text
COMPANY.md
PROJECT.md
.kernel/NOW.md
.kernel/company/<DOMAIN>.md
.kernel/project/<DOMAIN>.md
```

Company truth no longer hides inside project files. Project truth no longer repeats the system.

## Install the new system

From the 0.7 source checkout:

```sh
python3 scripts/install.py --user --force
```

Preview first when installed system files may contain user-authored changes:

```sh
python3 scripts/install.py --user --dry-run
```

Preserve stronger custom judgment before replacing Company Kernel-owned files.

## Move recognized project files

Preview:

```sh
python3 ~/.company-kernel/bin/init.py \
  --root /path/to/project \
  --migrate \
  --dry-run
```

Apply:

```sh
python3 ~/.company-kernel/bin/init.py \
  --root /path/to/project \
  --migrate
```

Mechanical moves:

```text
.kernel/CODING.md  -> .kernel/project/SOFTWARE.md
.kernel/PRODUCT.md -> .kernel/project/PRODUCT.md
.kernel/GTM.md     -> .kernel/project/GTM.md
```

The migration preserves content exactly. It does not claim that old content is correctly scoped.

## Recompile the context

Run:

```text
$project-update Audit and rewrite this migrated 0.6 context for Company Kernel 0.7.
Separate company truth, project truth, current state, and stale system doctrine.
Preserve earned decisions and evidence. Delete duplication. Create optional domain
files only where missing context can change future decisions.
```

Review every migrated statement:

- Does it apply across projects? Move it to `COMPANY.md` or `.kernel/company/<DOMAIN>.md`.
- Is it specific to this project? Keep it in `PROJECT.md` or `.kernel/project/<DOMAIN>.md`.
- Is it temporary? Move it to `.kernel/NOW.md`.
- Is it reusable judgment? Remove the duplicate and rely on the system domain.
- Is it unsupported or stale? Delete or mark the uncertainty.

## Replace routes

Run initialization once. It appends or refreshes a marked Company Kernel block inside `AGENTS.md` while preserving everything outside the markers.

Remove old unmarked Company Kernel routes only after confirming the new route resolves the installed system.

Do not leave two routes pointing to different topologies.

## Rename Coding to Software

The domain now owns architecture, implementation, interfaces, tests, deployment, reliability, observability, maintenance, migrations, and agentic engineering.

`SOFTWARE.md` names that full responsibility more accurately than `CODING.md`.

Do not keep both as aliases. Aliases create two places for technical judgment to drift.

## Validate

From the source repository:

```sh
python3 scripts/validate.py
```

From a migrated project:

```sh
python3 ~/.company-kernel/bin/scan.py --root /path/to/project --json
```

The scan should show:

- one installed marked route
- `COMPANY.md`, `PROJECT.md`, and `.kernel/NOW.md`
- optional company and project domains only where earned
- no legacy flat `.kernel/CODING.md`, `.kernel/PRODUCT.md`, or `.kernel/GTM.md`
- no duplicate skills or stale system paths

## The migration is complete when

A cold agent can distinguish the operating world, company belief, project truth, and current work without loading every domain or asking the founder to reconstruct the decisions that produced them.
