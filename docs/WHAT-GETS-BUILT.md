# What gets built

Company Kernel does not install one file per department.

It builds four kinds of things when they earn a place.

## 1. Shared system context

Created once above projects:

```text
~/.company-kernel/SYSTEM.md
~/.company-kernel/LENSES.md
~/.company-kernel/lenses/*
~/.company-kernel/CAPABILITIES.md
```

The root and every active lens contain one to ten lines.

The source library includes `SOFTWARE.md`, but no project automatically receives a `CODING.md`. Repository coding rules usually already live in `AGENTS.md`, tests, CI, and the codebase.

The source library includes both `MARKET-POWER.md` and `GTM-ENGINEERING.md`. A single generic `GTM.md` would hide two different judgments.

## 2. Project context

Created inside each repository:

```text
PROJECT.md
.project/NOW.md
```

More files appear only when needed. A startup may earn:

```text
.project/PRODUCT.md
.project/PRODUCT-SURFACES.md
.project/MARKET.md
.project/ACCOUNT-SIGNALS.md
.project/SALES-MOTION.md
.project/DISTRIBUTION.md
```

Another project may need none of them.

## 3. Capabilities

The integrator may keep, route, combine, rewrite, retire, or build skills.

Several capabilities can exist around one area when they own different jobs:

```text
account-discovery
trigger-sensing
account-intelligence
live-demo-generation
enterprise-procurement
```

Those should not be crushed into one generic GTM skill.

## 4. Access and deterministic machinery

A missing result may require:

```text
connector or permission  current data or external action
script                    bounded repeatable work
test or CI                mechanical enforcement
explicit limitation       capability that does not yet exist reliably
```

The system should build new machinery only after the current model, project context, installed skills, and available tools have failed to provide the repeated capability.
