# Company Kernel 0.7

**Give the model the world, the company, and the project before asking it to change any of them.**

Frontier models already know how to code, research, design, write, and sell. They do not begin with your resolved worldview, the company's earned beliefs, the project's hidden decisions, or the evidence that should change direction.

Company Kernel installs that missing context without loading an operating manual into every task.

## The stack

```text
SYSTEM
2026 context + reusable domain judgment
        ↓
COMPANY
truth that should survive across projects
        ↓
PROJECT
truth specific to this repository or outcome
        ↓
WORK
what must become true now
        ↓
EVIDENCE
update the narrowest level where the learning remains true
```

More specific context narrows broader context. It does not silently replace it.

A project can choose one market without turning that choice into universal strategy. A successful project deviation can update company truth without rewriting the system. A genuinely transferable lesson can be proposed back to the kernel.

## The hot path stays small

Normal work does not load every file.

The router identifies which domains can change the decision, then reads only:

1. the system router
2. the relevant system domains
3. `COMPANY.md` and matching company domain files that exist
4. `PROJECT.md`, `.kernel/NOW.md`, and matching project domain files that exist
5. the immediate task

A local bug fix should not inhale Strategy, GTM, and Customer. A launch should not pretend it is only a code change.

## System files

The canonical shared kernel installs to `~/.company-kernel` by default:

```text
KERNEL.md        routing, precedence, and context inheritance
CONTEXT.md       the 2026 operating environment
STRATEGY.md      what game to play and how bets compound
PRODUCT.md       what should exist and what the product should own
SOFTWARE.md      how systems become real, safe, and changeable
DESIGN.md        how the product explains itself and earns trust
GTM.md           how the market discovers, believes, and buys
CUSTOMER.md      how the promised outcome actually happens
RESEARCH.md      how uncertainty becomes decision-changing evidence
OPERATING.md     how whole outcomes are owned across domains
CAPABILITIES.md  model, instruction, skill, tool, and script routing
REVIEW.md        the cold path for changing durable context
```

These files contain judgment, not company facts.

## Project shape

Initialization creates only three context files and one thin route:

```text
AGENTS.md
COMPANY.md
PROJECT.md
.kernel/
  NOW.md
```

Optional truth earns a file only when it changes future decisions:

```text
.kernel/
  company/
    STRATEGY.md
    PRODUCT.md
    GTM.md
    ...
  project/
    PRODUCT.md
    SOFTWARE.md
    DESIGN.md
    ...
```

`COMPANY.md` owns the company identity, thesis, promise, boundary, and current direction.

`PROJECT.md` owns the outcome, responsibility, product boundary, core loop, proof, and non-goals of one project.

`.kernel/NOW.md` owns fast-moving state: the current outcome, active bets, live unknowns, blocks, and next proof.

Company domain files preserve truth that should survive across projects. Project domain files preserve truth that is local to this project. Missing files are not a defect.

## Install

### Codex plugin

```sh
codex plugin marketplace add rhinehart514/company-kernel --ref main
codex plugin add company-kernel@company-kernel
```

Then run from an active project:

```text
$kernel-setup Install or reconcile Company Kernel 0.7 and initialize this repository.
Inspect existing rules, skills, tools, company context, project context, and repository evidence first.
Preserve stronger work. Add only the context this company and project have earned.
```

### Portable install

```sh
python3 scripts/install.py --user --init-project /path/to/project
```

This installs the shared kernel, the three operating skills, project templates, `scan.py`, and `init.py`. It then initializes the project without replacing existing files.

Install without touching a project:

```sh
python3 scripts/install.py --user
```

Initialize later:

```sh
python3 ~/.company-kernel/bin/init.py --root /path/to/project
```

Preview either operation with `--dry-run`.

## The three skills

### `$kernel-setup`

Install, migrate, reconcile, or audit the shared kernel and one active project. It inspects the environment before writing and preserves stronger existing rules.

### `$project-update`

Update company or project truth after evidence, direction, boundaries, architecture, product, market, or operating state materially changes. It moves learning upward only as far as it remains true.

### `$kernel-review`

Review a qualified challenge to system, company, or project context. Shared system changes remain human-approved. The kernel does not become an autonomous constitution-writing hobbyist.

## The writing standard

Assume intelligence. Never assume context.

A cold model should understand why an important call exists, what changed in the environment, what remains scarce, what old default no longer deserves obedience, and what decision should become different.

Bad context transfers rules.

Good context transfers judgment.

Exceptional context transfers ambition.

Every domain file should leave the model able to think a useful thought that was less likely before it read the file.

See [`docs/WRITING.md`](docs/WRITING.md).

## What 0.7 refuses to build

- no dashboard
- no context database
- no permanent reflection agent
- no automatic system mutation
- no one-skill-per-department bureaucracy
- no generated company truth presented as fact
- no requirement to load every domain
- no duplicate system and project doctrine

The scarce thing is judgment, not Markdown production.

## Validate

```sh
python3 scripts/validate.py
```

The validator checks the full runtime, installer, initializer, idempotence, route preservation, migration detection, scanner, examples, plugin metadata, and skill shapes.

## Read next

- [Codebase map](docs/CODEBASE.md)
- [Install and first run](docs/INSTALL.md)
- [Migrate from 0.6](docs/MIGRATE-0.6.md)
- [Writing system context](docs/WRITING.md)

MIT.
