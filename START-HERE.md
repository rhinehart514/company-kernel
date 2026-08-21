# Start here

Company Kernel has one job: make the agent environment materially better for the project that exists now without replacing the rest of your setup.

## 1. Install the skills

Codex:

```sh
codex plugin marketplace add rhinehart514/company-kernel --ref main
codex plugin add company-kernel@company-kernel
```

Any Agent Skills-compatible client:

```sh
python3 scripts/install.py --user
```

Project-local installation:

```sh
python3 scripts/install.py --project .
```

## 2. Run the integration

Open the target project and run:

```text
$system-integrate Integrate this project. Inspect the existing system instructions, installed skills, available tools, repository, and current context. Compile a 1-10 line SYSTEM.md, preserve stronger local rules, rationalize the capability set, then initialize or refresh PROJECT.md and only the supporting context this project needs. Do not stop at an audit.
```

The agent should inspect before asking you to inventory the company or machine.

## 3. Expect a transformation

A normal first run should leave:

```text
SYSTEM.md
.system/*        optional thin lenses
PROJECT.md
.project/NOW.md
```

It may also create several files or capabilities around one important concern and none around another. It should not create a complete departmental template set merely to prove it owns a keyboard.

The final report should show:

- the exact compiled system context
- the current product or project truth
- context created, rewritten, merged, or removed
- skills and tools kept, routed, combined, retired, exposed, built, or still missing
- the sharpest product-coherence problem
- the most consequential frontier unlock
- the largest remaining uncertainty and next proof

## 4. Review four things

1. **System:** Are `SYSTEM.md` and any thin lenses distinctive, project-specific, and worth loading repeatedly?
2. **Product truth:** Could a new teammate understand what this is in one sentence?
3. **Capabilities:** Are relevant skills and tools easier to invoke without stacking overlapping ones?
4. **Trajectory:** Does winning the current wedge visibly unlock a much larger coherent project?

Correct bad truth immediately. Polished wrong context is an extremely efficient sabotage mechanism.

## 5. Keep operating normally

Use `$project-context` when the company or project model changes.

Use `$project-research` when a bounded uncertainty can change a decision.

Use `$system-integrate` again only after a meaningful change to the model, instruction layers, skills, tools, project-level system context, or company direction.
