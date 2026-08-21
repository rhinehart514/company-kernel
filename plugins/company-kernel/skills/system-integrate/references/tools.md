# Tool judgment

Tools provide current access or external action. Skills provide repeated judgment. Scripts provide deterministic work. Context provides truth.

Use a tool when the answer depends on current data, another system must be read or changed, or real external state must move.

Use a script when the work is bounded, repeatable, and exact enough that model tokens add no value.

Use a skill when several tools and decisions repeatedly combine into one stable outcome.

Filesystem configuration does not prove that a runtime tool is connected, authorized, or healthy. Trust the host's actual tool list.

Never print secrets from tool configuration. Record the capability and path, then inspect sensitive content only when necessary and authorized.

A tool earns installation by changing what the system can observe, decide, execute, verify, or learn.
