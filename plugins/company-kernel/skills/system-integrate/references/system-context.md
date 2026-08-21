# System context

The system layer is the smallest durable project-specific steering that should shape many tasks.

It is not the host's hidden system prompt. It is project-local context deliberately routed through the existing instruction system.

## Shape

```text
SYSTEM.md
.system/
  ...only the optional thin lenses this project earns
```

`SYSTEM.md` is always the entry point. After the title, keep one to ten non-empty steering lines. Three to seven is usually enough.

A `.system/*.md` lens is optional and also contains one to ten steering lines. It exists when a recurring subset of work needs distinctive judgment that should not occupy the root system context.

Every active lens must be linked from `SYSTEM.md`. An unlinked lens is inert clutter wearing a serious filename.

## What earns a line

A line earns permanence when it:

- corrects an inherited assumption that would produce the wrong project now
- preserves distinctive product, market, technical, or operating taste
- resolves a recurring tension the base model cannot infer from the repository alone
- names a project-specific scarcity or responsibility boundary
- keeps the current wedge connected to the larger coherent consequence
- prevents existing capabilities from being stacked or used at the wrong layer
- states what stronger evidence should be allowed to overturn

A line should remain useful across many tasks.

Temporary priorities belong in `.project/NOW.md`. Project facts belong in `PROJECT.md`. Implementation rules belong in the existing repository instruction system. Procedures belong in skills. Mechanical enforcement belongs in code and tests.

## Frontier compression

Intelligence, software production, research, content, and personalization are becoming cheaper.

Coherence, judgment, proof, trust, distribution, authority, proprietary context, physical execution, and current reality are not.

The useful consequence is not "add AI." It is to reconsider product boundaries, labor boundaries, interfaces, company shape, reachable markets, and the scale a tiny team can credibly attempt.

Translate that frontier into this project rather than repeating generic doctrine.

## Root and lenses

A strong root can combine global project taste with selective routing:

```text
Build the company as the operator for completed assurance work, not an AI layer on legacy dashboards.
Keep "completed review with defensible proof" obvious while the company expands into maintained customer assurance.
Treat generated answers and code as abundant; authority, source truth, verification, trust, and distribution remain scarce.
Apply [product coherence](.system/PRODUCT-COHERENCE.md) for product-shaping work.
Apply [market power](.system/MARKET-POWER.md) and [GTM engineering](.system/GTM-ENGINEERING.md) for market-shaping work.
Current customer and product evidence outrank strategy prose and historical assumptions.
```

A lens then carries only the additional durable judgment for that work:

```text
# Product coherence

Increasing capability should shorten the path from request to defensible proof rather than add product areas.
Exceptions and evidence deserve surfaces because they carry trust; internal agent machinery does not.
A useful capability belongs only when it makes review completion or maintained assurance context more central.
```

## Anti-patterns

Do not create `STRATEGY.md`, `PRODUCT.md`, `GTM.md`, and ten other system lenses merely because the words exist in business schools.

Do not create several paraphrases of the same frontier belief.

Do not put tasks, checklists, company facts, feature inventories, or long explanatory doctrine in the system layer.

Do not repeat generic reminders to think, plan, verify, be ambitious, or follow best practices.

When a line becomes obsolete because the project, model, or frontier changed, replace or delete it. System context accumulates debt too.
