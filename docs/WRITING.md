# Writing system context

The model experiences the kernel as language.

File structure matters. Routing matters. Evidence matters. But at runtime the model receives tokens, and those tokens either move its judgment or occupy context.

A correct MD can still be useless when it assumes the model already lived through the reasoning that made the conclusion meaningful.

## The target

Assume intelligence.

Never assume context.

A cold model should finish an important section with:

- a better model of the world
- a sharper distinction
- a stronger sense of what is possible
- a visible decision boundary
- enough roots to extend the call beyond the examples
- a clear consequence for the work

The goal is not to make documentation sound like X.

The goal is to write with the compression, conviction, concreteness, and intellectual voltage of people using language to move thought rather than satisfy a format.

## Do not give the model only the last twenty percent

A line like this is strong:

> Add capability aggressively. Add concepts reluctantly.

It becomes much stronger after the file installs why:

Software production became cheap enough to support several capabilities and experiments that would once have been rejected on implementation cost alone. User attention and product comprehension did not fall at the same rate. A feature can be cheap to produce while making the product expensive to understand.

Now the line carries a world:

> Add capability aggressively. Add concepts reluctantly.

The surrounding context should not explain every implication. It should install enough of the underlying model that a capable reader can derive them.

## Transfer judgment, then ambition

Bad context transfers rules.

> Keep the product simple.

Good context transfers judgment.

> A product can have many capabilities and still feel like one thing. A product with three disconnected ideas can already be too large.

Exceptional context transfers ambition.

> Build more. Make users understand less.

The last line works because the earlier thought gave it meaning. Alone, it risks becoming a slogan.

Every major section should contain at least one thought worth carrying into the work.

Not every sentence should demand applause. Most sentences should be plain enough to disappear into the idea.

## Give the model objects to think with

Useful language compresses repeated experience into an object that can participate in new reasoning.

Examples in the kernel include:

- experience tokens
- conceptual debt
- responsibility boundary
- minimum distance to evidence
- proof density
- compounding path
- current truth
- cold path

A good term should let the model ask better questions, see tradeoffs, or derive actions that the paragraph did not enumerate.

Do not coin language for novelty. A label that names nothing real increases conceptual debt while pretending to reduce it.

## Make the contrast do work

Contrast reveals the boundary faster than abstract explanation.

Weak:

> Maintain simplicity while supporting future requirements.

Stronger:

> Do not design for imaginary scale. Design so tomorrow's change is cheap.

Weak:

> Consider multiple approaches before committing.

Stronger:

> When comparison is cheaper than debate, build the alternatives.

Weak:

> Focus on outcomes rather than features.

Stronger:

> The customer did not buy access to the product. They bought a change in their world.

Use contrast when two plausible interpretations lead to different behavior. Do not turn every paragraph into a slogan duel.

## Make abstractions visible

Weak:

> Preserve product coherence across surfaces.

Stronger:

> The product should feel like it got more powerful, not like another product was bolted onto it.

Weak:

> Ensure effective failure handling.

Stronger:

> Define who notices failure, what state remains true, what can be retried safely, and how the system recovers.

Weak:

> Use evidence to guide decisions.

Stronger:

> A paid commitment can test willingness to pay. A prototype cannot.

The reader should be able to imagine the difference between following and violating the instruction.

## Use pressure, not politeness

"Consider," "strive," "aim," and "where appropriate" often preserve every escape route.

State the call.

State the condition that changes it.

Weak:

> Consider using existing concepts where appropriate.

Stronger:

> Before creating another concept, ask whether the capability can disappear into one the user already understands.

Do not fake certainty. Strong writing can expose uncertainty precisely:

> Keep the bet reversible until production behavior answers the reliability question.

## Let the prose think forward

System context should not only defend against mistakes.

It should make the model search a larger possibility space:

> Do not inherit the market's product boundaries. Many were drawn around work software could not previously understand, decide, generate, coordinate, or perform.

That sentence gives permission and a test. It does not merely demand ambition.

"Be ambitious" is weak because it supplies no changed world, no object, and no direction.

Describe the capability shift and the remaining constraint. The ambition will emerge from the model.

## Preserve hierarchy

A file should make clear:

- what the domain owns
- which calls matter most
- what wins when principles conflict
- what old defaults should not govern
- where human authority remains
- what done means at the level of the claim

Do not flatten the file into twenty equally weighted bullets.

Sequence the prose so later calls inherit meaning from earlier ones.

## Write for a cold capable reader

Before accepting a section, ask:

1. What did we learn that the fresh model did not live through?
2. Which part of that experience must survive for the conclusion to work?
3. What distinction stops the model from falling back to generic advice?
4. What does the language make newly possible to think?
5. Which next decision should change?
6. Can any sentence disappear without losing judgment?

If the model could have written the section before entering the company, the section probably did not earn runtime context.

## Keep local truth different

System writing installs reusable judgment.

Company writing states what this company currently believes and why.

Project writing states what is true here, including decisions, boundaries, evidence, and change conditions.

Do not make company and project files imitate the rhetorical density of the system. Their primary obligation is accuracy.

A project sentence can be plain:

> Agent execution stays behind the upload, review, and completed-result model. Do not expose a separate agent workspace.

It is strong because the decision is concrete and scoped.

## Edit ruthlessly, not cosmetically

Delete:

- throat clearing
- generic advice
- repeated conclusions
- section summaries that add no consequence
- decorative labels
- fake frameworks
- lists whose items have equal meaning in every company
- examples that merely restate the line
- history that does not change the next decision

Keep the reasoning substrate that lets compression work.

Ruthless editing does not mean reducing every idea to one line. It means preserving only the language required to transfer the earned model.

## The final test

Do not ask only whether the file is clear, concise, correct, or comprehensive.

Ask:

> After reading this, can the model think a useful thought it was less likely to think before?

If the answer is no, the MD is not finished.
