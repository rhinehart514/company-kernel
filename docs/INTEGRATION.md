# Integration

`$system-integrate` works across the shared environment and one active project.

## Shared home

The default system home is:

```text
~/.company-kernel
```

Use `COMPANY_KERNEL_HOME` or an explicit path when the environment needs another location.

The integrator may create or update files in the shared home when the user asked for system integration. It does not delete unrelated global instructions, skills, tool settings, authentication, or permissions.

## Inventory

Run the included scanner when shell access exists:

```sh
python3 plugins/company-kernel/skills/system-integrate/scripts/scan_environment.py --root . --json
```

The scanner finds instruction files, skills, exact skill duplicates, tool configuration paths, shared system context, project context, and Git state.

It reads metadata, not secrets. Tool configuration on disk does not prove that a tool is active in the current session.

## Build the shared system

The integrator starts from the packaged system library, compares it with the user's existing rules, and writes only what remains useful.

Strong system line:

```text
Keep ambition large and the user's product model small.
```

Weak system line:

```text
First research the market, then create a plan, then ask for approval.
```

The first is judgment. The second is a procedure and belongs in a skill, if it belongs anywhere.

## Clean up capabilities

A capability can be kept, routed, combined, rewritten, retired, built, exposed, or left missing.

The integrator decides what the gap actually is:

```text
missing judgment  skill or system lens
missing truth     project context
missing data      tool or connector
repeatable mechanics script
one-time work     do the work
```

Project-local changes are the default proving ground. Shared global changes stay proposals unless the user clearly authorized them.

## Build the project

After the shared system is ready, the integrator creates or refreshes `PROJECT.md` and `.project/NOW.md` inside the active repository.

The shared system shapes judgment. The project files state what is true now. They should not repeat each other.
