#!/usr/bin/env python3
"""Validate Company Kernel 0.5."""

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
INTEGRATE = SKILLS / "kernel-integrate"
PROJECT = SKILLS / "project-model"
REVIEW = SKILLS / "kernel-review"
SYSTEM_SOURCE = INTEGRATE / "assets" / "system"
EXPECTED_SKILLS = {"kernel-integrate", "project-model", "kernel-review"}
EXPECTED_DOMAINS = {"CODING.md", "PRODUCT.md", "GTM.md"}
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_RE = re.compile(r"\]\(([^)#]+)(?:#[^)]+)?\)")


class ValidationError(Exception):
    pass


def fail(message: str) -> None:
    raise ValidationError(message)


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"{path}: invalid JSON: {exc}")


def run(command: list[str], label: str) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        fail(f"{label} failed:\n{result.stdout}\n{result.stderr}")
    return result


def frontmatter(path: Path) -> tuple[dict[str, str], str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail(f"{path}: missing frontmatter")
    try:
        _, raw, body = text.split("---\n", 2)
    except ValueError:
        fail(f"{path}: malformed frontmatter")
    data = {}
    for line in raw.splitlines():
        if not line.strip() or line.startswith((" ", "\t")) or ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data, body


def local_links(path: Path, text: str | None = None) -> list[str]:
    text = text if text is not None else path.read_text(encoding="utf-8")
    return [x for x in LINK_RE.findall(text) if "://" not in x and not x.startswith(("#", "mailto:"))]


def validate_markdown() -> None:
    for path in ROOT.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        if "—" in text:
            fail(f"{path}: contains an em dash")
        for number, line in enumerate(text.splitlines(), 1):
            if len(line) > 280:
                fail(f"{path}:{number}: line exceeds 280 characters")
        for link in local_links(path):
            if not (path.parent / link).resolve().exists():
                fail(f"{path}: broken local link {link}")


def validate_skill(skill: Path) -> None:
    data, body = frontmatter(skill / "SKILL.md")
    if data.get("name") != skill.name or not NAME_RE.fullmatch(skill.name):
        fail(f"{skill}: invalid skill name")
    if data.get("version") and data.get("version") != "0.5.0":
        fail(f"{skill}: wrong version")
    description = data.get("description", "")
    if not 1 <= len(description) <= 1024:
        fail(f"{skill}: invalid description")
    if len((skill / "SKILL.md").read_text(encoding="utf-8").splitlines()) > 130:
        fail(f"{skill}: SKILL.md exceeds 130 lines")
    for link in local_links(skill / "SKILL.md", body):
        if not (skill / link).resolve().exists():
            fail(f"{skill}: broken link {link}")
    if not (skill / "agents" / "openai.yaml").is_file():
        fail(f"{skill}: missing agents/openai.yaml")
    for name in ("triggers.json", "behavior.json"):
        value = load_json(skill / "evals" / name)
        if not isinstance(value, list) or not value:
            fail(f"{skill}: invalid evals/{name}")


def validate_system() -> None:
    required = {
        SYSTEM_SOURCE / "KERNEL.md",
        SYSTEM_SOURCE / "CAPABILITIES.md",
        SYSTEM_SOURCE / "reviews" / "PROTOCOL.md",
    }
    required |= {SYSTEM_SOURCE / "standards" / name for name in EXPECTED_DOMAINS}
    required |= {SYSTEM_SOURCE / "reviews" / name for name in EXPECTED_DOMAINS}
    missing = [str(p) for p in required if not p.is_file()]
    if missing:
        fail(f"missing system files: {missing}")

    kernel_lines = [
        line for line in (SYSTEM_SOURCE / "KERNEL.md").read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.startswith("#")
    ]
    if len(kernel_lines) > 10:
        fail("KERNEL.md must remain a thin route")

    example = ROOT / "examples" / "system"
    for source in required:
        rel = source.relative_to(SYSTEM_SOURCE)
        mirror = example / rel
        if not mirror.is_file() or source.read_text() != mirror.read_text():
            fail(f"example system drift: {rel}")


def validate_project_example() -> None:
    root = ROOT / "examples" / "startup"
    required = {root / "PROJECT.md", root / ".kernel" / "NOW.md"}
    required |= {root / ".kernel" / name for name in EXPECTED_DOMAINS}
    if any(not p.is_file() for p in required):
        fail("startup example is incomplete")
    if (root / ".project").exists() or (root / "SYSTEM.md").exists():
        fail("startup example contains legacy context")


def validate_architecture() -> None:
    architecture = (ROOT / "docs" / "ARCHITECTURE.md").read_text(encoding="utf-8")
    for token in ("External review", "System standard", "Project model", "Evidence loop"):
        if token not in architecture:
            fail(f"architecture missing {token}")
    kernel = (SYSTEM_SOURCE / "KERNEL.md").read_text(encoding="utf-8")
    for token in ("standards/", "PROJECT.md", ".kernel/NOW.md", "reviews/", "$kernel-review"):
        if token not in kernel:
            fail(f"kernel route missing {token}")


def compile_scripts() -> None:
    scripts = [ROOT / "scripts" / "install.py", ROOT / "scripts" / "validate.py"]
    scripts += list(SKILLS.rglob("*.py"))
    with tempfile.TemporaryDirectory() as cache:
        for script in scripts:
            py_compile.compile(
                str(script), cfile=str(Path(cache) / f"{script.parent.name}-{script.stem}.pyc"), doraise=True
            )


def smoke() -> None:
    with tempfile.TemporaryDirectory() as target:
        result = run([sys.executable, str(ROOT / "scripts" / "install.py"), "--target", target], "installer")
        for skill in EXPECTED_SKILLS:
            if not (Path(target) / skill / "SKILL.md").is_file():
                fail(f"installer missed {skill}")
        if "$kernel-integrate" not in result.stdout:
            fail("installer next step is stale")

    project = run([
        sys.executable,
        str(PROJECT / "scripts" / "scan_project.py"),
        "--root", str(ROOT / "examples" / "startup"),
        "--json",
    ], "project scanner")
    project_data = json.loads(project.stdout)
    if not {"PROJECT.md", ".kernel/NOW.md"}.issubset(set(project_data["project_context"])):
        fail("project scanner missed context")

    with tempfile.TemporaryDirectory() as temp:
        base = Path(temp)
        home = base / "home"
        repo = base / "repo"
        system = home / ".company-kernel"
        home.mkdir(); repo.mkdir(); system.mkdir()
        (repo / "AGENTS.md").write_text("# Rules\nPreserve me.\n")
        (repo / ".mcp.json").write_text(json.dumps({"env": {"TOKEN": "SECRET_VALUE"}}))
        (system / "KERNEL.md").write_text("# Kernel\nRoute relevant work.\n")
        skill_a = repo / ".agents" / "skills" / "same"; skill_a.mkdir(parents=True)
        skill_b = home / ".agents" / "skills" / "same-copy"; skill_b.mkdir(parents=True)
        text = "---\nname: same\ndescription: Same.\n---\n\n# Same\n"
        (skill_a / "SKILL.md").write_text(text); (skill_b / "SKILL.md").write_text(text)
        result = run([
            sys.executable,
            str(INTEGRATE / "scripts" / "scan_environment.py"),
            "--root", str(repo), "--home", str(home), "--system-home", str(system), "--json",
        ], "environment scanner")
        if "SECRET_VALUE" in result.stdout:
            fail("scanner leaked secret content")
        data = json.loads(result.stdout)
        if not data["shared_kernel"] or not data["exact_skill_duplicates"]:
            fail("environment scanner missed kernel or duplicate skills")


def main() -> int:
    try:
        load_json(ROOT / ".agents" / "plugins" / "marketplace.json")
        plugin = load_json(PLUGIN / ".codex-plugin" / "plugin.json")
        if plugin.get("version") != "0.5.0":
            fail("plugin version must be 0.5.0")
        skills = {p.name: p for p in SKILLS.iterdir() if p.is_dir()}
        if set(skills) != EXPECTED_SKILLS:
            fail(f"unexpected skills: {sorted(skills)}")
        for skill in skills.values():
            validate_skill(skill)
        validate_markdown()
        validate_system()
        validate_project_example()
        validate_architecture()
        compile_scripts()
        smoke()
    except (ValidationError, py_compile.PyCompileError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    print("OK: Company Kernel 0.5 topology, standards, models, review path, skills, examples, and installer")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
