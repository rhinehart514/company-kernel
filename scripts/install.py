#!/usr/bin/env python3
"""Install Company Kernel 0.5 skills without changing system or project context."""

from __future__ import annotations

import argparse
import hashlib
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "plugins" / "company-kernel" / "skills"
CLIENT_PATHS = {
    "agents": (Path.home() / ".agents" / "skills", ".agents/skills"),
    "claude": (Path.home() / ".claude" / "skills", ".claude/skills"),
    "copilot": (Path.home() / ".copilot" / "skills", ".github/skills"),
}


def tree_digest(path: Path) -> str:
    digest = hashlib.sha256()
    for item in sorted(p for p in path.rglob("*") if p.is_file()):
        digest.update(item.relative_to(path).as_posix().encode())
        digest.update(b"\0")
        digest.update(item.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def copy_skill(source: Path, destination: Path, force: bool, dry_run: bool) -> str:
    if destination.exists():
        if tree_digest(source) == tree_digest(destination):
            return "unchanged"
        if not force:
            raise FileExistsError(
                f"{destination} exists with different content; use --force to replace it"
            )
    if dry_run:
        return "would install"
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists():
        shutil.rmtree(destination)
    shutil.copytree(source, destination)
    return "installed"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    scope = parser.add_mutually_exclusive_group()
    scope.add_argument("--user", action="store_true")
    scope.add_argument("--project", metavar="PATH")
    parser.add_argument("--client", choices=sorted(CLIENT_PATHS), default="agents")
    parser.add_argument("--target")
    parser.add_argument("--skill", action="append")
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def destination_root(ns: argparse.Namespace) -> Path:
    if ns.target:
        return Path(ns.target).expanduser().resolve()
    user_path, project_rel = CLIENT_PATHS[ns.client]
    if ns.project:
        return (Path(ns.project).expanduser().resolve() / project_rel).resolve()
    return user_path


def main() -> int:
    ns = parse_args()
    available = {p.name: p for p in SOURCE.iterdir() if (p / "SKILL.md").is_file()}
    selected = ns.skill or sorted(available)
    unknown = [name for name in selected if name not in available]
    if unknown:
        print(f"error: unknown skill(s): {', '.join(unknown)}", file=sys.stderr)
        print(f"available: {', '.join(sorted(available))}", file=sys.stderr)
        return 2

    destination = destination_root(ns)
    print(f"Company Kernel 0.5 skills -> {destination}")
    try:
        for name in selected:
            state = copy_skill(available[name], destination / name, ns.force, ns.dry_run)
            print(f"- {name}: {state}")
    except FileExistsError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    if not ns.dry_run:
        print("\nNext:\n")
        print(
            "$kernel-integrate Install Company Kernel 0.5 above my projects, "
            "inspect existing rules and capabilities, preserve stronger work, "
            "and initialize this repository."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
