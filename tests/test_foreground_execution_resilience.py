import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ROOT / "prompts" / "workflows"
ENGINEERING = ROOT / "prompts" / "engineering"


class ForegroundExecutionResilienceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.contract = (WORKFLOWS / "foreground-execution-resilience.md").read_text(
            encoding="utf-8"
        )
        cls.implement = (ENGINEERING / "implement-an-approved-issue.md").read_text(
            encoding="utf-8"
        )
        cls.autonomous = (WORKFLOWS / "autonomous-progression.md").read_text(
            encoding="utf-8"
        )
        cls.contract_lower = cls.contract.lower()
        cls.implement_lower = cls.implement.lower()
        cls.autonomous_lower = cls.autonomous.lower()

    def test_soft_budget_is_empirical_provisional_and_not_a_platform_guarantee(self):
        for marker in (
            "approximately **18-minute** foreground budget",
            "empirical, provisional operating hypothesis",
            "configurable and revisable",
            "not** an asserted openai or platform hard timeout",
        ):
            self.assertIn(marker, self.contract_lower)
        self.assertIn("rather than inventing timing precision", self.contract_lower)

    def test_checkpoint_order_precedes_deferrable_assurance(self):
        coherent = self.contract_lower.index("finish the smallest coherent scoped implementation state")
        safety = self.contract_lower.index("minimum pre-publication safety checks", coherent)
        immutable = self.contract_lower.index("establish one immutable candidate identity", safety)
        remaining = self.contract_lower.index("after the immutable candidate exists", immutable)
        assurance = self.contract_lower.index("candidate-bound assurance", remaining)
        self.assertLess(coherent, safety)
        self.assertLess(safety, immutable)
        self.assertLess(immutable, assurance)

    def test_exact_candidate_is_normal_minimum_and_pr_is_conditional(self):
        self.assertIn(
            "normal minimum continuation point is an exact candidate commit",
            self.contract_lower,
        )
        self.assertIn("pull-request creation is already authorised", self.contract_lower)
        self.assertIn("pr creation is never mandatory", self.contract_lower)
        self.assertIn("a pr bound to that exact candidate is preferred only", self.implement_lower)

    def test_prepublication_safety_is_not_authoritative_assurance(self):
        self.assertIn(
            "distinguish pre-publication safety checks from authoritative candidate-bound assurance",
            self.contract_lower,
        )
        for required in (
            "repository-required tests",
            "static checks",
            "ci",
            "integration evidence",
            "review",
        ):
            self.assertIn(required, self.contract_lower)
        self.assertIn("evidence for different bytes does not transfer", self.implement_lower)

    def test_checkpoint_is_persistence_not_validation_approval_or_completion(self):
        self.assertIn("persistence and reconstruction contract", self.contract_lower)
        self.assertIn("persistence identity", self.contract_lower)
        self.assertIn("not evidence that validation passed", self.contract_lower)
        for forbidden_claim in (
            "validated",
            "approved",
            "review-ready",
            "merged",
            "released",
            "deployed",
            "complete",
        ):
            self.assertIn(forbidden_claim, self.contract_lower)

    def test_changed_bytes_do_not_inherit_stale_validation(self):
        self.assertIn(
            "validation evidence from different bytes must never silently transfer",
            self.contract_lower,
        )
        self.assertIn("validation evidence remains bound to the bytes it actually covered", self.autonomous_lower)

    def test_later_session_reconstructs_without_prior_chat_memory(self):
        for marker in (
            "reconstructing current authority",
            "repository/task policy",
            "lifecycle state",
            "candidate identity",
            "validation/ci state",
            "durable authoritative sources",
            "prior-chat memory must not be required",
        ):
            self.assertIn(marker, self.contract_lower)
        self.assertIn("rather than prior-chat memory", self.autonomous_lower)

    def test_later_session_can_resume_exact_candidate_assurance(self):
        for marker in (
            "exact-head ci observation",
            "pull-request/evidence reconciliation",
            "remaining candidate-bound assurance",
            "genuinely fresh review boundary",
        ):
            self.assertIn(marker, self.contract_lower)
        self.assertIn("recover that exact candidate", self.autonomous_lower)
        self.assertIn("continuing exact-head ci observation", self.autonomous_lower)

    def test_session_split_does_not_create_authority_or_review_freshness(self):
        self.assertIn("crossing a session boundary grants no new", self.contract_lower)
        self.assertIn("remains non-fresh for substantive independent review", self.contract_lower)
        self.assertIn("session splitting does not create review independence", self.contract_lower)
        self.assertIn("does not become fresh for review merely because it is new", self.autonomous_lower)

    def test_budget_pressure_does_not_widen_execution_surface(self):
        self.assertIn("must not create authority for work, codex", self.contract_lower)
        self.assertIn("or any other surface", self.contract_lower)
        self.assertIn("does not widen the permitted execution surface", self.autonomous_lower)

    def test_interruption_is_truthful_and_uses_existing_terminal_model(self):
        self.assertIn("report the exact immutable continuation identity", self.contract_lower)
        self.assertIn("report the actual incomplete durable state", self.contract_lower)
        self.assertIn("never fabricate a candidate", self.contract_lower)
        self.assertIn("do not add a new conversational terminal state", self.contract_lower)
        self.assertIn("existing promptbook terminal-state model", self.contract_lower)

    def test_deterministic_recovery_sequence_reaches_fresh_review_boundary(self):
        markers = (
            "substantial governed implementation",
            "foreground budget risk becomes material",
            "coherent candidate c is persisted durably",
            "session ends before ci/reconciliation completes",
            "later session starts without prior-chat memory",
            "authority and lifecycle state reconstructed from durable sources",
            "exact candidate c recovered",
            "exact-head ci/reconciliation completed",
            "genuinely fresh review boundary reached",
        )
        positions = [self.contract_lower.index(marker) for marker in markers]
        self.assertEqual(positions, sorted(positions))

    def test_integration_points_link_to_the_contract(self):
        link = "foreground-execution-resilience.md"
        self.assertIn(link, self.implement_lower)
        self.assertIn(link, self.autonomous_lower)
        self.assertIn("implement an approved issue", self.contract_lower)
        self.assertIn("autonomous progression", self.contract_lower)


if __name__ == "__main__":
    unittest.main()
