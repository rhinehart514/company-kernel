# Portability

Company Kernel uses the open Agent Skills shape and keeps host-specific metadata separate.

## Skill locations

The installer supports common paths:

```text
~/.agents/skills
~/.claude/skills
~/.copilot/skills

.agents/skills
.claude/skills
.github/skills
```

Use an explicit target for another client:

```sh
python3 scripts/install.py --target /path/to/skills
```

## Shared system location

The default is client-neutral:

```text
~/.company-kernel
```

Set `COMPANY_KERNEL_HOME` when another path is required.

The integrator adds a small route to an instruction file the active client already reads. It does not assume every client loads arbitrary markdown automatically.

## Different clients, same layers

Clients differ in instruction precedence, skill discovery, tools, permissions, and context budgets.

The portable contract stays the same:

```text
shared system above projects
current project context in the repository
skills for repeated work
tools for access and action
existing local rules remain authoritative
```

Without shell access, the agent can inspect known files through repository tools.

Without web or connected data, it should preserve external unknowns rather than fabricate current truth.
