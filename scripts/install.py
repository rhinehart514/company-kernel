#!/usr/bin/env python3
"""Install Company Kernel 0.6 skills and the canonical shared kernel."""

from __future__ import annotations

import argparse
import hashlib
import os
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
KERNEL = ROOT / "kernel"
SCAN = ROOT / "scripts" / "scan.py"
CLIENT_PATHS = {
    "agents": (Path.home() / ".agents" / "skills", ".agents/skills"),
    "claude": (Path.home() / ".claude" / "skills", ".claude/skills"),
    "copilot": (Path.home() / ".copilot" / "skills", ".github/skills"),
}


def digest(path: Path) -> str:
    value = hashlib.sha256()
    if path.is_file():
        value.update(path.read_bytes())
        return value.hexdigest()
    for item in sorted(p for p in path.rglob("*") if p.is_file()):
        value.update(item.relative_to(path).as_posix().encode())
        value.update(b"\0")
        value.update(item.read_bytes())
        value.update(b"\0")
    return value.hexdigest()


def copy_tree(source: Path, destination: Path, force: bool, dry_run: bool) -> str:
    if destination.exists():
        if digest(source) == digest(destination):
            return "unchanged"
        if not force:
            return "changed; run $kernel-setup to reconcile or use --force"
    if dry_run:
        return "would install"
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists():
        shutil.rmtree(destination)
    shutil.copytree(source, destination)
    return "installed"


def copy_file(source: Path, destination: Path, force: bool, dry_run: bool) -> str:
    if destination.exists():
        if digest(source) == digest(destination):
            return "unchanged"
        if not force:
            return "changed; use --force to replace"
    if dry_run:
        return "would install"
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)
    return "installed"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    scope = parser.add_mutually_exclusive_group()
    scope.add_argument("--user", action="store_true", help="Install skills for the current user")
    scope.add_argument("--project", metavar="PATH", help="Install skills inside one project")
    parser.add_argument("--client", choices=sorted(CLIENT_PATHS), default="agents")
    parser.add_argument("--target-skills", help="Explicit skills directory, mainly for testing")
    parser.add_argument("--kernel-home", help="Shared kernel destination")
    parser.add_argument("--no-kernel", action="store_true", help="Install skills only")
    parser.add_argument("--skill", action="append", help="Install only this skill; repeat for several")
    parser.add_argument("--force", action="store_true", help="Replace changed Company Kernel files")
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def skills_destination(args: argparse.Namespace) -> Path:
    if args.target_skills:
        return Path(args.target_skills).expanduser().resolve()
    user_path, project_relative = CLIENT_PATHS[args.client]
    if args.project:
        return (Path(args.project).expanduser().resolve() / project_relative).resolve()
    return user_path


def kernel_destination(args: argparse.Namespace) -> Path:
    return Path(
        args.kernel_home
        or os.environ.get("COMPANY_KERNEL_HOME", Path.home() / ".company-kernel")
    ).expanduser().resolve()


def main() -> int:
    args = parse_args()
    available = {path.name: path for path in SKILLS.iterdir() if (path / "SKILL.md").is_file()}
    selected = args.skill or sorted(available)
    unknown = [name for name in selected if name not in available]
    if unknown:
        print(f"error: unknown skill(s): {', '.join(unknown)}", file=sys.stderr)
        print(f"available: {', '.join(sorted(available))}", file=sys.stderr)
        return 2

    destination = skills_destination(args)
    print(f"Company Kernel 0.6 skills -> {destination}")
    for name in selected:
        state = copy_tree(available[name], destination / name, args.force, args.dry_run)
        print(f"- {name}: {state}")

    if not args.no_kernel:
        kernel_home = kernel_destination(args)
        print(f"Company Kernel shared system -> {kernel_home}")
        for item in sorted(KERNEL.iterdir()):
            if item.is_dir():
                state = copy_tree(item, kernel_home / item.name, args.force, args.dry_run)
            else:
                state = copy_file(item, kernel_home / item.name, args.force, args.dry_run)
            print(f"- {item.name}: {state}")
        state = copy_file(SCAN, kernel_home / "bin" / "scan.py", args.force, args.dry_run)
        print(f"- bin/scan.py: {state}")

    if not args.dry_run:
        print("\nNext:\n")
        print(
            "$kernel-setup Set up or reconcile Company Kernel 0.6 on this machine, "
            "inspect existing rules and capabilities, preserve stronger work, "
            "add thin routes, and initialize this repository."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
