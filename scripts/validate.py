#!/usr/bin/env python3
"""Validate Company Kernel 0.9 as a small, composable skill pack."""

from __future__ import annotations

import json
import py_compile
import re
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"

EXPECTED_SKILLS = {
    "venture-judgment",
    "shape-project",
    "think-further",
    "product-coherence",
}
EXPECTED_REFERENCES = {
    "worldview.md",
    "strategy.md",
    "product.md",
    "software.md",
    "design.md",
    "gtm.md",
    "customer.md",
    "research.md",
    "operating.md",
    "writing.md",
}
FORBIDDEN_PATHS = {
    "kernel",
    "templates",
    ".kernel",
    "docs",
    "scripts/install.py",
    "scripts/init.py",
    "scripts/scan.py",
}
LINK_RE = re.compile(r"\]\(([^)#]+)(?:#[^)]+)?\)")
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


class ValidationError(Exception):
    pass


def fail(message: str) -> None:
    raise ValidationError(message)


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
    metadata = False
    for line in raw.splitlines():
        if line.strip() == "metadata:":
            metadata = True
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if metadata and line.startswith("  "):
            data[f"metadata.{key}"] = value
        elif not line.startswith((" ", "\t")):
            metadata = False
            data[key] = value
    return data, body


def local_links(path: Path, text: str | None = None) -> list[str]:
    value = text if text is not None else path.read_text(encoding="utf-8")
    return [
        link
        for link in LINK_RE.findall(value)
        if "://" not in link and not link.startswith(("#", "mailto:"))
    ]


def validate_layout() -> None:
    for forbidden in FORBIDDEN_PATHS:
        if (ROOT / forbidden).exists():
            fail(f"legacy machinery still exists: {forbidden}")

    skills = {path.name for path in SKILLS.iterdir() if path.is_dir()}
    if skills != EXPECTED_SKILLS:
        fail(f"unexpected skills: {sorted(skills)}")

    example = ROOT / "examples" / "project"
    expected = {"AGENTS.md", "PROJECT.md", "NOW.md"}
    actual = {path.name for path in example.iterdir() if path.is_file()}
    if actual != expected:
        fail(f"example project must contain only {sorted(expected)}")


def validate_plugin() -> None:
    plugin = load_json(ROOT / ".codex-plugin" / "plugin.json")
    if plugin.get("version") != "0.9.0":
        fail("plugin version must be 0.9.0")
    if plugin.get("skills") != "./skills/":
        fail("plugin must expose ./skills/")

    marketplace = load_json(ROOT / ".agents" / "plugins" / "marketplace.json")
    source = marketplace["plugins"][0]["source"]
    if source.get("path") != ".":
        fail("marketplace must point at the repository root")


def validate_skills() -> None:
    for name in EXPECTED_SKILLS:
        root = SKILLS / name
        skill = root / "SKILL.md"
        agent = root / "agents" / "openai.yaml"

        if not skill.is_file() or not agent.is_file():
            fail(f"{name}: missing SKILL.md or agents/openai.yaml")

        data, body = frontmatter(skill)
        if data.get("name") != name or not NAME_RE.fullmatch(name):
            fail(f"{name}: invalid skill name")
        if data.get("metadata.version") != "0.9.0":
            fail(f"{name}: version must be 0.9.0")
        if not data.get("description"):
            fail(f"{name}: missing description")
        if len(skill.read_text(encoding="utf-8").splitlines()) > 210:
            fail(f"{name}: SKILL.md is too large")

        for link in local_links(skill, body):
            if not (root / link).resolve().exists():
                fail(f"{name}: broken local link {link}")

    refs = {
        path.name
        for path in (SKILLS / "venture-judgment" / "references").iterdir()
        if path.is_file()
    }
    if refs != EXPECTED_REFERENCES:
        fail(f"unexpected venture references: {sorted(refs)}")

    shape = (SKILLS / "shape-project" / "SKILL.md").read_text(encoding="utf-8")
    for phrase in (
        "design tree",
        "frontier",
        "recommended answer",
        "AGENTS.md",
        "PROJECT.md",
        "NOW.md",
    ):
        if phrase.lower() not in shape.lower():
            fail(f"shape-project missing {phrase}")

    further = (SKILLS / "think-further" / "SKILL.md").read_text(encoding="utf-8")
    for phrase in ("Why now", "Kill condition", "First proof", "recommend"):
        if phrase.lower() not in further.lower():
            fail(f"think-further missing {phrase}")

    coherence = (SKILLS / "product-coherence" / "SKILL.md").read_text(encoding="utf-8")
    for phrase in ("default", "state", "replace", "kill it", "conceptual cost"):
        if phrase.lower() not in coherence.lower():
            fail(f"product-coherence missing {phrase}")


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


def validate_voice() -> None:
    combined = "\n".join(
        path.read_text(encoding="utf-8")
        for path in (SKILLS / "venture-judgment" / "references").glob("*.md")
    )

    required = (
        "Preserve YC's epistemology. Rewrite YC's economics.",
        "Code got cheaper faster than complexity did.",
        "Build more. Make users understand less.",
        "Be ambitious as fuck.",
        "experience tokens",
    )
    for phrase in required:
        if phrase.lower() not in combined.lower():
            fail(f"shared brain missing required belief: {phrase}")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for name in EXPECTED_SKILLS:
        if name not in readme:
            fail(f"README missing {name}")

    if "npx skills@latest add" not in readme:
        fail("README missing simple skill installation")


def compile_scripts() -> None:
    with tempfile.TemporaryDirectory() as cache:
        for script in (ROOT / "scripts").glob("*.py"):
            py_compile.compile(
                str(script),
                cfile=str(Path(cache) / f"{script.stem}.pyc"),
                doraise=True,
            )


def main() -> int:
    try:
        validate_layout()
        validate_plugin()
        validate_skills()
        validate_markdown()
        validate_voice()
        compile_scripts()
    except (ValidationError, py_compile.PyCompileError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1

    print(
        "OK: Company Kernel 0.9 is one shared brain, three user experiences, "
        "and only AGENTS.md, PROJECT.md, and NOW.md in a project"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
