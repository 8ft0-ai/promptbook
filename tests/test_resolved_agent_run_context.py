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
        cls.autonomous = (
            ROOT / "prompts" / "workflows" / "autonomous-progression.md"
        ).read_text(encoding="utf-8")
        cls.autonomous_lower = cls.autonomous.lower()

    def test_promptbook_is_canonical_owner_and_context_is_ephemeral(self):
        self.assertIn("promptbook is the canonical owner", self.contract_lower)
        self.assertIn("ephemeral derived state", self.contract_lower)
        self.assertIn("not a new durable authority source", self.contract_lower)
        self.assertIn("conversation transcript as executable state", self.contract_lower)

    def test_supported_operations_are_explicit_without_generalising_authority(self):
        self.assertIn(
            "explicitly supported operations are `/review`, `/fix`, and `/go`",
            self.contract_lower,
        )
        self.assertIn(
            "supporting one profile does not generalise another operation's permissions",
            self.contract_lower,
        )
        for operation in ("`/review`", "`/fix`", "`/go`"):
            self.assertIn(operation, self.contract)

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

    def test_go_context_has_required_fields(self):
        for field in (
            "operation",
            "repository_identity",
            "governing_objective_identity",
            "current_lifecycle_state",
            "current_candidate_identity",
            "current_review_disposition",
            "resolved_authority_sources",
            "applicable_repository_instructions",
            "effective_capabilities",
            "prohibited_capabilities",
            "owner_decision_boundaries",
            "continuation_mode",
            "next_governed_action",
            "required_preconditions",
            "required_evidence",
            "completion_conditions",
        ):
            self.assertIn(field, self.contract)
        self.assertIn("lifecycle object that can reconstruct the complete governed objective", self.contract_lower)
        self.assertIn("not permission to execute it", self.contract_lower)

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
        self.assertIn("prior candidate-specific review and validation attached to candidate a expire for b", self.contract_lower)
        self.assertIn("must not silently transfer as review or validation of b", self.contract_lower)
        self.assertIn("bind the observed result to `resulting_candidate_identity`", self.contract_lower)
        self.assertIn("fresh-context boundary", self.contract_lower)

    def test_go_capabilities_are_monotonically_narrowed(self):
        self.assertIn("effective_go_capabilities", self.contract)
        self.assertIn("technically_available_capabilities", self.contract)
        self.assertIn("authority_derived_capabilities", self.contract)
        self.assertIn("GO_OPERATION_CEILING", self.contract)
        self.assertIn("technical availability may remove executable capability", self.contract_lower)
        self.assertIn("must never grant authority", self.contract_lower)
        self.assertIn("may narrow the effective set further but must never widen it", self.contract_lower)
        self.assertIn("upper bound on what `/go` may execute", self.contract_lower)
        self.assertIn("it is not an authority grant", self.contract_lower)

    def test_go_operation_ceiling_preserves_separate_consequential_authority(self):
        for eligible in (
            "repository/work-item reads required for progression",
            "routine lifecycle metadata updates within the governing objective",
            "branch/pr state transitions already authorised by the governing workflow",
            "merge of the exact candidate when merge authority is independently established",
            "required post-action validation and evidence collection",
            "issue/work-item close-out when governing completion conditions and close-out authority are satisfied",
            "continuation into another promptbook workflow when current authority and continuation mode permit it",
        ):
            self.assertIn(eligible, self.contract_lower)
        for not_intrinsic in (
            "release or tag publication",
            "deployment",
            "infrastructure or provider mutation",
            "repository settings changes",
            "production-data mutation",
            "destructive actions",
            "material cost commitments",
            "unrelated scope expansion",
        ):
            self.assertIn(not_intrinsic, self.contract_lower)
        self.assertIn("NOT INTRINSICALLY AUTHORISED", self.contract)

    def test_go_action_gateway_is_explicit_ordered_and_fail_closed(self):
        section = self.contract[self.contract.index("## `/go` action gateway"):]
        forbid_pos = section.index("1. If higher-precedence authority")
        owner_pos = section.index("2. Else if current authority is insufficient")
        allow_pos = section.index("3. Else if current authoritative sources permit the exact action")
        missing_pos = section.index("4. Missing or ambiguous authority never defaults to ALLOW")
        self.assertLess(forbid_pos, owner_pos)
        self.assertLess(owner_pos, allow_pos)
        self.assertLess(allow_pos, missing_pos)
        for classification in ("FORBID", "REQUIRE OWNER / SEPARATE AUTHORITY", "ALLOW"):
            self.assertIn(classification, section)
        self.assertIn("keep authority classification separate from execution feasibility", section.lower())

    def test_go_approved_candidate_with_merge_authority_may_allow_merge(self):
        self.assertIn(
            "merge of the exact candidate when merge authority is independently established",
            self.contract_lower,
        )
        self.assertIn("current authoritative sources permit the exact action", self.contract_lower)
        self.assertIn("ALLOW", self.contract)

    def test_go_candidate_approval_does_not_create_merge_authority(self):
        self.assertIn("candidate approved", self.contract_lower)
        self.assertIn("merge authorised", self.contract_lower)
        candidate_pos = self.contract_lower.index("candidate approved")
        merge_pos = self.contract_lower.index("merge authorised", candidate_pos)
        self.assertLess(candidate_pos, merge_pos)
        self.assertIn("≠", self.contract[candidate_pos:merge_pos + len("merge authorised")])
        self.assertIn("REQUIRE OWNER / SEPARATE AUTHORITY", self.contract)

    def test_go_exact_decision_is_bounded_and_consumed_once(self):
        self.assertIn("## `/go` bounded approval consumption", self.contract)
        self.assertIn("concrete proposal/action presented", self.contract_lower)
        self.assertIn("exact decision target", self.contract_lower)
        self.assertIn("proposal identity", self.contract_lower)
        self.assertIn("bounded effect of acceptance", self.contract_lower)
        self.assertIn("accepted authority is consumed once for that bounded action", self.contract_lower)

    def test_go_material_change_invalidates_stale_approval(self):
        self.assertIn("invalidate the stale approval", self.contract_lower)
        self.assertIn("re-present the changed decision", self.contract_lower)
        for stale_input in (
            "candidate",
            "material proposal",
            "applicable policy",
            "required checks",
            "governing authority",
            "repository instructions",
        ):
            self.assertIn(stale_input, self.contract_lower)

    def test_go_merge_result_rebinds_identity_and_evidence(self):
        self.assertIn("approved candidate a", self.contract_lower)
        self.assertIn("merge commit m", self.contract_lower)
        self.assertIn("candidate-bound review, checks, or other evidence for a do not become post-merge evidence for m", self.contract_lower)
        self.assertIn("bind new observations to the resulting identity", self.contract_lower)
        self.assertIn("re-resolve before another consequential transition", self.contract_lower)

    def test_go_failed_post_merge_validation_prevents_complete(self):
        self.assertIn("merge succeeded", self.contract_lower)
        self.assertIn("objective complete", self.contract_lower)
        self.assertIn("a failed required post-merge validation therefore prevents `complete`", self.contract_lower)
        self.assertIn("required post-action verification", self.contract_lower)

    def test_go_merge_authority_does_not_create_release_or_deploy_authority(self):
        self.assertIn("merge authority for a", self.contract_lower)
        self.assertIn("release authority", self.contract_lower)
        self.assertIn("deployment authority", self.contract_lower)
        self.assertIn("authority or acceptance for one consequential transition must not silently become authority for a later transition", self.contract_lower)

    def test_go_technical_deployment_capability_cannot_create_authority(self):
        self.assertIn("technical capability must not intrinsically grant", self.contract_lower)
        self.assertIn("deployment", self.contract_lower)
        self.assertIn("technical availability never changes an unauthorised action into `allow`", self.contract_lower)

    def test_go_higher_precedence_prohibition_resolves_forbid(self):
        section = self.contract[self.contract.index("## `/go` action gateway"):]
        self.assertIn("If higher-precedence authority or the /go operation ceiling prohibits it", section)
        self.assertIn("FORBID", section)
        self.assertIn("cannot execute under the current `/go` contract", section)

    def test_go_authorised_but_unavailable_uses_external_boundary(self):
        self.assertIn("if an action is `allow` but the required execution capability is unavailable", self.contract_lower)
        self.assertIn("capability / `external_required` boundary", self.contract_lower)
        self.assertIn(
            "resolve another eligible execution locality before selecting a human-operated `external_required` hand-off",
            self.contract_lower,
        )
        self.assertIn("changing locality never widens the action's resolved authority", self.contract_lower)

    def test_go_closeout_requires_completion_conditions_and_authority(self):
        self.assertIn(
            "issue/work-item close-out when governing completion conditions and close-out authority are satisfied",
            self.contract_lower,
        )
        self.assertIn("completion conditions, and authorised close-out", self.contract_lower)

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

    def test_go_lifecycle_is_explicit(self):
        for stage in (
            "resolved governing objective and current lifecycle state",
            "current candidate/result identity and review/evidence state where applicable",
            "effective/prohibited go capabilities",
            "proposed next governed action",
            "refresh decision-critical state",
            "pre-action gateway classification",
            "execute one available allow transition or bounded delegated review only",
            "resulting lifecycle state and immutable identity",
            "result-bound validation/evidence",
            "re-resolve remaining authority and boundaries",
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

    def test_autonomous_progression_resolves_go_context_before_progression(self):
        self.assertIn("before substantive `/go` lifecycle progression", self.autonomous_lower)
        self.assertIn("resolved agent run context", self.autonomous_lower)
        self.assertIn("resolved-agent-run-context.md", self.autonomous)
        self.assertIn("treat `next_governed_action` as a proposal", self.autonomous_lower)
        self.assertIn("before every consequential `/go` transition", self.autonomous_lower)
        for classification in (
            "`ALLOW`",
            "`REQUIRE OWNER / SEPARATE AUTHORITY`",
            "`FORBID`",
        ):
            self.assertIn(classification, self.autonomous)

    def test_autonomous_progression_does_not_infer_authority_from_prior_success(self):
        self.assertIn("not authority for the next consequential transition", self.autonomous_lower)
        self.assertIn("consequential transitions must not be inferred from the prior workflow's success record alone", self.autonomous_lower)
        self.assertIn("candidate approval, merge authority, release authority, deployment authority", self.autonomous_lower)
        self.assertIn("authority consumed for one consequential action is not ambient permission", self.autonomous_lower)

    def test_autonomous_progression_rebinds_result_evidence_and_completion(self):
        self.assertIn("bind the resulting lifecycle state, immutable identity, validation and evidence", self.autonomous_lower)
        self.assertIn("candidate-bound evidence does not silently become result-bound evidence", self.autonomous_lower)
        self.assertIn("re-resolve authority and remaining boundaries before another consequential transition", self.autonomous_lower)
        self.assertIn("a successful intermediate action such as merge does not itself imply `complete`", self.autonomous_lower)

    def test_delegation_cannot_expand_authority(self):
        self.assertIn("child_authority ⊆ parent_authority", self.contract)
        self.assertIn("never gain authority merely through delegation", self.contract_lower)
        self.assertIn("resolved authorised subset", self.contract_lower)


if __name__ == "__main__":
    unittest.main()