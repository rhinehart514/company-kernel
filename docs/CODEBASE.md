# Codebase map

This repository is intentionally small. The layout is the architecture.

```text
.
├── kernel/
│   ├── KERNEL.md
│   ├── CAPABILITIES.md
│   ├── standards/
│   │   ├── CODING.md
│   │   ├── PRODUCT.md
│   │   └── GTM.md
│   └── review/
│       ├── REVIEW.md
│       ├── CODING.md
│       ├── PRODUCT.md
│       └── GTM.md
├── templates/
│   ├── PROJECT.md
│   └── .kernel/
│       ├── NOW.md
│       ├── CODING.md
│       ├── PRODUCT.md
│       └── GTM.md
├── skills/
│   ├── kernel-setup/
│   ├── project-update/
│   └── kernel-review/
├── scripts/
│   ├── install.py
│   ├── scan.py
│   └── validate.py
└── examples/startup/
```

## Read order

For understanding the product:

1. `README.md`
2. `kernel/KERNEL.md`
3. one file under `kernel/standards/`
4. the matching file under `templates/.kernel/`
5. the matching skill

For operating a real project:

1. installed `~/.company-kernel/KERNEL.md`
2. relevant installed standards
3. project `PROJECT.md`
4. project `.kernel/NOW.md`
5. matching project domain models

## Ownership

### `kernel/KERNEL.md`

Owns the shared 2026 startup prior and runtime route. It is loaded for consequential work.

### `kernel/standards/*`

Own reusable domain judgment. These files should change how a strong model resolves valid competing choices.

They must include:

- what changed
- what remains scarce
- default calls
- historical assumptions to reject
- human authority
- what done means

### `kernel/review/*`

Own cold-path triggers, qualification, classification, and amendment behavior. They are not normal runtime context.

### `templates/PROJECT.md`

Owns cross-domain project identity, outcome, boundary, core loop, direction, and non-goals.

### `templates/.kernel/NOW.md`

Owns fast-moving current state.

### `templates/.kernel/<DOMAIN>.md`

Owns durable project truth in one domain. These are not copies of system standards.

### `skills/*`

Own repeated non-obvious operating behavior. Skills inspect, decide, and write. They do not become another doctrine library.

### `scripts/*`

Own deterministic mechanics only. A script should inspect, copy, or validate. It should not pretend to make company judgment.

## Canonical source

`kernel/` is the only canonical shared system.

`templates/` is the only canonical project shape.

The repository root is the Codex plugin. There is no second generated plugin tree and no mirrored example system to keep in sync.

## How to change the codebase

A change to a domain usually touches four places:

1. `kernel/standards/<DOMAIN>.md`
2. `kernel/review/<DOMAIN>.md` when review triggers change
3. `templates/.kernel/<DOMAIN>.md` when project truth needs a new home
4. skill evals when behavior changes

Do not add a new domain because the company has another department. Add it only when it owns a distinct class of judgment and project truth that existing domains cannot safely own.

Strategy remains reserved for that reason.
