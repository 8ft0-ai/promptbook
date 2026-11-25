"""Issue #116: static /decide regressions, not live agent acceptance."""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / "prompts/workflows/decide-alternatives.md"
ROUTER = ROOT / "prompts/workflows/README.md"


class DecideCommandTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.workflow = WORKFLOW.read_text(encoding="utf-8").lower()
        cls.router = ROUTER.read_text(encoding="utf-8").lower()

    def test_public_discovery_and_stop_default(self):
        for path in ("README.md", "AGENTS.md", "guides/project-bootstrap.md",
                     "prompts/workflows/README.md"):
            with self.subTest(path=path):
                self.assertIn("/decide", (ROOT / path).read_text(encoding="utf-8"))
        self.assertIn("workflows/decide-alternatives.md", (ROOT / "prompts/README.md").read_text())
        self.assertIn("decide-alternatives.md", self.router)
        self.assertIn("| `/decide` | `stop` |", self.router)

    def test_explicit_criteria_and_hard_requirements(self):
        for marker in ("decision question", "accountable decision owner",
                       "candidate alternatives", "status quo", "hard constraints",
                       "disqualifiers", "weighted preference", "numerical weights"):
            with self.subTest(marker=marker):
                self.assertIn(marker, self.workflow)

    def test_fair_evidence_tradeoffs_and_uncertainty(self):
        for marker in ("same criteria", "evidence sources", "freshness",
                       "trade-offs", "counter-evidence", "dependency",
                       "reversibility", "absence of evidence",
                       "what would change the recommendation"):
            with self.subTest(marker=marker):
                self.assertIn(marker, self.workflow)

    def test_preference_defer_and_no_decision_supported(self):
        for marker in ("prefer <option>", "defer", "no decision",
                       "too ambiguous", "material evidence",
                       "no option satisfies", "ineligible winner"):
            with self.subTest(marker=marker):
                self.assertIn(marker, self.workflow)

    def test_distinct_from_other_commands(self):
        for marker in ("/assess", "/triage", "/risk", "/review",
                       "not an approval gate"):
            with self.subTest(marker=marker):
                self.assertIn(marker, self.workflow)

    def test_never_makes_decision_or_exercises_authority(self):
        for marker in ("read-only", "owner-reserved decision", "approve",
                       "independent reviewer", "accept risk", "waive hard requirements",
                       "remediate", "create or close issues/prs", "merge",
                       "deploy", "spend", "alter permissions",
                       "subsequent action requires its own authority"):
            with self.subTest(marker=marker):
                self.assertIn(marker, self.workflow)


if __name__ == "__main__":
    unittest.main()
