# Company Kernel 0.9

**Give the model the company judgment it did not start with. Then get out of
its way.**

Company Kernel is an installable skill pack for building ambitious
AI-native companies.

It combines durable YC judgment with the economics of 2026:

- launch, sell, talk to users, and let reality win
- treat code, research, personalization, and experimentation as abundant
- protect what stayed scarce: judgment, coherence, attention, distribution,
  trust, authority, proof, and contact with reality
- let a small team attempt outcomes that used to require several departments
- explore broadly when execution is cheap, then concentrate when evidence
  earns concentration
- build more capability while making users understand less

0.9 deletes the global kernel, domain inheritance tree, setup scanner,
initializer, review machinery, and project file bureaucracy.

The intelligence lives in the skills.

## The product

```text
venture-judgment      shared internal brain
        |
        +-- shape-project
        +-- think-further
        +-- product-coherence
```

### `venture-judgment`

The shared source of judgment. It holds the worldview, strategy, product,
software, design, GTM, customer, research, operating, and writing references.

It is loaded progressively by the other skills. Users rarely invoke it
directly.

### `$shape-project`

Inspect the repository and available evidence. Then use a design-tree grilling
session to resolve the decisions a cold model cannot safely infer.

The skill recommends answers, pushes back, introduces larger possibilities,
researches facts instead of assigning homework, and writes the smallest useful
project model.

Output:

```text
AGENTS.md
PROJECT.md
NOW.md
```

Run it again after material learning:

```text
$shape-project refresh
```

### `$think-further`

Ask what the company is still thinking too small about.

The skill finds larger outcomes, adjacent wedges, disappearing workflows,
new responsibility surfaces, compounding advantages, and product plus GTM
moves made possible by current agents.

It returns a few coherent trajectories, a recommendation, a first proof, and
a kill condition. It does not dump fifty ideas into a table and call that
strategy.

### `$product-coherence`

Make the product more powerful without making it feel larger.

Use it before or after consequential product work. It decides whether a
capability should become a default, action, state, extension, replacement,
new surface, deliberate separation, or nothing.

It then inspects the result for duplicated concepts, bolted-on workflows,
unnecessary settings, exposed machinery, and product boundaries inherited
from the codebase rather than the customer outcome.

## Install

Install the skill pack:

```sh
npx skills add rhinehart514/company-kernel
```

Codex plugin:

```sh
codex plugin marketplace add rhinehart514/company-kernel --ref main
codex plugin add company-kernel@company-kernel
```

Then open a real repository and run:

```text
$shape-project
```

The skill inspects before asking. You should not need to inventory your
repository, tools, skills, or documentation for it.

## Normal use

Start or rescue a project:

```text
$shape-project
```

Refresh context after evidence changes the model:

```text
$shape-project refresh
```

Push beyond an incremental roadmap:

```text
$think-further
```

Pressure-test a product addition:

```text
$product-coherence
```

Then work normally.

You do not invoke Company Kernel for every task. `PROJECT.md` and `NOW.md`
carry enough local truth for routine execution. The shared brain is pulled in
only when judgment can change the result.

## Project footprint

`AGENTS.md` routes consequential work.

`PROJECT.md` holds the durable company and project model: outcome, actor,
why now, product model, responsibility, wedge, core loop, compounding path,
decisions, evidence, and non-goals.

`NOW.md` holds the current edge: active outcome, bets, evidence, unknowns,
constraints, and next proof.

That is the whole installed architecture.

No global kernel home. No `.kernel/` directory. No domain files created for
symmetry. No automatic standards mutation. No permanent ideation agent.

## Repository map

```text
skills/
  venture-judgment/
    SKILL.md
    references/
  shape-project/
    SKILL.md
  think-further/
    SKILL.md
  product-coherence/
    SKILL.md

examples/project/
  AGENTS.md
  PROJECT.md
  NOW.md

scripts/validate.py
```

The references are internal source material, not project files.

## The call

Preserve YC's epistemology. Rewrite YC's economics.

Focus the thesis, not every cheap experiment.

Minimum viable means minimum distance to evidence, not minimum software.

Code got cheaper faster than complexity did.

Build more. Make users understand less.

Be ambitious as fuck. Make reality decide whether the ambition survives.

## Validate

```sh
python3 scripts/validate.py
```

MIT. The design-tree grilling method in `shape-project` is adapted from Matt
Pocock under MIT. See [third-party notices](THIRD_PARTY_NOTICES.md).
