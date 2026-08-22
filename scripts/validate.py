#!/usr/bin/env python3
"""Validate Company Kernel 0.7."""

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
DOMAINS = {
    "STRATEGY.md",
    "PRODUCT.md",
    "SOFTWARE.md",
    "DESIGN.md",
    "GTM.md",
    "CUSTOMER.md",
    "RESEARCH.md",
    "OPERATING.md",
}
SYSTEM_FILES = DOMAINS | {"KERNEL.md", "CONTEXT.md", "CAPABILITIES.md", "REVIEW.md"}
EXPECTED_SKILLS = {"kernel-setup", "project-update", "kernel-review"}
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_RE = re.compile(r"\]\(([^)#]+)(?:#[^)]+)?\)")
VERSION_RE = re.compile(r'^\s*version:\s*["\']?([^"\']+)', re.MULTILINE)
ROUTE_START = "<!-- company-kernel:route:start -->"
ROUTE_END = "<!-- company-kernel:route:end -->"


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


def frontmatter(path: Path) -> tuple[dict[str, str], str, str]:
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
    return data, body, raw


def local_links(path: Path, text: str | None = None) -> list[str]:
    text = text if text is not None else path.read_text(encoding="utf-8")
    return [
        link
        for link in LINK_RE.findall(text)
        if "://" not in link and not link.startswith(("#", "mailto:"))
    ]


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
    if plugin.get("version") != "0.7.0":
        fail("plugin version must be 0.7.0")
    if plugin.get("skills") != "./skills/":
        fail("repository root must be the plugin root")
    marketplace = load_json(ROOT / ".agents" / "plugins" / "marketplace.json")
    source = marketplace["plugins"][0]["source"]
    if source.get("path") != ".":
        fail("marketplace must point to repository root")
    if (ROOT / "plugins").exists():
        fail("nested plugin tree must not exist")


def validate_kernel() -> None:
    actual = {path.name for path in KERNEL.iterdir() if path.is_file() and path.suffix == ".md"}
    if actual != SYSTEM_FILES:
        fail(f"kernel files differ: expected {sorted(SYSTEM_FILES)}, found {sorted(actual)}")
    if (KERNEL / "standards").exists() or (KERNEL / "review").exists():
        fail("legacy standards or review directory remains")

    router = (KERNEL / "KERNEL.md").read_text(encoding="utf-8")
    for phrase in (
        "SYSTEM",
        "COMPANY",
        "PROJECT",
        "WORK",
        "Do not load all domains by default.",
        ".kernel/company/<DOMAIN>.md",
        ".kernel/project/<DOMAIN>.md",
    ):
        if phrase not in router:
            fail(f"KERNEL.md missing runtime contract: {phrase}")
    for domain in DOMAINS:
        if f"`{domain}`" not in router:
            fail(f"KERNEL.md does not route {domain}")
    if len(router.splitlines()) > 180:
        fail("KERNEL.md is too heavy for the hot path")

    context = (KERNEL / "CONTEXT.md").read_text(encoding="utf-8")
    for phrase in (
        "Preserve YC's epistemology. Rewrite its economics.",
        "Artifacts got cheaper faster than consequences did.",
        "Assume intelligence. Never assume context.",
    ):
        if phrase not in context:
            fail(f"CONTEXT.md missing prior: {phrase}")

    for domain in DOMAINS:
        text = (KERNEL / domain).read_text(encoding="utf-8")
        lines = len(text.splitlines())
        if not 55 <= lines <= 230:
            fail(f"{domain} has {lines} lines; domain context should be complete but bounded")
        for heading in ("## Do not inherit", "## Human gate", "## Done"):
            if heading not in text:
                fail(f"{domain} missing {heading}")
        if len(re.findall(r"\*\*[^*]+\*\*", text)) < 1:
            fail(f"{domain} lacks a compressed transferable call")


def validate_templates() -> None:
    required = {
        TEMPLATES / "COMPANY.md",
        TEMPLATES / "PROJECT.md",
        TEMPLATES / "DOMAIN.md",
        TEMPLATES / ".kernel" / "NOW.md",
    }
    missing = [str(path) for path in required if not path.is_file()]
    if missing:
        fail(f"missing templates: {missing}")
    legacy = [
        TEMPLATES / ".kernel" / "CODING.md",
        TEMPLATES / ".kernel" / "PRODUCT.md",
        TEMPLATES / ".kernel" / "GTM.md",
    ]
    if any(path.exists() for path in legacy):
        fail("legacy flat project domain templates remain")


def validate_skill(skill: Path) -> None:
    data, body, raw = frontmatter(skill / "SKILL.md")
    name = data.get("name", "")
    if name != skill.name or not NAME_RE.fullmatch(name):
        fail(f"{skill}: invalid skill name")
    version = VERSION_RE.search(raw)
    if not version or version.group(1) != "0.7.0":
        fail(f"{skill}: version must be 0.7.0")
    description = data.get("description", "")
    if not 1 <= len(description) <= 1024:
        fail(f"{skill}: invalid description")
    if len((skill / "SKILL.md").read_text(encoding="utf-8").splitlines()) > 170:
        fail(f"{skill}: SKILL.md exceeds 170 lines")
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
    required = {
        root / "AGENTS.md",
        root / "COMPANY.md",
        root / "PROJECT.md",
        root / ".kernel" / "NOW.md",
        root / ".kernel" / "company" / "STRATEGY.md",
        root / ".kernel" / "project" / "PRODUCT.md",
        root / ".kernel" / "project" / "SOFTWARE.md",
        root / ".kernel" / "project" / "GTM.md",
    }
    missing = [str(path) for path in required if not path.is_file()]
    if missing:
        fail(f"startup example is incomplete: {missing}")
    agents = (root / "AGENTS.md").read_text(encoding="utf-8")
    if ROUTE_START not in agents or ROUTE_END not in agents:
        fail("startup example lacks an installed route")
    legacy = [
        root / ".kernel" / "CODING.md",
        root / ".kernel" / "PRODUCT.md",
        root / ".kernel" / "GTM.md",
        root / ".project",
        root / "SYSTEM.md",
    ]
    if any(path.exists() for path in legacy):
        fail("startup example contains legacy context")


def compile_scripts() -> None:
    with tempfile.TemporaryDirectory() as cache:
        for script in (ROOT / "scripts").glob("*.py"):
            py_compile.compile(
                str(script),
                cfile=str(Path(cache) / f"{script.stem}.pyc"),
                doraise=True,
            )


def smoke_install_and_init() -> None:
    with tempfile.TemporaryDirectory() as temp:
        base = Path(temp)
        skills = base / "skills"
        kernel = base / "kernel"
        project = base / "project"
        project.mkdir()
        agents = project / "AGENTS.md"
        agents.write_text("# Existing rules\n\nPreserve me.\n", encoding="utf-8")

        result = run(
            [
                sys.executable,
                str(ROOT / "scripts" / "install.py"),
                "--target-skills",
                str(skills),
                "--kernel-home",
                str(kernel),
                "--init-project",
                str(project),
            ],
            "installer",
        )
        for name in EXPECTED_SKILLS:
            if not (skills / name / "SKILL.md").is_file():
                fail(f"installer missed {name}")
        for name in SYSTEM_FILES:
            if not (kernel / name).is_file():
                fail(f"installer missed system file {name}")
        for path in (
            kernel / "templates" / "COMPANY.md",
            kernel / "templates" / "PROJECT.md",
            kernel / "bin" / "init.py",
            kernel / "bin" / "scan.py",
        ):
            if not path.is_file():
                fail(f"installer missed {path}")
        for path in (
            project / "COMPANY.md",
            project / "PROJECT.md",
            project / ".kernel" / "NOW.md",
        ):
            if not path.is_file():
                fail(f"initializer missed {path}")
        first_route = agents.read_text(encoding="utf-8")
        if "Preserve me." not in first_route or first_route.count(ROUTE_START) != 1:
            fail("initializer replaced rules or duplicated route")

        run(
            [
                sys.executable,
                str(kernel / "bin" / "init.py"),
                "--root",
                str(project),
                "--kernel-home",
                str(kernel),
            ],
            "second initializer",
        )
        if agents.read_text(encoding="utf-8") != first_route:
            fail("initializer is not idempotent")
        if "$kernel-setup" not in result.stdout:
            fail("installer next step is stale")


def smoke_migration() -> None:
    with tempfile.TemporaryDirectory() as temp:
        base = Path(temp)
        kernel = base / "kernel"
        project = base / "project"
        (kernel / "templates" / ".kernel").mkdir(parents=True)
        (project / ".kernel").mkdir(parents=True)
        (kernel / "KERNEL.md").write_text("# Kernel\n", encoding="utf-8")
        for source in (TEMPLATES / "COMPANY.md", TEMPLATES / "PROJECT.md", TEMPLATES / "DOMAIN.md"):
            (kernel / "templates" / source.name).write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
        (kernel / "templates" / ".kernel" / "NOW.md").write_text(
            (TEMPLATES / ".kernel" / "NOW.md").read_text(encoding="utf-8"),
            encoding="utf-8",
        )
        (project / ".kernel" / "CODING.md").write_text("# Technical truth\n", encoding="utf-8")

        run(
            [
                sys.executable,
                str(ROOT / "scripts" / "init.py"),
                "--root",
                str(project),
                "--kernel-home",
                str(kernel),
                "--migrate",
            ],
            "migration",
        )
        if (project / ".kernel" / "CODING.md").exists():
            fail("migration left legacy CODING.md")
        migrated = project / ".kernel" / "project" / "SOFTWARE.md"
        if migrated.read_text(encoding="utf-8") != "# Technical truth\n":
            fail("migration did not preserve technical truth")


def smoke_scan() -> None:
    with tempfile.TemporaryDirectory() as temp:
        base = Path(temp)
        home = base / "home"
        repo = base / "repo"
        kernel = home / ".company-kernel"
        home.mkdir()
        repo.mkdir()
        kernel.mkdir()
        (repo / "AGENTS.md").write_text(
            f"# Rules\n\n{ROUTE_START}\nroute\n{ROUTE_END}\n",
            encoding="utf-8",
        )
        (repo / "COMPANY.md").write_text("# Company\n", encoding="utf-8")
        (repo / "PROJECT.md").write_text("# Project\n", encoding="utf-8")
        (repo / ".kernel").mkdir()
        (repo / ".kernel" / "NOW.md").write_text("# Now\n", encoding="utf-8")
        (repo / ".mcp.json").write_text(
            json.dumps({"env": {"TOKEN": "SECRET_VALUE"}}),
            encoding="utf-8",
        )
        (kernel / "KERNEL.md").write_text("# Kernel\n", encoding="utf-8")
        first = repo / ".agents" / "skills" / "same"
        second = home / ".agents" / "skills" / "same-copy"
        first.mkdir(parents=True)
        second.mkdir(parents=True)
        text = "---\nname: same\ndescription: Same.\n---\n\n# Same\n"
        (first / "SKILL.md").write_text(text, encoding="utf-8")
        (second / "SKILL.md").write_text(text, encoding="utf-8")

        result = run(
            [
                sys.executable,
                str(ROOT / "scripts" / "scan.py"),
                "--root",
                str(repo),
                "--home",
                str(home),
                "--kernel-home",
                str(kernel),
                "--json",
            ],
            "scanner",
        )
        if "SECRET_VALUE" in result.stdout:
            fail("scanner leaked secret content")
        data = json.loads(result.stdout)
        if not data["route"]["installed"]:
            fail("scanner missed route")
        if len(data["context"]["core"]) != 3:
            fail("scanner missed core context")
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
        smoke_install_and_init()
        smoke_migration()
        smoke_scan()
    except (ValidationError, py_compile.PyCompileError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1

    print(
        "OK: Company Kernel 0.7 system, company and project inheritance, selective routing, "
        "skills, install, initialization, migration, scanning, and examples"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
