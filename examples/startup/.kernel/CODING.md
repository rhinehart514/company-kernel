# Technical Truth

**Updated:** 2026-08-21

## Technical model

A web surface creates runs. A server-side runtime owns durable execution, tool calls, checkpoints, and result evidence. Customer credentials remain behind scoped connectors.

## Invariants and constraints

The browser cannot hold privileged credentials. Every external action must be attributable to one run and recoverable after interruption.

## Intentional decisions

The runtime is headless so product surfaces consume it without owning execution semantics.

## Technical direction

Consolidate execution state into one run model, add resumable checkpoints, and remove direct tool calls from the web layer.

## Local deviations

None currently.
