# System integration

`$system-integrate` is the first-run compiler for the full agent environment around one project.

## The promise

A successful run should leave:

- thinner permanent steering
- clearer instruction authority
- installed skills that have distinct jobs
- existing tools used before new machinery is proposed
- missing access distinguished from missing judgment
- a thin system layer
- a current project model beneath it
- an explicit list of changes withheld for permission

## Inventory

The included scanner can inspect common project and user locations:

```sh
python3 plugins/company-kernel/skills/system-integrate/scripts/scan_environment.py \
  --root .
```

JSON output:

```sh
python3 plugins/company-kernel/skills/system-integrate/scripts/scan_environment.py \
  --root . \
  --json
```

It discovers instruction files, skills, exact skill duplicates, duplicate skill names, tool configuration paths, and Git state.

It does not dump instruction bodies or secrets. The agent reads selected files after the inventory.

Tool configuration on disk is not proof that a tool is connected or available in the current host session.

## System compilation

The integrator selects only the beliefs and judgment the project needs from the frontier reference. Root `SYSTEM.md` carries the project-wide compression; optional linked `.system/*.md` lenses carry additional one-to-ten-line judgment for selected work.

A system file is not a small procedure. It is a small prior.

Strong:

```text
Increasing capability should make the product clearer, not larger.
Treat generated persuasion as cheap and proof as scarce.
```

Weak:

```text
First research the market, then create a plan, then ask the user...
```

The second belongs in a skill, if it belongs anywhere.

Validate a compiled system:

```sh
python3 plugins/company-kernel/skills/system-integrate/scripts/validate_system.py --root .
```

## Capability reconciliation

The integrator judges every relevant capability against the current model and project.

A skill should survive only when it adds repeated value through:

- distinctive judgment
- a reliable workflow
- project-specific environment knowledge
- deterministic scripts or assets
- evidence and stopping rules the base model would not infer consistently

A new skill is not the default response to a missing result.

```text
no current data       -> connect evidence
repetitive mechanical work -> script it
unclear project truth -> update context
repeated judgment gap -> create or improve a skill
model cannot do it    -> expose the limitation
```

## Skill creation

Project-local is the default proving ground.

A new skill should have:

- a specific job
- positive and negative triggers
- an expected artifact or state change
- minimal instructions
- references only when needed
- scripts only for deterministic work
- trigger and behavior cases

The skill description is routing policy. It should front-load the job and trigger because hosts may shorten descriptions when many skills are installed.

## Project compilation

After system context and capabilities are coherent, the integrator follows `$project-context` in the same run.

This produces the current product or project truth, current state, evidence, boundaries, and trajectory inside the newly compiled judgment environment.

System context must not absorb project facts. Project context must not repeat system doctrine.

## Integration report

The final report is part of the product experience.

It should tell the user what actually changed across:

```text
system
project
instructions
skills
tools
frontier
coherence
trajectory
authority
next proof
```

A report that only says “created SYSTEM.md and PROJECT.md” has missed the point rather efficiently.
