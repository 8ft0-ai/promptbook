import importlib.util
import re
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "validate_promptbook", ROOT / "scripts" / "validate_promptbook.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)

PUBLIC_COMMANDS = {
    "/go",
    "/review",
    "/plan",
    "/implement",
    "/fix",
    "/handoff",
    "/status",
}
COMMAND_RE = re.compile(r"`(/[-a-z]+)(?:\s[^`]*)?`")


def declared_commands(text: str, heading: str) -> set[str]:
    return {
        match.group(1)
        for match in COMMAND_RE.finditer(MODULE.section(text, heading))
    }


class PromptbookValidationTests(unittest.TestCase):
    def test_repository_is_valid(self):
        self.assertEqual([], MODULE.validate_repository(ROOT))

    def test_unknown_status_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "prompt.md"
            path.write_text(
                "# Test\n\n"
                "## Purpose\nX\n\n## When to use\nX\n\n"
                "## Prompt\n```text\nDo X\n```\n\n"
                "## Inputs\nNone.\n\n## What it does\nX\n\n"
                "## Boundaries / limitations\nX\n\n## Status\n`unknown`\n",
                encoding="utf-8",
            )
            errors = MODULE.validate_prompt_file(path)
            self.assertTrue(any("status must be one of" in error for error in errors))

    def test_undeclared_placeholder_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "prompt.md"
            path.write_text(
                "# Test\n\n"
                "## Purpose\nX\n\n## When to use\nX\n\n"
                "## Prompt\n```text\nReview <TARGET>\n```\n\n"
                "## Inputs\nNone.\n\n## What it does\nX\n\n"
                "## Boundaries / limitations\nX\n\n## Status\n`tested`\n",
                encoding="utf-8",
            )
            errors = MODULE.validate_prompt_file(path)
            self.assertTrue(any("placeholder <TARGET>" in error for error in errors))

    def test_private_identifier_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "doc.md"
            errors = MODULE.validate_text_safety(path, "source: ai-prompt-library")
            self.assertTrue(errors)

    def test_workflow_router_contract(self):
        text = (ROOT / "prompts" / "workflows" / "README.md").read_text(encoding="utf-8")
        lower = text.lower()

        for target in (
            "autonomous-progression.md",
            "fresh-independent-review.md",
            "next-session-handover.md",
            "../engineering/plan-an-issue.md",
            "../engineering/implement-an-approved-issue.md",
            "../engineering/remediate-review-findings.md",
        ):
            self.assertIn(target, text)

        for terminal_state in (
            "EXTERNAL_REQUIRED",
            "DECISION_REQUIRED",
            "BLOCKED",
            "COMPLETE",
        ):
            self.assertIn(terminal_state, text)

        self.assertEqual(PUBLIC_COMMANDS, declared_commands(text, "Shorthand commands"))

        self.assertIn("fresh", lower)
        self.assertIn("not genuinely fresh", lower)
        self.assertIn("handover", lower)
        self.assertIn("approval", lower)
        self.assertIn("execution authority", lower)
        self.assertIn("return control to the governing workflow", lower)
        self.assertIn("minimum-safe remediation", lower)
        self.assertIn("final deliverable", lower)
        self.assertIn("does not itself create mutation authority", lower)
        self.assertIn("commands do not grant authority", lower)
        self.assertIn("read-only", lower)
        self.assertIn("routine `proceed` confirmation", lower)

        for pattern in MODULE.PRIVATE_PATTERNS.values():
            self.assertNotIn(pattern, text)

    def test_fresh_review_composition_contract(self):
        text = (
            ROOT / "prompts" / "workflows" / "fresh-independent-review.md"
        ).read_text(encoding="utf-8")
        lower = text.lower()

        self.assertIn("single disposition is the review record", lower)
        self.assertIn("explicitly requested as the final deliverable", lower)
        self.assertIn("return control to that workflow", lower)
        self.assertIn("minimum-safe remediation", lower)
        self.assertIn("review result never creates mutation authority", lower)
        self.assertIn("must not claim a fresh independent review", lower)
        self.assertIn("already-authorised merge, verification, and close-out", lower)

        for pattern in MODULE.PRIVATE_PATTERNS.values():
            self.assertNotIn(pattern, text)

    def test_project_bootstrap_contract(self):
        path = ROOT / "guides" / "project-bootstrap.md"
        text = path.read_text(encoding="utf-8")
        lower = text.lower()

        self.assertIn("AGENTS.md", text)
        self.assertIn("prompts/workflows/README.md", text)
        self.assertIn("8ft0-ai/promptbook@vX.Y.Z", text)
        self.assertIn("stable release", lower)
        self.assertIn("track `main`", lower)
        self.assertIn("do not grant additional authority", lower)
        self.assertIn("read-only", lower)

        for terminal_state in (
            "EXTERNAL_REQUIRED",
            "DECISION_REQUIRED",
            "BLOCKED",
            "COMPLETE",
        ):
            self.assertIn(terminal_state, text)

        self.assertEqual(PUBLIC_COMMANDS, declared_commands(text, "Shorthand commands"))

        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        using = (ROOT / "guides" / "using-promptbook.md").read_text(encoding="utf-8")
        self.assertIn("guides/project-bootstrap.md", readme)
        self.assertIn("project-bootstrap.md", using)

        for pattern in MODULE.PRIVATE_PATTERNS.values():
            self.assertNotIn(pattern, text)

    def test_public_command_docs_stay_aligned(self):
        surfaces = (
            (ROOT / "README.md", "Quick commands"),
            (ROOT / "guides" / "project-bootstrap.md", "Shorthand commands"),
            (ROOT / "prompts" / "workflows" / "README.md", "Shorthand commands"),
            (ROOT / "AGENTS.md", "Public interface maintenance"),
        )

        for path, heading in surfaces:
            text = path.read_text(encoding="utf-8")
            self.assertEqual(
                PUBLIC_COMMANDS,
                declared_commands(text, heading),
                f"public command vocabulary drifted in {path}",
            )

    def test_bootstrap_copy_stays_aligned_with_guide(self):
        bootstrap = (ROOT / "BOOTSTRAP").read_text(encoding="utf-8").strip()
        guide = (ROOT / "guides" / "project-bootstrap.md").read_text(encoding="utf-8")

        self.assertIn(
            f"```text\n{bootstrap}\n```",
            guide,
            "BOOTSTRAP must match the copyable project bootstrap block in the guide",
        )

    def test_agents_declares_public_interface_maintenance(self):
        text = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        lower = text.lower()

        self.assertIn("prompts/workflows/README.md", text)
        self.assertIn("README.md", text)
        self.assertIn("guides/project-bootstrap.md", text)
        self.assertIn("BOOTSTRAP", text)
        self.assertIn("regression coverage", lower)
        self.assertIn("ci fails on accidental drift", lower)
        self.assertIn("fresh-review", lower)


if __name__ == "__main__":
    unittest.main()
