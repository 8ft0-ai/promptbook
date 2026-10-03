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
        cls.run_context = (
            WORKFLOWS / "resolved-agent-run-context.md"
        ).read_text(encoding="utf-8").lower()
        cls.autonomous = (
            WORKFLOWS / "autonomous-progression.md"
        ).read_text(encoding="utf-8").lower()
        cls.go_lifecycle = (
            ROOT / "guides" / "go-lifecycle.md"
        ).read_text(encoding="utf-8").lower()
        cls.foreground = (
            WORKFLOWS / "foreground-execution-resilience.md"
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
        self.assertIn("bounded sibling defect discovered by the sweep", self.router)
        self.assertIn("still attributable to the resolved remediation scope", self.router)
        self.assertIn("not an exhaustive search universe for the readiness sweep", self.fresh)
        self.assertIn("independently passes the `/fix` action gateway as `allow`", self.fresh)

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
        self.assertIn("starting candidate identity (candidate a)", self.fix)
        self.assertIn("resulting candidate identity (frozen candidate b)", self.fix)
        self.assertIn("validation/evidence bound to the resulting candidate b", self.fix)

    def test_canonical_run_context_owns_readiness_transition(self):
        candidate = self.run_context.index("→ provisional candidate b0")
        validation = self.run_context.index("→ b0-bound required validation")
        readiness = self.run_context.index("→ proportional remediation-readiness sweep")
        freeze = self.run_context.index(
            "→ exact final candidate b frozen only with current b-bound validation + readiness evidence"
        )
        fresh = self.run_context.index(
            "→ fresh-review boundary or other correct governed next state"
        )
        self.assertLess(candidate, validation)
        self.assertLess(validation, readiness)
        self.assertLess(readiness, freeze)
        self.assertLess(freeze, fresh)
        for marker in (
            "remediation_readiness_requirements",
            "fresh_review_boundary_requirement",
            "remediation_readiness_surface_and_evidence",
            "remediation_readiness_sweep_complete",
            "exact_resulting_candidate_frozen",
            "fresh_review_boundary_preserved",
        ):
            self.assertIn(marker, self.run_context)

    def test_sweep_discovered_mutation_rebinds_final_candidate_evidence(self):
        for marker in (
            "invalidates affected prior validation/readiness evidence",
            "requires affected validation and readiness challenges to be repeated",
            "freeze `resulting_candidate_identity` only after the current exact candidate",
            "current required validation and a completed readiness sweep",
        ):
            self.assertIn(marker, self.run_context)
        self.assertIn(
            "still attributable to the resolved remediation scope",
            self.run_context,
        )
        self.assertIn(
            "independently passes the action gateway as `allow`",
            self.run_context,
        )

    def test_go_progression_cannot_skip_readiness_before_fresh_review(self):
        for surface in (self.autonomous, self.go_lifecycle):
            self.assertIn("remediation-readiness sweep", surface)
        scenario = self.go_lifecycle.split(
            "### 2. review changes required, bounded remediation, fresh re-review", 1
        )[1].split("### 3.", 1)[0]
        go_fix = scenario.index("/fix produces provisional candidate b0")
        go_validation = scenario.index(
            "required validation bound to current provisional candidate"
        )
        go_readiness = scenario.index(
            "proportional author-side remediation-readiness sweep"
        )
        go_freeze = scenario.index(
            "freeze exact final candidate b only when validation + readiness evidence are current for b"
        )
        go_review = scenario.index(
            "resolve eligible isolated fresh-review context"
        )
        self.assertLess(go_fix, go_validation)
        self.assertLess(go_validation, go_readiness)
        self.assertLess(go_readiness, go_freeze)
        self.assertLess(go_freeze, go_review)
        self.assertIn(
            "complete the proportional author-side remediation-readiness sweep",
            self.autonomous,
        )

    def test_foreground_recovery_cannot_recreate_review_eligibility(self):
        self.assertIn(
            "not the semantic owner of review-readiness or fresh-review eligibility",
            self.foreground,
        )
        recovered = self.foreground.index("exact candidate c recovered")
        assurance = self.foreground.index("applicable assurance resumed for c", recovered)
        lifecycle = self.foreground.index(
            "governing operation establishes its own next eligible lifecycle state",
            assurance,
        )
        fresh = self.foreground.index(
            "genuinely fresh review boundary reached only when that governing lifecycle establishes fresh-review eligibility",
            lifecycle,
        )
        self.assertLess(recovered, assurance)
        self.assertLess(assurance, lifecycle)
        self.assertLess(lifecycle, fresh)
        for marker in (
            "required validation",
            "remediation-readiness requirements",
            "affected evidence rebinding",
            "exact final-candidate freeze",
        ):
            self.assertIn(marker, self.foreground)
        self.assertIn(
            "reconstruct the outstanding `/fix` assurance from the canonical resolved agent run context",
            self.fix,
        )
        self.assertIn(
            "foreground recovery does not independently establish review-readiness or fresh-review eligibility",
            self.autonomous,
        )

    def test_public_fix_summaries_reflect_readiness_without_new_command(self):
        self.assertIn("challenge review-readiness proportionately", self.root_readme)
        self.assertIn("proportional author-side remediation-readiness sweep", self.bootstrap)
        self.assertNotIn("/readiness", self.root_readme)
        self.assertNotIn("/readiness", self.bootstrap)


if __name__ == "__main__":
    unittest.main()
