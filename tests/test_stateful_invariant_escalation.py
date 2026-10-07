import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ROOT / "prompts" / "workflows"
ENGINEERING = ROOT / "prompts" / "engineering"


class StatefulInvariantEscalationContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.router = (WORKFLOWS / "README.md").read_text(encoding="utf-8")
        cls.router_lower = cls.router.lower()
        cls.analysis = (WORKFLOWS / "stateful-invariant-analysis.md").read_text(
            encoding="utf-8"
        )
        cls.analysis_lower = cls.analysis.lower()
        cls.fresh = (WORKFLOWS / "fresh-independent-review.md").read_text(
            encoding="utf-8"
        )
        cls.fresh_lower = cls.fresh.lower()
        cls.fix = (
            ENGINEERING / "remediate-review-findings.md"
        ).read_text(encoding="utf-8")
        cls.fix_lower = cls.fix.lower()
        cls.index = (ROOT / "prompts" / "README.md").read_text(encoding="utf-8")
        cls.root_readme = (ROOT / "README.md").read_text(encoding="utf-8")

    def test_stateful_analysis_is_indexed_read_only_and_proportionate(self):
        self.assertIn(
            "workflows/stateful-invariant-analysis.md",
            self.index,
        )
        self.assertIn("read-only stateful/invariant analysis", self.analysis_lower)
        self.assertIn(
            "materially stateful, lifecycle-sensitive, cross-component",
            self.analysis_lower,
        )
        self.assertIn(
            "do not impose this workflow on a simple local defect",
            self.analysis_lower,
        )
        self.assertIn("creates no mutation", self.analysis_lower)
        self.assertIn("does not create a new lifecycle stage", self.router_lower)

    def test_router_requires_two_materially_related_review_rounds(self):
        self.assertIn("### Repeated-review stateful escalation", self.router)
        for marker in (
            "substantive review round **r1**",
            "authorised remediation changed the candidate",
            "genuinely fresh substantive review round **r2**",
            "same behavioural/invariant domain **x**",
        ):
            self.assertIn(marker, self.router_lower)
        self.assertIn(
            "do not route directly to another narrow `/fix`",
            self.router_lower,
        )
        self.assertIn(
            "[stateful invariant analysis](stateful-invariant-analysis.md)",
            self.router_lower,
        )

    def test_router_rejects_false_escalation_triggers(self):
        for marker in (
            "two blockers in one substantive review",
            "duplicate/repeated review against unchanged bytes that adds no new substantive same-family blocker",
            "materially unrelated r1/r2 domains",
            "governing requirement that became applicable only after r1",
            "duplicate review records of one substantive adjudication",
            "non-substantive check/test failure by itself",
        ):
            self.assertIn(marker, self.router_lower)
        self.assertIn(
            "a later genuinely fresh substantive review may still expose a new material "
            "blocker on unchanged bytes",
            self.router_lower,
        )

    def test_escalation_is_process_not_redesign_authority(self):
        self.assertIn("process-driven rather than conclusion-driven", self.router_lower)
        self.assertIn("does not establish that an abstraction is unsound", self.router_lower)
        self.assertIn("does not authorise redesign", self.router_lower)
        self.assertIn("does not widen `/fix`", self.router_lower)
        self.assertIn("creates no mutation or later lifecycle authority", self.router_lower)
        self.assertIn(
            "creates no mutation, approval, merge, release, deployment, credential, "
            "production or other consequential authority",
            self.analysis_lower,
        )
        self.assertIn(
            "does not widen the `/fix` action gateway",
            self.fix_lower,
        )

    def test_analysis_binding_and_post_closure_lineage_are_explicit(self):
        for marker in (
            "current exact candidate",
            "r1 and r2 review identities and dispositions",
            "materially related blocker set or behavioural/invariant domain",
            "current governing contract",
        ):
            self.assertIn(marker, self.analysis_lower)
        self.assertIn(
            "candidate or governing contract moves materially",
            self.analysis_lower,
        )
        self.assertIn(
            "historical `invariant_closure_attempted(x)` lineage remains reconstructable",
            self.analysis_lower,
        )
        self.assertIn("closure_survived_this_review", self.analysis_lower)
        self.assertIn("closure falsification/post-closure recurrence", self.analysis_lower)
        self.assertNotIn(
            "the next genuinely fresh substantive review starts a new failure sequence",
            self.analysis_lower,
        )
        self.assertNotIn(
            "two further materially related failed review/remediation rounds",
            self.router_lower,
        )

    def test_post_closure_recurrence_routes_to_architecture_reconsideration(self):
        for marker in (
            "invariant_closure_attempted(x)",
            "closure_survived_this_review",
            "post-closure same-family recurrence",
            "architecture_reconsideration_required",
            "ordinary `/fix` ineligible",
        ):
            self.assertIn(marker, self.router_lower)
        self.assertIn(
            "the relevant x invariant/surface remained materially within the prior closure attempt",
            self.router_lower,
        )
        self.assertIn(
            "belongs to the same defect family covered by x's invariant-closure attempt",
            self.router_lower,
        )
        self.assertIn(
            "same broader behavioural/invariant domain x that is independently classified "
            "as a new defect family does not falsify closure",
            self.router_lower,
        )

    def test_structural_post_closure_recurrence_routes_to_governing_disposition_first(self):
        self.assertIn(
            "if the same-family recurrence is independently established as `equivalent_same_family_structural_falsification`",
            self.router_lower,
        )
        self.assertIn(
            "the structural classification takes precedence over the generic recurrence route",
            self.router_lower,
        )
        self.assertIn(
            "route the current strong-closure generation to `governing_disposition_required`, not directly to `architecture_reconsideration_required`",
            self.router_lower,
        )
        self.assertIn(
            "do not enter this architecture-reconsideration branch merely because a recurrence is also a structural falsification",
            self.analysis_lower,
        )
        self.assertIn(
            "the structural route takes precedence: stop at `governing_disposition_required` rather than entering architecture reconsideration",
            self.fix_lower,
        )

    def test_adjacent_model_omission_blocks_fix_until_model_closure(self):
        for marker in (
            "adjacent_model_omission",
            "omitted a necessary semantic owner",
            "ordinary `/fix` is ineligible",
            "bounded transition/adversarial matrix",
            "positive reachability",
            "one encompassing remediation plan",
        ):
            self.assertIn(marker, self.router_lower)
        self.assertIn(
            "canonical_multi_owner_intent_model",
            self.analysis_lower,
        )
        self.assertIn(
            "adversarial_interleaving_matrix",
            self.analysis_lower,
        )
        self.assertIn(
            "also stop before material mutation",
            self.fix_lower,
        )
        self.assertIn(
            "genuinely independent new defect families",
            self.fix_lower,
        )
        self.assertIn(
            "adjacent_model_omission",
            self.fresh_lower,
        )
        self.assertIn(
            "adjacency, shared terminology or finding count alone is insufficient",
            self.fresh_lower,
        )

    def test_adjacent_model_challenge_precedes_bounded_remediation_without_prior_closure(self):
        synthesis_start = self.router_lower.index(
            "when a completed review exposes `changes required`"
        )
        bounded_start = self.router_lower.index(
            "when response synthesis selects `bounded_remediation`"
        )
        synthesis_gate = self.router_lower[synthesis_start:bounded_start]
        for marker in (
            "adjacent_model_omission",
            "immediately preceding remediation",
            "did not represent",
            "can change correctness beyond the named reproduction or local predicate",
            "risk continuing an example-by-example review/fix loop",
            "does not require a prior r1/r2 invariant-closure attempt or post-closure lineage",
            "do not select ordinary `bounded_remediation` or route directly to `/fix`",
        ):
            self.assertIn(marker, synthesis_gate)
        self.assertIn(
            "whether or not a prior r1/r2 invariant-closure attempt exists",
            self.router_lower,
        )

    def test_architecture_reconsideration_requires_authority_and_has_one_shot_satisfaction(self):
        for marker in (
            "separate-authority boundary",
            "does not separately authorise the bounded read-only architecture reconsideration",
            "must surface `decision_required` rather than enter analysis",
            "no current architecture-reconsideration record already satisfies the bound recurrence",
            "architecture_reconsideration_completed",
            "do not re-enter architecture reconsideration while that record remains current",
        ):
            self.assertIn(marker, self.router_lower)
        self.assertIn(
            "require and bind a separately governed authority source",
            self.analysis_lower,
        )
        self.assertIn(
            "do not themselves supply that authority",
            self.analysis_lower,
        )
        self.assertIn(
            "satisfies the architecture-reconsideration analysis gate",
            self.analysis_lower,
        )
        self.assertIn(
            "do not repeat or re-enter the reconsideration while the record remains current",
            self.analysis_lower,
        )
        self.assertIn(
            "authority to perform the read-only architecture reconsideration is not remediation authority",
            self.fix_lower,
        )
        self.assertIn(
            "require a new candidate-bound remediation plan derived from the architecture result",
            self.fix_lower,
        )

    def test_regression_is_distinguished_from_post_closure_recurrence(self):
        self.assertIn(
            "intervening regression that demonstrably broke an already-established x contract",
            self.router_lower,
        )
        self.assertIn(
            "use the regression/restoration path",
            self.fix_lower,
        )
        self.assertIn(
            "new defect families, unrelated domains, newly applicable governing requirements "
            "and materially out-of-boundary changes",
            self.fix_lower,
        )

    def test_architecture_reconsideration_is_read_only_and_not_fix_authority(self):
        self.assertIn(
            "treat it as explicit architecture reconsideration",
            self.analysis_lower,
        )
        self.assertIn(
            "recurrence alone does not prove that it is",
            self.analysis_lower,
        )
        self.assertIn(
            "architecture reconsideration is read-only analysis/decision evidence",
            self.analysis_lower,
        )
        self.assertIn(
            "ordinary `/fix` is ineligible",
            self.fix_lower,
        )
        self.assertIn(
            "a previous invariant-closure analysis/remediation plan does not satisfy either stronger boundary",
            self.fix_lower,
        )

    def test_stateful_fix_requires_semantic_and_failure_recovery_completeness(self):
        for marker in (
            "codebase-wide decision-critical surface",
            "related call sites",
            "duplicated raw predicates",
            "policy bypasses",
            "failure/recovery matrix",
            "materially adjacent state transitions",
            "repeated or prolonged failure behaviour",
            "production integration paths",
            "sanitizer or runtime evidence",
            "state explicitly which material surface remains untested",
        ):
            self.assertIn(marker, self.fix_lower)
        self.assertIn(
            "do not perform another `/fix` until a current "
            "[stateful invariant analysis]",
            self.fix_lower,
        )

    def test_explicit_stateful_analyse_precedes_pending_review_route(self):
        routing = self.router.split("## Routing", 1)[1]
        analysis_route = (
            "2. **Mandatory architecture/stateful analysis is required now**"
        )
        review_route = "3. **An independent substantive review is required now**"
        self.assertLess(routing.index(analysis_route), routing.index(review_route))
        routing_lower = routing.lower()
        self.assertIn(
            "explicit read-only `/analyse` request is resolved before an otherwise "
            "pending independent-review lifecycle gate",
            routing_lower,
        )
        self.assertIn(
            "does not discharge, bypass, weaken, or satisfy that review gate",
            routing_lower,
        )

    def test_closure_method_falsification_routes_before_fix(self):
        for marker in (
            "closure_method_falsified",
            "governing_disposition_required",
            "unmodelled_decision_critical_primitive",
            "separate-authority boundary",
        ):
            self.assertIn(marker, self.router_lower)
        self.assertIn(
            "architecture closure analysis",
            self.analysis_lower,
        )
        self.assertIn(
            "ordinary isolated `/fix` is ineligible",
            self.fix_lower,
        )

    def test_fix_consumes_analysis_plan_as_authoritative_synthesis_input(self):
        self.assertIn(
            "consume its bounded remediation plan as the authoritative synthesis "
            "input to `/fix`",
            self.fix_lower,
        )
        self.assertIn(
            "the analysis-produced plan supersedes that earlier plan",
            self.fix_lower,
        )
        self.assertIn(
            "stale-plan, scope, action-gateway and authority checks",
            self.fix_lower,
        )
        self.assertIn("bounded remediation plan", self.analysis_lower)

    def test_fresh_review_covers_stateful_integration_without_universal_checklist(self):
        for marker in (
            "production integration paths",
            "stale and in-flight completion behaviour",
            "partial-success and incomplete-result behaviour",
            "failure/retry/recovery paths",
            "duplicated raw conditions or policy bypasses",
            "new failure handling introduced by remediation",
            "evidence required to justify negative inference",
        ):
            self.assertIn(marker, self.fresh_lower)
        self.assertIn(
            "not a universal state-machine checklist for every review",
            self.fresh_lower,
        )
        self.assertIn(
            "closing the previous blocker is necessary evidence but is not equivalent",
            self.fresh_lower,
        )

    def test_review_records_enough_domain_and_closure_evidence_for_later_routing(self):
        self.assertIn(
            "retain enough concise relationship evidence to reconstruct its behavioural/invariant domain",
            self.fresh_lower,
        )
        for marker in (
            "a new defect family",
            "same-family recurrence before invariant closure",
            "regression of an already-established contract",
            "post-closure same-family recurrence",
            "relevant prior invariant-closure attempt",
            "pertinent invariant/surface remained materially within that closure boundary",
        ):
            self.assertIn(marker, self.fresh_lower)
        self.assertIn(
            "must not inherit an author-side conclusion",
            self.fresh_lower,
        )
        self.assertIn(
            "must not turn finding count or historical closure lineage into an automatic abstraction diagnosis",
            self.fresh_lower,
        )

    def test_worked_wireless_example_covers_required_failure_family(self):
        for marker in (
            "wireless observation interface",
            "scan completeness",
            "absence or disappearance is inferred only from a complete authoritative observation",
            "stale scan completing after the pause",
            "repeated failed scans",
            "duplicate expiry or inference predicates",
        ):
            self.assertIn(marker, self.analysis_lower)

    def test_analyse_remains_compatibility_only_not_public_command(self):
        self.assertIn("## Compatibility intents", self.router)
        self.assertIn(
            "/analyse [target]` — read-only analysis/synthesis intent",
            self.router_lower,
        )
        quick = self.root_readme.split("## Quick commands", 1)[1].split(
            "## Compatibility intents", 1
        )[0]
        self.assertNotIn("/analyse", quick)


if __name__ == "__main__":
    unittest.main()
