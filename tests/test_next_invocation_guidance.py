import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ROOT / "prompts" / "workflows"
ENGINEERING = ROOT / "prompts" / "engineering"
DOCUMENTATION = ROOT / "prompts" / "documentation"


class NextInvocationGuidanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.router = (WORKFLOWS / "README.md").read_text(encoding="utf-8")
        cls.router_lower = cls.router.lower()
        cls.fresh = (WORKFLOWS / "fresh-independent-review.md").read_text(
            encoding="utf-8"
        )
        cls.fresh_lower = cls.fresh.lower()
        cls.handover = (WORKFLOWS / "next-session-handover.md").read_text(
            encoding="utf-8"
        )
        cls.handover_lower = cls.handover.lower()
        cls.autonomous = (WORKFLOWS / "autonomous-progression.md").read_text(
            encoding="utf-8"
        )
        cls.autonomous_lower = cls.autonomous.lower()
        cls.documentation_assessment = (
            WORKFLOWS / "documentation-assessment.md"
        ).read_text(encoding="utf-8")
        cls.documentation_assessment_lower = cls.documentation_assessment.lower()
        cls.plan = (ENGINEERING / "plan-an-issue.md").read_text(encoding="utf-8")
        cls.plan_lower = cls.plan.lower()
        cls.implement = (ENGINEERING / "implement-an-approved-issue.md").read_text(
            encoding="utf-8"
        )
        cls.implement_lower = cls.implement.lower()
        cls.remediate = (ENGINEERING / "remediate-review-findings.md").read_text(
            encoding="utf-8"
        )
        cls.remediate_lower = cls.remediate.lower()
        cls.repository_assessment = (
            DOCUMENTATION / "repository-assessment.md"
        ).read_text(encoding="utf-8")
        cls.repository_assessment_lower = cls.repository_assessment.lower()

    def test_router_defines_navigation_not_authority(self):
        self.assertIn("## Next-invocation guidance", self.router)
        self.assertIn("smallest safely determined next invocation", self.router_lower)
        self.assertIn("navigation metadata only", self.router_lower)
        self.assertIn("does not grant approval", self.router_lower)
        self.assertIn("receiving context must reconstruct", self.router_lower)

    def test_router_owns_continuation_policy(self):
        self.assertIn("## Continuation policy", self.router)
        self.assertIn(
            "continuation mode is a preference layer owned by this router",
            self.router_lower,
        )
        self.assertIn(
            "a specialised workflow's local output, disposition, implementation record, "
            "remediation record, or other workflow record is not permission to end a "
            "routed objective",
            self.router_lower,
        )
        for mode in ("`auto`", "`suggest`", "`stop`"):
            self.assertIn(mode, self.router)
        self.assertIn("hard constraints always win over continuation preferences", self.router_lower)
        self.assertIn("a continuation preference cannot create or bypass", self.router_lower)
        self.assertIn("navigation emitted under `suggest` or `stop`", self.router_lower)
        self.assertIn("never supplies authority to the receiving invocation", self.router_lower)

    def test_command_continuation_defaults_are_explicit(self):
        expected = {
            "/go": "auto",
            "/implement": "auto",
            "/fix": "auto",
            "/review": "suggest",
            "/plan": "suggest",
            "/status": "stop",
            "/handoff": "stop",
        }
        for command, mode in expected.items():
            self.assertIn(f"| `{command}` | `{mode}` |", self.router)

    def test_continuation_precedence_is_fail_closed(self):
        ordered_markers = [
            "explicit current-user qualifier",
            "repository/task-specific continuation preference",
            "managed project continuation preference",
            "promptbook command default",
        ]
        positions = [self.router_lower.index(marker) for marker in ordered_markers]
        self.assertEqual(sorted(positions), positions)
        for hard_constraint in (
            "platform safety",
            "explicit task authority",
            "repository-local mandatory policy",
            "fresh-independence requirements",
            "required validation",
            "current authoritative evidence",
            "accepted governance records that require a stop or hand-off",
        ):
            self.assertIn(hard_constraint, self.router_lower)
        self.assertIn(
            "a lower-precedence preference may choose only among actions already permitted",
            self.router_lower,
        )

    def test_autonomous_progression_applies_effective_mode(self):
        self.assertIn("resolve the effective continuation mode from the workflow router", self.autonomous_lower)
        self.assertIn("apply all hard governance constraints first", self.autonomous_lower)
        self.assertIn("continuation mode is only a preference", self.autonomous_lower)
        self.assertIn("a specialised workflow's local disposition or record is a workflow record", self.autonomous_lower)
        self.assertIn("return control to the router", self.autonomous_lower)
        self.assertIn("under `auto`, continue the next authorised workflow", self.autonomous_lower)
        self.assertIn("eligible isolated fresh-review context", self.autonomous_lower)
        self.assertIn("under `suggest`, emit the smallest safe navigation", self.autonomous_lower)
        self.assertIn("under `stop`, end the requested deliverable", self.autonomous_lower)

    def test_router_reachable_specialised_workflow_matrix(self):
        matrix = {
            "plan": (
                self.plan_lower,
                "that disposition is the planning record",
                "return control to the router",
            ),
            "implement": (
                self.implement_lower,
                "that implementation record is the workflow record",
                "return control to the router",
            ),
            "remediate": (
                self.remediate_lower,
                "that remediation record is the workflow record",
                "return control to the router",
            ),
            "fresh review": (
                self.fresh_lower,
                "single disposition is the review record",
                "return control to that workflow",
            ),
            "handover": (
                self.handover_lower,
                "first distinguish the handover type",
                "directly copyable as the next prompt",
            ),
            "documentation assessment": (
                self.documentation_assessment_lower,
                "assessment does not create target-repository mutation authority",
                "return control to promptbook's normal workflow router",
            ),
            "repository assessment": (
                self.repository_assessment_lower,
                "return one primary result: complete, partial, blocked, or not tested",
                "smallest sufficient next action",
            ),
        }
        for name, (text, record_marker, composition_marker) in matrix.items():
            with self.subTest(workflow=name):
                self.assertIn(record_marker, text)
                self.assertIn(composition_marker, text)

    def test_documentation_assessment_paths_obey_router_postcondition(self):
        self.assertIn(
            "[documentation assessment workflow](documentation-assessment.md)",
            self.router_lower,
        )
        self.assertIn(
            "[repository documentation assessment](../documentation/repository-assessment.md)",
            self.router_lower,
        )
        self.assertIn(
            "return control to promptbook's normal workflow router",
            self.documentation_assessment_lower,
        )
        self.assertIn(
            "return one primary result: complete, partial, blocked, or not tested",
            self.repository_assessment_lower,
        )
        self.assertIn(
            "a specialised workflow's local output, disposition, implementation record, "
            "remediation record, or other workflow record is not permission to end a "
            "routed objective",
            self.router_lower,
        )
        self.assertIn("apply the effective continuation mode", self.router_lower)

    def test_plan_and_go_positive_composition(self):
        self.assertIn("| `/plan` | `suggest` |", self.router)
        self.assertIn("that disposition is the planning record", self.plan_lower)
        self.assertIn("does not itself grant implementation", self.plan_lower)
        self.assertIn("| `/go` | `auto` |", self.router)
        self.assertIn("not permission to end a routed objective", self.router_lower)
        self.assertIn("enter the next safely authorised and executable workflow automatically", self.router_lower)
        self.assertIn("eligible genuinely isolated fresh-review context", self.router_lower)

    def test_implementation_and_fix_preserve_fresh_review_boundary(self):
        self.assertIn("required independent review is the next gate", self.implement_lower)
        self.assertIn("preserve the fresh-context boundary", self.implement_lower)
        self.assertIn("eligible genuinely isolated fresh-review context", self.implement_lower)
        self.assertIn("next chat: /review <approved_task>", self.implement_lower)
        self.assertIn("| `/fix` | `auto` |", self.router)
        self.assertIn("independent re-review is required", self.remediate_lower)
        self.assertIn("hard fresh-context boundary", self.remediate_lower)
        self.assertIn("eligible genuinely isolated fresh-review context", self.remediate_lower)
        self.assertIn("next chat: /review <reviewed_candidate>", self.remediate_lower)

    def test_review_default_and_explicit_override_are_composable(self):
        self.assertIn("| `/review` | `suggest` |", self.router)
        self.assertIn("explicitly requested as the final deliverable", self.fresh_lower)
        self.assertIn("append one minimal `next:` invocation", self.fresh_lower)
        self.assertIn("continue afterwards", self.router_lower)
        self.assertIn("explicit current-user qualifier", self.router_lower)
        self.assertIn("return control to that workflow", self.fresh_lower)

    def test_auto_cannot_bypass_hard_boundaries(self):
        for boundary in (
            "fresh independence",
            "missing authority",
            "failed or missing required validation",
            "materially changed accepted proposals",
            "repository/task policy requiring an explicit stop",
        ):
            self.assertIn(boundary, self.autonomous_lower)
        self.assertIn("`auto` must not cross them", self.autonomous_lower)
        self.assertIn("eligible isolated review context satisfies the freshness boundary", self.autonomous_lower)
        for terminal_state in (
            "EXTERNAL_REQUIRED",
            "DECISION_REQUIRED",
            "BLOCKED",
            "COMPLETE",
        ):
            self.assertIn(terminal_state, self.autonomous)
        self.assertIn("human-operated external execution", self.handover_lower)
        self.assertIn("slash command is not a substitute", self.autonomous_lower)
        self.assertIn("does not create new mutation, merge, production, close, or acceptance authority", self.autonomous_lower)

    def test_fresh_context_can_use_minimal_review_invocation(self):
        self.assertIn("Next chat:", self.router)
        self.assertIn("/review <exact review target>", self.router)
        self.assertIn("genuinely fresh-review boundary", self.router_lower)
        self.assertIn("durably identifiable", self.router_lower)
        self.assertIn("manual fallback", self.router_lower)
        self.assertIn("prefer an existing public shorthand invocation", self.handover_lower)
        self.assertIn("durable target is sufficient", self.handover_lower)
        self.assertIn("minimal result may be a `next chat:` invocation", self.handover_lower)
        self.assertIn("receiving context must refresh authoritative state", self.handover_lower)

    def test_external_execution_contract_is_not_replaced(self):
        self.assertIn("must never replace the complete commands", self.router_lower)
        self.assertIn("human-operated external execution", self.handover_lower)
        self.assertIn("do not let a shorthand next invocation replace", self.handover_lower)
        self.assertIn("complete copy/paste script or exact commands", self.handover_lower)
        self.assertIn("slash command is not a substitute", self.autonomous_lower)
        self.assertIn("complete human-operated external action", self.autonomous_lower)

    def test_bounded_review_requires_safe_navigation_without_continuing(self):
        self.assertIn("explicitly requested as the final deliverable", self.fresh_lower)
        self.assertIn(
            "when the broader governed objective remains active and the next invocation "
            "is safely determined from durable authoritative state, append one minimal "
            "`next:` invocation",
            self.fresh_lower,
        )
        self.assertNotIn("may append one minimal `next:` invocation", self.fresh_lower)
        self.assertNotIn("may also provide minimal navigation", self.fresh_lower)
        self.assertIn("does not execute continuation in this context", self.fresh_lower)
        self.assertIn("does not grant mutation authority", self.fresh_lower)

    def test_bounded_review_positive_next_routes_preserve_authority(self):
        self.assertIn(
            "if the disposition is approved, prefer `/go` targeting the governing objective",
            self.fresh_lower,
        )
        self.assertIn(
            "if the disposition is changes required, suggest `/fix` only when bounded "
            "remediation is already the safely authorised next path",
            self.fresh_lower,
        )
        self.assertIn(
            "otherwise expose the actual decision, blocker, or external boundary instead "
            "of manufacturing remediation authority",
            self.fresh_lower,
        )

    def test_target_selection_prefers_governing_lifecycle(self):
        self.assertIn("prefer the governing lifecycle object", self.router_lower)
        self.assertIn("rather than the reviewed intermediate artefact", self.router_lower)
        self.assertIn("prefer the governing objective for `/go`", self.autonomous_lower)

    def test_terminal_states_fail_closed(self):
        self.assertIn("must not be bypassed by a slash command", self.router_lower)
        self.assertIn("`blocked` must not manufacture", self.router_lower)
        self.assertIn("`complete` must state that no further action is required", self.router_lower)
        self.assertIn("if decision_required applies", self.autonomous_lower)
        self.assertIn("if blocked applies", self.autonomous_lower)
        self.assertIn("if complete applies, state that no further action is required", self.autonomous_lower)

    def test_public_shorthand_vocabulary_is_unchanged(self):
        commands = set(
            re.findall(r"^- `(/[-a-z]+)(?:\s[^`]*)?`", self.router, flags=re.MULTILINE)
        )
        self.assertEqual(
            {
                "/go",
                "/review",
                "/plan",
                "/implement",
                "/fix",
                "/handoff",
                "/status",
            },
            commands,
        )


if __name__ == "__main__":
    unittest.main()
