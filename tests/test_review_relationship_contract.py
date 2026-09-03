import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReviewRelationshipContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fresh = (
            ROOT / "prompts" / "workflows" / "fresh-independent-review.md"
        ).read_text(encoding="utf-8")
        cls.fresh_lower = cls.fresh.lower()
        cls.remediate = (
            ROOT / "prompts" / "engineering" / "remediate-review-findings.md"
        ).read_text(encoding="utf-8")
        cls.remediate_lower = cls.remediate.lower()
        cls.router = (ROOT / "prompts" / "workflows" / "README.md").read_text(
            encoding="utf-8"
        )
        cls.router_lower = cls.router.lower()

    def test_relationship_assessment_is_evidence_driven_not_count_driven(self):
        self.assertIn("assess their relationships proportionately", self.fresh_lower)
        self.assertIn(
            "do not infer an abstraction failure from the number of findings",
            self.fresh_lower,
        )
        self.assertIn("do not require a universal defect taxonomy", self.fresh_lower)
        self.assertIn("isolated defects in an otherwise sound abstraction", self.fresh_lower)
        self.assertIn("manifestations of a shared failure", self.fresh_lower)

    def test_shared_family_challenges_abstraction_before_local_exception(self):
        self.assertIn("when evidence indicates a shared defect family", self.fresh_lower)
        self.assertIn(
            "challenge whether the current abstraction or boundary remains sound "
            "before recommending another local exception",
            self.fresh_lower,
        )
        self.assertIn(
            "if the abstraction remains sound, a bounded local remediation may remain "
            "appropriate",
            self.fresh_lower,
        )

    def test_authorised_invariant_correction_can_be_minimum_safe_fix(self):
        self.assertIn(
            "the smallest safe correction is not necessarily the smallest textual or "
            "most local patch",
            self.remediate_lower,
        )
        self.assertIn(
            "shared invariant/boundary correction is objectively determined",
            self.remediate_lower,
        )
        self.assertIn("may be the minimum safe change", self.remediate_lower)
        self.assertIn(
            "minimum-safe remediation is not synonymous with the most local textual "
            "patch",
            self.fresh_lower,
        )

    def test_out_of_scope_abstraction_change_does_not_widen_fix_authority(self):
        self.assertIn(
            "requires materially new product, architecture, security, scope, owner, or "
            "other separate authority",
            self.remediate_lower,
        )
        self.assertIn("require owner / separate authority", self.remediate_lower)
        self.assertIn(
            "rather than decomposing it into superficially local exceptions or silently "
            "redesigning",
            self.remediate_lower,
        )
        self.assertIn("rather than manufacturing `/fix` authority", self.fresh_lower)

    def test_green_ci_does_not_establish_underlying_invariant(self):
        self.assertIn(
            "treat green ci and passing regression examples as evidence for the "
            "behaviours and cases currently specified",
            self.fresh_lower,
        )
        self.assertIn(
            "not as automatic proof that the underlying invariant or abstraction is "
            "sound",
            self.fresh_lower,
        )
        self.assertIn(
            "do not let passing example tests suppress substantive relationship/invariant "
            "review",
            self.fresh_lower,
        )

    def test_router_exposes_relationship_boundary_without_widening_fix(self):
        self.assertIn("materially related blockers", self.router_lower)
        self.assertIn("synthesise their relationship", self.router_lower)
        self.assertIn("does not widen `/fix`", self.router_lower)
        self.assertIn("already within existing remediation authority", self.router_lower)

    def test_review_completion_and_fresh_rereview_contracts_remain_present(self):
        self.assertIn(
            "derive a bounded decision-critical review surface for the exact candidate",
            self.fresh_lower,
        )
        self.assertIn(
            "discovering a material blocker determines that approval is impossible, "
            "but it does not end the substantive inspection",
            self.fresh_lower,
        )
        self.assertIn("fresh re-review after `/fix`", self.fresh_lower)
        self.assertIn(
            "derive and complete the full currently applicable decision-critical "
            "review surface again",
            self.fresh_lower,
        )
        self.assertIn("human-facing review concise", self.fresh_lower)


if __name__ == "__main__":
    unittest.main()
