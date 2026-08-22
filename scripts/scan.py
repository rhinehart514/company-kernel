#!/usr/bin/env python3
"""Inspect Company Kernel context and capability surfaces without reading secrets."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
from pathlib import Path

INSTRUCTION_NAMES = {
    "AGENTS.md", "CLAUDE.md", "GEMINI.md", "COPILOT.md", ".cursorrules", "PROJECT.md"
}
TOOL_CONFIG_NAMES = {".mcp.json", "mcp.json", "settings.json", "config.toml"}
SKILL_ROOTS = [".agents/skills", ".claude/skills", ".github/skills", ".copilot/skills"]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".")
    parser.add_argument("--home", default=str(Path.home()))
    parser.add_argument("--kernel-home")
    parser.add_argument("--json", action="store_true")
    return parser.parse_args()


def tree_digest(path: Path) -> str:
    digest = hashlib.sha256()
    for item in sorted(p for p in path.rglob("*") if p.is_file()):
        digest.update(item.relative_to(path).as_posix().encode())
        digest.update(b"\0")
        digest.update(item.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def relative(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return str(path)


def find_named(root: Path, names: set[str], depth: int) -> list[str]:
    if not root.exists():
        return []
    found = []
    for path in root.rglob("*"):
        if path.is_file() and path.name in names and len(path.relative_to(root).parts) <= depth:
            found.append(relative(path, root))
    return sorted(set(found))


def find_skills(roots: list[Path]) -> list[dict[str, str]]:
    found = []
    for root in roots:
        if not root.exists():
            continue
        for skill_file in root.glob("*/SKILL.md"):
            skill = skill_file.parent
            found.append({"name": skill.name, "path": str(skill), "digest": tree_digest(skill)})
    return sorted(found, key=lambda item: item["path"])


def git_state(root: Path) -> dict[str, object]:
    try:
        branch = subprocess.run(
            ["git", "-C", str(root), "branch", "--show-current"],
            capture_output=True, text=True, check=False,
        ).stdout.strip()
        status = subprocess.run(
            ["git", "-C", str(root), "status", "--porcelain"],
            capture_output=True, text=True, check=False,
        ).stdout.splitlines()
        recent = subprocess.run(
            ["git", "-C", str(root), "log", "-5", "--pretty=%h %s"],
            capture_output=True, text=True, check=False,
        ).stdout.splitlines()
        return {"branch": branch or None, "dirty": bool(status), "changed": status[:50], "recent": recent}
    except OSError:
        return {"branch": None, "dirty": None, "changed": [], "recent": []}


def main() -> int:
    args = parse_args()
    root = Path(args.root).expanduser().resolve()
    home = Path(args.home).expanduser().resolve()
    kernel_home = Path(
        args.kernel_home or os.environ.get("COMPANY_KERNEL_HOME", home / ".company-kernel")
    ).expanduser().resolve()

    instructions = []
    for base, depth in ((root, 5), (home, 3)):
        instructions.extend(
            {"root": str(base), "path": path}
            for path in find_named(base, INSTRUCTION_NAMES, depth)
        )

    skill_roots = [root / path for path in SKILL_ROOTS] + [home / path for path in SKILL_ROOTS]
    skills = find_skills(skill_roots)
    by_digest: dict[str, list[str]] = {}
    for skill in skills:
        by_digest.setdefault(skill["digest"], []).append(skill["path"])

    project_context = []
    for path in [root / "PROJECT.md", *(root / ".kernel").glob("*.md")]:
        if path.is_file():
            project_context.append(relative(path, root))

    result = {
        "root": str(root),
        "kernel_home": str(kernel_home),
        "instructions": instructions,
        "shared_kernel": sorted(
            relative(path, kernel_home)
            for path in kernel_home.rglob("*")
            if path.is_file()
        ) if kernel_home.exists() else [],
        "project_context": sorted(project_context),
        "legacy_company_kernel": sorted(
            relative(path, root)
            for path in [root / ".project", root / "SYSTEM.md", root / ".system"]
            if path.exists()
        ),
        "skills": skills,
        "exact_skill_duplicates": [paths for paths in by_digest.values() if len(paths) > 1],
        "tool_configs": find_named(root, TOOL_CONFIG_NAMES, 5) + find_named(home, TOOL_CONFIG_NAMES, 3),
        "git": git_state(root),
    }

    print(json.dumps(result, indent=2) if args.json else result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
