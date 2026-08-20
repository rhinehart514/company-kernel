#!/usr/bin/env python3

from __future__ import annotations

import json
import re
import sys
from urllib.parse import urlparse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

REQUIRED_FILES = [
    ROOT / "README.md",
    ROOT / "LICENSE",
    ROOT / ".agents/plugins/marketplace.json",
    ROOT / "plugins/company-kernel/.codex-plugin/plugin.json",
    ROOT / "plugins/company-kernel/templates/COMPANY.md",
    ROOT / "plugins/company-kernel/templates/AGENTS.route.md",
    ROOT / "plugins/company-kernel/templates/OPERATOR.md",
]

REQUIRED_COMPANY_HEADINGS = [
    "## Current model",
    "## 1. World and pressure",
    "## 2. Actor system",
    "## 3. Value contract",
    "## 4. Responsibility contract",
    "## 5. Delivery system",
    "## 6. Commercial system",
    "## 7. Accumulating assets",
    "## 8. Boundary and expansion",
    "## 9. Decision posture",
    "## 10. Current company decisions",
    "## 11. Evidence and unknowns",
    "## Change contract",
]

SEMVER_RE = re.compile(
    r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)"
    r"(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$"
)

failures: list[str] = []
counts = {
    "skills": 0,
    "behavioral_evals": 0,
    "trigger_cases": 0,
    "assertions": 0,
}


def fail(message: str) -> None:
    failures.append(message)


def frontmatter(text: str, path: Path) -> dict[str, str]:
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        fail(f"{path}: missing YAML frontmatter")
        return {}

    data: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip("\"'")
    return data


for path in REQUIRED_FILES:
    if not path.is_file():
        fail(f"missing required file: {path.relative_to(ROOT)}")

try:
    plugin = json.loads((ROOT / "plugins/company-kernel/.codex-plugin/plugin.json").read_text())
    if plugin.get("name") != "company-kernel":
        fail("plugin name must be company-kernel")
    if not SEMVER_RE.fullmatch(str(plugin.get("version", ""))):
        fail("plugin version must be strict semver")
    if not str(plugin.get("description", "")).strip():
        fail("plugin description is required")
    if plugin.get("skills") != "./skills/":
        fail("plugin skills path must be ./skills/")
    if plugin.get("license") != "MIT":
        fail("plugin license must match repository license")
    author = plugin.get("author")
    if not isinstance(author, dict) or not str(author.get("name", "")).strip():
        fail("plugin author.name is required")
    elif author.get("url"):
        parsed = urlparse(str(author["url"]))
        if parsed.scheme != "https" or not parsed.netloc:
            fail("plugin author.url must be an absolute https URL")
    interface = plugin.get("interface")
    if not isinstance(interface, dict):
        fail("plugin interface is required")
    else:
        for field in ("displayName", "shortDescription", "longDescription", "developerName", "category"):
            if not str(interface.get(field, "")).strip():
                fail(f"plugin interface.{field} is required")
        capabilities = interface.get("capabilities")
        if not isinstance(capabilities, list) or not all(isinstance(item, str) and item.strip() for item in capabilities):
            fail("plugin interface.capabilities must be a non-empty string array")
        prompts = interface.get("defaultPrompt")
        if not isinstance(prompts, list) or not 1 <= len(prompts) <= 3:
            fail("plugin interface.defaultPrompt must contain one to three prompts")
        else:
            for prompt in prompts:
                if not isinstance(prompt, str) or not prompt.strip() or len(prompt) > 128:
                    fail("each plugin default prompt must be a non-empty string of at most 128 characters")
except Exception as error:
    fail(f"invalid plugin.json: {error}")

try:
    marketplace = json.loads((ROOT / ".agents/plugins/marketplace.json").read_text())
    plugins = marketplace.get("plugins", [])
    entries = [item for item in plugins if item.get("name") == "company-kernel"]
    if len(entries) != 1:
        fail("marketplace must expose company-kernel exactly once")
    else:
        entry = entries[0]
        if entry.get("source") != {"source": "local", "path": "./plugins/company-kernel"}:
            fail("marketplace must point to ./plugins/company-kernel")
        if entry.get("policy") != {"installation": "AVAILABLE", "authentication": "ON_INSTALL"}:
            fail("marketplace policy must be explicit and supported")
        if not str(entry.get("category", "")).strip():
            fail("marketplace category is required")
except Exception as error:
    fail(f"invalid marketplace.json: {error}")

company_template = (ROOT / "plugins/company-kernel/templates/COMPANY.md").read_text() if (ROOT / "plugins/company-kernel/templates/COMPANY.md").is_file() else ""
for heading in REQUIRED_COMPANY_HEADINGS:
    if heading not in company_template:
        fail(f"COMPANY.md template missing heading: {heading}")

skill_dirs = sorted(path for path in (ROOT / "plugins/company-kernel/skills").iterdir() if path.is_dir())
if [path.name for path in skill_dirs] != ["company-model", "market-probe", "opportunity-evaluate"]:
    fail("skills must be exactly company-model, market-probe, and opportunity-evaluate")

for skill_dir in skill_dirs:
    name = skill_dir.name
    counts["skills"] += 1

    skill_file = skill_dir / "SKILL.md"
    metadata_file = skill_dir / "agents/openai.yaml"
    evals_file = skill_dir / "evals/evals.json"
    triggers_file = skill_dir / "evals/trigger-evals.json"

    for path in [skill_file, metadata_file, evals_file, triggers_file]:
        if not path.is_file():
            fail(f"{name}: missing {path.relative_to(skill_dir)}")

    if not skill_file.is_file():
        continue

    text = skill_file.read_text()
    meta = frontmatter(text, skill_file.relative_to(ROOT))
    if meta.get("name") != name:
        fail(f"{name}: frontmatter name must match directory")
    if not meta.get("description"):
        fail(f"{name}: frontmatter description is required")

    if re.search(r"\b(TODO|TBD|PLACEHOLDER)\b", text, re.IGNORECASE):
        fail(f"{name}: unfinished placeholder found")

    if metadata_file.is_file():
        metadata = metadata_file.read_text()
        if f"${name}" not in metadata:
            fail(f"{name}: default prompt must explicitly name the skill")
        if "allow_implicit_invocation: false" not in metadata:
            fail(f"{name}: skill must be explicit-only")

    if evals_file.is_file():
        try:
            data = json.loads(evals_file.read_text())
            if data.get("skill_name") != name:
                fail(f"{name}: behavioral eval skill_name mismatch")
            evals = data.get("evals", [])
            if len(evals) < 4:
                fail(f"{name}: at least four behavioral evals required")
            ids = [item.get("id") for item in evals]
            if len(ids) != len(set(ids)):
                fail(f"{name}: behavioral eval IDs must be unique")
            for item in evals:
                counts["behavioral_evals"] += 1
                assertions = item.get("assertions", [])
                counts["assertions"] += len(assertions)
                if f"${name}" not in item.get("prompt", ""):
                    fail(f"{name}/{item.get('id')}: prompt must explicitly invoke skill")
                if not item.get("expected_output", "").strip():
                    fail(f"{name}/{item.get('id')}: expected_output is required")
                if len(assertions) < 5:
                    fail(f"{name}/{item.get('id')}: at least five assertions required")
        except Exception as error:
            fail(f"{name}: invalid behavioral evals: {error}")

    if triggers_file.is_file():
        try:
            data = json.loads(triggers_file.read_text())
            if data.get("skill_name") != name:
                fail(f"{name}: trigger eval skill_name mismatch")
            if data.get("policy") != "explicit-only":
                fail(f"{name}: trigger policy must be explicit-only")
            cases = data.get("cases", [])
            counts["trigger_cases"] += len(cases)
            positive = [item for item in cases if item.get("should_activate") is True]
            negative = [item for item in cases if item.get("should_activate") is False]
            if len(positive) < 2:
                fail(f"{name}: at least two positive trigger cases required")
            if len(negative) < 4:
                fail(f"{name}: at least four negative trigger cases required")
            for item in positive:
                prompt = item.get("prompt", "").lower()
                if f"${name}" not in prompt and name not in prompt:
                    fail(f"{name}: positive trigger must name the skill")
        except Exception as error:
            fail(f"{name}: invalid trigger evals: {error}")

print(" ".join(f"{key}={value}" for key, value in counts.items()))

if failures:
    for failure in failures:
        print(f"FAIL {failure}", file=sys.stderr)
    print(f"validation=failed failures={len(failures)}")
    raise SystemExit(1)

print("validation=passed")
