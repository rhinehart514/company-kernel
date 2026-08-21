# Portability

Company Kernel uses the open Agent Skills directory shape and keeps host-specific metadata optional.

## Portable core

Each skill contains:

```text
SKILL.md
references/
assets/
scripts/
evals/
agents/openai.yaml
```

`SKILL.md`, references, assets, scripts, and evals carry the portable behavior.

`agents/openai.yaml` configures the OpenAI interface and explicit invocation policy without changing the core skill.

## Skill discovery

Clients differ in where they load skills and how they merge instructions.

The installer supports common locations:

```text
user Agent Skills     ~/.agents/skills
project Agent Skills  .agents/skills
user Claude skills    ~/.claude/skills
project Claude skills .claude/skills
user Copilot skills   ~/.copilot/skills
project Copilot       .github/skills
```

Use an explicit target for another host:

```sh
python3 scripts/install.py --target /path/to/skills
```

## Instruction discovery

Company Kernel does not assume that every client loads `SYSTEM.md` or follows links automatically.

When integration is requested, it adds a narrow route to the closest instruction source already recognized by the host. It does not replace the user's instruction system.

Codex, Claude Code, Gemini, Copilot, Cursor, and later hosts may differ in:

- global instruction locations
- project precedence
- nested overrides
- skill scope
- implicit invocation
- tool permissions
- context budgets

The system scanner inventories common locations. The model must inspect the actual host environment before mutating it.

## Global safety

User-level instructions and skills are shared across projects. They are read-only by default.

The integrator may:

- identify duplication
- propose exact edits
- create a project-local replacement
- recommend disabling an obsolete skill

It must not silently delete or rewrite global work.

## Tool portability

The scanner records common tool-configuration paths but does not claim a tool is active.

The host's actual exposed tools are the runtime source of truth.

Host-specific tool adapters can be added later without changing the system and project context model.

## Graceful degradation

Without shell access, the agent can inspect known files using repository tools.

Without web or connected evidence, it can compile only supported internal truth and preserve external unknowns.

Without cross-skill invocation, `$system-integrate` can read the packaged `$project-context` instructions directly and complete both layers in one run.

Without any recognized instruction file, the integrator can create the smallest host-appropriate route only when asked.
