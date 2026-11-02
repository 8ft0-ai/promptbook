"""Regression guard for the experimental, unrun PR Review Skill comparison."""

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "engineering-pr-review" / "SKILL.md"
BASELINE = ROOT / "prompts" / "engineering" / "pr-review.md"
FIXTURE = ROOT / "tests" / "fixtures" / "engineering_pr_review_skill_pilot.json"


class EngineeringPRReviewSkillPilotTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skill = SKILL.read_text(encoding="utf-8")
        cls.baseline = BASELINE.read_text(encoding="utf-8")
        cls.fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))

    def test_portable_skill_has_activation_metadata_and_bounded_size(self):
        self.assertTrue(self.skill.startswith("---\nname: engineering-pr-review\n"))
        self.assertIn("\ndescription: ", self.skill)
        self.assertIn("\n# Engineering PR review", self.skill)
        self.assertLess(len(self.skill), int(len(self.baseline) * 1.5))

    def test_skill_preserves_review_identity_authority_and_zero_writes(self):
        text = self.skill.lower()
        for required in (
            "agents.md", "take precedence", "governed `/review`",
            "exact head/base", "complete diff", "governing issue",
            "independence", "author or materially shape", "freshness",
            "negative paths", "security", "regressions",
            "missing host/integration evidence", "decision-critical",
            "finding one blocker does not end", "unverified",
            "zero writes", "do not submit github reviews/comments",
            "approved", "changes required", "cannot assess",
            "not formal github approval",
        ):
            with self.subTest(required=required):
                self.assertIn(required, text)

    def test_comparison_pins_single_exact_historical_revision(self):
        target = self.fixture["target"]
        self.assertEqual(self.fixture["fixture_version"], 1)
        self.assertEqual((target["repository"], target["pull_request"], target["governing_issue"]),
                         ("8ft0-ai/promptbook", 101, 100))
        self.assertEqual(target["exact_base"], "8b6e76a82ae877d2b4855e0521dce853c192f5a0")
        self.assertEqual(target["exact_head"], "000419dfc569e8eb990056e5f733a3a59efa76f7")
        self.assertEqual({entry["instruction"] for entry in self.fixture["alternatives"]},
                         {str(BASELINE.relative_to(ROOT)), str(SKILL.relative_to(ROOT))})

    def test_fixture_requires_real_independent_zero_write_observations(self):
        self.assertEqual(self.fixture["status"], "UNRUN")
        self.assertEqual(self.fixture["decision"], "HOLD")
        self.assertEqual(self.fixture["observations"], {"standalone": None, "skill": None})
        protocol = " ".join(self.fixture["protocol"]).lower()
        for required in ("separate reviewer contexts", "no github review",
                         "actual reads", "token/context", "negative",
                         "not force the governed /review router", "hold"):
            self.assertIn(required, protocol)
        self.assertIn("zero_writes", self.fixture["required_observations"])
        self.assertIn("material_findings", self.fixture["required_observations"])
        self.assertIn("portability_plain_markdown", self.fixture["required_observations"])


if __name__ == "__main__":
    unittest.main()
