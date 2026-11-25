"""Issue #116: static regressions for /triage; not live agent acceptance."""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / "prompts/workflows/triage-problems.md"
ROUTER = ROOT / "prompts/workflows/README.md"


class TriageCommandTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.workflow = WORKFLOW.read_text(encoding="utf-8").lower()
        cls.router = ROUTER.read_text(encoding="utf-8").lower()

    def test_public_command_discovery_and_stop_default(self):
        for path in ("README.md", "AGENTS.md", "guides/project-bootstrap.md",
                     "prompts/workflows/README.md"):
            with self.subTest(path=path):
                self.assertIn("/triage", (ROOT / path).read_text(encoding="utf-8"))
        self.assertIn("workflows/triage-problems.md", (ROOT / "prompts/README.md").read_text())
        self.assertIn("triage-problems.md", self.router)
        self.assertIn("| `/triage` | `stop` |", self.router)

    def test_finite_inputs_and_symptom_cause_separation(self):
        for marker in ("bounded, finite items", "consolidate duplicates",
                       "observed symptoms", "probable cause", "hypothesis",
                       "unverified report", "affected users", "evidence freshness"):
            with self.subTest(marker=marker):
                self.assertIn(marker, self.workflow)

    def test_all_classes_include_negative_and_inconclusive(self):
        for marker in ("blocker", "important", "defer", "noise", "inconclusive",
                       "no blocker", "no action", "insufficient/conflicting",
                       "never invent a blocker"):
            with self.subTest(marker=marker):
                self.assertIn(marker, self.workflow)

    def test_priority_is_evidence_linked_not_arbitrary(self):
        for marker in ("verified impact", "urgency", "dependency",
                       "reversibility", "intervention effort",
                       "ties or uncertain ordering", "made-up scores",
                       "smallest useful next intervention"):
            with self.subTest(marker=marker):
                self.assertIn(marker, self.workflow)

    def test_distinct_from_next_risk_and_execution(self):
        for marker in ("/next", "/risk", "/go", "/fix",
                       "does not", "not a proven blocker"):
            with self.subTest(marker=marker):
                self.assertIn(marker, self.workflow)

    def test_no_mutation_review_or_owner_authority(self):
        for marker in ("read-only", "do not edit or close issues",
                       "remediate defects", "create prs", "merge", "deploy",
                       "spend", "change permissions", "accept risk",
                       "approve a candidate", "independent review"):
            with self.subTest(marker=marker):
                self.assertIn(marker, self.workflow)


if __name__ == "__main__":
    unittest.main()
