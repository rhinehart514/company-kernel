#!/usr/bin/env python3
"""Scan a repository for instruction and project-context surfaces.

This script is deterministic discovery, not project judgment.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
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

EXACT_NAMES = {
    "AGENTS.md",
    "CLAUDE.md",
    "GEMINI.md",
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

SPECIAL_PATH_PARTS = {
    ".agents",
    ".claude",
    ".cursor",
    ".github",
    ".project",
    "skills",
}


def iter_candidates(root: Path, max_depth: int) -> Iterable[Path]:
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
            path = current_path / name
            rel = path.relative_to(root)
            if (
                name in EXACT_NAMES
                or name.endswith(".instructions.md")
                or name.endswith(".agent.md")
                or name == "SKILL.md"
                or any(part in SPECIAL_PATH_PARTS for part in rel.parts)
            ):
                yield path


def file_record(root: Path, path: Path) -> dict[str, object]:
    try:
        text = path.read_text(encoding="utf-8")
        lines = text.count("\n") + (1 if text else 0)
    except (UnicodeDecodeError, OSError):
        lines = None
    stat = path.stat()
    return {
        "path": path.relative_to(root).as_posix(),
        "bytes": stat.st_size,
        "lines": lines,
    }


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


def render_markdown(root: Path, records: list[dict[str, object]], git: dict[str, object] | None) -> str:
    lines = [f"# Context scan: `{root}`", "", "## Relevant files", ""]
    if records:
        for record in records:
            detail = f"{record['bytes']} bytes"
            if record["lines"] is not None:
                detail += f", {record['lines']} lines"
            lines.append(f"- `{record['path']}` ({detail})")
    else:
        lines.append("- No known instruction or project-context files found.")

    lines.extend(["", "## Git", ""])
    if git is None:
        lines.append("- Git metadata unavailable.")
    else:
        lines.append(f"- Branch: `{git['branch'] or '(detached)'}`")
        lines.append(f"- Working-tree changes: {len(git['status'])}")
        lines.append("- Recent commits:")
        for commit in git["recent_commits"]:
            lines.append(f"  - `{commit}`")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="Repository or project root")
    parser.add_argument("--max-depth", type=int, default=5)
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of Markdown")
    args = parser.parse_args()

    root = Path(args.root).expanduser().resolve()
    if not root.is_dir():
        parser.error(f"not a directory: {root}")

    records = sorted(
        (file_record(root, path) for path in iter_candidates(root, args.max_depth)),
        key=lambda record: str(record["path"]),
    )
    git = git_summary(root)

    if args.json:
        print(json.dumps({"root": str(root), "files": records, "git": git}, indent=2))
    else:
        print(render_markdown(root, records, git), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
