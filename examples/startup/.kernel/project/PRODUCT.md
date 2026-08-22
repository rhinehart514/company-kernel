# Project / Product

## Current model

Kestrel Intake is one case moving toward a completed approval packet.

The product should feel like delegated completion, not a set of AI tools. Users interact with the case, its evidence, and material exceptions. Internal agents, jobs, prompts, and source adapters remain implementation.

## Decisions

- one case is the durable product object
- terminal states are complete, exception, and cutoff
- a user reviews material exceptions, not every generated step
- proof appears inside the case at the decision it supports
- outbound follow-up is part of the case when authority is granted
- policy setup should become reusable company context, not repeated per case

## Boundaries

The product may collect, interpret, reconcile, request, assemble, and prove within granted sources and policy.

It may not create policy, silently override missing authority, or present uncertain completion as success.

A general workflow builder and agent workspace are outside this project.

## Evidence

Design partners understand the case model without explanation and prefer an explicit unresolved state to a confidence score. Production use has not proved that exception-only review is sufficient.

## Active bets

Exception-only review should reduce customer coordination while preserving trust. Continue when users can approve repeat execution after seeing provenance and policy once.

The packet should be the primary proof surface. Continue when a customer can recognize completion without opening the internal activity history.

## Change conditions

Reopen the model if customers consistently need to navigate internal steps, if cases require several unrelated primary objects, or if the packet cannot prove the promised result.
