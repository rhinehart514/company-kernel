#!/usr/bin/env python3
"""Install Company Kernel skills without changing system or project context."""

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
                f"{destination} already exists with different content; use --force to replace it"
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
    scope.add_argument("--user", action="store_true", help="Install for the current user")
    scope.add_argument("--project", metavar="PATH", help="Install inside one project")
    parser.add_argument("--client", choices=sorted(CLIENT_PATHS), default="agents")
    parser.add_argument("--target", help="Install into an explicit skills directory")
    parser.add_argument("--skill", action="append", help="Install only this skill; repeat for several")
    parser.add_argument("--force", action="store_true", help="Replace changed installed skills")
    parser.add_argument("--dry-run", action="store_true", help="Show changes without writing")
    return parser.parse_args()


def destination_root(args: argparse.Namespace) -> Path:
    if args.target:
        return Path(args.target).expanduser().resolve()
    user_path, project_rel = CLIENT_PATHS[args.client]
    if args.project:
        return (Path(args.project).expanduser().resolve() / project_rel).resolve()
    return user_path


def main() -> int:
    args = parse_args()
    if not SOURCE.is_dir():
        print(f"error: skill source not found: {SOURCE}", file=sys.stderr)
        return 2

    available = {path.name: path for path in SOURCE.iterdir() if (path / "SKILL.md").is_file()}
    selected = args.skill or sorted(available)
    unknown = [name for name in selected if name not in available]
    if unknown:
        print(f"error: unknown skill(s): {', '.join(unknown)}", file=sys.stderr)
        print(f"available: {', '.join(sorted(available))}", file=sys.stderr)
        return 2

    destination = destination_root(args)
    print(f"Company Kernel skills -> {destination}")
    try:
        for name in selected:
            state = copy_skill(available[name], destination / name, args.force, args.dry_run)
            print(f"- {name}: {state}")
    except FileExistsError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    if not args.dry_run:
        print("\nNext:\n")
        print(
            "$system-integrate Build or reconcile the shared Company Kernel system "
            "above my projects, inspect existing rules, skills, and tools, then "
            "initialize this repository. Do not delete unrelated global work."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
