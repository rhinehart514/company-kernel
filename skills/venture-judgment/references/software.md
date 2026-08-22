# Software

Code is cheap now. Stop optimizing like typing it is the bottleneck.

Cheap production increases the value of architecture, context, interfaces,
verification, observability, security, deployment, recovery, and knowing what
the system is supposed to do.

## Build for the product that exists

Choose architecture from current product truth and visible change pressure.

Do not future-proof imaginary companies.

Do not preserve a wrong boundary because the smallest diff is easier to
review.

A coherent change can cross several files or layers. It should not use that as
an excuse to redesign unrelated systems.

## Let abstractions earn their existence

Duplicate temporarily when the pattern is still uncertain.

Generalize after repeated pressure reveals a real boundary.

Generated code makes speculative abstraction less defensible, not more. It is
cheap to revise once the shape becomes clear.

Every abstraction should reduce more future complexity than it introduces now.

## Treat context as an engineering dependency

A coding agent without product intent can produce technically impressive
damage at remarkable speed.

Preserve:

- the behavior that must remain true
- hidden constraints
- authority and security boundaries
- intentional architecture
- failure semantics
- migration assumptions
- the proof required

Load the smallest context that can change the technical call.

Do not compensate for missing truth with more generated code.

## Parallelize real independence

Use agents in parallel for independent investigation, implementations,
migrations, tests, reviews, or proof.

Keep ownership, interfaces, merge boundaries, and attribution explicit.

Do not split one tightly coupled decision into several agents and call the
result orchestration.

Parallelism should compress time or create comparative evidence without
destroying coherence.

## Match proof to the claim

Types prove types.

Unit tests prove bounded behavior.

Integration tests prove interfaces.

End-to-end tests prove a complete path under a controlled environment.

Runtime checks prove actual execution.

Production evidence proves production behavior.

Do not use one as a costume for another.

Test the failure paths that carry the consequence, not every line equally.

## Design failure on purpose

Make consequential failure:

- visible
- contained
- attributable
- recoverable
- safe enough for the authority granted

Retries, idempotency, checkpoints, fallbacks, approval gates, and rollback are
tools. Use the ones the failure surface earns.

A product that takes responsibility must also take responsibility for being
wrong.

## Replace when preservation costs more

Existing code has no moral claim to survival.

Keep it when it carries working behavior, hard-won constraints, customer
continuity, or cheaper migration.

Replace it when the ceremony exists mainly to avoid admitting the foundation
is wrong.

Code volume is not progress.

Working behavior under real constraints is.
