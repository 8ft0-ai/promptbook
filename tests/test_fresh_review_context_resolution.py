import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ROOT / "prompts" / "workflows"
ENGINEERING = ROOT / "prompts" / "engineering"
GUIDE = ROOT / "guides" / "go-lifecycle.md"


class FreshReviewContextResolutionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.router = (WORKFLOWS / "README.md").read_text(encoding="utf-8")
        cls.fresh = (WORKFLOWS / "fresh-independent-review.md").read_text(
            encoding="utf-8"
        )
        cls.context = (WORKFLOWS / "resolved-agent-run-context.md").read_text(
            encoding="utf-8"
        )
        cls.autonomous = (WORKFLOWS / "autonomous-progression.md").read_text(
            encoding="utf-8"
        )
        cls.projection = (WORKFLOWS / "executor-capability-projection.md").read_text(
            encoding="utf-8"
        )
        cls.handover = (WORKFLOWS / "next-session-handover.md").read_text(
            encoding="utf-8"
        )
        cls.implement = (ENGINEERING / "implement-an-approved-issue.md").read_text(
            encoding="utf-8"
        )
        cls.remediate = (ENGINEERING / "remediate-review-findings.md").read_text(
            encoding="utf-8"
        )
        cls.guide = GUIDE.read_text(encoding="utf-8")

        for name in (
            "router",
            "fresh",
            "context",
            "autonomous",
            "projection",
            "handover",
            "implement",
            "remediate",
            "guide",
        ):
            setattr(cls, f"{name}_lower", getattr(cls, name).lower())

    def test_current_fresh_context_keeps_ordinary_review_path(self):
        self.assertIn(
            "if the current context is genuinely fresh for that decision",
            self.router_lower,
        )
        self.assertIn("[fresh independent review](fresh-independent-review.md)", self.router_lower)
        self.assertIn("fresh independence is a property of this reviewing context", self.fresh_lower)

    def test_nonfresh_context_delegates_when_isolated_context_is_eligible(self):
        nonfresh = self.router_lower.index("if the current context is not genuinely fresh")
        resolve = self.router_lower.index("eligible genuinely isolated review context", nonfresh)
        delegate = self.router_lower.index("invoke [fresh independent review]", resolve)
        fallback = self.router_lower.index("[next-session handover]", delegate)
        self.assertLess(nonfresh, resolve)
        self.assertLess(resolve, delegate)
        self.assertLess(delegate, fallback)
        self.assertIn("eligible genuinely isolated review context", self.autonomous_lower)

    def test_child_gets_minimal_target_and_reconstructs_authoritative_state(self):
        for marker in (
            "minimal durable review target",
            "independently bootstrap applicable project/repository authority",
            "reconstruct the exact candidate",
        ):
            self.assertIn(marker, self.fresh_lower)
        self.assertIn("minimal durable review target or equivalent reconstruction reference", self.context_lower)

    def test_author_side_substantive_adjudication_is_not_review_evidence(self):
        for marker in (
            "author-side private reasoning",
            "hidden conversational state",
            "proposed disposition",
            "expected conclusion",
        ):
            self.assertIn(marker, self.fresh_lower)
        self.assertIn("do not pass author-side substantive conclusions", self.router_lower)
        self.assertIn("do not include author-side substantive conclusions", self.handover_lower)

    def test_delegated_reviewer_uses_bounded_review_profile(self):
        self.assertIn("child_review_authority", self.context)
        self.assertIn("effective_review_authority", self.context)
        self.assertIn("child_review_authority", self.projection)
        self.assertIn("effective_review_authority", self.projection)
        self.assertIn("newly resolved child `/review` operation", self.projection_lower)
        for capability in (
            "repository_read",
            "work_item_read",
            "ci_evidence_read",
            "review_publish",
        ):
            self.assertIn(capability, self.projection)

    def test_author_side_mutation_and_later_lifecycle_capability_do_not_transfer(self):
        delegated_review = self.projection[
            self.projection.index("When ordinary `/review` is performed") :
            self.projection.index("### `/fix`")
        ].lower()
        for forbidden in (
            "candidate_write",
            "merge",
            "release_publish",
            "deploy",
            "settings",
            "provider",
            "production",
        ):
            self.assertIn(forbidden, delegated_review)
        self.assertIn("does not transfer", self.context_lower)

    def test_same_maintainer_identity_remains_only_existing_single_maintainer_case(self):
        self.assertIn("same maintainer account", self.fresh_lower)
        self.assertIn("single-maintainer", self.router_lower)
        self.assertIn("same-maintainer github identity remains compatible only", self.guide_lower)

    def test_distinct_human_or_formal_review_policy_is_not_bypassed(self):
        self.assertIn("another human, distinct formal reviewer identity", self.fresh_lower)
        self.assertIn("distinct human/formal reviewer", self.context_lower)
        self.assertIn("another human or formal reviewer", self.autonomous_lower)
        self.assertIn("another human/formal reviewer", self.guide_lower)

    def test_review_result_is_exact_candidate_bound_and_movement_invalidates_it(self):
        self.assertIn("exact candidate identity actually inspected", self.fresh_lower)
        self.assertIn("candidate moved", self.fresh_lower)
        self.assertIn("delegated review disposition bound to candidate a", self.context_lower)
        self.assertIn("review bound to candidate a cannot silently approve candidate a'", self.guide_lower)

    def test_changes_required_does_not_create_remediation_authority(self):
        self.assertIn("request_changes", self.fresh_lower)
        self.assertIn("identifies blockers, not remediation authority", self.fresh_lower)
        self.assertIn("does not add merge, remediation, release or deployment capability", self.projection_lower)

    def test_approved_does_not_create_merge_release_or_deploy_authority(self):
        self.assertIn("a recorded `approve` is review evidence/state, not merge authority", self.fresh_lower)
        self.assertIn(
            "review-recording authority does not grant remediation, merge, release, deployment",
            self.router_lower,
        )
        self.assertIn(
            "re-resolve any later remediation, merge, release, deployment, production or close-out authority independently",
            self.autonomous_lower,
        )

    def test_unavailable_or_unprovable_isolation_preserves_manual_fallback(self):
        self.assertIn("only when no eligible/provable isolated review context is available", self.router_lower)
        self.assertIn("existing manual fresh-context `external_required` hand-off", self.context_lower)
        self.assertIn("existing manual fresh-context `external_required` fallback", self.autonomous_lower)
        self.assertIn("next chat:", self.handover_lower)
        self.assertIn("/review", self.handover_lower)

    def test_unchanged_failed_delegation_does_not_loop(self):
        self.assertIn("do not repeatedly create equivalent failed review contexts", self.context_lower)
        self.assertIn("avoid repeatedly creating an equivalent failed review context", self.autonomous_lower)
        self.assertIn("do not retry an equivalent failed delegation indefinitely", self.router_lower)
        self.assertIn("do not repeatedly create an equivalent failed fresh-review child", self.guide_lower)

    def test_execution_locality_and_human_external_execution_semantics_remain_distinct(self):
        for locality in (
            "connected/native",
            "hosted/hermetic",
            "owner-local/bounded-executor",
        ):
            self.assertIn(locality, self.context_lower)
            self.assertIn(locality, self.autonomous_lower)
            self.assertIn(locality, self.guide_lower)
        self.assertIn("fresh-review context resolution is distinct", self.context_lower)
        self.assertIn("does not reuse the locality classes", self.context_lower)
        self.assertIn("this ladder does not resolve review freshness", self.autonomous_lower)
        self.assertIn("human-operated external execution", self.handover_lower)

    def test_implementation_and_remediation_return_to_router_before_manual_handoff(self):
        self.assertIn("return control to the router", self.implement_lower)
        self.assertIn("eligible genuinely isolated fresh-review context", self.implement_lower)
        self.assertIn("only when no eligible/provable isolated context", self.implement_lower)
        self.assertIn("return control to the router", self.remediate_lower)
        self.assertIn("eligible genuinely isolated fresh-review context", self.remediate_lower)
        self.assertIn("only when no eligible/provable isolated context", self.remediate_lower)


if __name__ == "__main__":
    unittest.main()
