#!/usr/bin/env python3
"""Discover shared system, instruction, skill, tool, and project surfaces.

The scanner reads metadata and skill frontmatter. It never prints tool secrets.
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

EXCLUDED = {".git", ".venv", "venv", "node_modules", "vendor", "dist", "build", "coverage", "__pycache__"}
INSTRUCTION_NAMES = {"AGENTS.md", "CLAUDE.md", "GEMINI.md", ".cursorrules", "copilot-instructions.md"}
PROJECT_CONTEXT_NAMES = {"PROJECT.md", "COMPANY.md", "PRODUCT.md", "MARKET.md", "GTM.md", "STRATEGY.md", "DESIGN.md", "ENGINEERING.md", "SOFTWARE.md", "RESEARCH.md", "OPERATING.md", "OPERATIONS.md", "NOW.md", "STATE.md"}
PROJECT_SKILL_ROOTS = (".agents/skills", ".codex/skills", ".claude/skills", ".copilot/skills", ".github/skills", ".gemini/skills", ".cursor/skills")
USER_SKILL_ROOTS = (("agents", ".agents/skills"), ("codex", ".codex/skills"), ("claude", ".claude/skills"), ("copilot", ".copilot/skills"), ("gemini", ".gemini/skills"), ("cursor", ".cursor/skills"), ("agents-plugin", ".agents/plugins"), ("codex-plugin", ".codex/plugins"), ("claude-plugin", ".claude/plugins"))
USER_INSTRUCTIONS = (("agents", ".agents/AGENTS.md"), ("codex", ".codex/AGENTS.md"), ("claude", ".claude/CLAUDE.md"), ("gemini", ".gemini/GEMINI.md"))
USER_TOOL_CONFIGS = (("codex", ".codex/config.toml"), ("claude", ".claude.json"), ("claude", ".claude/settings.json"), ("cursor", ".cursor/mcp.json"), ("vscode", ".vscode/mcp.json"), ("generic", ".mcp.json"))
PROJECT_TOOL_CONFIGS = (("generic", ".mcp.json"), ("cursor", ".cursor/mcp.json"), ("vscode", ".vscode/mcp.json"))
FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def display(path: Path, root: Path, home: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        try:
            return "~/" + path.relative_to(home).as_posix()
        except ValueError:
            return str(path)


def file_meta(path: Path) -> tuple[int | None, int]:
    size = path.stat().st_size
    try:
        text = path.read_text(encoding="utf-8")
        return text.count("\n") + (1 if text else 0), size
    except (UnicodeDecodeError, OSError):
        return None, size


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()[:16]


def skill_frontmatter(path: Path) -> tuple[str, str]:
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
        key = key.strip()
        if key in {"name", "description"}:
            values[key] = value.strip().strip('"').strip("'")
    return values.get("name", path.parent.name), values.get("description", "")


def record_file(path: Path, scope: str, client: str, root: Path, home: Path) -> dict[str, object]:
    lines, size = file_meta(path)
    return {"scope": scope, "client": client, "path": display(path, root, home), "lines": lines, "bytes": size, "digest": digest(path)}


def record_skill(path: Path, scope: str, client: str, root: Path, home: Path) -> dict[str, object]:
    lines, size = file_meta(path)
    name, description = skill_frontmatter(path)
    return {"scope": scope, "client": client, "name": name, "description": description, "path": display(path.parent, root, home), "skill_file": display(path, root, home), "lines": lines, "bytes": size, "digest": digest(path)}


def scan_skill_root(skill_root: Path, scope: str, client: str, root: Path, home: Path) -> list[dict[str, object]]:
    if not skill_root.is_dir():
        return []
    return [record_skill(path, scope, client, root, home) for path in sorted(skill_root.rglob("SKILL.md")) if not any(part in EXCLUDED for part in path.parts)]


def iter_project_files(root: Path, max_depth: int):
    base = len(root.parts)
    for current, dirs, names in os.walk(root):
        here = Path(current)
        depth = len(here.parts) - base
        dirs[:] = [name for name in dirs if name not in EXCLUDED and depth < max_depth]
        for name in names:
            yield here / name


def ancestor_instructions(root: Path, home: Path):
    current = root.parent
    while current != current.parent:
        for name in ("AGENTS.md", "CLAUDE.md", "GEMINI.md"):
            candidate = current / name
            if candidate.is_file():
                yield candidate
        if current == home or home not in current.parents:
            break
        current = current.parent


def git_state(root: Path) -> dict[str, object] | None:
    try:
        if subprocess.run(["git", "-C", str(root), "rev-parse", "--is-inside-work-tree"], capture_output=True, text=True, check=True).stdout.strip() != "true":
            return None
        branch = subprocess.run(["git", "-C", str(root), "branch", "--show-current"], capture_output=True, text=True, check=True).stdout.strip()
        status = subprocess.run(["git", "-C", str(root), "status", "--short"], capture_output=True, text=True, check=True).stdout.splitlines()
        commits = subprocess.run(["git", "-C", str(root), "log", "-n", "8", "--date=short", "--pretty=format:%h%x09%ad%x09%s"], capture_output=True, text=True, check=True).stdout.splitlines()
        return {"branch": branch, "status": status, "recent_commits": commits}
    except (FileNotFoundError, subprocess.CalledProcessError):
        return None


def duplicates(skills: list[dict[str, object]], field: str) -> list[dict[str, object]]:
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    for skill in skills:
        value = str(skill.get(field, ""))
        if value:
            grouped[value].append(skill)
    return [{field: value, "skills": [{"name": item["name"], "scope": item["scope"], "path": item["path"]} for item in items]} for value, items in sorted(grouped.items()) if len(items) > 1]


def scan(root: Path, home: Path, system_home: Path, max_depth: int, include_home: bool) -> dict[str, object]:
    instructions: list[dict[str, object]] = []
    skills: list[dict[str, object]] = []
    tool_configs: list[dict[str, object]] = []
    project_context: list[dict[str, object]] = []
    legacy_project_system: list[dict[str, object]] = []
    shared_system: list[dict[str, object]] = []
    seen: set[Path] = set()

    for path in iter_project_files(root, max_depth):
        rel = path.relative_to(root)
        name = path.name
        support_content = "skills" in rel.parts or (rel.parts and rel.parts[0] == "examples")
        if not support_content and (name in INSTRUCTION_NAMES or name.endswith((".instructions.md", ".agent.md")) or ".cursor/rules" in rel.as_posix()):
            if path not in seen:
                instructions.append(record_file(path, "project", "detected", root, home)); seen.add(path)
        if name == "SKILL.md" and path not in seen:
            skills.append(record_skill(path, "project", "detected", root, home)); seen.add(path)
        if support_content:
            continue
        if name == "SYSTEM.md" or ".system" in rel.parts:
            if path.suffix.lower() == ".md":
                legacy_project_system.append(record_file(path, "project", "legacy", root, home))
        elif name in PROJECT_CONTEXT_NAMES or ".project" in rel.parts:
            if path.suffix.lower() == ".md":
                project_context.append(record_file(path, "project", "context", root, home))

    for path in ancestor_instructions(root, home):
        if path not in seen:
            instructions.append(record_file(path, "ancestor", "detected", root, home)); seen.add(path)

    for client, rel in PROJECT_TOOL_CONFIGS:
        path = root / rel
        if path.is_file():
            lines, size = file_meta(path)
            tool_configs.append({"scope": "project", "client": client, "path": display(path, root, home), "lines": lines, "bytes": size})

    if system_home.is_dir():
        for path in sorted(system_home.rglob("*.md")):
            shared_system.append(record_file(path, "shared", "company-kernel", root, home))

    if include_home:
        for client, rel in USER_INSTRUCTIONS:
            path = home / rel
            if path.is_file() and path not in seen:
                instructions.append(record_file(path, "user", client, root, home)); seen.add(path)
        for client, rel in USER_SKILL_ROOTS:
            skills.extend(scan_skill_root(home / rel, "user", client, root, home))
        for client, rel in USER_TOOL_CONFIGS:
            path = home / rel
            if path.is_file():
                lines, size = file_meta(path)
                tool_configs.append({"scope": "user", "client": client, "path": display(path, root, home), "lines": lines, "bytes": size})

    instructions.sort(key=lambda item: (str(item["scope"]), str(item["path"])))
    skills.sort(key=lambda item: (str(item["scope"]), str(item["name"]), str(item["path"])))
    tool_configs.sort(key=lambda item: (str(item["scope"]), str(item["path"])))
    project_context.sort(key=lambda item: str(item["path"]))
    legacy_project_system.sort(key=lambda item: str(item["path"]))
    shared_system.sort(key=lambda item: str(item["path"]))

    return {
        "root": str(root),
        "system_home": str(system_home),
        "home_scanned": include_home,
        "instructions": instructions,
        "skills": skills,
        "skill_name_collisions": duplicates(skills, "name"),
        "exact_skill_duplicates": duplicates(skills, "digest"),
        "tool_configs": tool_configs,
        "shared_system": shared_system,
        "project_context": project_context,
        "legacy_project_system": legacy_project_system,
        "git": git_state(root),
        "notes": [
            "Tool configuration contents were not read.",
            "Runtime tools may exist beyond filesystem configuration.",
            "Name collisions and exact duplicates are discovery signals, not automatic merge decisions.",
        ],
    }


def render(data: dict[str, object]) -> str:
    lines = [f"# Environment scan: `{data['root']}`", "", f"Shared system: `{data['system_home']}`"]
    for key, title in (("shared_system", "Shared system"), ("instructions", "Instructions"), ("skills", "Skills"), ("tool_configs", "Tool configuration paths"), ("project_context", "Project context"), ("legacy_project_system", "Legacy project-local system")):
        lines.extend(["", f"## {title}", ""])
        items = data[key]
        if items:
            for item in items:
                name = f"`${item['name']}` " if "name" in item else ""
                lines.append(f"- {name}`{item['path']}` [{item.get('scope','')}/{item.get('client','')}]" )
        else:
            lines.append("- None detected.")
    lines.extend(["", "## Discovery signals", ""])
    lines.append(f"- Skill-name collisions: {len(data['skill_name_collisions'])}")
    lines.append(f"- Exact skill duplicates: {len(data['exact_skill_duplicates'])}")
    lines.extend(["", "## Git", ""])
    git = data["git"]
    if git is None:
        lines.append("- Git metadata unavailable.")
    else:
        lines.append(f"- Branch: `{git['branch'] or '(detached)'}`")
        lines.append(f"- Working-tree changes: {len(git['status'])}")
    lines.extend(["", "## Notes", ""])
    for note in data["notes"]:
        lines.append(f"- {note}")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".")
    parser.add_argument("--home", default=str(Path.home()))
    parser.add_argument("--system-home", default=None)
    parser.add_argument("--max-depth", type=int, default=6)
    parser.add_argument("--no-home", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    root = Path(args.root).expanduser().resolve()
    home = Path(args.home).expanduser().resolve()
    system_home = Path(args.system_home or os.environ.get("COMPANY_KERNEL_HOME", home / ".company-kernel")).expanduser().resolve()
    if not root.is_dir():
        parser.error(f"not a directory: {root}")
    if not home.is_dir():
        parser.error(f"not a directory: {home}")
    data = scan(root, home, system_home, args.max_depth, not args.no_home)
    print(json.dumps(data, indent=2) if args.json else render(data))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
