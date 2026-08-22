# Design

The interface is the product's explanation of itself.

More intelligence should require less interface, not more machinery for the
user to supervise.

## Start from the product model

A coherent interface reveals:

- what the product is
- what the user can ask it to own
- what state the work is in
- where judgment is still required
- what happened
- what happens next
- how to recover

Do not let the component library or code structure define the user's mental
model.

## Choose the right interaction

Chat is useful for ambiguous intent, exploration, explanation, and exceptions.

Forms are useful when the required structure is known.

Direct manipulation is useful when spatial or visual judgment matters.

Workflows are useful when state and handoffs must remain legible.

Commands are useful for expert repetition.

Generated interfaces are useful when the right surface depends on the task.

Combine them when the product model requires it. Do not make chat the lobby
for every action merely because a model exists.

## Hide machinery, preserve control

The user should not need to understand prompts, agents, tool calls, routing,
memory layers, or internal orchestration to receive the outcome.

Hide implementation machinery.

Do not hide consequential authority, uncertainty, state, proof, or failure.

Good control means the user can understand and change what matters without
managing every internal step.

## Design the full state space

The happy path is not the product.

Design:

- empty
- loading
- working
- waiting on the user
- waiting on another system
- partially complete
- degraded
- blocked
- failed
- recovered
- completed
- verified

AI products need especially clear stopping, exception, approval, and recovery
states.

## Make proof part of the experience

When trust matters, show the evidence near the claim:

- sources
- provenance
- changed state
- completed work
- exceptions
- approvals
- confidence where useful
- recovery options

A marketing promise is not product proof.

A busy activity feed is not product proof either.

## Use visual systems to strengthen meaning

Hierarchy should reveal importance before decoration.

Consistency should make repeated concepts easier to recognize.

Distinctiveness should support the product's identity, not become a theme
layer pasted over default components.

Every new surface must earn its place in the product's explanation of itself.
