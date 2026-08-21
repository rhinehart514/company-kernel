#!/usr/bin/env python3
"""Validate Company Kernel 0.4."""

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
SYSTEM_SOURCE = SKILLS / "system-integrate" / "references" / "system"
EXPECTED_SKILLS = {"system-integrate", "project-context", "project-research"}
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_RE = re.compile(r"\]\(([^)#]+)(?:#[^)]+)?\)")


class ValidationError(Exception):
    pass


def fail(message: str) -> None:
    raise ValidationError(message)


def run(command: list[str], label: str) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        fail(f"{label} failed:\n{result.stdout}\n{result.stderr}")
    return result


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"{path}: invalid JSON: {exc}")


def frontmatter(path: Path) -> tuple[dict[str, str], str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail(f"{path}: missing frontmatter")
    try:
        _, raw, body = text.split("---\n", 2)
    except ValueError:
        fail(f"{path}: malformed frontmatter")
    data: dict[str, str] = {}
    for line in raw.splitlines():
        if not line.strip() or line.startswith((" ", "\t")) or ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data, body


def local_links(path: Path, text: str | None = None) -> list[str]:
    text = text if text is not None else path.read_text(encoding="utf-8")
    return [link for link in LINK_RE.findall(text) if "://" not in link and not link.startswith(("#", "mailto:"))]


def steering_lines(path: Path) -> list[str]:
    return [line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip() and not line.lstrip().startswith("#")]


def validate_markdown_style() -> None:
    for path in ROOT.rglob("*.md"):
        if any(part in {".git"} for part in path.parts):
            continue
        text = path.read_text(encoding="utf-8")
        if "—" in text:
            fail(f"{path}: contains an em dash")
        for number, line in enumerate(text.splitlines(), start=1):
            if len(line) > 260:
                fail(f"{path}:{number}: line exceeds 260 characters")

    for skill in SKILLS.iterdir():
        if not skill.is_dir():
            continue
        skill_lines = len((skill / "SKILL.md").read_text(encoding="utf-8").splitlines())
        if skill_lines > 130:
            fail(f"{skill / 'SKILL.md'}: exceeds 130 lines")
        refs = skill / "references"
        if refs.is_dir():
            for path in refs.rglob("*.md"):
                if path.name == "LENSES.md":
                    continue
                lines = len(path.read_text(encoding="utf-8").splitlines())
                if lines > 100:
                    fail(f"{path}: exceeds 100 lines")


def validate_skill(skill: Path) -> None:
    data, body = frontmatter(skill / "SKILL.md")
    name = data.get("name", "")
    description = data.get("description", "")
    if name != skill.name or not NAME_RE.fullmatch(name):
        fail(f"{skill}: invalid name {name!r}")
    if not 1 <= len(description) <= 1024:
        fail(f"{skill}: description must contain 1-1024 characters")
    if data.get("metadata", ""):
        pass
    for link in local_links(skill / "SKILL.md", body):
        if not (skill / link).resolve().exists():
            fail(f"{skill / 'SKILL.md'}: broken link {link}")

    for filename in ("triggers.json", "behavior.json"):
        path = skill / "evals" / filename
        if not path.is_file():
            fail(f"{skill}: missing evals/{filename}")
        value = load_json(path)
        if not isinstance(value, list) or not value:
            fail(f"{path}: expected non-empty list")

    for case in load_json(skill / "evals" / "triggers.json"):
        if set(case) != {"prompt", "should_trigger"} or not isinstance(case["should_trigger"], bool):
            fail(f"{skill}: invalid trigger case")
    for case in load_json(skill / "evals" / "behavior.json"):
        if set(case) != {"name", "prompt", "must", "must_not"}:
            fail(f"{skill}: invalid behavior case")
        if not isinstance(case["must"], list) or not isinstance(case["must_not"], list):
            fail(f"{skill}: behavior must/must_not must be lists")
    if not (skill / "agents" / "openai.yaml").is_file():
        fail(f"{skill}: missing agents/openai.yaml")


def validate_system_source() -> None:
    validator = SKILLS / "system-integrate" / "scripts" / "validate_system.py"
    run([sys.executable, str(validator), "--system-home", str(SYSTEM_SOURCE)], "canonical system validation")
    run([sys.executable, str(validator), "--system-home", str(ROOT / "examples" / "system")], "example system validation")

    if len(steering_lines(SYSTEM_SOURCE / "SYSTEM.md")) > 10:
        fail("canonical SYSTEM.md is not thin")
    lenses = sorted((SYSTEM_SOURCE / "lenses").glob("*.md"))
    if len(lenses) < 10:
        fail("canonical system library is unexpectedly small")


def validate_project_examples() -> None:
    for name in ("startup", "open-source"):
        project = ROOT / "examples" / name
        if not (project / "PROJECT.md").is_file() or not (project / ".project" / "NOW.md").is_file():
            fail(f"{project}: missing PROJECT.md or .project/NOW.md")
        if (project / "SYSTEM.md").exists() or (project / ".system").exists():
            fail(f"{project}: shared system must not live inside a project")
        for path in [project / "PROJECT.md", *(project / ".project").glob("*.md")]:
            for link in local_links(path):
                if not (path.parent / link).resolve().exists():
                    fail(f"{path}: broken link {link}")


def compile_scripts() -> None:
    scripts = [ROOT / "scripts" / "install.py", ROOT / "scripts" / "validate.py", SKILLS / "project-context" / "scripts" / "scan_context.py", SKILLS / "system-integrate" / "scripts" / "scan_environment.py", SKILLS / "system-integrate" / "scripts" / "validate_system.py"]
    with tempfile.TemporaryDirectory() as cache:
        for script in scripts:
            py_compile.compile(str(script), cfile=str(Path(cache) / f"{script.parent.name}-{script.stem}.pyc"), doraise=True)


def smoke_install() -> None:
    with tempfile.TemporaryDirectory() as target:
        result = run([sys.executable, str(ROOT / "scripts" / "install.py"), "--target", target], "installer")
        for skill in EXPECTED_SKILLS:
            if not (Path(target) / skill / "SKILL.md").is_file():
                fail(f"installer did not copy {skill}")
        if "$system-integrate" not in result.stdout:
            fail("installer did not point to system integration")


def smoke_scanners() -> None:
    project_scan = run([sys.executable, str(SKILLS / "project-context" / "scripts" / "scan_context.py"), "--root", str(ROOT / "examples" / "startup"), "--json"], "project scanner")
    project = json.loads(project_scan.stdout)
    paths = {item["path"] for item in project["project_context"]}
    if not {"PROJECT.md", ".project/NOW.md"}.issubset(paths):
        fail("project scanner missed project context")
    if project["legacy_project_system"]:
        fail("project example contains legacy local system context")

    with tempfile.TemporaryDirectory() as temp:
        base = Path(temp)
        project_root = base / "project"
        home = base / "home"
        system_home = home / ".company-kernel"
        project_root.mkdir(); home.mkdir(); system_home.mkdir()
        (project_root / "AGENTS.md").write_text("# Rules\nKeep local rules.\n")
        (project_root / "PROJECT.md").write_text("# Project\n\n> Test project.\n")
        (project_root / ".mcp.json").write_text(json.dumps({"env": {"TOKEN": "SUPER_SECRET_VALUE"}}))
        (system_home / "SYSTEM.md").write_text("# System\n\nBuild for current capability.\nUse [lenses](LENSES.md).\n")
        (system_home / "LENSES.md").write_text("# Lenses\n\n- [Proof](lenses/PROOF.md)\n")
        lens = system_home / "lenses" / "PROOF.md"; lens.parent.mkdir(); lens.write_text("# Proof\n\nCompletion outranks claims.\n")
        local_skill = project_root / ".agents" / "skills" / "shared"; local_skill.mkdir(parents=True)
        global_skill = home / ".agents" / "skills" / "shared-copy"; global_skill.mkdir(parents=True)
        skill_text = "---\nname: shared\ndescription: Shared test capability.\n---\n\n# Shared\n"
        (local_skill / "SKILL.md").write_text(skill_text)
        (global_skill / "SKILL.md").write_text(skill_text)

        result = run([sys.executable, str(SKILLS / "system-integrate" / "scripts" / "scan_environment.py"), "--root", str(project_root), "--home", str(home), "--system-home", str(system_home), "--json"], "environment scanner")
        if "SUPER_SECRET_VALUE" in result.stdout:
            fail("environment scanner leaked a secret")
        scan = json.loads(result.stdout)
        if not scan["shared_system"]:
            fail("environment scanner missed shared system")
        if len(scan["skills"]) != 2 or not scan["exact_skill_duplicates"]:
            fail("environment scanner missed duplicate skills")
        if not scan["tool_configs"]:
            fail("environment scanner missed tool configuration")


def validate_architecture_text() -> None:
    project_skill = (SKILLS / "project-context" / "SKILL.md").read_text(encoding="utf-8")
    if "Do not create a project-local `SYSTEM.md`" not in project_skill:
        fail("project-context must explicitly keep system above project")
    route = (SKILLS / "project-context" / "assets" / "ROUTE.md").read_text(encoding="utf-8")
    for token in ("<SYSTEM_HOME>", "PROJECT.md", "$project-context", "$project-research"):
        if token not in route:
            fail(f"project route missing {token}")


def main() -> int:
    try:
        load_json(ROOT / ".agents" / "plugins" / "marketplace.json")
        plugin = load_json(PLUGIN / ".codex-plugin" / "plugin.json")
        if plugin.get("version") != "0.4.0":
            fail("plugin version must be 0.4.0")

        skills = sorted(path for path in SKILLS.iterdir() if path.is_dir())
        if {path.name for path in skills} != EXPECTED_SKILLS:
            fail(f"unexpected skill set: {sorted(path.name for path in skills)}")
        for skill in skills:
            validate_skill(skill)

        validate_markdown_style()
        validate_system_source()
        validate_project_examples()
        validate_architecture_text()
        compile_scripts()
        smoke_install()
        smoke_scanners()
    except (ValidationError, py_compile.PyCompileError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1

    print("OK: v0.4 system, project context, skills, writing, scanners, examples, and installer")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
