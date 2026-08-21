#!/usr/bin/env python3
"""Validate Company Kernel manifests, skills, resources, evals, scripts, and examples."""

from __future__ import annotations

import json
import py_compile
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "company-kernel"
SKILLS = PLUGIN / "skills"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_RE = re.compile(r"\]\(([^)#]+)(?:#[^)]+)?\)")


class ValidationError(Exception):
    pass


def fail(message: str) -> None:
    raise ValidationError(message)


def parse_frontmatter(path: Path) -> tuple[dict[str, str], str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail(f"{path}: missing YAML frontmatter")
    try:
        _, raw, body = text.split("---\n", 2)
    except ValueError:
        fail(f"{path}: malformed frontmatter")
    data: dict[str, str] = {}
    in_metadata = False
    for line in raw.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith("metadata:"):
            in_metadata = True
            continue
        if line.startswith((" ", "\t")):
            continue
        in_metadata = False
        if ":" not in line:
            fail(f"{path}: unsupported frontmatter line: {line!r}")
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data, body


def validate_json(path: Path) -> object:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"{path}: invalid JSON: {exc}")


def validate_skill(skill: Path) -> None:
    skill_file = skill / "SKILL.md"
    data, body = parse_frontmatter(skill_file)
    name = data.get("name", "")
    description = data.get("description", "")
    if name != skill.name:
        fail(f"{skill_file}: name {name!r} must match directory {skill.name!r}")
    if not NAME_RE.fullmatch(name):
        fail(f"{skill_file}: invalid skill name {name!r}")
    if not description or len(description) > 1024:
        fail(f"{skill_file}: description must contain 1-1024 characters")
    if len(body.splitlines()) > 500:
        fail(f"{skill_file}: body exceeds 500-line progressive-disclosure limit")

    for link in LINK_RE.findall(body):
        if "://" in link or link.startswith(("mailto:", "#")):
            continue
        target = (skill / link).resolve()
        if not target.exists():
            fail(f"{skill_file}: broken referenced resource {link}")

    eval_dir = skill / "evals"
    for name in ("triggers.json", "behavior.json"):
        path = eval_dir / name
        if not path.is_file():
            fail(f"{skill}: missing {path.relative_to(skill)}")
        data_obj = validate_json(path)
        if not isinstance(data_obj, list) or not data_obj:
            fail(f"{path}: expected a non-empty list")
    triggers = validate_json(eval_dir / "triggers.json")
    for index, case in enumerate(triggers):
        if set(case) != {"prompt", "should_trigger"}:
            fail(f"{eval_dir / 'triggers.json'}[{index}]: invalid keys")
        if not isinstance(case["should_trigger"], bool):
            fail(f"{eval_dir / 'triggers.json'}[{index}]: should_trigger must be boolean")

    agent_file = skill / "agents" / "openai.yaml"
    if not agent_file.is_file():
        fail(f"{skill}: missing agents/openai.yaml")


def validate_examples() -> None:
    for project in sorted((ROOT / "examples").iterdir()):
        project_file = project / "PROJECT.md"
        if not project_file.is_file():
            fail(f"{project}: missing PROJECT.md")
        text = project_file.read_text(encoding="utf-8")
        for link in LINK_RE.findall(text):
            if "://" in link:
                continue
            target = (project / link).resolve()
            if not target.exists():
                fail(f"{project_file}: broken link {link}")


def validate_scripts() -> None:
    scripts = [
        ROOT / "scripts" / "install.py",
        ROOT / "scripts" / "validate.py",
        SKILLS / "project-context" / "scripts" / "scan_context.py",
    ]
    with tempfile.TemporaryDirectory() as cache:
        for script in scripts:
            py_compile.compile(
                str(script),
                cfile=str(Path(cache) / f"{script.stem}.pyc"),
                doraise=True,
            )

    with tempfile.TemporaryDirectory() as target:
        result = subprocess.run(
            [
                sys.executable,
                str(ROOT / "scripts" / "install.py"),
                "--target",
                target,
            ],
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            fail(f"installer smoke test failed:\n{result.stdout}\n{result.stderr}")
        for skill in ("project-context", "project-research"):
            if not (Path(target) / skill / "SKILL.md").is_file():
                fail(f"installer did not copy {skill}")

    result = subprocess.run(
        [
            sys.executable,
            str(SKILLS / "project-context" / "scripts" / "scan_context.py"),
            "--root",
            str(ROOT / "examples" / "startup"),
            "--json",
        ],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        fail(f"context scanner smoke test failed:\n{result.stdout}\n{result.stderr}")
    scan = json.loads(result.stdout)
    paths = {record["path"] for record in scan["files"]}
    if "PROJECT.md" not in paths or ".project/NOW.md" not in paths:
        fail("context scanner did not find example context files")


def main() -> int:
    try:
        for path in (
            ROOT / ".agents" / "plugins" / "marketplace.json",
            PLUGIN / ".codex-plugin" / "plugin.json",
        ):
            validate_json(path)

        skills = sorted(path for path in SKILLS.iterdir() if path.is_dir())
        if {path.name for path in skills} != {"project-context", "project-research"}:
            fail("unexpected skill set")
        for skill in skills:
            validate_skill(skill)

        validate_examples()
        validate_scripts()
    except (ValidationError, py_compile.PyCompileError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1

    print("OK: manifests, skills, references, evals, scripts, installer, and examples")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
