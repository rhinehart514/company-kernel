# Install and first run

## Fast path

From a source checkout:

```sh
python3 scripts/install.py --user --init-project /path/to/project
```

This installs the shared system and three skills, then initializes the project without replacing existing context.

The project receives:

```text
AGENTS.md
COMPANY.md
PROJECT.md
.kernel/NOW.md
```

No optional company or project domain files are created automatically.

Open the project and work normally. The route in `AGENTS.md` loads only context relevant to the decision.

## Codex plugin

```sh
codex plugin marketplace add rhinehart514/company-kernel --ref main
codex plugin add company-kernel@company-kernel
```

Then run from an active project:

```text
$kernel-setup Install or reconcile Company Kernel 0.7 and initialize this repository.
Inspect existing global rules, skills, tools, shared system files, company context,
project context, and repository evidence first. Preserve stronger work. Add only
context this company and project have earned.
```

## Portable install

Install for the current user:

```sh
python3 scripts/install.py --user
```

Install skills inside one project instead:

```sh
python3 scripts/install.py --project /path/to/project
```

Use another client skill path:

```sh
python3 scripts/install.py --user --client claude
python3 scripts/install.py --user --client copilot
```

Use an explicit kernel home:

```sh
python3 scripts/install.py --user --kernel-home /path/to/kernel
```

Preview writes:

```sh
python3 scripts/install.py --user --init-project /path/to/project --dry-run
```

Replace changed Company Kernel-owned installed files after review:

```sh
python3 scripts/install.py --user --force
```

`--force` does not rewrite unrelated user files. Project initialization still preserves existing core context and edits only the marked route inside `AGENTS.md`.

## What installs

Shared system:

```text
~/.company-kernel/
  KERNEL.md
  CONTEXT.md
  STRATEGY.md
  PRODUCT.md
  SOFTWARE.md
  DESIGN.md
  GTM.md
  CUSTOMER.md
  RESEARCH.md
  OPERATING.md
  CAPABILITIES.md
  REVIEW.md
  templates/
  bin/
    init.py
    scan.py
```

Skills install to the selected client skill directory:

```text
kernel-setup/
project-update/
kernel-review/
```

## Initialize later

```sh
python3 ~/.company-kernel/bin/init.py --root /path/to/project
```

Use a custom kernel home:

```sh
python3 /path/to/kernel/bin/init.py \
  --root /path/to/project \
  --kernel-home /path/to/kernel
```

Preview:

```sh
python3 ~/.company-kernel/bin/init.py --root /path/to/project --dry-run
```

## Route shape

Initialization appends one marked block to the existing `AGENTS.md` or creates the file when missing.

```text
<!-- company-kernel:route:start -->
## Company Kernel

System entry: `~/.company-kernel/KERNEL.md`.

For consequential work, follow system -> company -> project -> work.

Read COMPANY.md, PROJECT.md, and .kernel/NOW.md. Load only relevant system,
company-domain, and project-domain files.
<!-- company-kernel:route:end -->
```

Text outside the markers is preserved. Running initialization again replaces only the marked block and otherwise leaves the file unchanged.

Do not paste the full kernel into `AGENTS.md`. That converts selective context into an expensive wallpaper pattern.

## Fill the first context

The initializer creates safe shapes. `$kernel-setup` should inspect the repository and available first-party evidence to compile an accurate starting point.

Keep the levels distinct:

- `COMPANY.md`: truth that should survive across projects
- `PROJECT.md`: truth specific to this repository or outcome
- `.kernel/NOW.md`: state that may change soon
- `.kernel/company/<DOMAIN>.md`: optional durable company truth
- `.kernel/project/<DOMAIN>.md`: optional durable project truth

Do not invent market, customer, strategic, or authority claims from code.

## Migrate from 0.6

Preview recognized project moves:

```sh
python3 ~/.company-kernel/bin/init.py \
  --root /path/to/project \
  --migrate \
  --dry-run
```

Apply:

```sh
python3 ~/.company-kernel/bin/init.py \
  --root /path/to/project \
  --migrate
```

The deterministic migration moves:

```text
.kernel/CODING.md  -> .kernel/project/SOFTWARE.md
.kernel/PRODUCT.md -> .kernel/project/PRODUCT.md
.kernel/GTM.md     -> .kernel/project/GTM.md
```

It does not reinterpret the content. Run `$project-update` afterward to separate company truth, project truth, current state, and stale system prose.

See [Migrate from 0.6](MIGRATE-0.6.md).

## Inspect

```sh
python3 ~/.company-kernel/bin/scan.py --root /path/to/project --json
```

The scanner reports routes, local context, installed system files, skills, exact duplicates, legacy paths, tool configuration paths, and Git state. It does not print secret values.

## Validate the source repository

```sh
python3 scripts/validate.py
```
