# Capabilities

Use the strongest capability already available before adding another layer.

A model, instruction, skill, tool, connector, script, or person can all carry work. They should not all carry the same work.

## Route by what the need actually is

**Model-owned**

Use the model directly when the work is one-time, judgment-heavy, well-supported by current context, and does not require a repeatable mechanical procedure.

**Instruction-owned**

Use system, company, or project context when a durable belief, boundary, decision, or way of reasoning should change future work.

**Skill-owned**

Use a skill when a repeated non-obvious workflow needs inspection, judgment, tool use, and a consistent finish. A skill should teach behavior, not duplicate a domain file.

**Tool-owned**

Use a tool or connector when the work depends on external capability, current data, an account, a system of record, or a write outside the repository.

**Script-owned**

Use a script when the operation is deterministic, testable, and should behave the same without model judgment.

**Human-owned**

Keep people on decisions requiring authority, relationship, taste, accountability, sensitive judgment, or a commitment the agent cannot safely make.

## Current Company Kernel routes

- installation, migration, environment reconciliation, and initialization: `$kernel-setup`
- company and project context updates: `$project-update`
- qualified context challenges and amendment proposals: `$kernel-review`
- deterministic installation: `bin/install.py` after installation, or `scripts/install.py` in source
- deterministic project initialization: `bin/init.py` after installation, or `scripts/init.py` in source
- deterministic inspection: `bin/scan.py` after installation, or `scripts/scan.py` in source
- repository validation: `scripts/validate.py` in source

External research should use the strongest available source, research tool, connected system, experiment, or direct evidence. `RESEARCH.md` governs judgment; it is not a substitute for access.

## Inspect before adding

Before creating a capability, check:

- whether the model can already perform the work from better context
- whether an installed skill already owns the workflow
- whether an available tool exposes the real system of record
- whether a deterministic script is safer
- whether the need is temporary
- whether the new capability duplicates another name or surface
- whether the company should own the problem at all

Do not infer duplication from names alone.

Do not make a skill for one task.

Do not wrap a tool in ceremony merely to call it agentic.

Do not keep a capability because it once mattered.

## Record only useful routing

This file is not an inventory of everything installed on a machine.

Record a capability only when future agents need to know:

- where a repeated need routes
- what authority or access the capability carries
- what evidence it can and cannot provide
- what material gap remains
- which duplicate should be removed
- which capability is intentionally preferred

A long capability catalog makes the model spend context deciding among tools that never mattered.

## Capability gaps

A missing capability deserves work when it repeatedly blocks an important outcome, forces unsafe improvisation, creates expensive rediscovery, or prevents credible evidence.

Name the gap before choosing the implementation.

The answer may be better context, a new skill, a connector, a small script, a product change, or a human relationship.

## Done

Capability routing is healthy when the model can find the right leverage quickly, repeated needs have one clear owner, deterministic work is not improvised, judgment is not buried in scripts, and the environment gains power without gaining an equal amount of machinery.
