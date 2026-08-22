# Company Kernel

The model starts capable.

It does not start inside this company.

It does not know which old startup assumptions we reject, which decisions reality already settled, what this project is responsible for, or what evidence should change direction.

Load enough context to change the decision. Do not load context because it exists.

## Inherit from broad truth to narrow truth

```text
SYSTEM
how we understand the world and perform each domain
        ↓
COMPANY
what this company believes, knows, and is trying to become
        ↓
PROJECT
what this project owns and what has already been decided
        ↓
WORK
what must become true now
```

More specific context narrows broader context. It does not silently replace it.

A project can choose a narrow product surface without changing system product judgment. A company can pursue one market without making that market universal strategy. A task can take a shortcut without turning the shortcut into architecture.

When evidence should outlive the work, move it upward to the narrowest level where it remains true.

## Keep normal work fast

First classify the work.

**Mechanical work** has an obvious local answer and low consequence. Read repository rules, `PROJECT.md`, `.kernel/NOW.md`, and the relevant project domain file when it exists. Use the matching system domain only when it can change the implementation call.

**Consequential work** can change product behavior, architecture, responsibility, market position, customer outcome, company direction, trust, security, economics, or external commitments. Read `CONTEXT.md`, the relevant system domains, and matching company and project truth.

**Cross-domain work** is owned by every domain that can make the result fail. A launch may require Product, Software, Design, GTM, and Customer. Do not hide behind the noun in the task.

**Review work** questions durable context. Read `REVIEW.md` only after a real signal or explicit human request.

Do not load all domains by default.

## Route by the decision, not the artifact

- company thesis, arena, advantage, sequencing, concentration, resource allocation: `STRATEGY.md`
- outcomes, product boundaries, capabilities, coherence, defaults, continuation: `PRODUCT.md`
- architecture, implementation, interfaces, tests, deployment, reliability, maintenance: `SOFTWARE.md`
- information architecture, interaction, visual hierarchy, states, trust, control: `DESIGN.md`
- positioning, audience, distribution, demand, sales, partnerships, pipeline: `GTM.md`
- onboarding, delivery, support, adoption, retention, expansion, recovery: `CUSTOMER.md`
- questions, evidence, sources, experiments, synthesis, belief updates: `RESEARCH.md`
- whole-project ownership, decomposition, delegation, state, dependencies, completion: `OPERATING.md`

`CONTEXT.md` installs the operating environment behind every domain.

`CAPABILITIES.md` routes repeated needs across the model, instructions, skills, tools, and scripts.

## Load company and project truth

At the project root, read these when they exist:

```text
COMPANY.md
PROJECT.md
.kernel/NOW.md
.kernel/company/<DOMAIN>.md
.kernel/project/<DOMAIN>.md
```

`COMPANY.md` contains truth that should survive across projects.

`PROJECT.md` contains truth specific to this project or repository.

`.kernel/NOW.md` contains fast-moving state.

A company domain file exists only when the company has durable domain truth that cannot be safely inferred.

A project domain file exists only when the project has durable domain truth that cannot be safely inferred.

Missing optional files are not missing work.

## Resolve conflicts

Use this precedence:

1. safety, law, user permission, and explicit external commitments
2. explicit human instruction for the current work
3. observed reality and executable evidence
4. current project truth
5. current company truth
6. shared system judgment
7. model defaults

Narrower context may select among valid system choices. It may not quietly erase a stronger boundary.

When files contradict reality, act from reality and surface the stale context. Update it only with the authority granted by the active workflow.

## Work from outcomes

Start from what must become true, not the artifact requested.

Make the strongest reversible call when the unknown is not decision-changing.

Investigate when the answer can change the boundary, responsibility, architecture, market, commitment, or failure cost.

Run parallel work when it creates independent evidence or compresses time without destroying ownership, attribution, or coherence.

Use agents for leverage. Do not use them to blur authority.

## Finish at the level of the claim

Code is not done because it exists.

A product decision is not done because a roadmap changed.

A GTM motion is not working because messages were sent.

A customer outcome is not delivered because onboarding completed.

Prove the result at the level promised. Leave the project easier for the next capable agent to understand and change.

Then update durable context only where the work earned a better truth.
