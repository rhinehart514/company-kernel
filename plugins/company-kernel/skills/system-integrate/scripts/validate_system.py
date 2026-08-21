#!/usr/bin/env python3
"""Validate shared Company Kernel system context."""

from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path

LINK_RE = re.compile(r"\]\(([^)#]+)(?:#[^)]+)?\)")


def steering_lines(path: Path) -> list[str]:
    return [line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip() and not line.lstrip().startswith("#")]


def links(path: Path) -> list[str]:
    return [link for link in LINK_RE.findall(path.read_text(encoding="utf-8")) if "://" not in link and not link.startswith(("#", "mailto:"))]


def validate(home: Path) -> dict[str, object]:
    errors: list[str] = []
    system = home / "SYSTEM.md"
    index = home / "LENSES.md"
    lens_dir = home / "lenses"
    if not system.is_file():
        errors.append("SYSTEM.md is required")
    if not index.is_file():
        errors.append("LENSES.md is required")
    lenses = sorted(lens_dir.glob("*.md")) if lens_dir.is_dir() else []
    active = [path for path in [system, *lenses] if path.is_file()]
    records = []
    for path in active:
        count = len(steering_lines(path))
        if not 1 <= count <= 10:
            errors.append(f"{path.relative_to(home)}: expected 1-10 steering lines, found {count}")
        text = path.read_text(encoding="utf-8")
        if "TODO" in text or "TBD" in text:
            errors.append(f"{path.relative_to(home)}: contains TODO/TBD")
        records.append({"path": path.relative_to(home).as_posix(), "steering_lines": count})
    if system.is_file() and "LENSES.md" not in links(system):
        errors.append("SYSTEM.md must link to LENSES.md")
    if index.is_file():
        indexed = {(index.parent / link).resolve() for link in links(index) if link.startswith("lenses/")}
        for lens in lenses:
            if lens.resolve() not in indexed:
                errors.append(f"{lens.relative_to(home)}: not linked from LENSES.md")
        for target in indexed:
            if not target.is_file():
                errors.append(f"LENSES.md: broken lens link {target}")
    return {"system_home": str(home), "files": records, "errors": errors, "ok": not errors}


def main() -> int:
    default_home = Path(os.environ.get("COMPANY_KERNEL_HOME", Path.home() / ".company-kernel"))
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--system-home", default=str(default_home))
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    home = Path(args.system_home).expanduser().resolve()
    result = validate(home)
    if args.json:
        print(json.dumps(result, indent=2))
    elif result["ok"]:
        print("OK: shared system context is valid")
        for item in result["files"]:
            print(f"- {item['path']}: {item['steering_lines']} steering lines")
    else:
        print("FAIL: shared system context")
        for error in result["errors"]:
            print(f"- {error}")
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
