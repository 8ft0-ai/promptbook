import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ProjectBoundaryGuardTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.bootstrap = (ROOT / "BOOTSTRAP").read_text(encoding="utf-8")
        cls.bootstrap_lower = cls.bootstrap.lower()
        cls.guide = (ROOT / "guides" / "project-bootstrap.md").read_text(
            encoding="utf-8"
        )
        cls.guide_lower = cls.guide.lower()

    def test_project_identity_is_explicit(self):
        self.assertIn("CURRENT_PROJECT", self.bootstrap)
        self.assertIn("name: <PROJECT_NAME>", self.bootstrap)
        self.assertIn("primary_repository: <OWNER/REPOSITORY>", self.bootstrap)
        self.assertIn("PERMITTED_CROSS_PROJECT_REFERENCES", self.bootstrap)

    def test_guard_runs_before_tools_or_substantive_execution(self):
        self.assertIn("before any substantive analysis", self.bootstrap_lower)
        self.assertIn("external tool call", self.bootstrap_lower)
        self.assertIn("do not use tools to decide the preflight", self.bootstrap_lower)
        self.assertIn("perform no substantive work", self.bootstrap_lower)
        self.assertIn("repository read", self.bootstrap_lower)
        self.assertIn("mutation", self.bootstrap_lower)

    def test_guard_defines_required_outcomes_and_acknowledgement(self):
        for outcome in ("MATCH", "PROJECT_MISMATCH", "PROJECT_AMBIGUOUS"):
            self.assertIn(outcome, self.bootstrap)

        self.assertIn("insufficient evidence to establish", self.bootstrap_lower)
        self.assertIn("ACKNOWLEDGE", self.bootstrap)
        self.assertIn("exact blocked instruction", self.bootstrap_lower)
        self.assertIn("consumed once", self.bootstrap_lower)
        self.assertIn("does not disable this preflight for later prompts", self.bootstrap_lower)
        self.assertIn("materially new work", self.bootstrap_lower)

    def test_shared_references_do_not_become_work_targets(self):
        self.assertIn("incidental documentation, workflow, dependency", self.bootstrap_lower)
        self.assertIn("suppresses false positives for legitimate references only", self.bootstrap_lower)
        self.assertIn("never authorises one of those projects as the work target", self.bootstrap_lower)
        self.assertIn("explicit work-target language still wins", self.guide_lower)

    def test_guard_does_not_require_cross_project_memory(self):
        self.assertIn("do not depend on cross-project memory", self.bootstrap_lower)
        self.assertIn("does not depend on cross-project memory", self.guide_lower)
        self.assertIn("explicit project instructions are the source of truth", self.guide_lower)

    def test_warning_contract_is_documented(self):
        self.assertIn("PROJECT_MISMATCH — acknowledgement required", self.guide)
        self.assertIn("Current project:", self.guide)
        self.assertIn("Apparent target:", self.guide)
        self.assertIn("Reason:", self.guide)
        self.assertIn(
            "No substantive work, repository reads, external tool calls or mutations have been performed",
            self.guide,
        )
        self.assertIn("Recommended: STOP", self.guide)
        self.assertIn("ACKNOWLEDGE — proceed with this blocked instruction here anyway", self.guide)
        self.assertIn("STOP — do not execute it", self.guide)

    def test_required_regression_scenarios_are_documented(self):
        self.assertIn("## Regression scenarios", self.guide)
        for scenario in (
            "Matched",
            "Mismatched",
            "Ambiguous",
            "Insufficient target evidence",
            "Shared reference",
            "Intentional cross-project override",
        ):
            self.assertIn(f"| {scenario} |", self.guide)

        self.assertIn("`MATCH`; proceed silently", self.guide)
        self.assertIn("`PROJECT_MISMATCH`; no tool use; acknowledgement required", self.guide)
        self.assertIn("`PROJECT_AMBIGUOUS`; no tool use; acknowledgement required", self.guide)
        self.assertIn("later prompts are checked again", self.guide_lower)

    def test_missing_explicit_target_does_not_create_routine_friction(self):
        self.assertIn(
            "a prompt that merely omits a project name is not ambiguous",
            self.bootstrap_lower,
        )
        self.assertIn(
            "absence of a repository name by itself must not create friction",
            self.guide_lower,
        )
        self.assertIn(
            "a genuinely new instruction with insufficient evidence",
            self.guide_lower,
        )


if __name__ == "__main__":
    unittest.main()
