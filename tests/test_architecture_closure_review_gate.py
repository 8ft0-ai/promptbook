import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ROOT / "prompts" / "workflows"
ENGINEERING = ROOT / "prompts" / "engineering"


def parse_lifecycle(router: str):
    marker = "ARCHITECTURE_CLOSURE_LIFECYCLE_V1\n"
    if marker not in router:
        raise AssertionError("canonical closure lifecycle table missing")
    block = router.split(marker, 1)[1].split("```", 1)[0]
    rows = {}
    for raw in block.splitlines():
        line = raw.strip()
        if not line or line.startswith("CURRENT |"):
            continue
        parts = [part.strip() for part in line.split("|")]
        if len(parts) != 5:
            raise AssertionError(f"invalid lifecycle row: {raw}")
        current, event, next_state, projection, action = parts
        key = (current, event)
        if key in rows:
            raise AssertionError(f"duplicate lifecycle transition: {key}")
        rows[key] = {"next": next_state, "projection": projection, "action": action}
    return rows


class ArchitectureClosureReviewGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.router_raw = (WORKFLOWS / "README.md").read_text(encoding="utf-8")
        cls.router = cls.router_raw.lower()
        cls.transitions = parse_lifecycle(cls.router_raw)
        cls.closure = (WORKFLOWS / "architecture-closure-analysis.md").read_text(encoding="utf-8").lower()
        cls.review = (WORKFLOWS / "fresh-independent-review.md").read_text(encoding="utf-8").lower()
        cls.analysis = (WORKFLOWS / "stateful-invariant-analysis.md").read_text(encoding="utf-8").lower()
        cls.context = (WORKFLOWS / "resolved-agent-run-context.md").read_text(encoding="utf-8").lower()
        cls.auto = (WORKFLOWS / "autonomous-progression.md").read_text(encoding="utf-8").lower()
        cls.go = (ROOT / "guides" / "go-lifecycle.md").read_text(encoding="utf-8").lower()
        cls.plan = (ENGINEERING / "plan-an-issue.md").read_text(encoding="utf-8").lower()
        cls.implement = (ENGINEERING / "implement-an-approved-issue.md").read_text(encoding="utf-8").lower()
        cls.fix = (ENGINEERING / "remediate-review-findings.md").read_text(encoding="utf-8").lower()

    def transition(self, current, event):
        return self.transitions[(current, event)]

    def test_lifecycle_table_routes_required_scenarios(self):
        expected = {
            ("ORDINARY_BOUNDED_REMEDIATION", "REVIEW_CHANGES_REQUIRED"): ("FIX_REQUIRED", "NOT_APPLICABLE", "FIX"),
            ("FIX_REQUIRED", "REMEDIATION_IMPLEMENTED_AND_VALIDATED"): ("REMEDIATION_READINESS_REQUIRED", "NOT_APPLICABLE", "READINESS_SWEEP"),
            ("ADJACENT_MODEL_OMISSION", "ARCHITECTURE_CLOSURE_SELECTED"): ("ARCHITECTURE_CLOSURE_ANALYSIS_REQUIRED", "NO", "ANALYSE_CLOSURE"),
            ("ARCHITECTURE_CLOSURE_READY", "NONE"): ("CLOSURE_REVIEW_REQUIRED", "NO", "FRESH_CLOSURE_REVIEW"),
            ("CLOSURE_REVIEW_REQUIRED", "DURABLE_CHANGES_REQUIRED_RECORDED"): ("CLOSURE_RECONSTRUCTION_REQUIRED", "NO", "REVISE_OR_RECONSTRUCT_CLOSURE"),
            ("CLOSURE_REVIEW_REQUIRED", "DURABLE_APPROVED_FOR_CANDIDATE_PROJECTION_RECORDED"): ("CLOSURE_APPROVED", "SEPARATE_AUTHORITY_REQUIRED", "RESOLVE_CANDIDATE_AUTHORITY"),
            ("CLOSURE_APPROVED", "NEW_DECISION_CRITICAL_SEMANTICS"): ("CLOSURE_REVIEW_REQUIRED", "NO", "RETURN_TO_CLOSURE"),
            ("CLOSURE_APPROVED", "CANDIDATE_PROJECTED"): ("CANDIDATE_REVIEW_REQUIRED", "ALREADY_PROJECTED", "FRESH_CANDIDATE_REVIEW"),
            ("CLOSURE_REVIEW_REQUIRED", "REVIEW_ATTEMPTS_IMPLEMENTATION_OR_MERGE"): ("CLOSURE_REVIEW_REQUIRED", "NO", "FORBID_UNRELATED_AUTHORITY"),
            ("CLOSURE_REVIEW_REQUIRED", "GO_ATTEMPTS_CANDIDATE_PROJECTION"): ("CLOSURE_REVIEW_REQUIRED", "NO", "FORBID_PROJECTION"),
            ("APPROVED_CLOSURE_LINEAGE", "CLOSURE_METHOD_FALSIFIED"): ("COMPLEXITY_DISPOSITION_REQUIRED", "NO", "SIMPLIFY_OR_JUSTIFY_COMPLEXITY"),
            ("APPROVED_CLOSURE_LINEAGE", "EQUIVALENT_SAME_FAMILY_STRUCTURAL_FALSIFICATION"): ("COMPLEXITY_DISPOSITION_REQUIRED", "NO", "SIMPLIFY_OR_JUSTIFY_COMPLEXITY"),
            ("LOCAL_OR_INCOMPLETE_DESIGN", "NO_STRONG_CLOSURE_CLAIM"): ("ORDINARY_FLOW", "NOT_APPLICABLE", "NO_CLOSURE_REVIEW"),
        }
        for key, value in expected.items():
            row = self.transition(*key)
            self.assertEqual((row["next"], row["projection"], row["action"]), value)

    def test_read_only_approval_does_not_clear_durable_gate(self):
        row = self.transition("CLOSURE_REVIEW_REQUIRED", "READ_ONLY_APPROVED_FOR_CANDIDATE_PROJECTION")
        self.assertEqual(row["next"], "CLOSURE_REVIEW_REQUIRED")
        self.assertEqual(row["projection"], "NO")
        self.assertEqual(row["action"], "DURABLE_REVIEW_RECORD_REQUIRED")

    def test_non_pr_closure_review_has_durable_record_identity(self):
        self.assertIn("top-level comment on that owning issue", self.router)
        self.assertIn("created comment id", self.router)
        self.assertIn("architecture_closure_review_identity", self.review)
        self.assertIn("review_record_target", self.context)
        self.assertIn("explicitly `not_applicable` for a pre-candidate closure review", self.context)
        self.assertIn("current_closure_review_identity", self.auto)

    def test_projection_remains_bound_and_candidate_review_stays_fresh(self):
        self.assertIn("architecture_closure_source=<exact closure artefact identity>", self.closure)
        self.assertIn("architecture_closure_review=<exact fresh review identity with approved_for_candidate_projection>", self.closure)
        self.assertIn("stop projection and return to closure analysis/review", self.implement)
        self.assertIn(
            "governing sources → closure artefact → genuinely fresh closure review "
            "→ approved closure artefact → candidate projection → genuinely fresh candidate review",
            self.plan,
        )

    def test_same_family_structural_falsification_requires_complexity_disposition(self):
        row = self.transition("APPROVED_CLOSURE_LINEAGE", "EQUIVALENT_SAME_FAMILY_STRUCTURAL_FALSIFICATION")
        self.assertEqual(row["next"], "COMPLEXITY_DISPOSITION_REQUIRED")
        self.assertIn("equivalent_same_family_structural_falsification", self.router)
        self.assertIn("equivalent_same_family_structural_falsification", self.closure)
        self.assertIn("equivalent_same_family_structural_falsification", self.review)
        self.assertIn("complexity_disposition_required", self.analysis)
        self.assertIn("local regression inside a still-sound model", self.router)

    def test_bounded_remediation_and_local_design_do_not_acquire_closure_gate(self):
        remediation = self.transition("ORDINARY_BOUNDED_REMEDIATION", "REVIEW_CHANGES_REQUIRED")
        local = self.transition("LOCAL_OR_INCOMPLETE_DESIGN", "NO_STRONG_CLOSURE_CLAIM")
        self.assertEqual(remediation["next"], "FIX_REQUIRED")
        self.assertEqual(remediation["action"], "FIX")
        readiness = self.transition("FIX_REQUIRED", "REMEDIATION_IMPLEMENTED_AND_VALIDATED")
        self.assertEqual(readiness["next"], "REMEDIATION_READINESS_REQUIRED")
        self.assertEqual(readiness["action"], "READINESS_SWEEP")
        self.assertEqual(local["action"], "NO_CLOSURE_REVIEW")
        self.assertIn("ordinary `/fix` and its remediation-readiness sweep cannot satisfy that gate", self.fix)

    def test_no_new_public_command_is_required(self):
        self.assertNotIn("/review-closure", self.router)
        self.assertIn("route `/review`", self.router)


if __name__ == "__main__":
    unittest.main()
