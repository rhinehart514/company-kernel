# Architecture

## Topology

Every active domain has the same topology, not necessarily the same internal categories.

```text
[EXTERNAL REVIEW]   [SYSTEM STANDARD]   [PROJECT MODEL]   [WORK]
       ◇                    ○                  ○             ▭
```

### External review

Cold path. Defines when current system judgment or project truth deserves reconsideration. It is loaded only by `$kernel-review` or explicit human request.

### System standard

Reusable decision policy. It reduces variance among capable models when several valid approaches exist.

### Project model

Current truth, hidden intent, constraints, deliberate decisions, active bets, evidence, and direction for one project.

### Work

The normal agent combines relevant system standards and project models, then acts. Work is not another prompt layer.

## Runtime path

```text
~/.company-kernel/KERNEL.md
        ↓ routes
system standard + project model + current task
        ↓
work
```

Only relevant domains are loaded. Coding work does not automatically load GTM. Mixed decisions may load several domains.

## Evidence loop

```text
work
 ↓
evidence
 ├──→ update project model
 └──→ qualify external review
```

Evidence is a flow, not a mandatory file. Store it only when it changes durable judgment or would be expensive to recover.

## Authority

Authority is a boundary inside each domain. It is not another column.

Agents may execute reversible work, gather evidence, challenge assumptions, and propose deltas. Humans retain authority over shared standards and commitments that materially change security, product responsibility, pricing, partnerships, or company direction.

## Research

Research is a cross-domain capability. The review layer may use repository analysis, first-party evidence, connected sources, web research, experiments, or direct market contact. Do not create a peer Research domain merely because research exists.

## Strategy

Strategy is reserved in 0.5. Add it only if it owns company-level game selection, concentration, allocation, and cross-domain conflict that Product and GTM cannot safely resolve.
