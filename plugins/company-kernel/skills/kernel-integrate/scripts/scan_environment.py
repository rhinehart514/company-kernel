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
    "AGENTS.md", "CLAUDE.md", "GEMINI.md", "COPILOT.md",
    ".cursorrules", "PROJECT.md",
}
TOOL_CONFIG_NAMES = {".mcp.json", "mcp.json", "settings.json", "config.toml"}
SKILL_ROOTS = [
    ".agents/skills", ".claude/skills", ".github/skills", ".copilot/skills",
]


def args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".")
    parser.add_argument("--home", default=str(Path.home()))
    parser.add_argument("--system-home")
    parser.add_argument("--json", action="store_true")
    return parser.parse_args()


def digest(path: Path) -> str:
    h = hashlib.sha256()
    for item in sorted(p for p in path.rglob("*") if p.is_file()):
        h.update(item.relative_to(path).as_posix().encode())
        h.update(b"\0")
        h.update(item.read_bytes())
        h.update(b"\0")
    return h.hexdigest()


def rel(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return str(path)


def find_files(root: Path, names: set[str], depth: int = 5) -> list[str]:
    found = []
    if not root.exists():
        return found
    for path in root.rglob("*"):
        if path.is_file() and path.name in names and len(path.relative_to(root).parts) <= depth:
            found.append(rel(path, root))
    return sorted(set(found))


def find_skills(roots: list[Path]) -> list[dict[str, str]]:
    out = []
    for root in roots:
        if not root.exists():
            continue
        for skill_file in root.glob("*/SKILL.md"):
            folder = skill_file.parent
            out.append({"path": str(folder), "name": folder.name, "digest": digest(folder)})
    return sorted(out, key=lambda x: x["path"])


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
        return {"branch": branch or None, "dirty": bool(status), "changed": status[:50]}
    except OSError:
        return {"branch": None, "dirty": None, "changed": []}


def main() -> int:
    ns = args()
    root = Path(ns.root).expanduser().resolve()
    home = Path(ns.home).expanduser().resolve()
    system_home = Path(
        ns.system_home or os.environ.get("COMPANY_KERNEL_HOME", home / ".company-kernel")
    ).expanduser().resolve()

    instruction_roots = [root, home]
    instructions = []
    for base in instruction_roots:
        instructions.extend({"root": str(base), "path": p} for p in find_files(base, INSTRUCTION_NAMES, 4))

    skill_roots = [root / p for p in SKILL_ROOTS] + [home / p for p in SKILL_ROOTS]
    skills = find_skills(skill_roots)
    by_digest: dict[str, list[str]] = {}
    for skill in skills:
        by_digest.setdefault(skill["digest"], []).append(skill["path"])

    result = {
        "root": str(root),
        "system_home": str(system_home),
        "instructions": instructions,
        "shared_kernel": sorted(
            rel(p, system_home) for p in system_home.rglob("*") if p.is_file()
        ) if system_home.exists() else [],
        "project_context": sorted(
            rel(p, root) for p in [root / "PROJECT.md", *(root / ".kernel").glob("*.md")]
            if p.is_file()
        ),
        "legacy_context": sorted(
            rel(p, root) for p in [root / ".project", root / "SYSTEM.md", root / ".system"]
            if p.exists()
        ),
        "skills": skills,
        "exact_skill_duplicates": [paths for paths in by_digest.values() if len(paths) > 1],
        "tool_configs": find_files(root, TOOL_CONFIG_NAMES, 5) + find_files(home, TOOL_CONFIG_NAMES, 4),
        "git": git_state(root),
    }

    if ns.json:
        print(json.dumps(result, indent=2))
    else:
        for key, value in result.items():
            print(f"{key}: {value}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
