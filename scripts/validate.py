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
EXPECTED_SKILLS = {"system-integrate", "project-context", "project-research"}


class ValidationError(Exception):
    pass


def fail(message: str) -> None:
    raise ValidationError(message)


def run_checked(command: list[str], label: str) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        fail(f"{label} failed:\n{result.stdout}\n{result.stderr}")
    return result


def parse_frontmatter(path: Path) -> tuple[dict[str, str], str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail(f"{path}: missing YAML frontmatter")
    try:
        _, raw, body = text.split("---\n", 2)
    except ValueError:
        fail(f"{path}: malformed frontmatter")
    data: dict[str, str] = {}
    for line in raw.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith((" ", "\t")):
            continue
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


def steering_lines(path: Path) -> list[str]:
    lines: list[str] = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or line.startswith("<!--"):
            continue
        lines.append(line)
    return lines


def validate_thin_file(path: Path) -> None:
    if not path.is_file():
        fail(f"{path}: missing thin context file")
    count = len(steering_lines(path))
    if not 1 <= count <= 10:
        fail(f"{path}: expected 1-10 steering lines; found {count}")


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
    for filename in ("triggers.json", "behavior.json"):
        path = eval_dir / filename
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

    behavior = validate_json(eval_dir / "behavior.json")
    for index, case in enumerate(behavior):
        if set(case) != {"name", "prompt", "must", "must_not"}:
            fail(f"{eval_dir / 'behavior.json'}[{index}]: invalid keys")
        if not isinstance(case["must"], list) or not isinstance(case["must_not"], list):
            fail(f"{eval_dir / 'behavior.json'}[{index}]: must and must_not must be lists")

    if not (skill / "agents" / "openai.yaml").is_file():
        fail(f"{skill}: missing agents/openai.yaml")


def validate_examples() -> None:
    system_validator = SKILLS / "system-integrate" / "scripts" / "validate_system.py"
    for project in sorted(path for path in (ROOT / "examples").iterdir() if path.is_dir()):
        project_file = project / "PROJECT.md"
        if not project_file.is_file():
            fail(f"{project}: missing PROJECT.md")

        run_checked(
            [sys.executable, str(system_validator), "--root", str(project)],
            f"system context validation for {project.name}",
        )

        text = project_file.read_text(encoding="utf-8")
        for link in LINK_RE.findall(text):
            if "://" in link:
                continue
            target = (project / link).resolve()
            if not target.exists():
                fail(f"{project_file}: broken link {link}")


def validate_environment_scanner(script: Path) -> None:
    with tempfile.TemporaryDirectory() as temp:
        base = Path(temp)
        project = base / "project"
        home = base / "home"
        project.mkdir()
        home.mkdir()

        (project / "AGENTS.md").write_text("# Rules\nPreserve local behavior.\n")
        (project / "SYSTEM.md").write_text(
            "# System\nBuild for current capability.\nApply [proof](.system/PROOF.md).\n"
        )
        lens = project / ".system" / "PROOF.md"
        lens.parent.mkdir()
        lens.write_text("# Proof\nObservable completion outranks claims.\n")
        (project / ".mcp.json").write_text(
            json.dumps(
                {
                    "mcpServers": {
                        "analytics": {
                            "command": "server",
                            "env": {"TOKEN": "SUPER_SECRET_VALUE"},
                        }
                    }
                }
            )
        )

        local_skill = project / ".agents" / "skills" / "shared"
        global_skill = home / ".agents" / "skills" / "shared-copy"
        local_skill.mkdir(parents=True)
        global_skill.mkdir(parents=True)
        skill_text = (
            "---\n"
            "name: shared\n"
            "description: Shared test capability.\n"
            "---\n\n"
            "# Shared\n"
        )
        (local_skill / "SKILL.md").write_text(skill_text)
        (global_skill / "SKILL.md").write_text(skill_text)

        result = run_checked(
            [
                sys.executable,
                str(script),
                "--root",
                str(project),
                "--home",
                str(home),
                "--json",
            ],
            "environment scanner smoke test",
        )
        if "SUPER_SECRET_VALUE" in result.stdout:
            fail("environment scanner leaked a configuration value")

        scan = json.loads(result.stdout)
        instruction_paths = {record["path"] for record in scan["instructions"]}
        system_paths = {record["path"] for record in scan["system_context"]}
        skill_names = {record["name"] for record in scan["skills"]}

        if "AGENTS.md" not in instruction_paths:
            fail("environment scanner did not find project instruction surfaces")
        if not {"SYSTEM.md", ".system/PROOF.md"}.issubset(system_paths):
            fail("environment scanner did not find root and linked system context")
        if "shared" not in skill_names or len(scan["skills"]) != 2:
            fail("environment scanner did not find project and global skills")
        if not scan["exact_skill_duplicates"]:
            fail("environment scanner did not identify byte-identical skill files")
        if not scan["tool_configs"] or scan["tool_configs"][0]["path"] != ".mcp.json":
            fail("environment scanner did not identify the project tool-config surface")


def validate_scripts() -> None:
    scripts = [
        ROOT / "scripts" / "install.py",
        ROOT / "scripts" / "validate.py",
        SKILLS / "project-context" / "scripts" / "scan_context.py",
        SKILLS / "system-integrate" / "scripts" / "scan_environment.py",
        SKILLS / "system-integrate" / "scripts" / "validate_system.py",
    ]
    with tempfile.TemporaryDirectory() as cache:
        for script in scripts:
            py_compile.compile(
                str(script),
                cfile=str(Path(cache) / f"{script.parent.name}-{script.stem}.pyc"),
                doraise=True,
            )

    with tempfile.TemporaryDirectory() as target:
        result = run_checked(
            [sys.executable, str(ROOT / "scripts" / "install.py"), "--target", target],
            "installer smoke test",
        )
        for skill in EXPECTED_SKILLS:
            if not (Path(target) / skill / "SKILL.md").is_file():
                fail(f"installer did not copy {skill}")
        if "$system-integrate" not in result.stdout:
            fail("installer did not point to the first-run integrator")

    result = run_checked(
        [
            sys.executable,
            str(SKILLS / "project-context" / "scripts" / "scan_context.py"),
            "--root",
            str(ROOT / "examples" / "startup"),
            "--json",
        ],
        "context scanner smoke test",
    )
    scan = json.loads(result.stdout)
    paths = {record["path"] for record in scan["files"]}
    required = {
        "SYSTEM.md",
        ".system/PRODUCT-COHERENCE.md",
        "PROJECT.md",
        ".project/NOW.md",
    }
    if not required.issubset(paths):
        fail("context scanner did not find integrated system and project context files")

    validate_environment_scanner(
        SKILLS / "system-integrate" / "scripts" / "scan_environment.py"
    )


def validate_integration_assets() -> None:
    validate_thin_file(SKILLS / "system-integrate" / "assets" / "SYSTEM.seed.md")
    validate_thin_file(SKILLS / "system-integrate" / "assets" / "LENS.seed.md")

    for path in (
        SKILLS / "system-integrate" / "assets" / "ROUTE.md",
        SKILLS / "project-context" / "assets" / "ROUTE.md",
    ):
        text = path.read_text(encoding="utf-8")
        for required in (
            "SYSTEM.md",
            ".system",
            "PROJECT.md",
            "$system-integrate",
            "$project-context",
            "$project-research",
        ):
            if required not in text:
                fail(f"{path}: missing route token {required}")


def main() -> int:
    try:
        for path in (
            ROOT / ".agents" / "plugins" / "marketplace.json",
            PLUGIN / ".codex-plugin" / "plugin.json",
        ):
            validate_json(path)

        skills = sorted(path for path in SKILLS.iterdir() if path.is_dir())
        if {path.name for path in skills} != EXPECTED_SKILLS:
            fail(f"unexpected skill set: {sorted(path.name for path in skills)}")
        for skill in skills:
            validate_skill(skill)

        validate_examples()
        validate_integration_assets()
        validate_scripts()
    except (ValidationError, py_compile.PyCompileError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1

    print(
        "OK: manifests, thin system context, skills, references, evals, scripts, installer, scanners, and examples"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
