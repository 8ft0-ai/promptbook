import importlib.util
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

        for target in (
            "autonomous-progression.md",
            "fresh-independent-review.md",
            "next-session-handover.md",
        ):
            self.assertIn(target, text)

        for terminal_state in (
            "EXTERNAL_REQUIRED",
            "DECISION_REQUIRED",
            "BLOCKED",
            "COMPLETE",
        ):
            self.assertIn(terminal_state, text)

        self.assertIn("fresh", text.lower())
        self.assertIn("not genuinely fresh", text.lower())
        self.assertIn("handover", text.lower())
        self.assertIn("approval", text.lower())
        self.assertIn("execution authority", text.lower())
        self.assertIn("return control to the governing workflow", text.lower())
        self.assertIn("minimum-safe remediation", text.lower())
        self.assertIn("final deliverable", text.lower())
        self.assertIn("does not itself create mutation authority", text.lower())

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


if __name__ == "__main__":
    unittest.main()
