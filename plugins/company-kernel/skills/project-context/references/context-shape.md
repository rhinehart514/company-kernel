# Context shape

## Split by a real boundary

Create or split files when at least one is true:

- **cadence:** the content changes materially faster or slower than the root project truth
- **authority:** evidence, founder direction, operator preference, or implementation constraint should not be conflated
- **audience:** only a particular class of work needs the detail
- **size:** the root file can no longer stay legible
- **ownership:** one context surface has a clear maintainer or source of truth
- **risk:** a high-stakes boundary deserves explicit treatment

Do not split merely because a familiar department name exists.

## The integrated moving-project set

```text
SYSTEM.md
PROJECT.md
.project/NOW.md
```

`SYSTEM.md` is one to ten lines of project-specific judgment. `$system-integrate` normally owns it.

`PROJECT.md` is durable compression and routing.

`.project/NOW.md` is current momentum and can be rewritten aggressively.

A project-only setup may omit `SYSTEM.md`. A simple or slow project may need only `PROJECT.md`.

## Additional files

Choose names that match the project's actual model. Examples are not requirements:

```text
.project/PRODUCT.md
.project/PRODUCT-SURFACES.md
.project/USER-LOOP.md
.project/AGENT-AUTHORITY.md
.project/MARKET.md
.project/ACCOUNT-SIGNALS.md
.project/SALES-MOTION.md
.project/DISTRIBUTION.md
.project/DELIVERY.md
.project/ECONOMICS.md
.project/EVIDENCE.md
.project/ADOPTION.md
.project/POLICY.md
.project/RESEARCH.md
.project/CAPABILITIES.md
```

Several files may cover one complex concern. Conventional domains with little durable context should have no file.

## Root-file standard

`PROJECT.md` should usually contain:

- one-sentence project or product truth
- `as of` date
- desired outcome
- why now
- core actors or users
- core loop
- responsibility and boundary
- entry and trajectory
- negative identity
- context map

It should not contain every feature, task, research artifact, campaign, implementation detail, or the system beliefs already in `SYSTEM.md`.

## Supporting-file standard

Each supporting file should state why it exists and when it was last reconciled.

Prefer claims and relationships over broad prose.

Keep active uncertainty visible.

Link back to `PROJECT.md` or ensure `PROJECT.md` links to it.

## Update standard

Rewrite rather than append.

Remove dead sections.

Rename files when the concept changed.

Merge files that now repeat one another.

Split files only when the new boundary reduces confusion or context cost.

Git preserves history. Current context should preserve current truth.
