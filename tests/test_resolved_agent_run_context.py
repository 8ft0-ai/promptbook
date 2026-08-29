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

    def test_promptbook_is_canonical_owner_and_context_is_ephemeral(self):
        self.assertIn("promptbook is the canonical owner", self.contract_lower)
        self.assertIn("ephemeral derived state", self.contract_lower)
        self.assertIn("not a new durable authority source", self.contract_lower)
        self.assertIn("conversation transcript as executable state", self.contract_lower)

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
        self.assertIn("read_only_review_capabilities", self.contract)
        self.assertIn("requires an explicit owner decision", self.contract_lower)

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

    def test_fresh_review_integrates_context_before_adjudication(self):
        self.assertIn("before substantive adjudication", self.fresh_lower)
        self.assertIn("resolve the ephemeral resolved agent run context", self.fresh_lower)
        self.assertIn("resolved-agent-run-context.md", self.fresh)
        self.assertIn("derive it from current authoritative inputs", self.fresh_lower)
        self.assertIn("evidence-bearing provenance", self.fresh_lower)
        self.assertIn("do not fabricate executed evidence", self.fresh_lower)

    def test_delegation_cannot_expand_authority(self):
        self.assertIn("child_authority ⊆ parent_authority", self.contract)
        self.assertIn("never gain authority merely through delegation", self.contract_lower)


if __name__ == "__main__":
    unittest.main()
