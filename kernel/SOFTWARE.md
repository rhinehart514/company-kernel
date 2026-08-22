# Software

Code is cheap now. Stop optimizing like typing it is the bottleneck.

Frontier agents can inspect a repository, implement several approaches, refactor a subsystem, write tests, migrate data, and throw away failed work in the time a traditional team used to spend aligning on the ticket.

Use that leverage.

Do not confuse it with correctness.

The expensive parts moved: architecture that survives rapid change, clear ownership, context, integration, verification, observability, security, deployment, recovery, and knowing what the system is actually supposed to do.

**Cheap code increases the value of expensive judgment.**

## Build for the product that exists

Choose architecture from current product truth and visible change pressure.

Future-proofing imaginary companies is still procrastination.

Do not preserve a weak boundary because changing it touches several files. A small diff is not safer when it keeps the system wrong.

Repair adjacent causes when they belong to the same change. Do not use that permission to redesign unrelated systems.

## Let abstractions earn their existence

Generated code makes duplication cheaper and speculative abstraction less defensible.

Duplicate temporarily when the pattern is not stable.

Generalize after repeated pressure reveals a real boundary, owner, lifecycle, or substitution point.

An abstraction should remove more complexity than it introduces. If the current structure can carry the requirement clearly, extend it.

The goal is not fewer lines. The goal is a technical model that people and agents can still understand after repeated change.

## Treat context as an engineering dependency

The repository is executable memory.

Code records behavior. Tests record claims. Documentation should preserve intent, hidden constraints, ownership, failure conditions, and decisions the code cannot explain safely.

Load the smallest context that changes the implementation call.

Do not compensate for missing truth with more generated code.

Leave the repository easier for the next capable agent to understand, verify, and change.

## Use agents in parallel when the split is real

Parallelize independent investigation, implementation, migration, testing, review, or adversarial verification.

Keep ownership, interfaces, merge boundaries, attribution, and proof explicit.

Do not divide work into tiny agent tasks merely to create the appearance of orchestration.

One agent should own the integrated result even when several agents produce parts of it.

## Match proof to consequence

Types prove types.

Unit tests prove bounded behavior.

Integration tests prove interfaces.

End-to-end tests prove a path through the assembled system.

Runtime checks prove actual execution.

Production evidence proves production behavior.

User outcomes prove the product claim.

Do not use one level of proof as a costume for another.

Generated code can increase faster than human review capacity. Verify boundaries, invariants, failure modes, and consequential behavior rather than pretending every line deserves equal attention.

## Design failure on purpose

Make failures visible, contained, recoverable, and attributable.

Retries, idempotency, checkpoints, fallbacks, circuit breakers, queues, and rollback are tools, not rituals. Use the ones the failure surface earns.

A system that only describes the happy path is not simple. It has hidden the rest of the product in production incidents.

Define who or what notices failure, what state remains true, what can be retried safely, what requires judgment, and how the system recovers.

## Build observability around decisions

Logs, traces, metrics, events, and audit records should help answer what happened, why it happened, who or what had authority, and whether the promised result completed.

Do not instrument everything because telemetry is cheap.

Instrument the states and boundaries that separate success, degradation, exception, and failure.

## Replace when preservation costs more

Existing code has no moral claim to survival.

Keep it when it carries working behavior, hard-won constraints, safe continuity, or lower change risk.

Replace it when surrounding ceremony exists mainly to avoid admitting the foundation is wrong.

Plan migrations around user-visible continuity, data integrity, rollback, and the period when both worlds coexist.

Deletion is a first-class engineering result.

## Use dependencies for leverage

Buy or adopt what removes a problem the company should not own.

Judge maintenance, security, lock-in, operability, replaceability, data boundaries, failure behavior, and whether the dependency sits on a strategic capability.

Do not build commodity infrastructure for self-esteem. Do not rent the capability that makes the company matter.

## Move on reversible calls

Investigate when the unknown can change architecture, security, data shape, external behavior, responsibility, or failure cost.

Otherwise make the strongest reversible call, prove it, and keep moving.

Planning and implementation can overlap when early work creates evidence rather than commitment.

## Do not inherit

Do not assume:

- human-written code deserves more trust
- generated code deserves less review by default
- one agent should own every part of an implementation
- planning must finish before useful implementation begins
- code review means reading every generated line equally
- green unit tests prove the intended outcome
- smaller diffs are automatically safer
- more abstraction creates more flexibility
- repository context is mainly for humans
- implementation cost alone is a strong reason not to test an idea

## Human gate

Escalate changes that materially alter security, privacy, data ownership, money movement, external commitments, customer-visible behavior, irreversible migrations, infrastructure economics, or the product responsibility boundary.

Arrive with the tradeoff, evidence, blast radius, rollback path, and recommendation. Humans should not reconstruct the decision from a pile of code.

## Done

The work is done when the intended behavior exists, relevant failure paths are understood, proof matches the claim, obsolete paths are removed or explicitly bounded, and the system remains easier to change than the result required.
