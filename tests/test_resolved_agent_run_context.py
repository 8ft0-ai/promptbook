import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ResolvedAgentRunContextTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.contract = (
            ROOT / "prompts" / "workflows" / "resolved-agent-run-context.md"
        ).read_text(encoding="utf-8")
        cls.contract_lower = cls.contract.lower()
        cls.fresh = (
            ROOT / "prompts" / "workflows" / "fresh-independent-review.md"
        ).read_text(encoding="utf-8")
        cls.fresh_lower = cls.fresh.lower()
        cls.remediate = (
            ROOT / "prompts" / "engineering" / "remediate-review-findings.md"
        ).read_text(encoding="utf-8")
        cls.remediate_lower = cls.remediate.lower()

    def test_promptbook_is_canonical_owner_and_context_is_ephemeral(self):
        self.assertIn("promptbook is the canonical owner", self.contract_lower)
        self.assertIn("ephemeral derived state", self.contract_lower)
        self.assertIn("not a new durable authority source", self.contract_lower)
        self.assertIn("conversation transcript as executable state", self.contract_lower)

    def test_supported_operations_are_explicit_without_generalising_authority(self):
        self.assertIn("explicitly supported operations are `/review` and `/fix`", self.contract_lower)
        self.assertIn("supporting `/fix` does not generalise `/review` permissions", self.contract_lower)
        self.assertIn("neither profile defines `/go` authority", self.contract_lower)

    def test_review_context_has_required_fields(self):
        for field in (
            "operation",
            "repository_identity",
            "work_item_identity",
            "immutable_candidate_identity",
            "resolved_authority_sources",
            "applicable_repository_instructions",
            "effective_capabilities",
            "prohibited_capabilities",
            "owner_decision_boundaries",
            "required_evidence",
        ):
            self.assertIn(field, self.contract)

    def test_fix_context_has_required_fields(self):
        for field in (
            "operation",
            "repository_identity",
            "work_item_identity",
            "starting_candidate_identity",
            "resolved_authority_sources",
            "applicable_repository_instructions",
            "remediation_scope",
            "effective_capabilities",
            "prohibited_capabilities",
            "owner_decision_boundaries",
            "required_validation",
            "required_evidence",
        ):
            self.assertIn(field, self.contract)

    def test_resolution_is_deterministic_from_authoritative_inputs(self):
        self.assertIn("equivalent authoritative inputs", self.contract_lower)
        self.assertIn("equivalent effective authority", self.contract_lower)
        self.assertIn("resolved context does not create authority", self.contract_lower)
        self.assertIn("filling the gap from conversation memory", self.contract_lower)

    def test_candidate_identity_invalidates_candidate_specific_review(self):
        self.assertIn("bind the context to the exact candidate commit", self.contract_lower)
        self.assertIn("if the candidate identity changes", self.contract_lower)
        self.assertIn("invalidate the prior candidate-specific context", self.contract_lower)
        self.assertIn("refresh the candidate identity", self.contract_lower)

    def test_review_capabilities_are_explicit_and_bounded(self):
        for allowed in (
            "repository read",
            "issue / pr read",
            "review-comment read",
            "ci / check evidence read",
        ):
            self.assertIn(allowed, self.contract_lower)
        for forbidden in (
            "repository mutation",
            "branch mutation",
            "merge",
            "release",
            "unrelated external execution",
        ):
            self.assertIn(forbidden, self.contract_lower)
        self.assertIn("access and permission are distinct", self.contract_lower)
        self.assertIn("read_only_review_capabilities", self.contract_lower)
        self.assertIn("requires an explicit owner decision", self.contract_lower)

    def test_fix_capabilities_are_monotonically_narrowed(self):
        self.assertIn("effective_fix_capabilities", self.contract)
        self.assertIn("technically_available_capabilities", self.contract)
        self.assertIn("authority_derived_capabilities", self.contract)
        self.assertIn("FIX_OPERATION_CEILING", self.contract)
        self.assertIn("technical availability can only remove executable capability", self.contract_lower)
        self.assertIn("it cannot grant authority", self.contract_lower)
        self.assertIn("must never widen it", self.contract_lower)

    def test_fix_operation_ceiling_allows_only_bounded_remediation(self):
        for allowed in (
            "repository/work-item reads required for the remediation",
            "bounded implementation mutation attributable to the resolved remediation scope",
            "work-branch/candidate mutation required to produce the remediated candidate",
            "validation and evidence collection required by repository authority",
        ):
            self.assertIn(allowed, self.contract_lower)
        for forbidden in (
            "merge",
            "release or tag publication",
            "deployment",
            "unrelated repository mutation",
            "infrastructure or provider mutation",
            "repository settings, credential, or secret mutation",
            "expansion of remediation scope merely because a tool is available",
        ):
            self.assertIn(forbidden, self.contract_lower)

    def test_fix_action_gateway_is_explicit_and_fail_closed(self):
        self.assertIn("## `/fix` action gateway", self.contract)
        self.assertIn("FORBID", self.contract)
        self.assertIn("REQUIRE OWNER / SEPARATE AUTHORITY", self.contract)
        self.assertIn("ALLOW", self.contract)
        self.assertIn("missing or ambiguous authority never defaults to allow", self.contract_lower)
        forbid_pos = self.contract.index("1. If higher-precedence authority")
        owner_pos = self.contract.index("2. Else if the action is not attributable")
        allow_pos = self.contract.index("3. Else if current authoritative sources permit it")
        self.assertLess(forbid_pos, owner_pos)
        self.assertLess(owner_pos, allow_pos)

    def test_authority_classification_is_separate_from_execution_feasibility(self):
        self.assertIn("keep authority classification separate from execution feasibility", self.contract_lower)
        self.assertIn("do not reclassify it as `require owner / separate authority`", self.contract_lower)
        self.assertIn("technical availability never changes an unauthorised action into `allow`", self.contract_lower)

    def test_fix_candidate_transition_is_explicit(self):
        self.assertIn("FixRunContext(A)", self.contract)
        self.assertIn("FixResult(B, delta, validation, evidence, remaining boundaries)", self.contract)
        self.assertIn("starting_candidate_identity", self.contract)
        self.assertIn("resulting_candidate_identity", self.contract)
        self.assertIn("immediately before the first material write", self.contract_lower)
        self.assertIn("if unexpected external candidate movement is detected", self.contract_lower)

    def test_candidate_a_review_and_validation_expire_for_b(self):
        self.assertIn("candidate-a-specific review and validation", self.contract_lower)
        self.assertIn("must not silently transfer as review or validation of b", self.contract_lower)
        self.assertIn("bind the observed result to `resulting_candidate_identity`", self.contract_lower)
        self.assertIn("fresh-context boundary", self.contract_lower)

    def test_instruction_provenance_and_evidence_are_reconstructable(self):
        self.assertIn("where each applicable instruction", self.contract_lower)
        self.assertIn("evidence should be proportionate, bounded, and reconstructable", self.contract_lower)
        self.assertIn("do not fabricate executed evidence", self.contract_lower)
        for evidence_class in ("`STATIC`", "`EXECUTED`", "`DURABLE`"):
            self.assertIn(evidence_class, self.contract)

    def test_evidence_bearing_finding_shape_is_defined(self):
        for field in (
            "claim",
            "affected_code_or_location",
            "applicable_authority_or_rule",
            "observation",
            "evidence",
            "immutable_candidate_identity",
            "priority",
            "confidence",
        ):
            self.assertIn(field, self.contract)

    def test_review_lifecycle_is_explicit(self):
        for stage in (
            "production routing",
            "resolved repository/work authority",
            "immutable review candidate",
            "applicable instruction provenance",
            "effective review capabilities",
            "required evidence resolution",
            "evidence collection",
            "evidence-bearing findings",
            "evidence-backed disposition",
        ):
            self.assertIn(stage, self.contract_lower)

    def test_fix_lifecycle_is_explicit(self):
        for stage in (
            "starting immutable candidate a",
            "bounded remediation scope",
            "effective/prohibited capabilities",
            "pre-action gateway classification",
            "bounded allow mutations only",
            "resulting immutable candidate b",
            "b-bound validation/evidence",
            "fresh-review boundary or other correct governed next state",
        ):
            self.assertIn(stage, self.contract_lower)

    def test_fresh_review_integrates_context_before_adjudication(self):
        self.assertIn("before substantive adjudication", self.fresh_lower)
        self.assertIn("resolve the ephemeral resolved agent run context", self.fresh_lower)
        self.assertIn("resolved-agent-run-context.md", self.fresh)
        self.assertIn("derive it from current authoritative inputs", self.fresh_lower)
        self.assertIn("evidence-bearing provenance", self.fresh_lower)
        self.assertIn("do not fabricate executed evidence", self.fresh_lower)

    def test_remediation_integrates_fix_context_before_mutation(self):
        self.assertIn("before substantive mutation", self.remediate_lower)
        self.assertIn("resolve the `/fix` resolved agent run context", self.remediate_lower)
        self.assertIn("resolved-agent-run-context.md", self.remediate)
        self.assertIn("exact starting candidate identity", self.remediate_lower)
        self.assertIn("bounded remediation scope", self.remediate_lower)
        self.assertIn("required validation", self.remediate_lower)
        self.assertIn("required evidence", self.remediate_lower)

    def test_remediation_uses_action_gateway_and_preserves_authority_boundary(self):
        self.assertIn("before each material action", self.remediate_lower)
        for classification in (
            "`ALLOW`",
            "`REQUIRE OWNER / SEPARATE AUTHORITY`",
            "`FORBID`",
        ):
            self.assertIn(classification, self.remediate)
        self.assertIn("missing or ambiguous authority never defaults to `allow`", self.remediate_lower)
        self.assertIn("technically available tool never grants authority", self.remediate_lower)
        self.assertIn("execute only `allow` actions that are actually available", self.remediate_lower)

    def test_remediation_record_is_bound_to_resulting_candidate(self):
        for field in (
            "starting candidate identity",
            "bounded implementation delta",
            "resulting candidate identity",
            "validation/evidence bound to the resulting candidate",
            "remaining boundaries and next governed state",
        ):
            self.assertIn(field, self.remediate_lower)
        self.assertIn("candidate-a-specific review and validation do not silently transfer to b", self.remediate_lower)
        self.assertIn("`STATIC`", self.remediate)
        self.assertIn("`EXECUTED`", self.remediate)
        self.assertIn("`DURABLE`", self.remediate)

    def test_remediation_preserves_fresh_review_boundary(self):
        self.assertIn("independent re-review is required", self.remediate_lower)
        self.assertIn("hard fresh-context boundary", self.remediate_lower)
        self.assertIn("next chat: /review <reviewed_candidate>", self.remediate_lower)
        self.assertIn("author-side remediation as fresh approval evidence", self.remediate_lower)

    def test_delegation_cannot_expand_authority(self):
        self.assertIn("child_authority ⊆ parent_authority", self.contract)
        self.assertIn("never gain authority merely through delegation", self.contract_lower)
        self.assertIn("resolved authorised subset", self.contract_lower)


if __name__ == "__main__":
    unittest.main()
