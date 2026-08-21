# Company Kernel

**Compile the agent environment around the project you are actually building.**

Company Kernel is a portable context system for ambitious startups and fast-moving projects. It inspects the rules, skills, tools, repository, and project context already present; writes a tiny project-specific system layer; then compiles the smallest current project model and capability set that makes frontier models materially better at operating it.

It does not replace your existing `AGENTS.md`, install one synthetic executive per department, or assume every missing capability can be solved with another prompt file. Human civilization remains safe from at least that particular folder tree.

[Start here](START-HERE.md)

## The first run

Run one skill:

```text
$system-integrate Integrate this project. Inspect the existing system instructions, installed skills, available tools, repository, and current context. Compile a 1-10 line SYSTEM.md, preserve stronger local rules, rationalize the capability set, then initialize or refresh PROJECT.md and only the supporting context this project needs. Do not stop at an audit.
```

A moving startup will usually end up with:

```text
SYSTEM.md
.system/          optional thin lenses
PROJECT.md
.project/
  NOW.md
  ...only the additional context and capability routing this project earns
```

### `SYSTEM.md` and optional `.system/*`

`SYSTEM.md` contains one to ten project-specific lines of beliefs, taste, and judgment. A recurring specialized judgment may earn its own one-to-ten-line `.system/<LENS>.md`; several may cover one important concern and entire conventional domains may need none.

It translates the current frontier into this project: what inherited constraint should be questioned, what the product must remain, what scarce factors matter, how the wedge connects to the larger company, and how existing capabilities should be used without being stacked into sludge.

It is additive project context, not a replacement hidden system prompt.

When one recurring judgment deserves selective loading, Kernel may add a `.system/<LENS>.md` file. Every lens is also limited to 1-10 lines, and `SYSTEM.md` links to it. A startup may need product-coherence, market-power, and GTM-engineering lenses while needing no generic strategy file. Another project may need none.

### `PROJECT.md`

The compressed current truth and context map.

### `.project/NOW.md`

The fast-changing objective, momentum, bets, constraints, contradictions, and next evidence.

### Adaptive supporting context

Additional files exist only when a real boundary of cadence, authority, audience, risk, or size improves the work:

```text
.project/
  PRODUCT.md
  PRODUCT-SURFACES.md
  USER-LOOP.md
  MARKET.md
  ACCOUNT-SIGNALS.md
  SALES-MOTION.md
  DISTRIBUTION.md
  DELIVERY.md
  AGENT-AUTHORITY.md
  ECONOMICS.md
  EVIDENCE.md
  CAPABILITIES.md
```

There may be several files and several skills around one important concern, and none around another. The system does not reward symmetry.

## The capability pass

`$system-integrate` also inspects what the environment can already do.

For relevant skills, tools, scripts, and connected evidence, it decides whether to:

- keep them
- route them more clearly
- combine genuine duplicates
- retire obsolete scaffolding
- expose an available but underused tool or source
- build a missing project-local skill, script, adapter, or context surface
- leave a capability explicitly missing when access or reliability does not exist

It distinguishes missing judgment from missing data, missing access, deterministic work, and one-time work. A new skill has to beat the current model and the existing environment, not merely possess a plausible folder name.

Global skills, instructions, tools, authentication, and permissions are not destructively changed without explicit authority.

## What it optimizes for

The project becomes more ambitious while becoming easier for the user to understand.

The current wedge remains clear without capping the destination company.

Product capability expands without turning into a pile of surfaces.

GTM, onboarding, product behavior, delivery, and proof describe the same responsibility.

Project context is rewritten as reality changes rather than accumulated into a museum of expired beliefs.

Better models should require less persistent steering over time.

## Included skills

### `$system-integrate`

The flagship first run and major recompile.

Use it when:

- installing the Kernel into an existing environment
- global and project instructions have become layered or contradictory
- skills have multiplied without clear routing
- the model, tool set, or capability frontier changed materially
- the startup pivoted or no longer feels like one coherent product
- missing capability may require building a skill, script, adapter, or tool connection

### `$project-context`

Refresh the project model after product, market, responsibility, evidence, economics, or current direction moves. It reads `SYSTEM.md` but does not recompile the whole machine.

### `$project-research`

Resolve one uncertainty that could change the project model. It researches to change a decision, weaken a belief, expose contradiction, or confirm that no update is warranted.

## Installation

### Codex plugin

```sh
codex plugin marketplace add rhinehart514/company-kernel --ref main
codex plugin add company-kernel@company-kernel
```

Start a new Codex session after installation.

### Portable Agent Skills

Clone or download the repository, then install into the shared Agent Skills location:

```sh
python3 scripts/install.py --user
```

Or install inside one project:

```sh
python3 scripts/install.py --project /path/to/project
```

The installer copies skills only. It does not edit instructions or project files before the integrator has inspected them.

Use `--client claude`, `--client copilot`, or `--target PATH` when a client expects another skills directory.

## Operating loop

First integration:

```text
$system-integrate Integrate this project and apply safe project-local changes.
```

Project-only refresh:

```text
$project-context Refresh the project context against the repository, recent work, and available evidence. Rewrite stale truth; do not append history.
```

Bounded research:

```text
$project-research Determine whether [uncertainty] changes [decision or project belief]. Use current evidence, look for contradiction, and update project context only if reality changed.
```

Major environment recompile:

```text
$system-integrate Recompile after the model, skills, tools, and product direction changed. Preserve global files unless I explicitly authorize changes.
```

Read [First run](docs/FIRST-RUN.md), [Integration](docs/INTEGRATION.md), [Architecture](docs/ARCHITECTURE.md), [Portability](docs/PORTABILITY.md), and [Evaluation](docs/EVALUATION.md) for the machinery hidden behind the simple experience.

## Validate

No dependencies are required.

```sh
python3 scripts/validate.py
```

## License

MIT.
