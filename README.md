# Company Kernel

**Give a capable agent the project it is actually operating.**

Company Kernel is a portable context system for ambitious startups and fast-moving projects. It helps an agent inspect the repository, existing rules, current evidence, and outside reality, then build the smallest set of project context files that keeps the work coherent.

It does not replace your `AGENTS.md`, install a synthetic management team, or force every project into one giant company document. Humanity has produced enough blank strategy templates.

[Start here](START-HERE.md)

## The experience

Run one skill:

```text
$project-context Initialize this project. Inspect the existing instructions and repository, preserve stronger local rules, and create the smallest context set that makes the project clear and current. Integrate a minimal route into the existing instructions without replacing them.
```

For a moving startup, the result usually begins with:

```text
PROJECT.md
.project/
  NOW.md
  ...only the additional context this project needs
```

`PROJECT.md` is the compressed project truth and map.

`.project/NOW.md` carries the fast-changing objective, momentum, bets, constraints, and next evidence.

Additional files are created only when a real separation of cadence, authority, or complexity improves the model. They can be named for the project rather than copied from an org chart:

```text
.project/
  PRODUCT.md
  PRODUCT-SURFACES.md
  MARKET.md
  SALES-MOTION.md
  DELIVERY.md
  ECONOMICS.md
  EVIDENCE.md
  ADOPTION.md
  POLICY.md
```

There may be several files around one concern and none around another. The system does not reward symmetry.

## What it is optimizing for

The project should become more ambitious while becoming easier for a user to understand.

The current wedge should be clear without capping the destination company.

Product capability should expand without turning the product into a pile of surfaces.

GTM, onboarding, product behavior, delivery, and customer proof should describe the same company.

Project context should be rewritten as reality changes, not accumulated into a museum of expired beliefs.

Existing repository rules remain authoritative for implementation.

## Included skills

### `$project-context`

Create, audit, reorganize, or refresh the project context set.

Use it when:

- starting or inheriting a project
- product or market direction materially changed
- agents keep misunderstanding what the project is
- context has become stale, contradictory, or scattered
- the repo contains several competing instruction files
- a moving startup needs its current truth and momentum compressed again

Do not use it for routine code changes.

### `$project-research`

Resolve one uncertainty that could change the project model.

Use it for current capability shifts, customer or market questions, GTM structure, regulation, technical feasibility, economics, responsibility boundaries, or other external facts that could change a real decision.

It is not a generic research-report generator. Its job is to change a decision, weaken a belief, or confirm that no project change is warranted.

## Installation

### Codex plugin

```sh
codex plugin marketplace add rhinehart514/company-kernel --ref main
codex plugin add company-kernel@company-kernel
```

Start a new Codex session after installation.

### Portable Agent Skills

Clone or download this repository, then install into the shared Agent Skills location:

```sh
python3 scripts/install.py --user
```

Or install the skills inside one repository:

```sh
python3 scripts/install.py --project /path/to/project
```

The installer copies only the skills. It does not edit the target project's instructions or create project context. The skill handles that after inspecting the project.

Use `--client claude`, `--client copilot`, or `--target PATH` when a client expects another skills directory.

## Daily use

Initialize once:

```text
$project-context Initialize this project and integrate it minimally.
```

Refresh after a material company or project change:

```text
$project-context Refresh the project context against the repository, recent work, and available evidence. Rewrite stale truth; do not append history.
```

Audit without writing:

```text
$project-context Audit the current context for product incoherence, stale beliefs, missing momentum, conflicting instructions, and a wedge that no longer connects to the larger trajectory. Do not edit files.
```

Resolve a consequential unknown:

```text
$project-research Determine whether recent browser-agent reliability changes let this project own the workflow instead of merely assisting it. Update project context only if the evidence materially changes the model.
```

## Design

```text
thin persistent steering
        +
progressively loaded skills
        +
current repository and connected evidence
        +
adaptive project context
        +
reality
```

The model supplies broad intelligence. Company Kernel supplies distinctive taste, evidence obligations, context shape, and a repeatable way to keep a moving project legible.

Read [Architecture](docs/ARCHITECTURE.md), [Portability](docs/PORTABILITY.md), and [Evaluation](docs/EVALUATION.md) for the machinery hidden behind the simple first run.

## Validate

No dependencies are required.

```sh
python3 scripts/validate.py
```

## License

MIT.
