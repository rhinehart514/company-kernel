# Technical Truth

**Updated:** 2026-08-21

## Technical model

A web surface creates runs. A server-side runtime owns durable execution, tool calls, checkpoints, and result evidence. Scoped connectors own customer credentials.

## Invariants and constraints

The browser cannot hold privileged credentials. Every external action must be attributable to one run and recoverable after interruption.

## Intentional decisions

The runtime is headless so product surfaces consume it without defining execution semantics.

## Technical direction

Consolidate state into one run model, add resumable checkpoints, and remove direct tool calls from the web layer.

## Risk and uncertainty

Connector retries can duplicate external actions. Idempotency is not yet proven across every provider.

## Local deviations

None.
