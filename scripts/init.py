#!/usr/bin/env python3
"""Initialize Company Kernel 0.7 in one project without replacing existing truth."""

from __future__ import annotations

import argparse
import os
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = ROOT / "templates"
ROUTE_START = "<!-- company-kernel:route:start -->"
ROUTE_END = "<!-- company-kernel:route:end -->"
LEGACY_PROJECT_FILES = {
    ".kernel/CODING.md": ".kernel/project/SOFTWARE.md",
    ".kernel/PRODUCT.md": ".kernel/project/PRODUCT.md",
    ".kernel/GTM.md": ".kernel/project/GTM.md",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="Project root")
    parser.add_argument("--kernel-home", help="Installed Company Kernel home")
    parser.add_argument("--migrate", action="store_true", help="Move recognized 0.6 project files")
    parser.add_argument("--no-route", action="store_true", help="Do not add or refresh AGENTS.md route")
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def kernel_destination(args: argparse.Namespace) -> Path:
    return Path(
        args.kernel_home
        or os.environ.get("COMPANY_KERNEL_HOME", Path.home() / ".company-kernel")
    ).expanduser().resolve()


def display_path(path: Path) -> str:
    try:
        return "~/" + path.relative_to(Path.home()).as_posix()
    except ValueError:
        return str(path)


def route_text(kernel_home: Path) -> str:
    entry = display_path(kernel_home / "KERNEL.md")
    return f"""{ROUTE_START}
## Company Kernel

System entry: `{entry}`.

For consequential work, follow system -> company -> project -> work.

Read `COMPANY.md`, `PROJECT.md`, and `.kernel/NOW.md` when they exist. Load only the system domains and matching `.kernel/company/<DOMAIN>.md` or `.kernel/project/<DOMAIN>.md` files that can materially change the decision.

Use system files as judgment, company files as cross-project truth, project files as local truth, and the current request as the immediate outcome. More specific context narrows broader context without silently replacing it.

Observed reality outranks stale context. Use `$project-update` when durable truth changes. Do not modify shared system files without explicit human approval.
{ROUTE_END}"""


def ensure_from_template(template: Path, destination: Path, dry_run: bool) -> str:
    if destination.exists():
        return "preserved"
    if dry_run:
        return "would create"
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(template, destination)
    return "created"


def upsert_route(path: Path, block: str, dry_run: bool) -> str:
    text = path.read_text(encoding="utf-8") if path.exists() else "# Agent instructions\n"
    has_start = ROUTE_START in text
    has_end = ROUTE_END in text
    if has_start != has_end:
        raise ValueError(f"{path}: incomplete Company Kernel route markers")

    if has_start:
        before, remainder = text.split(ROUTE_START, 1)
        _, after = remainder.split(ROUTE_END, 1)
        updated = before.rstrip() + "\n\n" + block + after
    else:
        updated = text.rstrip() + "\n\n" + block + "\n"

    if updated == text:
        return "unchanged"
    if dry_run:
        return "would update" if path.exists() else "would create"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(updated, encoding="utf-8")
    return "updated" if has_start else ("appended" if text.strip() != "# Agent instructions" else "created")


def migrate_project(root: Path, dry_run: bool) -> list[str]:
    states: list[str] = []
    for source_name, destination_name in LEGACY_PROJECT_FILES.items():
        source = root / source_name
        destination = root / destination_name
        if not source.is_file():
            continue
        if destination.exists():
            states.append(f"- {source_name}: preserved; {destination_name} already exists")
            continue
        if not dry_run:
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(source), str(destination))
        states.append(f"- {source_name} -> {destination_name}: {'would move' if dry_run else 'moved'}")
    return states


def main() -> int:
    args = parse_args()
    root = Path(args.root).expanduser().resolve()
    kernel_home = kernel_destination(args)

    if not root.is_dir():
        print(f"error: project root does not exist: {root}", file=sys.stderr)
        return 2
    if not (kernel_home / "KERNEL.md").is_file():
        print(f"error: Company Kernel is not installed at {kernel_home}", file=sys.stderr)
        return 2
    if not TEMPLATES.is_dir():
        print(f"error: templates not found at {TEMPLATES}", file=sys.stderr)
        return 2

    print(f"Company Kernel 0.7 project -> {root}")

    core = {
        "COMPANY.md": TEMPLATES / "COMPANY.md",
        "PROJECT.md": TEMPLATES / "PROJECT.md",
        ".kernel/NOW.md": TEMPLATES / ".kernel" / "NOW.md",
    }
    for destination_name, template in core.items():
        state = ensure_from_template(template, root / destination_name, args.dry_run)
        print(f"- {destination_name}: {state}")

    if args.migrate:
        migrated = migrate_project(root, args.dry_run)
        if migrated:
            print("- migration:")
            print("\n".join(f"  {line}" for line in migrated))
        else:
            print("- migration: no recognized 0.6 project files")

    if not args.no_route:
        try:
            state = upsert_route(root / "AGENTS.md", route_text(kernel_home), args.dry_run)
        except ValueError as exc:
            print(f"error: {exc}", file=sys.stderr)
            return 2
        print(f"- AGENTS.md route: {state}")

    legacy = [
        name
        for name in ("SYSTEM.md", ".system", ".project")
        if (root / name).exists()
    ]
    if legacy:
        print(f"- legacy context preserved for review: {', '.join(legacy)}")

    print("- optional domains: withheld until durable truth earns them")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
