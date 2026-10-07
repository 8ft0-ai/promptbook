import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / "prompts" / "workflows" / "bounded-concern-lifecycle.md"


class BoundedConcernLifecycleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = WORKFLOW.read_text(encoding="utf-8")
        cls.lower = cls.text.lower()

    def test_bounded_not_universal(self):
        for marker in ("does not establish an exhaustive concern universe", "universal semantic primitive", "dependency completeness", "new_concern"):
            self.assertIn(marker, self.lower)

    def test_review_routing_fails_closed(self):
        self.assertIn("fresh substantive review owns", self.lower)
        self.assertIn("correction eligibility is ambiguous", self.lower)
        self.assertIn("route fail-closed to gd", self.lower)
        self.assertIn("author evidence may inform but cannot downgrade", self.lower)

    def test_correction_invalidates_all_declared_concern_evidence(self):
        self.assertIn("invalidates the old review_package", self.lower)
        self.assertIn("invalidate every frozen declared concern result", self.lower)
        self.assertIn("rerun every frozen concern", self.lower)
        self.assertIn("all concern-closure inputs and outputs are unchanged", self.lower)

    def test_budgets_are_monotone(self):
        self.assertIn("author_correction_allowance=1", self.lower)
        self.assertIn("post_review_correction_allowance=1", self.lower)
        self.assertIn("generation-owned monotone values", self.lower)
        self.assertIn("never restored", self.lower)

    def test_concern_register_contract_is_explicit(self):
        for marker in (
            "concern identifier/name",
            "decision-critical claim",
            "authoritative source/owner",
            "applicability rationale",
            "explicit exclusions",
            "required evidence outputs",
            "closure disposition",
            "reconstruction inputs",
        ):
            self.assertIn(marker, self.lower)

    def test_concern_contract_interface_is_explicit(self):
        for marker in (
            "finite obligation/output set",
            "closure criterion",
            "evidence required to reconstruct",
            "correction boundary",
            "conditions that constitute scope/assurance/authority movement",
        ):
            self.assertIn(marker, self.lower)

    def test_review_package_manifest_and_admission_are_explicit(self):
        for marker in (
            "review_package manifest",
            "exact candidate/review target",
            "required inputs",
            "advertised author-side outputs/results",
            "every required locator to resolve",
            "integrity identities to match",
            "required inputs/outputs to be present",
            "regenerated/recomputed outputs to match",
            "review_package_reproducible=false",
            "s5 is unreachable",
        ):
            self.assertIn(marker, self.lower)

    def test_negative_outcomes_exist_before_terminal(self):
        self.assertIn("generation-lifetime append-only outcome_record", self.lower)
        self.assertIn("append the gd event before active progression stops", self.lower)
        self.assertIn("negative, null, abandoned, decomposed, and non-convergent outcomes", self.lower)

    def test_outcome_record_retains_reconstructable_configuration_and_history(self):
        for marker in (
            "generation and predecessor identities",
            "case_id",
            "frozen objective/assurance and concern_register identities",
            "concern count and concern_contract identities",
            "author-side defects and correction consumption",
            "admission attempts/failures",
            "fresh-review identities, findings and routing classifications",
            "post-review correction attempts",
            "gd trigger and consumed allowances",
            "fresh-review count",
            "effort proxy and lifecycle timestamps",
            "pending/terminal governing disposition",
            "final governing disposition",
        ):
            self.assertIn(marker, self.lower)

    def test_case_identity_cannot_be_reset_by_lifecycle_labels(self):
        self.assertIn("separately governed pilot case-selection", self.lower)
        self.assertIn("inherits the case_id", self.lower)
        self.assertIn("cannot create a new case_id", self.lower)
        self.assertIn("preserve continuity", self.lower)

    def test_admission_is_not_approval(self):
        self.assertIn("review_package_reproducible only", self.lower)
        self.assertIn("it is not correctness", self.lower)

    def test_external_ownership_and_authority_boundaries(self):
        self.assertIn("concern-contract semantic ownership external", self.lower)
        self.assertIn("creates no implementation, pr, merge", self.lower)
        self.assertIn("does not add a public command", self.lower)


if __name__ == "__main__":
    unittest.main()
