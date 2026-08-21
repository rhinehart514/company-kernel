# Start here

Company Kernel builds one shared system above your projects, then keeps each project current beneath it.

## 1. Install

Codex:

```sh
codex plugin marketplace add rhinehart514/company-kernel --ref main
codex plugin add company-kernel@company-kernel
```

Any Agent Skills-compatible client:

```sh
python3 scripts/install.py --user
```

## 2. Run the first integration

Open a real project and run:

```text
$system-integrate Build or reconcile the shared Company Kernel system above my projects.
Inspect my existing global rules, installed skills, and available tools.
Keep stronger rules. Write a readable 1-10 line SYSTEM.md and only useful lenses
under ~/.company-kernel, create a clear capability map, then initialize this repository
with PROJECT.md and .project/NOW.md. Do not delete or rewrite unrelated global work.
```

The agent should inspect the machine and repository before asking you to describe what is already visible.

## 3. Review the result

Look at four things:

1. **System:** Does `~/.company-kernel/SYSTEM.md` contain distinctive judgment rather than slogans?
2. **Project:** Can a new teammate explain the project after reading `PROJECT.md`?
3. **Capabilities:** Is it clearer which skills and tools own which jobs?
4. **Trajectory:** Does the current entry visibly earn a much larger coherent outcome?

Correct wrong truth immediately. Elegant wrong context only helps the agent fail faster.

## 4. Keep moving

Use `$project-context` when the project changes.

Use `$project-research` when one uncertainty can change a decision.

Use `$system-integrate` again only when the shared rules, skills, tools, model capability, or operating beliefs change materially.
