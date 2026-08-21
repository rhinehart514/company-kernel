# Project

> Patchline is an open protocol and reference implementation for exchanging verified software-change evidence between coding agents and repositories.

**As of:** 2026-08-21

## Outcome

Any agent or repository can exchange a change, its intent, verification evidence, and unresolved risk without depending on one coding client.

## Why now

Multiple coding agents can produce large changes, but their context, test evidence, and review assumptions remain trapped in vendor-specific sessions.

## Actors

Coding agents produce and consume change evidence. Maintainers define acceptance boundaries. CI systems verify claims. Tool vendors and repositories integrate the protocol.

## Core loop

Agent proposes change → evidence package is produced → repository verifies → maintainer or agent judges unresolved risk → accepted evidence improves future interoperability.

## Responsibility

Patchline defines the interchange shape and provides a trustworthy reference implementation. It does not decide whether a repository should accept a change.

## Entry and trajectory

The entry is portable evidence for agent-created pull requests. Adoption can establish Patchline as infrastructure for agent handoffs, automated review, and cross-client software work.

## Boundary

Patchline is a protocol and implementation, not another agent orchestration product.

## Context map

- [System](SYSTEM.md): project-specific beliefs, taste, and judgment
- [Now](.project/NOW.md): current adoption and technical objective
- [Adoption](.project/ADOPTION.md): ecosystem strategy and proof
