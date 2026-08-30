import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ExecutorCapabilityProjectionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.projection = (
            ROOT / "prompts" / "workflows" / "executor-capability-projection.md"
        ).read_text(encoding="utf-8")
        cls.projection_lower = cls.projection.lower()
        cls.context = (
            ROOT / "prompts" / "workflows" / "resolved-agent-run-context.md"
        ).read_text(encoding="utf-8")
        cls.context_lower = cls.context.lower()

    def test_projection_can_narrow_but_never_widen(self):
        self.assertIn("projected_executor_capabilities", self.projection)
        self.assertIn("resolved_effective_capabilities", self.projection)
        self.assertIn("actual_executor_capabilities", self.projection)
        self.assertIn("executor_supported_capabilities", self.projection)
        self.assertIn("executor_local_safety_policy", self.projection)
        self.assertIn("cannot add a capability absent", self.projection_lower)

    def test_profile_is_derived_state_not_authority(self):
        self.assertIn("derived execution state", self.projection_lower)
        self.assertIn("not a durable authority source", self.projection_lower)
        self.assertIn("technical availability is never authority", self.projection_lower)
        self.assertIn("credential", self.projection_lower)
        self.assertIn("network", self.projection_lower)

    def test_required_profile_fields_are_explicit(self):
        for field in (
            "profile_version",
            "operation",
            "repository_identity",
            "governing_work_or_objective_identity",
            "bound_state_identity",
            "resolved_context_identity_or_provenance",
            "allowed_capabilities",
            "denied_capabilities",
            "execution_constraints",
            "stale_or_expiry_conditions",
            "required_execution_evidence",
            "projection_provenance",
        ):
            self.assertIn(field, self.projection)

    def test_portable_capability_vocabulary_preserves_material_effects(self):
        for capability in (
            "repository_read",
            "work_item_read",
            "ci_evidence_read",
            "candidate_write",
            "work_item_evidence_update",
            "review_publish",
            "validation_execute",
            "workflow_dispatch",
            "merge",
            "release_publish",
            "deploy",
            "repository_settings_write",
            "credential_use",
            "network_access",
            "provider_mutation",
            "production_data_mutation",
        ):
            self.assertIn(capability, self.projection)
        self.assertIn("does not imply `release_publish` or `deploy`", self.projection_lower)

    def test_action_gateway_classification_controls_projection(self):
        self.assertIn("ALLOW", self.projection)
        self.assertIn("REQUIRE OWNER / SEPARATE AUTHORITY", self.projection)
        self.assertIn("FORBID", self.projection)
        self.assertIn("must not be projected as executable authority", self.projection_lower)
        self.assertIn("capability must not be projected", self.projection_lower)

    def test_review_read_only_projects_no_write(self):
        section = self.projection[
            self.projection.index("### `/review --read-only`") :
            self.projection.index("### Ordinary `/review`")
        ]
        self.assertIn("repository_read", section)
        self.assertIn("work_item_read", section)
        self.assertIn("ci_evidence_read", section)
        self.assertIn("must not include any write capability", section.lower())
        self.assertIn("`review_publish`", section)

    def test_ordinary_review_projects_only_narrow_publication_write(self):
        section = self.projection[
            self.projection.index("### Ordinary `/review`") :
            self.projection.index("### `/fix`")
        ]
        self.assertIn("review_publish", section)
        for forbidden in (
            "candidate mutation",
            "workflow dispatch",
            "merge",
            "release",
            "deployment",
        ):
            self.assertIn(forbidden, section.lower())

    def test_fix_projects_candidate_write_but_not_merge_release_deploy(self):
        section = self.projection[
            self.projection.index("### `/fix`") :
            self.projection.index("### `/go`")
        ]
        self.assertIn("candidate_write", section)
        self.assertIn("validation_execute", section)
        self.assertIn("must not include `merge`, `release_publish` or `deploy`", section.lower())

    def test_go_projection_is_action_specific(self):
        section = self.projection[self.projection.index("### `/go`") :]
        self.assertIn("exact next governed action", section.lower())
        self.assertIn("merge", section)
        self.assertIn("release_publish", section)
        self.assertIn("deploy", section)
        self.assertIn("newly projected profile", section.lower())

    def test_environment_state_cannot_widen_projection(self):
        for ambient in (
            "connector",
            "shell",
            "credential",
            "token",
            "network reachability",
            "repository write permission",
            "executor support",
            "previous successful execution",
        ):
            self.assertIn(ambient, self.projection_lower)
        self.assertIn("may widen a projection", self.projection_lower)

    def test_profile_is_invalidated_by_material_state_change(self):
        self.assertIn("invalidate and re-project", self.projection_lower)
        self.assertIn("candidate or result identity", self.projection_lower)
        self.assertIn("accepted proposal identity", self.projection_lower)
        self.assertIn("consumed approval", self.projection_lower)
        self.assertIn("stale approval", self.projection_lower)
        self.assertIn("moved candidate a'", self.projection_lower)

    def test_executor_results_distinguish_authority_and_feasibility(self):
        for result in (
            "PROFILE_DENIED",
            "EXECUTOR_UNSUPPORTED",
            "STALE_PROFILE",
            "GUARD_MISMATCH",
            "EXECUTED",
        ):
            self.assertIn(result, self.projection)
        self.assertIn("not the same result", self.projection_lower)

    def test_enforcement_evidence_has_required_shape(self):
        for field in (
            "profile_identity",
            "bound_state_identity",
            "requested_capability",
            "enforcement_decision",
            "executor_capability_intersection",
            "execution_status",
            "result_identity_or_evidence",
            "limitations",
        ):
            self.assertIn(field, self.projection)
        self.assertIn("must not include raw secret values", self.projection_lower)

    def test_executor_consumer_is_not_policy_owner(self):
        self.assertIn("does not become a repository-policy", self.projection_lower)
        self.assertIn("external executors remain mechanisms", self.projection_lower)
        self.assertIn("never interpret arbitrary command text as authority", self.projection_lower)

    def test_delegation_cannot_widen_parent_authority(self):
        self.assertIn("child_authority ⊆ parent_authority", self.projection)
        self.assertIn("subset of the parent operation's current effective capabilities", self.projection_lower)
        self.assertIn("cannot refresh stale parent authority", self.projection_lower)

    def test_projection_does_not_change_existing_operation_authority(self):
        self.assertIn("does not change the authority semantics", self.projection_lower)
        for operation in ("`/review`", "`/fix`", "`/go`"):
            self.assertIn(operation, self.projection)
            self.assertIn(operation, self.context)
        self.assertIn("technical availability never changes an unauthorised action", self.context_lower)

    def test_machine_enforcement_is_not_claimed_before_executor_proof(self):
        self.assertIn("do not claim machine enforcement", self.projection_lower)
        self.assertIn("later executor implementation must be governed separately", self.projection_lower)


if __name__ == "__main__":
    unittest.main()
