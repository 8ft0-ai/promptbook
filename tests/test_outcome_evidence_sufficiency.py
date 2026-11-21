"""Source-contract regressions for observable outcome evidence.

These verify that the loaded /go contract distinguishes supporting checks from
outcome evidence. They do NOT establish real-model behavioural compliance.
"""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROGRESSION = ROOT / "prompts" / "workflows" / "autonomous-progression.md"
ROUTER = ROOT / "prompts" / "workflows" / "README.md"


class OutcomeEvidenceSufficiencyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        source = PROGRESSION.read_text(encoding="utf-8")
        cls.verify = source.split("4. VERIFY:", 1)[1].split("\n5. STOP:", 1)[0].lower()
        cls.router = ROUTER.read_text(encoding="utf-8").lower()

    def test_acceptance_reaches_observable_boundary_not_intermediate_success(self):
        for requirement in (
            "requested result at the lowest relevant observable boundary",
            "application behaviour",
            "integration consumer readback",
            "operational effect",
            "cannot replace outcome evidence",
        ):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement, self.verify)

    def test_green_engine_tests_do_not_mask_broken_application(self):
        # An engine with all tests passing, but a broken delivered application.
        for supporting_evidence in (
            "generated code",
            "unit tests",
            "green ci",
            "process exit",
            "artefacts",
        ):
            with self.subTest(supporting_evidence=supporting_evidence):
                self.assertIn(supporting_evidence, self.verify)
        self.assertIn("a broken application", self.verify)
        self.assertIn("precludes complete", self.verify)

    def test_successful_api_without_required_readback_is_not_complete(self):
        # Transport success cannot establish consumer-observed delivery.
        self.assertIn("integration consumer readback", self.verify)
        self.assertIn("missing mandatory consumer readback precludes complete", self.verify)

    def test_verified_positive_result_can_complete_without_extra_work(self):
        # A working application and verified consumer remain eligible to finish.
        self.assertIn("verified behaviour permits complete", self.verify)
        self.assertIn("when conditions hold", self.verify)
        self.assertIn("least expensive sufficient authorised checks", self.verify)
        self.assertIn("stop when satisfied without optional pr/review", self.verify)
        self.assertIn("return complete immediately", self.router)

    def test_unavailable_verification_does_not_invent_authority(self):
        # Unavailable or prohibited integration evidence cannot be called PASS.
        self.assertIn("if verification is unavailable or prohibited", self.verify)
        self.assertIn("report the unverified boundary", self.verify)
        self.assertIn("do not demand a routine `proceed` confirmation", self.router)
        self.assertIn("without inventing success or authority", self.verify)
        self.assertIn("authorised checks", self.verify)
        self.assertIn("including relevant negative paths", self.verify)

    def test_existing_lifecycle_and_review_boundaries_remain_intact(self):
        for invariant in (
            "after every observed tool result",
            "under /go (until_boundary)",
            "under /step (one_transition)",
        ):
            self.assertIn(invariant, self.verify)
        for status in ("external_required", "decision_required", "blocked", "complete"):
            self.assertIn(status, self.router)


if __name__ == "__main__":
    unittest.main()
