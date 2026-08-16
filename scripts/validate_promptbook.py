#!/usr/bin/env python3
"""Dependency-free structural validation for Promptbook."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
PROMPTS = ROOT / "prompts"
REQUIRED_ROOT = [
    "README.md",
    "AGENTS.md",
    "BOOTSTRAP",
    "CONTRIBUTING.md",
    "LICENSE",
    "templates/prompt-template.md",
]
REQUIRED_HEADINGS = [
    "Purpose",
    "When to use",
    "Prompt",
    "Inputs",
    "What it does",
    "Boundaries / limitations",
    "Status",
]
ALLOWED_STATUS = {"experimental", "tested", "stable"}
PLACEHOLDER_RE = re.compile(r"<[A-Z][A-Z0-9_]*>")
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
PRIVATE_PATTERNS = {
    "private source repository name": "ai-prompt-library",
    "GitHub classic token prefix": "ghp_",
    "GitHub fine-grained token prefix": "github_pat_",
    "private image host": "private-user-images.githubusercontent.com",
    "private key marker": "BEGIN OPENSSH PRIVATE KEY",
}


def section(text: str, heading: str) -> str:
    marker = f"## {heading}"
    start = text.find(marker)
    if start < 0:
        return ""
    start += len(marker)
    next_heading = text.find("\n## ", start)
    return text[start:] if next_heading < 0 else text[start:next_heading]


def validate_prompt_file(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")

    positions = []
    for heading in REQUIRED_HEADINGS:
        marker = f"## {heading}"
        pos = text.find(marker)
        if pos < 0:
            errors.append(f"{path}: missing heading {marker}")
        positions.append(pos)
    present = [pos for pos in positions if pos >= 0]
    if present != sorted(present):
        errors.append(f"{path}: required headings are out of order")

    status_lines = [line.strip().strip("`") for line in section(text, "Status").splitlines() if line.strip()]
    if not status_lines or status_lines[0] not in ALLOWED_STATUS:
        errors.append(f"{path}: status must be one of {sorted(ALLOWED_STATUS)}")

    prompt_text = section(text, "Prompt")
    inputs_text = section(text, "Inputs")
    for placeholder in sorted(set(PLACEHOLDER_RE.findall(prompt_text))):
        if placeholder not in inputs_text:
            errors.append(f"{path}: placeholder {placeholder} is not declared in Inputs")

    if any(token in text for token in ("TODO", "TBD", "FIXME")):
        errors.append(f"{path}: unresolved TODO/TBD/FIXME marker")

    return errors


def validate_text_safety(path: Path, text: str) -> list[str]:
    errors: list[str] = []
    for label, pattern in PRIVATE_PATTERNS.items():
        if pattern in text:
            errors.append(f"{path}: contains forbidden {label}")
    return errors


def validate_links(path: Path, text: str, root: Path) -> list[str]:
    errors: list[str] = []
    for raw in LINK_RE.findall(text):
        target = raw.split("#", 1)[0].strip()
        if not target or target.startswith(("http://", "https://", "mailto:")):
            continue
        target = unquote(target)
        resolved = (path.parent / target).resolve()
        try:
            resolved.relative_to(root.resolve())
        except ValueError:
            errors.append(f"{path}: link escapes repository: {raw}")
            continue
        if not resolved.exists():
            errors.append(f"{path}: broken repository link: {raw}")
    return errors


def validate_repository(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    for relative in REQUIRED_ROOT:
        if not (root / relative).exists():
            errors.append(f"missing required path: {relative}")

    prompt_root = root / "prompts"
    prompt_files = sorted(
        path for path in prompt_root.rglob("*.md") if path.name != "README.md"
    ) if prompt_root.exists() else []
    if len(prompt_files) < 8:
        errors.append(f"expected at least 8 published prompts, found {len(prompt_files)}")

    for path in prompt_files:
        errors.extend(validate_prompt_file(path))

    public_text_paths = set(root.rglob("*.md"))
    bootstrap = root / "BOOTSTRAP"
    if bootstrap.exists():
        public_text_paths.add(bootstrap)

    for path in sorted(public_text_paths):
        text = path.read_text(encoding="utf-8")
        errors.extend(validate_text_safety(path, text))
        errors.extend(validate_links(path, text, root))

    return errors


def main() -> int:
    errors = validate_repository()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Promptbook validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
