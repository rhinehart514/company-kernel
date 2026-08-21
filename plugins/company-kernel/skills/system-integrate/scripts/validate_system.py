#!/usr/bin/env python3
"""Validate a target project's thin SYSTEM.md and linked .system lenses."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

LINK_RE = re.compile(r"\]\(([^)#]+)(?:#[^)]+)?\)")


def steering_lines(path: Path) -> list[str]:
    lines: list[str] = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        text = raw.strip()
        if not text or text.startswith("#") or text.startswith("<!--"):
            continue
        lines.append(text)
    return lines


def local_links(path: Path) -> list[str]:
    links: list[str] = []
    for link in LINK_RE.findall(path.read_text(encoding="utf-8")):
        if "://" in link or link.startswith(("mailto:", "#")):
            continue
        links.append(link)
    return links


def validate(root: Path) -> dict[str, object]:
    system = root / "SYSTEM.md"
    errors: list[str] = []
    records: list[dict[str, object]] = []

    if not system.is_file():
        return {
            "root": str(root),
            "files": [],
            "errors": ["SYSTEM.md is required."],
            "ok": False,
        }

    lens_dir = root / ".system"
    lenses = sorted(path for path in lens_dir.rglob("*.md") if path.is_file()) if lens_dir.is_dir() else []
    files = [system, *lenses]

    system_links = {
        (system.parent / link).resolve()
        for link in local_links(system)
        if link.startswith(".system/")
    }

    for path in files:
        relative = path.relative_to(root).as_posix()
        lines = steering_lines(path)
        if not 1 <= len(lines) <= 10:
            errors.append(
                f"{relative}: expected 1-10 non-empty steering lines excluding headings; found {len(lines)}"
            )
        text = path.read_text(encoding="utf-8")
        if "TODO" in text or "TBD" in text:
            errors.append(f"{relative}: contains TODO/TBD placeholder")
        broken: list[str] = []
        for link in local_links(path):
            target = (path.parent / link).resolve()
            if not target.exists():
                broken.append(link)
                errors.append(f"{relative}: broken link {link}")
        records.append({
            "path": relative,
            "steering_lines": len(lines),
            "broken_links": broken,
        })

    for lens in lenses:
        if lens.resolve() not in system_links:
            errors.append(
                f"{lens.relative_to(root).as_posix()}: lens is not linked from SYSTEM.md"
            )

    for linked in system_links:
        if lens_dir.resolve() not in linked.parents:
            errors.append(f"SYSTEM.md: linked system lens escapes .system: {linked}")

    return {"root": str(root), "files": records, "errors": errors, "ok": not errors}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    root = Path(args.root).expanduser().resolve()
    if not root.is_dir():
        parser.error(f"not a directory: {root}")

    result = validate(root)
    if args.json:
        print(json.dumps(result, indent=2))
    elif result["ok"]:
        print("OK: thin system context is valid")
        for item in result["files"]:
            print(f"- {item['path']}: {item['steering_lines']} steering lines")
    else:
        print("FAIL: system context validation")
        for error in result["errors"]:
            print(f"- {error}")
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
