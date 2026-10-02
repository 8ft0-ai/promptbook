import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ROOT / "prompts" / "workflows"
ENGINEERING = ROOT / "prompts" / "engineering"

ISSUEOPS_COMPATIBILITY_BASELINE = "v0.3.0"

# Hermetic compatibility fixture for the pinned external semantic kernel.
#
# These entries identify the IssueOps v0.3.0 normative rule being protected
# without copying IssueOps lifecycle machinery into Promptbook. Each regression
# test below maps one of these repository-local obligations to the generic
# Promptbook invariants that must preserve it.
ISSUEOPS_V0_3_0_RULES = {
    "implementation_plan_approval": {
        "source": "docs/issueops-protocol.md#3-post-and-obtain-approval-of-the-implementation-plan",
        "requirement": (
            "A separate durable human approval of the detailed implementation plan "
            "must exist before branch creation or implementation mutation."
        ),
    },
    "exact_state_merge_authority": {
        "source": "docs/reference/review-decisions-and-merge-blockers.md#durable-merge-authority-provenance",
        "requirement": (
            "Merge requires a durable human decision for the exact current PR head "
            "and accepted review state; moved state makes earlier authority stale."
        ),
    },
    "bounded_remediation_then_review": {
        "source": "docs/issueops-protocol.md#10-remediate-review-feedback-inside-the-contract",
        "requirement": (
            "Review remediation stays inside the execution contract, reruns affected "
            "validation, and does not replace review of the resulting state."
        ),
    },
    "ordered_lifecycle_gate": {
        "source": "docs/reference/review-decisions-and-merge-blockers.md#pre-implementation-lifecycle-authority",
        "requirement": (
            "Later artefacts cannot retrospectively satisfy a missing required "
            "pre-action authority gate."
        ),
    },
    "exact_candidate_review": {
        "source": "docs/issueops-protocol.md#9-review-against-the-contract",
        "requirement": (
            "Review adjudicates the final pull-request state and current evidence "
            "against the governing contract."
        ),
    },
}


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

    def assert_issueops_rule(self, rule_name, *promptbook_markers):
        rule = ISSUEOPS_V0_3_0_RULES[rule_name]
        self.assertTrue(rule["source"].startswith("docs/"))
        self.assertTrue(rule["requirement"])
        for haystack, marker in promptbook_markers:
            self.assertIn(marker, haystack)

    def test_baseline_is_pinned_to_issueops_v0_3_0_with_normative_sources(self):
        self.assertEqual("v0.3.0", ISSUEOPS_COMPATIBILITY_BASELINE)
        self.assertEqual(
            {
                "implementation_plan_approval",
                "exact_state_merge_authority",
                "bounded_remediation_then_review",
                "ordered_lifecycle_gate",
                "exact_candidate_review",
            },
            set(ISSUEOPS_V0_3_0_RULES),
        )
        for rule in ISSUEOPS_V0_3_0_RULES.values():
            self.assertTrue(rule["source"].startswith("docs/"))
            self.assertTrue(rule["requirement"])

    def test_go_stops_at_missing_implementation_authority(self):
        self.assert_issueops_rule(
            "implementation_plan_approval",
            (
                self.router_lower,
                "commands do not grant authority beyond the narrow operation authority",
            ),
            (
                self.plan_lower,
                "planning record does not itself grant implementation or repository-mutation authority",
            ),
            (self.implement_lower, "authorised repository write path"),
            (
                self.autonomous_lower,
                "technical capability availability never creates authority",
            ),
            (
                self.autonomous_lower,
                "missing or ambiguous authority never defaults to `allow`",
            ),
        )

    def test_go_requires_exact_state_merge_authority(self):
        self.assert_issueops_rule(
            "exact_state_merge_authority",
            (
                self.fresh_review_lower,
                "review result never creates mutation authority",
            ),
            (
                self.run_context_lower,
                "merge of the exact candidate when merge authority is independently established",
            ),
            (self.run_context_lower, "approved candidate a"),
            (self.run_context_lower, "owner authorises merge of a"),
            (self.run_context_lower, "refresh a / review / checks / authority"),
            (self.run_context_lower, "merge a if unchanged"),
            (
                self.run_context_lower,
                "technical capability availability may only narrow executable capability; "
                "it must never create authority",
            ),
        )

    def test_fix_is_bounded_and_cannot_satisfy_required_independent_review(self):
        self.assert_issueops_rule(
            "bounded_remediation_then_review",
            (
                self.fix_lower,
                "execute only `allow` actions that are actually available",
            ),
            (
                self.fix_lower,
                "implement the bounded corrections",
            ),
            (
                self.fix_lower,
                "starting candidate a plus authorised bounded remediation produces candidate b",
            ),
            (
                self.fix_lower,
                "author-side remediation cannot substitute for fresh independent review",
            ),
            (
                self.fresh_review_lower,
                "must not claim a fresh independent review",
            ),
            (
                self.run_context_lower,
                "candidate a does not transfer to moved candidate a'",
            ),
        )

    def test_status_is_read_only_and_exposes_earliest_outstanding_gate(self):
        self.assert_issueops_rule(
            "ordered_lifecycle_gate",
            (self.router_lower, "/status [target]` — read-only"),
            (
                self.router_lower,
                "reconstruct and report broader authoritative current state",
            ),
            (
                self.router_lower,
                "the same next transition reported by `/next`",
            ),
            (
                self.run_context_lower,
                "proposed next governed action, required preconditions, required evidence, "
                "and completion conditions",
            ),
            (
                self.run_context_lower,
                "equivalent authoritative inputs must not produce a different next transition "
                "merely because the user selected a different read-only projection command",
            ),
            (
                self.autonomous_lower,
                "missing or ambiguous authority never defaults to `allow`",
            ),
            (
                self.run_context_lower,
                "if authority is missing or stale, surface the appropriate "
                "owner/separate-authority boundary",
            ),
        )
        self.assertIn("/status -> reports next: t/b", self.router_lower)
        self.assertIn(
            "/go     -> repeats the same transition loop until b",
            self.router_lower,
        )

    def test_review_is_bound_to_exact_candidate_and_freshness(self):
        self.assert_issueops_rule(
            "exact_candidate_review",
            (
                self.fresh_review_lower,
                "bind the review to the candidate actually inspected",
            ),
            (
                self.fresh_review_lower,
                "candidate moved materially enough that the completed review is stale",
            ),
            (
                self.fresh_review_lower,
                "must not claim a fresh independent review",
            ),
            (
                self.fresh_review_lower,
                "review result never creates mutation authority",
            ),
        )

    def test_plan_remains_non_authorising_and_preserves_local_plan_approval(self):
        self.assert_issueops_rule(
            "implementation_plan_approval",
            (self.plan_lower, "do not begin implementation while planning"),
            (self.plan_lower, "ready for implementation"),
            (
                self.plan_lower,
                "planning record does not itself grant implementation or repository-mutation authority",
            ),
            (
                self.router_lower,
                "repository-local instructions and current authoritative evidence remain higher precedence",
            ),
            (
                self.autonomous_lower,
                "missing or ambiguous authority never defaults to `allow`",
            ),
            (self.implement_lower, "authorised repository write path"),
            (
                self.implement_lower,
                "do not merge, deploy, release, or broaden scope unless that action is "
                "already authorised separately",
            ),
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
        self.assertIn(
            "candidate approved\n    ≠\nmerge authorised",
            self.run_context_lower,
        )


if __name__ == "__main__":
    unittest.main()
