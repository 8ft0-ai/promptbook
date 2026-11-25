"""Issue #112: /simplify contract regressions; no claim of live-agent behaviour."""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / "prompts/workflows/simplify.md"
ROUTER = ROOT / "prompts/workflows/README.md"


class SimplifyCommandTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.workflow = WORKFLOW.read_text(encoding="utf-8").lower()
        cls.router = ROUTER.read_text(encoding="utf-8").lower()

    def test_command_is_visible_and_read_only(self):
        for path in ("README.md", "AGENTS.md", "guides/project-bootstrap.md",
                     "prompts/workflows/README.md"):
            with self.subTest(path=path):
                self.assertIn("/simplify", (ROOT / path).read_text(encoding="utf-8"))
        self.assertIn("workflows/simplify.md", (ROOT / "prompts/README.md").read_text())
        self.assertIn("| `/simplify` | `stop` |", self.router)
        self.assertIn("read-only", self.workflow)

    def test_subtractive_proposal_has_comparison_and_negative_outcome(self):
        for text in ("subtract", "removing, consolidating or reusing",
                     "minimal alternative", "baseline versus alternative",
                     "no change", "inconclusive", "reversibility", "cost",
                     "failure modes", "estimated benefit"):
            with self.subTest(text=text):
                self.assertIn(text, self.workflow)

    def test_hard_guards_are_preserved(self):
        for text in ("security", "data integrity", "independent review",
                     "rollback", "verification", "hard gate",
                     "repository-local requirements", "risk acceptance",
                     "no implementation authority"):
            with self.subTest(text=text):
                self.assertIn(text, self.workflow)

    def test_not_a_mutation_or_approval_shortcut(self):
        for text in ("do not edit files", "merge", "deploy",
                     "alter permissions", "claim independent review",
                     "separate approval", "no implementation authority"):
            with self.subTest(text=text):
                self.assertIn(text, self.workflow)


if __name__ == "__main__":
    unittest.main()
