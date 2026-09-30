import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ROOT / "prompts" / "workflows"
ENGINEERING = ROOT / "prompts" / "engineering"


class ArchitectureClosureCompletenessTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.closure = (WORKFLOWS / "architecture-closure-analysis.md").read_text(encoding="utf-8")
        cls.closure_lower = cls.closure.lower()
        cls.router = (WORKFLOWS / "README.md").read_text(encoding="utf-8")
        cls.router_lower = cls.router.lower()
        cls.analysis = (WORKFLOWS / "stateful-invariant-analysis.md").read_text(encoding="utf-8")
        cls.analysis_lower = cls.analysis.lower()
        cls.fix = (ENGINEERING / "remediate-review-findings.md").read_text(encoding="utf-8")
        cls.fix_lower = cls.fix.lower()
        cls.review = (WORKFLOWS / "fresh-independent-review.md").read_text(encoding="utf-8")
        cls.review_lower = cls.review.lower()

    def test_closure_universe_is_independent_of_candidate_model(self):
        self.assertIn("derive a bounded **source/obligation universe** independently", self.closure_lower)
        self.assertIn("do not define the closure universe by reading the candidate", self.closure_lower)
        self.assertIn("completeness requires evidence that the closure universe itself contains", self.closure_lower)
        self.assertIn("authoritative inputs for this decision", self.closure_lower)

    def test_source_obligation_universe_has_total_source_to_primitive_coverage(self):
        self.assertIn("closed source/obligation universe", self.closure_lower)
        self.assertIn("total source → primitive coverage", self.closure_lower)
        self.assertIn(
            "applicable_source_obligation_without_primitive_count = 0",
            self.closure_lower,
        )
        self.assertIn(
            "primitive_without_source_or_derivation_basis_count = 0",
            self.closure_lower,
        )
        self.assertIn("candidate silence never closes an obligation", self.closure_lower)
        self.assertIn("source → primitive completeness is mandatory", self.closure_lower)

    def test_primitive_classification_is_closed_and_unambiguous(self):
        self.assertIn(
            "exactly one **primary role** from this closed partition",
            self.closure_lower,
        )
        self.assertIn("secondary annotations may be used", self.closure_lower)
        self.assertIn(
            "must not replace the single primary classification",
            self.closure_lower,
        )

    def test_five_inventories_and_extensional_ownership_are_required(self):
        for marker in (
            "five explicit closure inventories",
            "same possible irreversible governed real-world consequence",
            "same_consequence",
            "disjoint_consequences",
            "opaque provenance fields are not proof of extensional ownership",
        ):
            self.assertIn(marker, self.closure_lower)

    def test_authority_freshness_is_cross_bound_to_state_revision(self):
        for marker in (
            "state/revision/epoch/freshness predicate",
            "authoritative state movement invalidates",
            "returning later to a semantically similar state must not revive stale authority",
            "authority freshness/state binding",
            "stale-authority revival",
            "stale authority survives authoritative movement",
        ):
            self.assertIn(marker, self.closure_lower)
        self.assertIn("state-sensitive authority", self.review_lower)
        self.assertIn("revive stale authority", self.review_lower)

    def test_extensional_authority_and_effect_challenge_families_are_pinned(self):
        for marker in (
            "cardinality",
            "consumption/reissue",
            "replay/substitution",
            "idempotency key",
            "replacement candidates",
            "retries/reissues",
            "multiple executors",
            "protocol revisions",
            "direct versus migration paths",
        ):
            self.assertIn(marker, self.closure_lower)
        self.assertIn("for every pair of admissible effect paths", self.closure_lower)
        self.assertIn("same_consequence", self.closure_lower)
        self.assertIn("disjoint_consequences", self.closure_lower)

    def test_omitted_applicable_source_obligation_blocks_ready(self):
        self.assertIn(
            "omitted source obligation with internally valid primitives",
            self.closure_lower,
        )
        self.assertIn(
            "the analysis must return `architecture_closure_not_ready`",
            self.closure_lower,
        )
        self.assertIn(
            "it must not infer completeness from the listed primitives",
            self.closure_lower,
        )
        self.assertIn(
            "primitive → source traceability is not evidence of source → primitive completeness",
            self.review_lower,
        )

    def test_closure_model_has_required_global_dimensions(self):
        for marker in (
            "closed source/obligation universe",
            "decision-critical primitive universe",
            "five explicit closure inventories",
            "global identity-dependency dag",
            "ownership / state / transition matrix",
            "positive reachability witnesses",
            "end-to-end authority/effect matrix",
            "observation / ambiguity / crash-recovery matrix",
            "equivalence / overlap / symmetry proofs",
            "terminal provenance matrix",
            "migration / fence matrix when applicable",
        ):
            self.assertIn(marker, self.closure_lower)

    def test_global_identity_closure_requires_one_acyclic_construction_order(self):
        for marker in (
            "one graph covering every identity-bearing/content-addressed object",
            "no direct or indirect dependency",
            "one deterministic topological construction order",
            "locally valid object definitions that compose into a global cycle",
        ):
            self.assertIn(marker, self.closure_lower)

    def test_positive_reachability_rejects_vacuous_safety(self):
        self.assertIn("at least one valid witness path from an admitted initial state", self.closure_lower)
        self.assertIn("reject vacuous safety claims", self.closure_lower)
        self.assertIn("repair semantics whose preconditions can never be satisfied", self.closure_lower)

    def test_effect_closure_reaches_external_consequence_and_recovery(self):
        for marker in (
            "external system boundary",
            "lost-response / ambiguous-result handling",
            "authoritative terminal projection",
            "internal state closure is not end-to-end effect closure",
            "crash-after-effect-before-result",
            "retry after ambiguous outcome",
        ):
            self.assertIn(marker, self.closure_lower)

    def test_equivalence_and_terminal_provenance_are_normative(self):
        self.assertIn("require a normative proof/witness/validator contract", self.closure_lower)
        self.assertIn("a prose assertion of equivalence or disjointness is not closure evidence", self.closure_lower)
        self.assertIn("every terminal state must identify the exact durable result/outcome provenance", self.closure_lower)

    def test_closure_dispositions_distinguish_model_error_from_method_failure(self):
        for marker in (
            "architecture_closure_ready",
            "architecture_closure_not_ready",
            "closure_method_falsified",
            "modelled_but_wrong",
            "unmodelled_decision_critical_primitive",
        ):
            self.assertIn(marker, self.closure_lower)
        self.assertIn("do not falsify the closure method merely because a represented primitive is wrong", self.closure_lower)

    def test_closure_method_falsification_requires_reconstruction_and_blocks_fix(self):
        for marker in (
            "closure_method_falsified",
            "architecture_closure_reconstruction_required",
            "ordinary isolated",
            "do not merely append the newly discovered primitive to prose",
        ):
            self.assertIn(marker, self.closure_lower)
        self.assertIn("ordinary isolated", self.fix_lower)
        self.assertIn("return control to the router", self.fix_lower)

    def test_reconstruction_is_separate_authority_and_one_shot(self):
        self.assertIn("is a separate-authority boundary", self.closure_lower)
        self.assertIn("does not silently become unlimited authority to rerun closure reconstruction", self.closure_lower)
        self.assertIn("perform exactly one fresh closure reconstruction", self.closure_lower)
        self.assertIn("do not loop into repeated reconstruction while it remains current", self.router_lower)

    def test_first_closure_proof_lives_inside_authorised_reconsideration(self):
        self.assertIn("if that authorised architecture reconsideration needs to establish architecture closure", self.analysis_lower)
        self.assertIn("architecture closure analysis", self.analysis_lower)
        self.assertIn("within the same one-shot read-only reconsideration authority", self.analysis_lower)
        self.assertIn("the architecture-closure proof is part of the current one-shot read-only reconsideration", self.router_lower)

    def test_review_attacks_internal_correctness_and_universe_completeness(self):
        self.assertIn("independently review **internal model correctness**, **source-universe completeness**, and **source → primitive/model coverage**", self.review_lower)
        self.assertIn("first attempt to identify an applicable authoritative obligation", self.review_lower)
        self.assertIn("source → primitive completeness", self.review_lower)
        self.assertIn("must not inherit", self.closure_lower)
        self.assertIn("source/obligation universe or primitive universe is complete", self.closure_lower)
        self.assertIn("modelled_but_wrong", self.review_lower)
        self.assertIn("unmodelled_decision_critical_primitive", self.review_lower)

    def test_fix_requires_finding_model_and_parent_non_regression_closure(self):
        for marker in ("finding_closure", "model_closure", "parent_non_regression"):
            self.assertIn(marker, self.fix_lower)
        self.assertIn("patching all reported findings is not enough to claim architecture closure", self.fix_lower)

    def test_regression_examples_cover_gitstate_failure_classes(self):
        for marker in (
            "global identity cycle hidden by locally valid objects",
            "unmodelled external effect",
            "missing durable authority binding",
            "stale authority survives authoritative movement",
            "missing equivalence proof",
            "missing terminal provenance",
            "modelled local defect",
            "new requirement after closure",
        ):
            self.assertIn(marker, self.closure_lower)

    def test_negative_cases_do_not_automatically_falsify_closure_method(self):
        for marker in (
            "new governing requirement became applicable later",
            "materially new architecture scope was introduced later",
            "genuinely unrelated defect family appears",
            "non-substantive check/test fails",
        ):
            self.assertIn(marker, self.closure_lower)

    def test_router_exposes_falsification_before_fix(self):
        self.assertIn("fresh review establishes", self.router_lower)
        self.assertIn("closure_method_falsified", self.router_lower)
        self.assertIn("architecture_closure_reconstruction_required", self.router_lower)
        self.assertIn("stops without remediation mutation", self.router_lower)


if __name__ == "__main__":
    unittest.main()
