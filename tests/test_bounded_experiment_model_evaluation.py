"""Issue #112: static contract checks for finite experiments and fair model evaluations.

Source contract coverage only; these tests do not prove receiving-agent behaviour.
"""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WF = ROOT / "prompts/workflows"
ROUTER = (WF / "README.md").read_text().lower()
INDEX = (ROOT / "prompts/README.md").read_text().lower()


class BoundedExperimentModelEvaluationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.experiment = (WF / "bounded-experiment.md").read_text().lower()
        cls.evaluation = (WF / "model-evaluation.md").read_text().lower()

    def test_discoverable_under_existing_go_not_new_command(self):
        for file in ("bounded-experiment.md", "model-evaluation.md"):
            self.assertIn(file, ROUTER)
            self.assertIn("workflows/" + file, INDEX)
        self.assertIn("existing `/go`", self.evaluation)
        self.assertIn("ordinary `/go`", self.experiment)

    def test_experiment_is_predeclared_finite_reproducible_and_negative(self):
        for phrase in ("falsifiable", "null/negative", "fixed input/source",
                       "success/failure threshold", "maximum trials",
                       "stop conditions", "source receipts", "protected holdout",
                       "no-go", "hold", "no unstated retries", "paid fallback"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.experiment)

    def test_comparison_is_fair_bounded_and_reconstructable(self):
        for phrase in ("same eligible tasks", "rubric", "primary metric",
                       "minimum meaningful difference", "model/provider/version",
                       "unequal tool access", "free-tier eligibility",
                       "paired comparisons", "per-task result", "failures",
                       "inconclusive", "judge/model bias", "cost", "latency"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.evaluation)

    def test_no_silent_permissions_or_independent_review(self):
        for contract in (self.experiment, self.evaluation):
            for phrase in ("authority", "review", "deploy"):
                with self.subTest(phrase=phrase):
                    self.assertIn(phrase, contract)
        self.assertIn("not permission to trade", self.experiment)
        self.assertIn("no inference budget", self.evaluation)

if __name__ == "__main__":
    unittest.main()
