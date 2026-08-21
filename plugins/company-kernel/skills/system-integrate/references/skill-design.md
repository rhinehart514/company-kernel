# Skill design

A skill is persistent capability for work the current model should not have to reconstruct from scratch every time.

## Before creating one

Require:

- a repeated job
- a clear positive trigger
- a clear negative boundary
- a meaningful result or artifact
- distinctive judgment, workflow, environment knowledge, or deterministic resources
- evidence that project context, existing skills, and available tools are insufficient

Do not create a skill to restate the system worldview, impersonate a job title, or make one prompt reusable once.

## Description

The description is routing policy.

Front-load what the skill does, when it should trigger, and the important negative boundary. Keep it specific enough to survive truncation when many skills are installed.

## Body

Keep `SKILL.md` focused on:

- inputs and authority
- relevant evidence
- key decisions
- tool or script use
- output or state change
- stopping and verification

Move deep material to focused references. Put deterministic mechanics in scripts. Put reusable templates in assets.

Do not explain broad capabilities the current model already demonstrates reliably.

## Scope

Prefer project-local skills for project-specific data, workflows, language, tools, and judgment.

Prefer user-level skills for durable capabilities that remain useful across unrelated repositories.

Do not create one skill per domain. Create as many or as few as repeated capabilities justify.

## Evaluation

Before retaining a new or rewritten skill, test at minimum:

- three prompts that should trigger
- three adjacent prompts that should not trigger
- two representative behavior cases
- one case where existing project rules must win

Check the trace and resulting state, not only the final prose.

## Mutation

When merging or replacing skills:

- preserve distinctive behavior and resources
- keep the old skill disabled until the replacement works
- update routing and descriptions
- avoid duplicate names because hosts may show both rather than merge them
- record what was intentionally retired and why
