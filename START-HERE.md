# Start here

Company Kernel has one job: make your agent understand the project that exists now without replacing the rest of your setup.

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

## 2. Initialize one project

Open the target project in your agent and run:

```text
$project-context Initialize this project. Inspect the existing instructions and repository, preserve stronger local rules, and create the smallest context set that makes the project clear and current. Integrate a minimal route into the existing instructions without replacing them.
```

The agent should inspect before asking you to inventory the company. It may still ask about a missing fact that cannot be recovered from the repo or available evidence.

## 3. Review three things

After the first run, check:

1. **Product truth:** Could a new teammate understand what this is in one sentence?
2. **Now:** Does `.project/NOW.md` reflect what is actually moving, blocked, or being tested?
3. **Trajectory:** Does the current wedge visibly unlock a larger coherent project rather than merely more features?

Correct bad truth immediately. Polished wrong context is unusually efficient sabotage.

## 4. Keep using your normal agent

The installed route should make consequential work load `PROJECT.md` and the linked files relevant to the task.

Do not refresh after every commit. Refresh when the project model changes: user, promise, product boundary, market motion, economics, operating responsibility, evidence, or current objective.

## 5. Use research only when it can change something

```text
$project-research Resolve whether [uncertainty] changes [decision or project belief]. Use current evidence, look for contradiction, and update project context only if reality changed.
```

That is the entire loop. The deeper architecture remains available, but it does not need to sit in every prompt looking important.
