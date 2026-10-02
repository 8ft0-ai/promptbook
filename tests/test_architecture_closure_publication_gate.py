import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ROOT / "prompts" / "workflows"
ENGINEERING = ROOT / "prompts" / "engineering"


class ArchitectureClosurePublicationGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.closure = (WORKFLOWS / "architecture-closure-analysis.md").read_text(encoding="utf-8").lower()
        cls.router = (WORKFLOWS / "README.md").read_text(encoding="utf-8").lower()
        cls.analysis = (WORKFLOWS / "stateful-invariant-analysis.md").read_text(encoding="utf-8").lower()
        cls.review = (WORKFLOWS / "fresh-independent-review.md").read_text(encoding="utf-8").lower()
        cls.plan = (ENGINEERING / "plan-an-issue.md").read_text(encoding="utf-8").lower()
        cls.implement = (ENGINEERING / "implement-an-approved-issue.md").read_text(encoding="utf-8").lower()
        cls.fix = (ENGINEERING / "remediate-review-findings.md").read_text(encoding="utf-8").lower()

    def test_a_proactive_trigger_requires_material_risk_and_strong_completeness(self):
        self.assertIn("the proactive trigger is conjunctive", self.closure)
        for marker in (
            "irreversible-effect",
            "migration/cutover-sensitive",
            "closed-world",
            "architecture-closed",
            "closure-ready",
            "equivalent strong completeness claim",
        ):
            self.assertIn(marker, self.closure)
        self.assertIn("both conditions are established", self.router)
        self.assertIn("before closure-ready candidate authoring/publication", self.router)

    def test_b_current_independent_closure_artefact_precedes_candidate_and_review(self):
        self.assertIn(
            "governing sources\n→ source/obligation universe\n→ primitive universe\n→ closure artefact\n→ closure-ready candidate",
            self.closure,
        )
        self.assertIn("current independently derived", self.implement)
        self.assertIn("consume/project that artefact into the candidate", self.implement)
        self.assertIn("genuinely fresh substantive review remains a separate challenge boundary", self.closure)

    def test_c_ordinary_architecture_draft_does_not_trigger_heavyweight_closure(self):
        for marker in (
            "ordinary bounded design",
            "exploratory proposals",
            "explicitly modelled-but-incomplete drafts",
        ):
            self.assertIn(marker, self.closure)
        self.assertIn("ordinary exploratory", self.review)
        self.assertIn("solely because architecture/security terminology appears", self.review)

    def test_d_local_simple_design_remains_proportionate(self):
        self.assertIn("local architecture decisions", self.closure)
        self.assertIn("bounded local design", self.plan)
        self.assertIn("must not be forced through this gate", self.plan)

    def test_e_scope_movement_stales_coverage_but_local_modelled_change_can_reuse(self):
        for marker in (
            "material movement",
            "invalidates the affected closure evidence",
            "requires refresh or rederivation before publication",
            "local correction wholly inside an already-modelled primitive",
        ):
            self.assertIn(marker, self.closure)
        self.assertIn("newly introduced decision-critical primitive", self.fix)
        self.assertIn("do not mechanically force full closure reconstruction for every candidate edit", self.fix)

    def test_f_omitted_primitive_preserves_closure_method_falsification(self):
        for marker in (
            "unmodelled_decision_critical_primitive",
            "closure_method_falsified",
            "architecture_closure_reconstruction_required",
        ):
            self.assertIn(marker, self.closure)
            self.assertIn(marker, self.review)

    def test_g_modelled_local_defect_does_not_automatically_falsify_method(self):
        self.assertIn("modelled_but_wrong", self.closure)
        self.assertIn(
            "does not automatically establish `closure_method_falsified`",
            self.closure,
        )
        self.assertIn("modelled local defect", self.review)
        self.assertIn("does not by itself falsify the closure method", self.review)

    def test_publication_gate_requires_explicit_zero_or_true_closure_evidence(self):
        for marker in (
            "applicable_source_obligation_without_primitive_count = 0",
            "primitive_without_source_or_derivation_basis_count = 0",
            "undeclared_decision_critical_reference_count = 0",
            "unconstructable_identity_count = 0",
            "undeclared_state_count = 0",
            "authority_without_issuer_or_provenance_count = 0",
            "state_sensitive_authority_without_freshness_binding_count = 0",
            "irreversible_effect_without_claim_result_recovery_count = 0",
            "terminal_state_without_exact_provenance_count = 0",
            "unreachable_advertised_capability_count = 0",
            "unproved_consequence_overlap_count = 0",
        ):
            self.assertIn(marker, self.closure)

    def test_planning_and_authoring_cannot_reconstruct_completeness_from_candidate_prose(self):
        self.assertIn("pre-authoring dependency", self.plan)
        self.assertIn("governing sources → closure artefact → candidate → fresh review", self.plan)
        self.assertIn("do not plan to infer the completeness universe from candidate prose", self.plan)
        self.assertIn("do not reconstruct the completeness universe from candidate prose", self.implement)

    def test_proactive_and_reactive_entry_paths_share_method_without_collapsing_lineage(self):
        self.assertIn("proactive architecture-closure publication gate", self.router)
        self.assertIn("closure_method_falsified", self.router)
        self.assertIn("architecture_reconsideration_required", self.router)
        self.assertIn("reactive architecture-governance branch", self.analysis)
        self.assertIn("both entry paths share the same closure method", self.analysis)
        self.assertIn(
            "do not manufacture repeated-review, closure-falsification or architecture-reconsideration lineage",
            self.analysis,
        )


if __name__ == "__main__":
    unittest.main()
