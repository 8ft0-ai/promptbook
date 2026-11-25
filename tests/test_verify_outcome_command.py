"""Issue #112: source-level regression coverage for read-only /verify.

These assertions establish contract wiring, not actual agent behavioural compliance.
"""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROUTER = ROOT / "prompts/workflows/README.md"
VERIFY = ROOT / "prompts/workflows/verify-outcome.md"
README = ROOT / "README.md"
BOOTSTRAP_GUIDE = ROOT / "guides/project-bootstrap.md"
AGENTS = ROOT / "AGENTS.md"


class VerifyOutcomeCommandTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.verify = VERIFY.read_text(encoding="utf-8").lower()
        cls.router = ROUTER.read_text(encoding="utf-8").lower()

    def test_command_is_discoverable_across_public_surfaces(self):
        for path in (ROUTER, README, BOOTSTRAP_GUIDE, AGENTS):
            with self.subTest(path=str(path)):
                self.assertIn("/verify", path.read_text(encoding="utf-8"))
        self.assertIn("verify-outcome.md", self.router)
        self.assertIn("verify-outcome.md", (ROOT / "prompts/README.md").read_text())

    def test_source_tests_cannot_be_substituted_for_delivered_outcome(self):
        for marker in (
            "source inspection", "tests/ci", "observed consumer or operational behaviour",
            "green ci", "consumer readback", "delivered behaviour",
            "stale candidate", "conflicting evidence",
        ):
            with self.subTest(marker=marker):
                self.assertIn(marker, self.verify)

    def test_unavailable_or_failed_evidence_cannot_be_pass(self):
        for marker in ("verified", "failed", "inconclusive", "missing evidence",
                       "every applicable mandatory criterion", "read-only"):
            self.assertIn(marker, self.verify)
        self.assertIn("never a manufactured pass", self.verify)

    def test_verify_does_not_authorise_implementation_or_fresh_review(self):
        for marker in (
            "do not remediate", "write reviews", "merge", "deploy",
            "fresh reviewer independence", "no lifecycle authority",
        ):
            self.assertIn(marker, self.verify)
        self.assertIn("| `/verify` | `stop` |", self.router)
        self.assertIn("does not write back", self.router)


if __name__ == "__main__":
    unittest.main()
