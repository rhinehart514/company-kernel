#!/usr/bin/env python3
"""Discover instruction, skill, tool-config, and project-context surfaces.

This script reports metadata only. It does not judge semantic overlap, read secrets,
or modify the environment.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
from collections import defaultdict
from pathlib import Path
from typing import Iterable

EXCLUDED_DIRS = {
    ".git",
    ".hg",
    ".svn",
    ".venv",
    "venv",
    "node_modules",
    "vendor",
    "dist",
    "build",
    "coverage",
    "__pycache__",
}

INSTRUCTION_NAMES = {
    "AGENTS.md",
    "CLAUDE.md",
    "GEMINI.md",
    ".cursorrules",
    "copilot-instructions.md",
}

PROJECT_CONTEXT_NAMES = {
    "PROJECT.md",
    "COMPANY.md",
    "PRODUCT.md",
    "GTM.md",
    "STRATEGY.md",
    "DESIGN.md",
    "ENGINEERING.md",
    "SOFTWARE.md",
    "RESEARCH.md",
    "OPERATING.md",
    "OPERATIONS.md",
    "NOW.md",
    "STATE.md",
}

TOOL_CONFIG_NAMES = {
    ".mcp.json",
    "mcp.json",
    "mcp-config.json",
}

PROJECT_SKILL_ROOTS = (
    ".agents/skills",
    ".codex/skills",
    ".claude/skills",
    ".copilot/skills",
    ".github/skills",
    ".gemini/skills",
    ".cursor/skills",
)

USER_SKILL_ROOTS = (
    ("agents", ".agents/skills"),
    ("codex", ".codex/skills"),
    ("claude", ".claude/skills"),
    ("copilot", ".copilot/skills"),
    ("gemini", ".gemini/skills"),
    ("cursor", ".cursor/skills"),
    ("agents-plugin", ".agents/plugins"),
    ("codex-plugin", ".codex/plugins"),
    ("claude-plugin", ".claude/plugins"),
)

USER_INSTRUCTION_PATHS = (
    ("agents", ".agents/AGENTS.md"),
    ("codex", ".codex/AGENTS.md"),
    ("claude", ".claude/CLAUDE.md"),
    ("gemini", ".gemini/GEMINI.md"),
)

USER_TOOL_CONFIG_PATHS = (
    ("codex", ".codex/config.toml"),
    ("claude", ".claude.json"),
    ("claude", ".claude/settings.json"),
    ("cursor", ".cursor/mcp.json"),
    ("vscode", ".vscode/mcp.json"),
    ("generic", ".mcp.json"),
)

FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def display_path(path: Path, root: Path, home: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        pass
    try:
        return "~/" + path.relative_to(home).as_posix()
    except ValueError:
        return str(path)


def text_metadata(path: Path) -> tuple[int | None, int]:
    size = path.stat().st_size
    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return None, size
    return text.count("\n") + (1 if text else 0), size


def digest_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(65536), b""):
            digest.update(block)
    return digest.hexdigest()[:16]


def parse_skill_frontmatter(path: Path) -> tuple[str, str]:
    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return path.parent.name, ""
    match = FRONTMATTER_RE.search(text)
    if not match:
        return path.parent.name, ""
    values: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if line.startswith((" ", "\t")) or ":" not in line:
            continue
        key, value = line.split(":", 1)
        value = value.strip().strip('"').strip("'")
        if key.strip() in {"name", "description"}:
            values[key.strip()] = value
    return values.get("name", path.parent.name), values.get("description", "")


def iter_project_files(root: Path, max_depth: int) -> Iterable[Path]:
    root_depth = len(root.parts)
    for current, dirs, names in os.walk(root):
        current_path = Path(current)
        depth = len(current_path.parts) - root_depth
        dirs[:] = [
            name
            for name in dirs
            if name not in EXCLUDED_DIRS and depth < max_depth
        ]
        for name in names:
            yield current_path / name


def instruction_record(path: Path, scope: str, client: str, root: Path, home: Path) -> dict[str, object]:
    lines, size = text_metadata(path)
    return {
        "scope": scope,
        "client": client,
        "path": display_path(path, root, home),
        "bytes": size,
        "lines": lines,
        "digest": digest_file(path),
    }


def skill_record(skill_file: Path, scope: str, client: str, root: Path, home: Path) -> dict[str, object]:
    lines, size = text_metadata(skill_file)
    name, description = parse_skill_frontmatter(skill_file)
    return {
        "scope": scope,
        "client": client,
        "name": name,
        "description": description,
        "path": display_path(skill_file.parent, root, home),
        "skill_file": display_path(skill_file, root, home),
        "bytes": size,
        "lines": lines,
        "digest": digest_file(skill_file),
    }


def scan_skill_root(path: Path, scope: str, client: str, root: Path, home: Path) -> list[dict[str, object]]:
    if not path.is_dir():
        return []
    records = []
    for skill_file in sorted(path.rglob("SKILL.md")):
        if any(part in EXCLUDED_DIRS for part in skill_file.parts):
            continue
        records.append(skill_record(skill_file, scope, client, root, home))
    return records


def ancestor_instruction_files(root: Path, home: Path) -> Iterable[Path]:
    current = root.parent
    while current != current.parent:
        for name in ("AGENTS.md", "CLAUDE.md", "GEMINI.md"):
            path = current / name
            if path.is_file():
                yield path
        if current == home or home not in current.parents:
            break
        current = current.parent


def git_summary(root: Path) -> dict[str, object] | None:
    try:
        inside = subprocess.run(
            ["git", "-C", str(root), "rev-parse", "--is-inside-work-tree"],
            capture_output=True,
            text=True,
            check=True,
        ).stdout.strip()
        if inside != "true":
            return None
        branch = subprocess.run(
            ["git", "-C", str(root), "branch", "--show-current"],
            capture_output=True,
            text=True,
            check=True,
        ).stdout.strip()
        log = subprocess.run(
            [
                "git",
                "-C",
                str(root),
                "log",
                "-n",
                "8",
                "--date=short",
                "--pretty=format:%h%x09%ad%x09%s",
            ],
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        status = subprocess.run(
            ["git", "-C", str(root), "status", "--short"],
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()
        return {"branch": branch, "recent_commits": log, "status": status}
    except (FileNotFoundError, subprocess.CalledProcessError):
        return None


def duplicate_groups(skills: list[dict[str, object]], field: str) -> list[dict[str, object]]:
    groups: dict[str, list[dict[str, object]]] = defaultdict(list)
    for skill in skills:
        value = str(skill.get(field, ""))
        if value:
            groups[value].append(skill)
    return [
        {
            field: value,
            "skills": [
                {"name": item["name"], "scope": item["scope"], "path": item["path"]}
                for item in items
            ],
        }
        for value, items in sorted(groups.items())
        if len(items) > 1
    ]


def scan(root: Path, home: Path, max_depth: int, include_home: bool) -> dict[str, object]:
    instructions: list[dict[str, object]] = []
    system_context: list[dict[str, object]] = []
    project_context: list[dict[str, object]] = []
    tool_configs: list[dict[str, object]] = []
    skills: list[dict[str, object]] = []

    seen_instruction: set[Path] = set()
    seen_system_context: set[Path] = set()
    seen_project_context: set[Path] = set()
    seen_tool: set[Path] = set()
    seen_skill: set[Path] = set()

    for path in iter_project_files(root, max_depth):
        rel = path.relative_to(root)
        name = path.name
        if (
            name in INSTRUCTION_NAMES
            or name.endswith(".instructions.md")
            or name.endswith(".agent.md")
            or ".cursor/rules" in rel.as_posix()
        ) and path not in seen_instruction:
            instructions.append(instruction_record(path, "project", "detected", root, home))
            seen_instruction.add(path)

        if (
            name == "SYSTEM.md" or ".system" in rel.parts
        ) and path.suffix.lower() == ".md" and path not in seen_system_context:
            lines, size = text_metadata(path)
            system_context.append({
                "scope": "project",
                "path": display_path(path, root, home),
                "bytes": size,
                "lines": lines,
                "digest": digest_file(path),
            })
            seen_system_context.add(path)
        elif (
            name in PROJECT_CONTEXT_NAMES or ".project" in rel.parts
        ) and path.suffix.lower() == ".md" and path not in seen_project_context:
            lines, size = text_metadata(path)
            project_context.append({
                "scope": "project",
                "path": display_path(path, root, home),
                "bytes": size,
                "lines": lines,
                "digest": digest_file(path),
            })
            seen_project_context.add(path)

        if name in TOOL_CONFIG_NAMES and path not in seen_tool:
            lines, size = text_metadata(path)
            tool_configs.append({
                "scope": "project",
                "client": "detected",
                "path": display_path(path, root, home),
                "bytes": size,
                "lines": lines,
            })
            seen_tool.add(path)

        if name == "SKILL.md" and path not in seen_skill:
            skills.append(skill_record(path, "project", "detected", root, home))
            seen_skill.add(path)

    for path in ancestor_instruction_files(root, home):
        if path not in seen_instruction:
            instructions.append(instruction_record(path, "ancestor", "detected", root, home))
            seen_instruction.add(path)

    for rel in PROJECT_SKILL_ROOTS:
        skill_root = root / rel
        for record in scan_skill_root(skill_root, "project", rel.split("/")[0], root, home):
            skill_path = (root / record["skill_file"]).resolve() if not str(record["skill_file"]).startswith("~") else None
            if skill_path is None or skill_path not in seen_skill:
                skills.append(record)
                if skill_path is not None:
                    seen_skill.add(skill_path)

    project_tool_paths = (
        ("vscode", root / ".vscode/mcp.json"),
        ("cursor", root / ".cursor/mcp.json"),
        ("generic", root / ".mcp.json"),
    )
    for client, path in project_tool_paths:
        if path.is_file() and path not in seen_tool:
            lines, size = text_metadata(path)
            tool_configs.append({
                "scope": "project",
                "client": client,
                "path": display_path(path, root, home),
                "bytes": size,
                "lines": lines,
            })
            seen_tool.add(path)

    if include_home:
        for client, rel in USER_INSTRUCTION_PATHS:
            path = home / rel
            if path.is_file() and path not in seen_instruction:
                instructions.append(instruction_record(path, "user", client, root, home))
                seen_instruction.add(path)

        for client, rel in USER_SKILL_ROOTS:
            for record in scan_skill_root(home / rel, "user", client, root, home):
                skill_file = home / str(record["skill_file"]).removeprefix("~/")
                if skill_file not in seen_skill:
                    skills.append(record)
                    seen_skill.add(skill_file)

        for client, rel in USER_TOOL_CONFIG_PATHS:
            path = home / rel
            if path.is_file() and path not in seen_tool:
                lines, size = text_metadata(path)
                tool_configs.append({
                    "scope": "user",
                    "client": client,
                    "path": display_path(path, root, home),
                    "bytes": size,
                    "lines": lines,
                })
                seen_tool.add(path)

    instructions.sort(key=lambda item: (str(item["scope"]), str(item["path"])))
    system_context.sort(key=lambda item: str(item["path"]))
    project_context.sort(key=lambda item: str(item["path"]))
    tool_configs.sort(key=lambda item: (str(item["scope"]), str(item["path"])))
    skills.sort(key=lambda item: (str(item["scope"]), str(item["name"]), str(item["path"])))

    return {
        "root": str(root),
        "home_scanned": include_home,
        "instructions": instructions,
        "skills": skills,
        "skill_name_collisions": duplicate_groups(skills, "name"),
        "exact_skill_duplicates": duplicate_groups(skills, "digest"),
        "tool_configs": tool_configs,
        "system_context": system_context,
        "project_context": project_context,
        "git": git_summary(root),
        "notes": [
            "Tool configuration contents were not read.",
            "Runtime tools and connectors may exist beyond filesystem configuration and must be added by host inspection.",
            "Name collisions and exact duplicates are discovery signals, not semantic merge decisions.",
        ],
    }


def render_markdown(data: dict[str, object]) -> str:
    lines = [f"# Environment scan: `{data['root']}`", ""]

    lines.extend(["## Instructions", ""])
    instructions = data["instructions"]
    if instructions:
        for item in instructions:
            lines.append(
                f"- `{item['path']}` [{item['scope']}/{item['client']}] "
                f"({item['lines']} lines, {item['bytes']} bytes)"
            )
    else:
        lines.append("- None detected.")

    lines.extend(["", "## Skills", ""])
    skills = data["skills"]
    if skills:
        for item in skills:
            description = f" — {item['description']}" if item["description"] else ""
            lines.append(
                f"- `${item['name']}` [{item['scope']}/{item['client']}] "
                f"`{item['path']}`{description}"
            )
    else:
        lines.append("- None detected.")

    lines.extend(["", "## Exact discovery signals", ""])
    if data["skill_name_collisions"]:
        lines.append("- Skill-name collisions:")
        for group in data["skill_name_collisions"]:
            paths = ", ".join(f"`{item['path']}`" for item in group["skills"])
            lines.append(f"  - `{group['name']}`: {paths}")
    else:
        lines.append("- No repeated skill names detected.")
    if data["exact_skill_duplicates"]:
        lines.append("- Byte-identical `SKILL.md` files detected.")
    else:
        lines.append("- No byte-identical `SKILL.md` files detected.")

    lines.extend(["", "## Tool configuration surfaces", ""])
    if data["tool_configs"]:
        for item in data["tool_configs"]:
            lines.append(f"- `{item['path']}` [{item['scope']}/{item['client']}] (contents not read)")
    else:
        lines.append("- None detected on disk. Runtime tools may still be available.")

    lines.extend(["", "## System context", ""])
    if data["system_context"]:
        for item in data["system_context"]:
            lines.append(f"- `{item['path']}` ({item['lines']} lines)")
    else:
        lines.append("- None detected.")

    lines.extend(["", "## Project context", ""])
    if data["project_context"]:
        for item in data["project_context"]:
            lines.append(f"- `{item['path']}` ({item['lines']} lines)")
    else:
        lines.append("- None detected.")

    lines.extend(["", "## Git", ""])
    git = data["git"]
    if git is None:
        lines.append("- Git metadata unavailable.")
    else:
        lines.append(f"- Branch: `{git['branch'] or '(detached)'}`")
        lines.append(f"- Working-tree changes: {len(git['status'])}")
        lines.append("- Recent commits:")
        for commit in git["recent_commits"]:
            lines.append(f"  - `{commit}`")

    lines.extend(["", "## Notes", ""])
    for note in data["notes"]:
        lines.append(f"- {note}")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="Project root")
    parser.add_argument("--home", default=str(Path.home()), help="Home directory to inspect")
    parser.add_argument("--max-depth", type=int, default=6)
    parser.add_argument("--no-home", action="store_true", help="Do not inspect known user-level paths")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of Markdown")
    args = parser.parse_args()

    root = Path(args.root).expanduser().resolve()
    home = Path(args.home).expanduser().resolve()
    if not root.is_dir():
        parser.error(f"not a directory: {root}")
    if not home.is_dir():
        parser.error(f"not a directory: {home}")

    data = scan(root, home, args.max_depth, not args.no_home)
    if args.json:
        print(json.dumps(data, indent=2))
    else:
        print(render_markdown(data), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
