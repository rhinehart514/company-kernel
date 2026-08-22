#!/usr/bin/env python3
"""Inspect project context and repository evidence without interpreting company truth."""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

CONTEXT_NAMES = {"PROJECT.md", "AGENTS.md", "CLAUDE.md", "GEMINI.md"}
EVIDENCE_DIRS = {"src", "app", "apps", "packages", "tests", "docs", ".github"}


def parse() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".")
    parser.add_argument("--json", action="store_true")
    return parser.parse_args()


def git(root: Path) -> dict[str, object]:
    branch = subprocess.run(
        ["git", "-C", str(root), "branch", "--show-current"],
        capture_output=True, text=True, check=False,
    ).stdout.strip()
    recent = subprocess.run(
        ["git", "-C", str(root), "log", "-5", "--pretty=%h %s"],
        capture_output=True, text=True, check=False,
    ).stdout.splitlines()
    changed = subprocess.run(
        ["git", "-C", str(root), "status", "--porcelain"],
        capture_output=True, text=True, check=False,
    ).stdout.splitlines()
    return {"branch": branch or None, "recent": recent, "changed": changed[:50]}


def main() -> int:
    ns = parse()
    root = Path(ns.root).expanduser().resolve()
    context = []
    for name in CONTEXT_NAMES:
        path = root / name
        if path.is_file():
            context.append(name)
    kernel = root / ".kernel"
    if kernel.exists():
        context.extend(p.relative_to(root).as_posix() for p in kernel.glob("*.md"))

    evidence = []
    for name in EVIDENCE_DIRS:
        path = root / name
        if path.exists():
            evidence.append(name)

    result = {
        "root": str(root),
        "project_context": sorted(context),
        "legacy_context": sorted(
            p.relative_to(root).as_posix()
            for p in [root / ".project", root / "SYSTEM.md", root / ".system"]
            if p.exists()
        ),
        "evidence_surfaces": sorted(evidence),
        "git": git(root),
    }
    print(json.dumps(result, indent=2) if ns.json else result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
