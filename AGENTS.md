# Repository rules

This repository steers already-capable models. Prefer removing instructions to explaining common sense.

The flagship flow inspects the existing agent environment, compiles a project-local `SYSTEM.md` of one to ten high-information lines, then compiles current project context.

Keep the portable core host-agnostic. Put client-specific metadata in adapters, not in shared skill judgment.

Beliefs and taste belong in thin system context. Verbs belong in skills. Current project truth belongs in `PROJECT.md` and linked `.project/*` files.

Do not replace a user's existing instruction system. Integrate minimally and preserve stronger local rules.

Do not create one skill or context file per conventional domain. Several capabilities may serve one important concern and entire functions may need none.

Every persistent instruction, skill, script, and context file must earn its cost through a repeated job, representative failure, clear safety boundary, or meaningful routing improvement.

Run `python3 scripts/validate.py` before committing.
