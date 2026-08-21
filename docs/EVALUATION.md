# Evaluation

Thin steering is a bet. The repo therefore evaluates behavior rather than celebrating the existence of Markdown.

## Trigger evals

Each skill contains positive and negative trigger cases.

A good description should load the skill for project initialization, context drift, or consequential research. It should stay out of bug fixes, ordinary code review, copy edits, and trivia.

Run trigger cases several times in the target client. Model routing is nondeterministic.

## Behavior evals

Behavior cases test whether the model demonstrates the intended judgment:

- preserves existing instructions
- creates an adaptive context set instead of every possible file
- separates durable project truth from fast-moving state
- keeps the current product easy to explain
- preserves both the entry wedge and the larger trajectory
- treats implementation capacity as cheap without making scope incoherent
- distinguishes evidence, inference, direction, and bets
- rewrites stale context instead of appending contradiction
- researches when current reality can change a decision
- stops research when more evidence is unlikely to alter the decision
- avoids imposing venture language on non-startup projects

## What not to optimize

Do not grade outputs by:

- number of files created
- number of sections completed
- length of research
- source count without source quality
- use of startup vocabulary
- confidence theater
- how forcefully the model says the project will dominate a market

The desired outcome is better project judgment and clearer execution.

## Running the repository validator

```sh
python3 scripts/validate.py
```

The validator checks manifests, skill frontmatter, referenced resources, eval shapes, Python syntax, installer behavior, and links in the bundled examples.

It does not claim to measure product taste. The JSON behavior cases are fixtures for running real model evals in the clients you care about.
