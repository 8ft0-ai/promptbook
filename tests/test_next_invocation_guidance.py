import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ROOT / "prompts" / "workflows"


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

    def test_router_defines_navigation_not_authority(self):
        self.assertIn("## Next-invocation guidance", self.router)
        self.assertIn("smallest safely determined next invocation", self.router_lower)
        self.assertIn("navigation metadata only", self.router_lower)
        self.assertIn("does not grant approval", self.router_lower)
        self.assertIn("receiving context must reconstruct", self.router_lower)

    def test_fresh_context_can_use_minimal_review_invocation(self):
        self.assertIn("Next chat:", self.router)
        self.assertIn("/review <exact review target>", self.router)
        self.assertIn("genuinely fresh context", self.router_lower)
        self.assertIn("durable authoritative sources", self.router_lower)
        self.assertIn("prefer an existing public shorthand invocation", self.handover_lower)
        self.assertIn("durable target is sufficient", self.handover_lower)
        self.assertIn("minimal shorthand invocation", self.handover_lower)
        self.assertIn("receiving context must refresh authoritative state", self.handover_lower)

    def test_external_execution_contract_is_not_replaced(self):
        self.assertIn("must never replace the complete commands", self.router_lower)
        self.assertIn("human-operated external execution", self.handover_lower)
        self.assertIn("do not let a shorthand next invocation replace", self.handover_lower)
        self.assertIn("complete copy/paste script or exact commands", self.handover_lower)
        self.assertIn("slash command is not a substitute", self.autonomous_lower)
        self.assertIn("complete human-operated external action", self.autonomous_lower)

    def test_bounded_review_can_append_navigation_without_continuing(self):
        self.assertIn("explicitly requested as the final deliverable", self.fresh_lower)
        self.assertIn("append one minimal `next:` invocation", self.fresh_lower)
        self.assertIn("does not execute continuation in this context", self.fresh_lower)
        self.assertIn("prefer `/go` targeting the governing objective", self.fresh_lower)
        self.assertIn("suggest `/fix` only when bounded remediation is already", self.fresh_lower)
        self.assertIn("does not grant mutation authority", self.fresh_lower)

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
