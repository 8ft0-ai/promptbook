import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ROOT / "prompts" / "workflows"
ENGINEERING = ROOT / "prompts" / "engineering"


class ArchitectureClosureReviewGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.router = (WORKFLOWS / "README.md").read_text(encoding="utf-8").lower()
        cls.closure = (WORKFLOWS / "architecture-closure-analysis.md").read_text(encoding="utf-8").lower()
        cls.review = (WORKFLOWS / "fresh-independent-review.md").read_text(encoding="utf-8").lower()
        cls.analysis = (WORKFLOWS / "stateful-invariant-analysis.md").read_text(encoding="utf-8").lower()
        cls.context = (WORKFLOWS / "resolved-agent-run-context.md").read_text(encoding="utf-8").lower()
        cls.auto = (WORKFLOWS / "autonomous-progression.md").read_text(encoding="utf-8").lower()
        cls.go = (ROOT / "guides" / "go-lifecycle.md").read_text(encoding="utf-8").lower()
        cls.plan = (ENGINEERING / "plan-an-issue.md").read_text(encoding="utf-8").lower()
        cls.implement = (ENGINEERING / "implement-an-approved-issue.md").read_text(encoding="utf-8").lower()
        cls.fix = (ENGINEERING / "remediate-review-findings.md").read_text(encoding="utf-8").lower()

    def test_ready_closure_is_not_self_approving(self):
        for surface in (self.router, self.closure, self.analysis):
            self.assertIn("closure_review_required", surface)
        self.assertIn("does not self-approve", self.closure)
        self.assertIn("not self-approval", self.router)
        self.assertIn("does not make replacement-candidate authoring eligible", self.analysis)

    def test_fresh_closure_review_precedes_projection(self):
        self.assertIn("review_type=architecture_closure", self.router)
        self.assertIn("review_type=architecture_closure", self.review)
        self.assertIn("approved_for_candidate_projection", self.router)
        self.assertIn("approved_for_candidate_projection", self.review)
        self.assertIn("candidate projection is not yet eligible", self.auto)
        self.assertIn("closure-review disposition", self.auto)
        self.assertIn("architecture closure, fresh closure review, candidate projection", self.go)

    def test_closure_review_changes_required_blocks_candidate_authoring(self):
        for surface in (self.router, self.review, self.auto, self.go):
            self.assertIn("changes required", surface)
        self.assertIn("must not route to `/fix` or candidate authoring", self.router)
        self.assertIn("keeps candidate projection ineligible", self.review)
        self.assertIn("no candidate projection", self.go)

    def test_closure_approval_is_exact_and_not_mutation_authority(self):
        self.assertIn("exact closure artefact", self.review)
        self.assertIn("separate current authority", self.router)
        self.assertIn("is not candidate, implementation, merge, deployment or execution approval", self.review)
        self.assertIn("cannot add candidate-write", self.context)

    def test_run_context_binds_closure_review_state(self):
        for marker in (
            "review_target_type",
            "architecture_closure_identity",
            "current_architecture_closure_identity",
            "current_closure_review_requirement",
            "current_closure_review_identity",
            "current_closure_review_disposition",
        ):
            self.assertIn(marker, self.context)
        self.assertIn("approved_for_candidate_projection", self.context)

    def test_projection_is_bound_to_approved_closure_and_no_new_semantics(self):
        for marker in (
            "architecture_closure_source=<exact closure artefact identity>",
            "architecture_closure_review=<exact fresh review identity with approved_for_candidate_projection>",
            "new decision-critical primitive",
        ):
            self.assertIn(marker, self.closure)
        self.assertIn("bind candidate projection to the exact approved closure artefact", self.implement)
        self.assertIn("stop projection and return to closure analysis/review", self.implement)

    def test_planning_sequence_contains_two_distinct_fresh_reviews(self):
        self.assertIn(
            "governing sources → closure artefact → genuinely fresh closure review "
            "→ approved closure artefact → candidate projection → genuinely fresh candidate review",
            self.plan,
        )

    def test_reviewed_closure_falsification_requires_complexity_disposition(self):
        for marker in ("simplify_or_decompose", "additional_model_complexity_justified"):
            self.assertIn(marker, self.router)
            self.assertIn(marker, self.closure)
        self.assertIn("platform-primitive reuse", self.closure)
        self.assertIn("objective narrowing", self.closure)

    def test_bounded_remediation_remains_separate(self):
        self.assertIn("ordinary `/fix` and its remediation-readiness sweep cannot satisfy that gate", self.fix)
        self.assertIn("bounded remediation that never enters architecture closure", self.fix)
        self.assertIn("must not acquire this stronger gate", self.fix)

    def test_go_cannot_skip_closure_review_gate(self):
        self.assertIn("`/go` must not skip this gate", self.auto)
        self.assertIn("`/go` must not propose candidate authoring while `closure_review_required` is unsatisfied", self.go)

    def test_no_new_public_command_is_required(self):
        self.assertNotIn("/review-closure", self.router)
        self.assertIn("route `/review`", self.router)


if __name__ == "__main__":
    unittest.main()
