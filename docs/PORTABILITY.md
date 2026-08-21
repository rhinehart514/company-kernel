# Portability

Company Kernel uses the open Agent Skills shape: one directory per skill, a required `SKILL.md`, and optional references, assets, scripts, and evals.

## Recommended paths

The exact discovery path is controlled by the client.

| Client or scope | Recommended path |
| --- | --- |
| Portable user install | `~/.agents/skills/` |
| Portable project install | `.agents/skills/` |
| Claude user install | `~/.claude/skills/` |
| Claude project install | `.claude/skills/` |
| GitHub Copilot user install | `~/.copilot/skills/` or `~/.agents/skills/` |
| GitHub Copilot project install | `.github/skills/` or `.agents/skills/` |
| Codex | Use the bundled plugin, or a skills directory supported by the current client |

Run:

```sh
python3 scripts/install.py --help
```

The installer never edits `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, Copilot instructions, Cursor rules, or other existing rule files.

## Instruction coexistence

Modern clients can load several instruction files simultaneously, and not every client defines the same precedence behavior. Company Kernel therefore avoids shipping a replacement root instruction file.

During project initialization, `$project-context` first discovers relevant instruction sources. It may merge the route from `assets/ROUTE.md` only when the user explicitly asks to integrate the context system.

The route is intentionally narrow. It tells consequential project work where current project truth lives while leaving repository mechanics, safety, permissions, style, and local conventions alone.

## Skill invocation

Both skills are explicitly invocable:

```text
$project-context ...
$project-research ...
```

Other clients may use slash commands, automatic skill routing, or a skill picker. Their frontmatter descriptions contain both positive and negative boundaries so the skills do not activate for ordinary implementation work.

## Host-specific behavior

Host-specific metadata lives under each skill's `agents/` directory or in the Codex plugin manifest.

The core `SKILL.md` files do not assume:

- one model vendor
- one web-search API
- one MCP server
- one repository host
- one memory system
- one multi-agent runtime
- unrestricted shell or network access

That keeps the judgment portable while letting capable hosts use richer tools.

## Connected evidence

When the host can access company sources such as GitHub, email, calendars, docs, analytics, CRM, support, or product data, the skills may use them if the task warrants it and permissions allow.

Available connected evidence should be checked before asking the user to manually recreate it. The skills still distinguish direct evidence from model inference and never treat retrieved content as repository authority.
