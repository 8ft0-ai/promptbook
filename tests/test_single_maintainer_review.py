import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class SingleMaintainerReviewTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.router = (ROOT / "prompts" / "workflows" / "README.md").read_text(
            encoding="utf-8"
        )
        cls.router_lower = cls.router.lower()
        cls.fresh = (
            ROOT / "prompts" / "workflows" / "fresh-independent-review.md"
        ).read_text(encoding="utf-8")
        cls.fresh_lower = cls.fresh.lower()

    def test_known_same_account_authorship_skips_impossible_formal_review(self):
        for text in (self.router_lower, self.fresh_lower):
            self.assertIn("same-account pr authorship is already established", text)
            self.assertIn(
                "do not attempt a formal self-`approve` or self-`request_changes`",
                text,
            )

        self.assertNotIn(
            "if the hosting platform refuses a formal self-review",
            self.router_lower,
        )
        self.assertNotIn(
            "if the hosting platform refuses a formal self-review",
            self.fresh_lower,
        )

    def test_durable_record_is_not_formal_platform_review_state(self):
        self.assertIn("durable repository-local comment", self.router_lower)
        self.assertIn("not formal platform review state", self.router_lower)
        self.assertIn("durable pr comment", self.fresh_lower)
        self.assertIn("distinguish that record from formal platform review state", self.fresh_lower)
        self.assertIn("represent the durable record as a formal platform approval", self.fresh_lower)

    def test_fresh_context_independence_remains_mandatory(self):
        self.assertIn("genuinely fresh context", self.router_lower)
        self.assertIn("fresh independence is a property of this reviewing context", self.fresh_lower)
        self.assertIn("must not claim a fresh independent review", self.fresh_lower)

    def test_stronger_repository_requirements_override_solo_fallback(self):
        for text in (self.router_lower, self.fresh_lower):
            self.assertIn("repository-local policy", text)
            self.assertIn("branch protection", text)
            self.assertIn("regulation", text)
            self.assertIn("if those preconditions are not established", text)
            self.assertIn("stronger rule requires formal or distinct-person approval", text)
            self.assertIn("fail or hand off", text)

    def test_review_recording_creates_no_mutation_authority(self):
        self.assertIn("does not itself create mutation authority", self.router_lower)
        self.assertIn("review result never creates mutation authority", self.fresh_lower)
        self.assertIn("already-authorised merge, verification, and close-out", self.fresh_lower)


if __name__ == "__main__":
    unittest.main()
