"""Issue #116: static regressions for /assess; not a live-agent acceptance test."""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / "prompts/workflows/assess-objective.md"
ROUTER = ROOT / "prompts/workflows/README.md"


class AssessCommandTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.workflow = WORKFLOW.read_text(encoding="utf-8").lower()
        cls.router = ROUTER.read_text(encoding="utf-8").lower()

    def test_public_discovery_and_read_only_default(self):
        for path in (
            "README.md", "AGENTS.md", "guides/project-bootstrap.md",
            "prompts/workflows/README.md",
        ):
            with self.subTest(path=path):
                self.assertIn("/assess", (ROOT / path).read_text(encoding="utf-8"))
        self.assertIn("workflows/assess-objective.md", (ROOT / "prompts/README.md").read_text())
        self.assertIn("assess-objective.md", self.router)
        self.assertIn("| `/assess` | `stop` |", self.router)

    def test_goal_alignment_drift_and_no_drift_both_supported(self):
        for marker in (
            "original user objective", "success criteria", "current direction",
            "direction drift", "scope expansion", "diminishing returns",
            "opportunity cost", "ordinary progress", "justified changes",
            "no drift", "drift", "contrary evidence",
        ):
            with self.subTest(marker=marker):
                self.assertIn(marker, self.workflow)

    def test_all_recommendations_and_uncertainty_are_express(self):
        for marker in (
            "continue", "correct course", "simplify", "stop", "inconclusive",
            "missing, stale or conflicting", "evidence", "smallest useful next action",
            "no change is warranted", "recommend rather than decide",
        ):
            with self.subTest(marker=marker):
                self.assertIn(marker, self.workflow)

    def test_distinct_from_state_outcome_and_review(self):
        for marker in ("/status", "/verify", "/reflect", "/challenge",
                       "/simplify", "/review", "not a new lifecycle gate"):
            self.assertIn(marker, self.workflow)

    def test_no_execution_authority_or_false_completeness(self):
        for marker in (
            "read-only", "do not remediate", "close an issue", "edit files",
            "author a pr", "merge", "deploy", "spend", "alter permissions",
            "accept risk", "independent review", "not `/go` terminal states",
            "static source-contract tests cannot prove live agent behaviour",
        ):
            with self.subTest(marker=marker):
                self.assertIn(marker, self.workflow)


if __name__ == "__main__":
    unittest.main()
