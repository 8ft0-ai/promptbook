import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ROOT / "prompts" / "workflows"
ENGINEERING = ROOT / "prompts" / "engineering"

ISSUEOPS_COMPATIBILITY_BASELINE = "v0.3.0"


class IssueOpsV030CommandCompatibilityTests(unittest.TestCase):
    """Regression coverage for Promptbook compatibility with IssueOps v0.3.0."""

    @classmethod
    def setUpClass(cls):
        cls.router = (WORKFLOWS / "README.md").read_text(encoding="utf-8")
        cls.router_lower = cls.router.lower()
        cls.autonomous = (WORKFLOWS / "autonomous-progression.md").read_text(
            encoding="utf-8"
        )
        cls.autonomous_lower = cls.autonomous.lower()
        cls.run_context = (WORKFLOWS / "resolved-agent-run-context.md").read_text(
            encoding="utf-8"
        )
        cls.run_context_lower = cls.run_context.lower()
        cls.fresh_review = (WORKFLOWS / "fresh-independent-review.md").read_text(
            encoding="utf-8"
        )
        cls.fresh_review_lower = cls.fresh_review.lower()
        cls.plan = (ENGINEERING / "plan-an-issue.md").read_text(encoding="utf-8")
        cls.plan_lower = cls.plan.lower()
        cls.implement = (ENGINEERING / "implement-an-approved-issue.md").read_text(
            encoding="utf-8"
        )
        cls.implement_lower = cls.implement.lower()
        cls.fix = (ENGINEERING / "remediate-review-findings.md").read_text(
            encoding="utf-8"
        )
        cls.fix_lower = cls.fix.lower()

    def test_baseline_is_pinned_to_issueops_v0_3_0(self):
        self.assertEqual("v0.3.0", ISSUEOPS_COMPATIBILITY_BASELINE)

    def test_go_stops_at_missing_implementation_authority(self):
        self.assertIn(
            "commands do not grant authority beyond the narrow operation authority",
            self.router_lower,
        )
        self.assertIn(
            "planning record does not itself grant implementation or repository-mutation authority",
            self.plan_lower,
        )
        self.assertIn("authorised repository write path", self.implement_lower)
        self.assertIn(
            "technical capability availability never creates authority",
            self.autonomous_lower,
        )
        self.assertIn(
            "missing or ambiguous authority never defaults to `allow`",
            self.autonomous_lower,
        )

    def test_go_does_not_treat_review_or_capability_as_merge_authority(self):
        self.assertIn(
            "review result never creates mutation authority",
            self.fresh_review_lower,
        )
        self.assertIn(
            "does not intrinsically grant merge",
            self.run_context_lower,
        )
        self.assertIn("merge where already authorised", self.autonomous_lower)
        self.assertIn(
            "technical capability availability may only narrow executable capability; "
            "it must never create authority",
            self.run_context_lower,
        )

    def test_fix_cannot_satisfy_required_independent_review(self):
        self.assertIn(
            "author-side remediation cannot substitute for fresh independent review",
            self.fix_lower,
        )
        self.assertIn(
            "must not claim a fresh independent review",
            self.fresh_review_lower,
        )
        self.assertIn("candidate a", self.fix_lower)
        self.assertIn("candidate b", self.fix_lower)
        self.assertIn(
            "candidate a does not transfer to moved candidate a'",
            self.run_context_lower,
        )

    def test_status_is_read_only_and_projects_the_same_next_gate(self):
        self.assertIn("/status [target]` — read-only", self.router_lower)
        self.assertIn(
            "reconstruct and report broader authoritative current state",
            self.router_lower,
        )
        self.assertIn(
            "the same next transition reported by `/next`",
            self.router_lower,
        )
        self.assertIn(
            "`/next`, `/status`, and `/help` project the same resolved state read-only",
            self.run_context_lower,
        )
        self.assertIn("/status -> reports next: t/b", self.router_lower)
        self.assertIn(
            "/go     -> repeats the same transition loop until b",
            self.router_lower,
        )

    def test_review_is_bound_to_exact_candidate_and_freshness(self):
        self.assertIn(
            "bind the review to the candidate actually inspected",
            self.fresh_review_lower,
        )
        self.assertIn(
            "candidate moved materially enough that the completed review is stale",
            self.fresh_review_lower,
        )
        self.assertIn(
            "must not claim a fresh independent review",
            self.fresh_review_lower,
        )
        self.assertIn(
            "review result never creates mutation authority",
            self.fresh_review_lower,
        )

    def test_plan_remains_non_authorising(self):
        self.assertIn("do not begin implementation while planning", self.plan_lower)
        self.assertIn("ready for implementation", self.plan_lower)
        self.assertIn(
            "planning record does not itself grant implementation or repository-mutation authority",
            self.plan_lower,
        )
        self.assertIn("authorised repository write path", self.implement_lower)
        self.assertIn(
            "do not merge, deploy, release, or broaden scope unless that action is "
            "already authorised separately",
            self.implement_lower,
        )

    def test_cross_command_projection_and_authority_invariants_remain_composed(self):
        for marker in (
            "/next   -> reports transition t or boundary b",
            "/status -> reports next: t/b",
            "/step   -> executes t only when t is allow and executable; otherwise reports b",
            "/go     -> repeats the same transition loop until b",
        ):
            self.assertIn(marker, self.router_lower)
        self.assertIn(
            "technical capability availability never creates authority",
            self.autonomous_lower,
        )
        self.assertIn(
            "candidate a does not transfer to moved candidate a'",
            self.run_context_lower,
        )


if __name__ == "__main__":
    unittest.main()
