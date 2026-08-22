# Project / Software

## Current model

The case state machine is the source of truth for workflow progress. Agent execution may propose events, but only validated transitions change case state.

Every material field in the completed packet must retain provenance to a source, extraction event, policy version, and human override when one exists.

## Decisions

- state transitions are explicit and idempotent
- long-running work resumes from persisted checkpoints
- source adapters normalize into one evidence model before policy evaluation
- customer policy is versioned and attached to each in-flight case
- an agent cannot mark a case complete directly
- completion requires deterministic validation of required evidence
- manual operator actions use the same event path as automated actions

## Boundaries

The implementation may use several agents and queues internally.

Those components do not define product state and may be replaced without changing the case contract.

External submissions require an explicit authority token scoped to the action and customer.

## Evidence

Document ingestion and extraction pass fixture tests. The preview packet preserves field provenance. Retry and recovery behavior has not been proved against a real interrupted case.

## Active bets

One event model should support both automated and manual recovery without hidden state. Continue if the first production case can be reconstructed from its event history.

Deterministic completion validation should bound model uncertainty. Continue if policy variation can be expressed without embedding customer-specific branches throughout the codebase.

## Change conditions

Reopen the architecture if state cannot be reconstructed, if source or policy versioning changes a completed result, if recovery requires direct database edits, or if one case can complete without the evidence promised to the user.
