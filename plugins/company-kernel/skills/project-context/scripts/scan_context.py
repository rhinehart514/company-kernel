#!/usr/bin/env python3
"""Find instruction and project-context surfaces in one repository."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
from pathlib import Path

EXCLUDED = {".git", ".venv", "venv", "node_modules", "vendor", "dist", "build", "coverage", "__pycache__"}
INSTRUCTIONS = {"AGENTS.md", "CLAUDE.md", "GEMINI.md", ".cursorrules", "copilot-instructions.md"}
PROJECT_NAMES = {"PROJECT.md", "COMPANY.md", "PRODUCT.md", "MARKET.md", "GTM.md", "STRATEGY.md", "DESIGN.md", "ENGINEERING.md", "SOFTWARE.md", "RESEARCH.md", "OPERATING.md", "OPERATIONS.md", "NOW.md", "STATE.md"}


def meta(root: Path, path: Path) -> dict[str, object]:
    try:
        text = path.read_text(encoding="utf-8")
        lines = text.count("\n") + (1 if text else 0)
    except (UnicodeDecodeError, OSError):
        lines = None
    return {"path": path.relative_to(root).as_posix(), "bytes": path.stat().st_size, "lines": lines}


def git_state(root: Path) -> dict[str, object] | None:
    try:
        inside = subprocess.run(["git", "-C", str(root), "rev-parse", "--is-inside-work-tree"], capture_output=True, text=True, check=True).stdout.strip()
        if inside != "true":
            return None
        branch = subprocess.run(["git", "-C", str(root), "branch", "--show-current"], capture_output=True, text=True, check=True).stdout.strip()
        status = subprocess.run(["git", "-C", str(root), "status", "--short"], capture_output=True, text=True, check=True).stdout.splitlines()
        commits = subprocess.run(["git", "-C", str(root), "log", "-n", "8", "--date=short", "--pretty=format:%h%x09%ad%x09%s"], capture_output=True, text=True, check=True).stdout.splitlines()
        return {"branch": branch, "status": status, "recent_commits": commits}
    except (FileNotFoundError, subprocess.CalledProcessError):
        return None


def scan(root: Path, max_depth: int) -> dict[str, object]:
    groups = {"instructions": [], "project_context": [], "skills": [], "legacy_project_system": []}
    base_depth = len(root.parts)
    for current, dirs, names in os.walk(root):
        here = Path(current)
        depth = len(here.parts) - base_depth
        dirs[:] = [name for name in dirs if name not in EXCLUDED and depth < max_depth]
        for name in names:
            path = here / name
            rel = path.relative_to(root)
            support_content = "skills" in rel.parts or (rel.parts and rel.parts[0] == "examples")
            if not support_content and (name in INSTRUCTIONS or name.endswith((".instructions.md", ".agent.md"))):
                groups["instructions"].append(meta(root, path))
            if name == "SKILL.md":
                groups["skills"].append(meta(root, path))
            if support_content:
                continue
            if name == "SYSTEM.md" or ".system" in rel.parts:
                groups["legacy_project_system"].append(meta(root, path))
            elif name in PROJECT_NAMES or ".project" in rel.parts:
                if path.suffix.lower() == ".md":
                    groups["project_context"].append(meta(root, path))
    for values in groups.values():
        values.sort(key=lambda item: str(item["path"]))
    return {"root": str(root), **groups, "git": git_state(root)}


def render(data: dict[str, object]) -> str:
    lines = [f"# Project scan: `{data['root']}`"]
    for key, title in (("instructions", "Instructions"), ("project_context", "Project context"), ("skills", "Project skills"), ("legacy_project_system", "Legacy project system")):
        lines.extend(["", f"## {title}", ""])
        items = data[key]
        if items:
            for item in items:
                lines.append(f"- `{item['path']}` ({item['lines']} lines, {item['bytes']} bytes)")
        else:
            lines.append("- None detected.")
    lines.extend(["", "## Git", ""])
    git = data["git"]
    if git is None:
        lines.append("- Git metadata unavailable.")
    else:
        lines.append(f"- Branch: `{git['branch'] or '(detached)'}`")
        lines.append(f"- Working-tree changes: {len(git['status'])}")
        for commit in git["recent_commits"]:
            lines.append(f"- `{commit}`")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".")
    parser.add_argument("--max-depth", type=int, default=6)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    root = Path(args.root).expanduser().resolve()
    if not root.is_dir():
        parser.error(f"not a directory: {root}")
    data = scan(root, args.max_depth)
    print(json.dumps(data, indent=2) if args.json else render(data))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
