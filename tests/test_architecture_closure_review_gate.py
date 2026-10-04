import unittest
from collections import defaultdict, deque
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
        rows[key] = {
            "current": current,
            "event": event,
            "next": next_state,
            "projection": projection,
            "action": action,
        }
    return rows


def reachable(rows, start, target, forbidden_events=()):
    graph = defaultdict(list)
    forbidden = set(forbidden_events)
    for row in rows.values():
        if row["event"] not in forbidden:
            graph[row["current"]].append(row["next"])
    seen = {start}
    queue = deque([start])
    while queue:
        current = queue.popleft()
        if current == target:
            return True
        for nxt in graph[current]:
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    return False


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

    def test_positive_path_reaches_candidate_review_only_through_closure_and_readiness(self):
        sequence = [
            ("ARCHITECTURE_CLOSURE_ANALYSIS_REQUIRED", "READY_CLOSURE_SNAPSHOT_FROZEN", "CLOSURE_REVIEW_REQUIRED"),
            ("CLOSURE_REVIEW_REQUIRED", "DURABLE_APPROVED_FOR_CURRENT_SNAPSHOT_RECORDED", "CLOSURE_APPROVED"),
            ("CLOSURE_APPROVED", "CANDIDATE_AUTHORITY_CURRENT", "CANDIDATE_PROJECTION_ELIGIBLE"),
            ("CANDIDATE_PROJECTION_ELIGIBLE", "CANDIDATE_PROJECTED_WITHIN_APPROVED_UNIVERSE", "CANDIDATE_READINESS_REQUIRED"),
            ("CANDIDATE_READINESS_REQUIRED", "VALIDATION_AND_READINESS_COMPLETE", "CANDIDATE_REVIEW_REQUIRED"),
        ]
        for current, event, nxt in sequence:
            self.assertEqual(self.transition(current, event)["next"], nxt)

    def test_changes_required_has_positive_recovery_to_new_snapshot_and_review(self):
        self.assertEqual(
            self.transition("CLOSURE_REVIEW_REQUIRED", "DURABLE_CHANGES_REQUIRED_RECORDED")["next"],
            "CLOSURE_RECONSTRUCTION_REQUIRED",
        )
        self.assertEqual(
            self.transition("CLOSURE_RECONSTRUCTION_REQUIRED", "READY_CLOSURE_SNAPSHOT_FROZEN")["next"],
            "CLOSURE_REVIEW_REQUIRED",
        )
        self.assertTrue(reachable(self.transitions, "CLOSURE_RECONSTRUCTION_REQUIRED", "CANDIDATE_REVIEW_REQUIRED"))

    def test_durable_approval_is_the_only_route_from_review_gate_to_projection_eligibility(self):
        self.assertFalse(
            reachable(
                self.transitions,
                "CLOSURE_REVIEW_REQUIRED",
                "CANDIDATE_PROJECTION_ELIGIBLE",
                forbidden_events={"DURABLE_APPROVED_FOR_CURRENT_SNAPSHOT_RECORDED"},
            )
        )
        row = self.transition("CLOSURE_REVIEW_REQUIRED", "READ_ONLY_APPROVED_FOR_CANDIDATE_PROJECTION")
        self.assertEqual((row["next"], row["projection"]), ("CLOSURE_REVIEW_REQUIRED", "NO"))

    def test_new_projection_semantics_require_reconstruction_before_re_review(self):
        row = self.transition("CANDIDATE_PROJECTION_ELIGIBLE", "NEW_DECISION_CRITICAL_SEMANTICS")
        self.assertEqual((row["next"], row["action"]), ("CLOSURE_RECONSTRUCTION_REQUIRED", "ANALYSE_CLOSURE"))
        self.assertNotEqual(row["next"], "CLOSURE_REVIEW_REQUIRED")
        self.assertEqual(
            self.transition("CLOSURE_RECONSTRUCTION_REQUIRED", "READY_CLOSURE_SNAPSHOT_FROZEN")["next"],
            "CLOSURE_REVIEW_REQUIRED",
        )

    def test_snapshot_or_review_movement_revokes_projection_eligibility(self):
        self.assertEqual(
            self.transition("CANDIDATE_PROJECTION_ELIGIBLE", "CLOSURE_SNAPSHOT_CHANGED")["next"],
            "CLOSURE_RECONSTRUCTION_REQUIRED",
        )
        self.assertEqual(
            self.transition("CANDIDATE_PROJECTION_ELIGIBLE", "CLOSURE_REVIEW_RECORD_CHANGED_OR_INVALID")["next"],
            "CLOSURE_REVIEW_REQUIRED",
        )
        self.assertEqual(
            self.transition("CANDIDATE_PROJECTION_ELIGIBLE", "GOVERNING_SCOPE_CHANGED")["next"],
            "ARCHITECTURE_CLOSURE_ANALYSIS_REQUIRED",
        )

    def test_candidate_projection_requires_readiness_before_fresh_candidate_review(self):
        projected = self.transition(
            "CANDIDATE_PROJECTION_ELIGIBLE",
            "CANDIDATE_PROJECTED_WITHIN_APPROVED_UNIVERSE",
        )
        self.assertEqual(
            (projected["next"], projected["action"]),
            ("CANDIDATE_READINESS_REQUIRED", "VALIDATE_AND_READINESS"),
        )
        ready = self.transition("CANDIDATE_READINESS_REQUIRED", "VALIDATION_AND_READINESS_COMPLETE")
        self.assertEqual(
            (ready["next"], ready["action"]),
            ("CANDIDATE_REVIEW_REQUIRED", "FRESH_CANDIDATE_REVIEW"),
        )

    def test_mutable_comment_locator_is_not_treated_as_snapshot_identity(self):
        for text in (self.router, self.review, self.context):
            self.assertIn("locator", text)
            self.assertIn("edit-sensitive", text)
        self.assertIn("append-only evidence", self.review)
        self.assertIn("in-place edit", self.review)
        self.assertIn("review_target_snapshot_identity_when_mutable", self.context)

    def test_canonical_closure_workflow_contains_no_direct_artefact_to_candidate_bypass(self):
        self.assertNotIn("closure artefact\n→ closure-ready candidate", self.closure)
        self.assertIn("frozen closure snapshot", self.closure)
        self.assertIn("genuinely fresh closure review", self.closure)
        self.assertIn("validation/readiness as applicable", self.closure)

    def test_same_family_structural_falsification_requires_complexity_disposition(self):
        row = self.transition("APPROVED_CLOSURE_LINEAGE", "EQUIVALENT_SAME_FAMILY_STRUCTURAL_FALSIFICATION")
        self.assertEqual(row["next"], "COMPLEXITY_DISPOSITION_REQUIRED")
        self.assertIn("equivalent_same_family_structural_falsification", self.router)
        self.assertIn("equivalent_same_family_structural_falsification", self.closure)
        self.assertIn("complexity_disposition_required", self.analysis)

    def test_bounded_remediation_and_local_design_do_not_acquire_closure_gate(self):
        remediation = self.transition("ORDINARY_BOUNDED_REMEDIATION", "REVIEW_CHANGES_REQUIRED")
        local = self.transition("LOCAL_OR_INCOMPLETE_DESIGN", "NO_STRONG_CLOSURE_CLAIM")
        self.assertEqual((remediation["next"], remediation["action"]), ("FIX_REQUIRED", "FIX"))
        readiness = self.transition("FIX_REQUIRED", "REMEDIATION_IMPLEMENTED_AND_VALIDATED")
        self.assertEqual(
            (readiness["next"], readiness["action"]),
            ("REMEDIATION_READINESS_REQUIRED", "READINESS_SWEEP"),
        )
        self.assertEqual(local["action"], "NO_CLOSURE_REVIEW")
        self.assertIn("ordinary `/fix` and its remediation-readiness sweep cannot satisfy that gate", self.fix)

    def test_no_new_public_command_is_required(self):
        self.assertNotIn("/review-closure", self.router)
        self.assertIn("route `/review`", self.router)


if __name__ == "__main__":
    unittest.main()
