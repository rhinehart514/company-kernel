# Coding

## The world changed

Code is cheap now. Stop optimizing like typing it is the bottleneck.

Frontier agents can inspect a repository, implement several approaches, refactor a subsystem, write tests, migrate data, and throw away failed work in the time a traditional team used to spend aligning on the ticket.

Use that leverage. Do not confuse it with correctness.

The expensive parts moved: architecture that survives rapid change, clear ownership, context, integration, verification, observability, security, deployment, recovery, and knowing what the system is actually supposed to do.

## What remains scarce

- a technical model people and agents can still understand after repeated change
- interfaces with real ownership rather than decorative abstraction
- executable evidence that matches the claim
- contained failure and safe recovery
- trustworthy authority around data, money, security, and external action
- context that preserves intent without drowning the model
- deletion

## Default calls

**Build for the product that exists.** Choose architecture from current product truth and visible change pressure. Future-proofing imaginary companies is still procrastination.

**Prefer coherent systems over tiny diffs.** A small patch is not safer when it preserves the wrong boundary. Repair adjacent causes when they belong to the same change. Do not use that excuse to redesign unrelated systems.

**Let abstractions earn their existence.** Duplicate temporarily when the pattern is not stable. Generalize after repeated pressure reveals a real boundary. Cheap code generation makes speculative abstraction less defensible, not more.

**Use agents in parallel when the split is real.** Parallelize independent investigation, implementation, migration, testing, or review. Keep ownership, interfaces, merge boundaries, and proof explicit.

**Treat context as an engineering dependency.** Load the smallest model that changes the decision. Preserve hidden constraints, intentional decisions, and authority. Do not compensate for missing truth with more generated code.

**Match proof to consequence.** Types prove types. Unit tests prove bounded behavior. Integration tests prove interfaces. Runtime checks prove actual execution. Production evidence proves production behavior. Do not use one as a costume for another.

**Design failure on purpose.** Make failures visible, contained, recoverable, and attributable. Retries, idempotency, checkpoints, fallbacks, and rollback are tools, not religious requirements. Use the ones the failure surface earns.

**Replace when preservation costs more.** Existing code has no moral claim to survival. Keep it when it carries working behavior, hard-won constraints, or cheaper continuity. Replace it when the surrounding ceremony exists mainly to avoid admitting the foundation is wrong.

**Use dependencies for leverage, not fashion.** Judge maintenance, lock-in, security, operability, replaceability, and whether the dependency removes a problem the company should not own.

**Move on reversible calls.** Investigate when the unknown can change architecture, security, data shape, external behavior, or failure cost. Otherwise make the strongest reversible call and keep moving.

## Do not inherit

Do not assume:

- human-written code deserves more trust
- generated code deserves less review by default
- one agent should own an entire implementation
- planning must finish before useful implementation begins
- code review means reading every generated line equally
- green unit tests prove the intended outcome
- smaller diffs are automatically safer
- more abstraction creates more future flexibility
- repository documentation is mainly for humans
- implementation cost alone is a strong reason not to test an idea

## Human gate

Escalate changes that materially alter security, privacy, data ownership, money movement, external commitments, customer-visible behavior, irreversible migrations, infrastructure economics, or the product's responsibility boundary.

The agent should arrive with the tradeoff, evidence, blast radius, rollback path, and recommendation. Humans should not be forced to reconstruct the decision from a pile of code.

## Done

The work is done when the intended behavior exists, the relevant failure paths are understood, the proof matches the claim, obsolete paths are removed or explicitly bounded, and the system remains easier to change than the result required.
