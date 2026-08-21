# Tool judgment

Tools provide access or deterministic action. Skills provide judgment and repeatable use of capability. Context provides truth and steering.

Do not solve an access problem with prose.

## Use a tool when

- the answer depends on current external or connected data
- the project needs to read or change another system
- deterministic computation, extraction, transformation, or validation improves reliability
- the action must leave real external state

## Use a skill when

- tool choice depends on repeated non-obvious judgment
- several tools must be coordinated toward one stable outcome
- the work needs project-specific evidence standards, stopping conditions, or output contracts
- the same failure pattern recurs despite capable models and available tools

## Use a script when

- the operation is bounded and deterministic
- exact repeatability matters
- bulk collection, filtering, comparison, validation, or file generation would waste model context

Keep interpretation, contradiction handling, strategy, product judgment, and ambiguous synthesis in the model.

## Inventory limits

A filesystem scan can find configuration and installed resources. It cannot prove that a host tool is connected, authorized, healthy, or visible in the current session.

Use the host's actual tool list as the source of truth for runtime capability.

Never print secrets from tool configuration. Record paths and capability hints, then inspect sensitive files only when necessary and authorized.

## Missing tools

State the concrete decision or repeated workflow blocked by missing access.

Do not recommend a connector merely because the service exists. A tool earns installation by changing what the project can observe, decide, execute, verify, or learn.
