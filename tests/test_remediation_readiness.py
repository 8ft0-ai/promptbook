import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ROOT / "prompts" / "workflows"
ENGINEERING = ROOT / "prompts" / "engineering"


class RemediationReadinessContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.router = (WORKFLOWS / "README.md").read_text(encoding="utf-8").lower()
        cls.fix = (
            ENGINEERING / "remediate-review-findings.md"
        ).read_text(encoding="utf-8").lower()
        cls.fresh = (
            WORKFLOWS / "fresh-independent-review.md"
        ).read_text(encoding="utf-8").lower()
        cls.root_readme = (ROOT / "README.md").read_text(encoding="utf-8").lower()
        cls.bootstrap = (
            ROOT / "guides" / "project-bootstrap.md"
        ).read_text(encoding="utf-8").lower()

    def test_enumerated_findings_are_not_the_exhaustive_readiness_surface(self):
        self.assertIn("findings are strong inputs but not the exhaustive search universe", self.fix)
        self.assertIn("actual resulting candidate and changed integration paths", self.fix)
        self.assertIn("repaired blocker list is not mistaken for a review-ready candidate", self.fix)

    def test_author_side_readiness_is_not_review_or_approval(self):
        for marker in (
            "remediation_readiness_sweep=complete",
            "never represent that author-side result as `approved`",
            "formal/independent review evidence",
        ):
            self.assertIn(marker, self.fix)
        self.assertIn("do not treat `remediation_readiness_sweep=complete`", self.fresh)
        self.assertIn("independently reconstruct the applicable review surface", self.fresh)

    def test_simple_local_fix_remains_proportionate(self):
        self.assertIn("a simple local fix with no meaningful sibling surface", self.fix)
        self.assertIn("lightweight adjacent caller/path inspection", self.fix)
        self.assertIn("do not manufacture a state machine or architecture matrix", self.fix)

    def test_configuration_and_contract_identity_escape_is_challenged(self):
        self.assertIn("caller-controlled/configurable state changes governed semantics", self.fix)
        self.assertIn("canonical output identity", self.fix)
        self.assertIn("substituted configuration", self.fix)

    def test_symmetric_uncertainty_is_challenged(self):
        self.assertIn("two sides/windows/records receive asymmetric uncertainty handling", self.fix)
        self.assertIn("what symmetric case reaches the same comparison", self.fix)
        self.assertIn("incomplete/unknown evidence on either side", self.fix)

    def test_alternate_integration_paths_are_challenged(self):
        self.assertIn("alternate production entry paths bypass the corrected helper/policy", self.fix)
        self.assertIn("what other production path implements or bypasses it", self.fix)
        self.assertIn("bypass paths", self.fix)

    def test_new_bounded_defect_stays_in_same_remediation_cycle(self):
        self.assertIn("correct it in the same remediation cycle", self.fix)
        self.assertIn("repeat required validation affected by the changed candidate", self.fix)
        self.assertIn("do not freeze candidate b until those affected challenges are satisfied", self.fix)

    def test_new_authority_or_design_boundary_stops_mutation(self):
        self.assertIn("stop mutation and return to response routing", self.fix)
        self.assertIn("broader product, architecture, security, scope, owner or other authority boundary", self.fix)

    def test_existing_escalation_precedes_and_wins_over_readiness_sweep(self):
        adjacent = self.router.index("before selecting ordinary `bounded_remediation`")
        readiness = self.router.index("once ordinary `bounded_remediation` is valid")
        self.assertLess(adjacent, readiness)
        for marker in (
            "repeated-review stateful escalation",
            "post-closure recurrence",
            "closure-method falsification",
            "`adjacent_model_omission`",
        ):
            self.assertIn(marker, self.router)
        self.assertIn("that stronger route wins", self.router)

    def test_candidate_identity_validation_and_fresh_boundary_are_bound_together(self):
        for marker in (
            "`findings_addressed`",
            "`required_validation_passed`",
            "`remediation_readiness_sweep_complete`",
            "`exact_resulting_candidate_frozen`",
            "`fresh_review_boundary_preserved`",
        ):
            self.assertIn(marker, self.router)
            self.assertIn(marker, self.fix)
        self.assertIn("resulting frozen candidate b identity", self.fix)
        self.assertIn("validation/evidence bound to b", self.fix)

    def test_public_fix_summaries_reflect_readiness_without_new_command(self):
        self.assertIn("challenge review-readiness proportionately", self.root_readme)
        self.assertIn("proportional author-side remediation-readiness sweep", self.bootstrap)
        self.assertNotIn("/readiness", self.root_readme)
        self.assertNotIn("/readiness", self.bootstrap)


if __name__ == "__main__":
    unittest.main()
