#!/usr/bin/env python3
"""Validate Company Kernel 0.6."""

from __future__ import annotations

import json
import py_compile
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
KERNEL = ROOT / "kernel"
TEMPLATES = ROOT / "templates"
EXPECTED_SKILLS = {"kernel-setup", "project-update", "kernel-review"}
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


def validate_markdown() -> None:
    for path in ROOT.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        if "—" in text:
            fail(f"{path}: contains an em dash")
        for number, line in enumerate(text.splitlines(), 1):
            if len(line) > 300:
                fail(f"{path}:{number}: line exceeds 300 characters")
        for link in local_links(path):
            if not (path.parent / link).resolve().exists():
                fail(f"{path}: broken local link {link}")


def validate_plugin() -> None:
    plugin = load_json(ROOT / ".codex-plugin" / "plugin.json")
    if plugin.get("version") != "0.6.0":
        fail("plugin version must be 0.6.0")
    if plugin.get("skills") != "./skills/":
        fail("repository root must be the plugin root")
    marketplace = load_json(ROOT / ".agents" / "plugins" / "marketplace.json")
    source = marketplace["plugins"][0]["source"]
    if source.get("path") != ".":
        fail("marketplace must point to repository root")
    if (ROOT / "plugins").exists():
        fail("nested plugin tree must not exist in 0.6")


def validate_kernel() -> None:
    required = {
        KERNEL / "KERNEL.md",
        KERNEL / "CAPABILITIES.md",
        KERNEL / "review" / "REVIEW.md",
    }
    required |= {KERNEL / "standards" / name for name in EXPECTED_DOMAINS}
    required |= {KERNEL / "review" / name for name in EXPECTED_DOMAINS}
    missing = [str(path) for path in required if not path.is_file()]
    if missing:
        fail(f"missing kernel files: {missing}")

    kernel_text = (KERNEL / "KERNEL.md").read_text(encoding="utf-8")
    for heading in ("## The 2026 prior", "## How to operate", "## Runtime"):
        if heading not in kernel_text:
            fail(f"KERNEL.md missing {heading}")

    for domain in EXPECTED_DOMAINS:
        text = (KERNEL / "standards" / domain).read_text(encoding="utf-8")
        for heading in (
            "## The world changed",
            "## What remains scarce",
            "## Default calls",
            "## Do not inherit",
            "## Human gate",
            "## Done",
        ):
            if heading not in text:
                fail(f"{domain} missing {heading}")
        if len(text.splitlines()) < 45:
            fail(f"{domain} is too compressed to reset the model prior")


def validate_templates() -> None:
    required = {TEMPLATES / "PROJECT.md", TEMPLATES / ".kernel" / "NOW.md"}
    required |= {TEMPLATES / ".kernel" / name for name in EXPECTED_DOMAINS}
    missing = [str(path) for path in required if not path.is_file()]
    if missing:
        fail(f"missing templates: {missing}")


def validate_skill(skill: Path) -> None:
    data, body = frontmatter(skill / "SKILL.md")
    name = data.get("name", "")
    if name != skill.name or not NAME_RE.fullmatch(name):
        fail(f"{skill}: invalid skill name")
    if data.get("version") and data.get("version") != "0.6.0":
        fail(f"{skill}: wrong version")
    description = data.get("description", "")
    if not 1 <= len(description) <= 1024:
        fail(f"{skill}: invalid description")
    if len((skill / "SKILL.md").read_text(encoding="utf-8").splitlines()) > 150:
        fail(f"{skill}: SKILL.md exceeds 150 lines")
    for link in local_links(skill / "SKILL.md", body):
        if not (skill / link).resolve().exists():
            fail(f"{skill}: broken skill link {link}")
    if not (skill / "agents" / "openai.yaml").is_file():
        fail(f"{skill}: missing agents/openai.yaml")
    for filename in ("triggers.json", "behavior.json"):
        value = load_json(skill / "evals" / filename)
        if not isinstance(value, list) or not value:
            fail(f"{skill}: invalid evals/{filename}")


def validate_skills() -> None:
    skills = {path.name: path for path in SKILLS.iterdir() if path.is_dir()}
    if set(skills) != EXPECTED_SKILLS:
        fail(f"unexpected skills: {sorted(skills)}")
    for skill in skills.values():
        validate_skill(skill)


def validate_example() -> None:
    root = ROOT / "examples" / "startup"
    required = {root / "PROJECT.md", root / ".kernel" / "NOW.md"}
    required |= {root / ".kernel" / name for name in EXPECTED_DOMAINS}
    if any(not path.is_file() for path in required):
        fail("startup example is incomplete")
    if (root / ".project").exists() or (root / "SYSTEM.md").exists():
        fail("startup example contains legacy context")


def compile_scripts() -> None:
    with tempfile.TemporaryDirectory() as cache:
        for script in (ROOT / "scripts").glob("*.py"):
            py_compile.compile(
                str(script),
                cfile=str(Path(cache) / f"{script.stem}.pyc"),
                doraise=True,
            )


def smoke_install() -> None:
    with tempfile.TemporaryDirectory() as temp:
        base = Path(temp)
        skills = base / "skills"
        kernel = base / "kernel"
        result = run(
            [
                sys.executable,
                str(ROOT / "scripts" / "install.py"),
                "--target-skills", str(skills),
                "--kernel-home", str(kernel),
            ],
            "installer",
        )
        for name in EXPECTED_SKILLS:
            if not (skills / name / "SKILL.md").is_file():
                fail(f"installer missed {name}")
        if not (kernel / "KERNEL.md").is_file() or not (kernel / "bin" / "scan.py").is_file():
            fail("installer missed the shared kernel")
        if "$kernel-setup" not in result.stdout:
            fail("installer next step is stale")


def smoke_scan() -> None:
    with tempfile.TemporaryDirectory() as temp:
        base = Path(temp)
        home = base / "home"
        repo = base / "repo"
        kernel = home / ".company-kernel"
        home.mkdir(); repo.mkdir(); kernel.mkdir()
        (repo / "AGENTS.md").write_text("# Rules\nPreserve me.\n", encoding="utf-8")
        (repo / ".mcp.json").write_text(json.dumps({"env": {"TOKEN": "SECRET_VALUE"}}), encoding="utf-8")
        (kernel / "KERNEL.md").write_text("# Kernel\nRoute relevant work.\n", encoding="utf-8")
        first = repo / ".agents" / "skills" / "same"; first.mkdir(parents=True)
        second = home / ".agents" / "skills" / "same-copy"; second.mkdir(parents=True)
        text = "---\nname: same\ndescription: Same.\n---\n\n# Same\n"
        (first / "SKILL.md").write_text(text, encoding="utf-8")
        (second / "SKILL.md").write_text(text, encoding="utf-8")
        result = run(
            [
                sys.executable,
                str(ROOT / "scripts" / "scan.py"),
                "--root", str(repo),
                "--home", str(home),
                "--kernel-home", str(kernel),
                "--json",
            ],
            "scanner",
        )
        if "SECRET_VALUE" in result.stdout:
            fail("scanner leaked secret content")
        data = json.loads(result.stdout)
        if not data["shared_kernel"] or not data["exact_skill_duplicates"]:
            fail("scanner missed kernel or duplicate skills")


def main() -> int:
    try:
        validate_markdown()
        validate_plugin()
        validate_kernel()
        validate_templates()
        validate_skills()
        validate_example()
        compile_scripts()
        smoke_install()
        smoke_scan()
    except (ValidationError, py_compile.PyCompileError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1

    print("OK: Company Kernel 0.6 prior, standards, project models, review path, skills, installer, scanner, and examples")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
