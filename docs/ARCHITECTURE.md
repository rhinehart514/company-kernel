# Architecture

Company Kernel compiles two different kinds of context around an existing agent environment.

```text
EXISTING ENVIRONMENT
instructions + skills + tools + model capability
        ↓
SYSTEM CONTEXT
thin persistent steering
        ↓
PROJECT CONTEXT
current project truth and state
        ↓
REALITY
repository + users + market + operations + evidence
```

## Existing environment

The environment already has authority, capability, and history:

- global and project instruction files
- user and repository skills
- plugins and scripts
- tools and connected systems
- model-specific behavior
- repository conventions and tests

Company Kernel inspects this environment before adding anything. It has no default right to replace global work.

## System context

System context answers:

> What should shape judgment across consequential work in this project?

The preferred shape is:

```text
SYSTEM.md
.system/
  ...only the thin lenses this project needs
```

Every newly created system file contains one to ten non-empty steering lines, excluding its title.

System context carries beliefs, taste, judgment, authority, and negative identity. It does not carry current market facts, feature state, tasks, or procedures.

Several lenses may cover one important concern. A project is not required to have `STRATEGY.md`, `PRODUCT.md`, `GTM.md`, or any other symmetrical set.

Examples:

```text
.system/PRODUCT-COHERENCE.md
.system/OUTCOME-OWNERSHIP.md
.system/GTM-ENGINEERING.md
.system/PROOF.md
.system/AGENT-AUTHORITY.md
```

## Project context

Project context answers:

> What is true about this project now?

A moving project normally starts with:

```text
PROJECT.md
.project/NOW.md
```

`PROJECT.md` is durable compression and routing. It normally carries the project truth, desired outcome, why now, actors, core loop, responsibility boundary, entry wedge, negative identity, trajectory, and links to supporting context.

`.project/NOW.md` carries the current objective, momentum, bets, constraints, contradictions, decisions in motion, and next evidence.

Additional files split around real differences in:

- cadence
- authority
- audience
- ownership
- risk
- size

The project may need several product files, several market files, and no strategy file. Context follows the actual model of the project rather than an assumed organization chart.

## Capability environment

Skills, tools, scripts, and context solve different problems:

```text
system lens      persistent judgment or taste
skill            repeated capability or workflow
project context  current truth
connector/tool   access or external action
script           deterministic operation
model            ambiguous reasoning and synthesis
```

The integrator evaluates existing skills as keep, route, merge, rewrite, disable, or create.

It does not infer redundancy from names. Two design skills may be complementary. Two differently named skills may be exact duplicates.

New project-local capabilities are preferred before promoting something to user scope.

## Compilation order

The flagship integration runs in this order:

1. inventory instructions, skills, tools, context, repository, and evidence
2. establish mutation authority
3. compile or reconcile thin system context
4. reconcile instructions and capabilities
5. compile or refresh project context beneath the system layer
6. validate links, line limits, current truth, and instruction preservation
7. report the transformation and withheld changes

The order matters. Project context should be built inside the judgment environment that will later use it.

## Context routing

The closest appropriate instruction source may receive one narrow route:

```text
For consequential work, read SYSTEM.md and PROJECT.md, then only the linked
.system and .project files relevant to the task.
```

The route does not paste the system or project model into `AGENTS.md`. Existing repository instructions continue to own implementation conventions and permissions.

## Mutation boundaries

When integration was explicitly requested, Company Kernel may create or update project-local:

- system context
- project context
- routing instructions
- skills
- scripts
- eval fixtures

User-level skills, global instructions, shared plugins, and tool configuration remain read-only unless broader authority was explicit.

Disabling is preferred to deleting until a replacement has been proven.

## Recompilation

Use `$project-context` when the project model changes.

Use `$system-integrate` when the environment changes materially:

- a new model removes old scaffolding needs
- skills are added, duplicated, or no longer useful
- tools or connected evidence change
- instruction precedence becomes confusing
- the project now needs different persistent judgment

System and project context are rewritten rather than accumulated. Git stores history. Current context stores current truth.
