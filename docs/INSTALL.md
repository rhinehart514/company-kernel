# Install and first run

## Codex plugin

```sh
codex plugin marketplace add rhinehart514/company-kernel --ref main
codex plugin add company-kernel@company-kernel
```

Then run `$kernel-setup` from an active project.

## Portable install

```sh
python3 scripts/install.py --user
```

This installs:

- the three skills into the selected client skill directory
- the canonical kernel into `~/.company-kernel`
- `scan.py` into `~/.company-kernel/bin`

Use another kernel home with:

```sh
python3 scripts/install.py --user --kernel-home /path/to/kernel
```

Install project-local skills with:

```sh
python3 scripts/install.py --project /path/to/project
```

## First setup

Run from a real repository:

```text
$kernel-setup Set up Company Kernel 0.6 on this machine and initialize this repository.
Inspect existing global rules, skills, tools, shared kernel files, and project context first.
Preserve stronger work. Install or reconcile the canonical kernel, add the smallest routes,
and create only the project models this repository actually needs.
```

The setup should leave:

```text
~/.company-kernel/
PROJECT.md
.kernel/NOW.md
.kernel/<DOMAIN>.md only where earned
```

## Route shape

Global route:

```text
Company Kernel lives at ~/.company-kernel/KERNEL.md.
For consequential project work, follow that route and load only relevant domain standards.
Preserve stronger safety, permission, and user rules.
```

Project route:

```text
For consequential work, read ~/.company-kernel/KERNEL.md, PROJECT.md,
.kernel/NOW.md, and only the matching .kernel/<DOMAIN>.md files.
Use system standards as judgment and project files as current truth.
```

Do not paste the whole kernel into `AGENTS.md`. That defeats the system with impressive efficiency.
