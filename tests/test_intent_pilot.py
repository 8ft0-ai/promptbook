import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ROOT / "prompts" / "workflows"

PUBLIC_COMMANDS = ("/risk", "/reflect", "/challenge")

# Scenario evidence is deliberately data-only: these are ordinary repository facts,
# not Watchtower/Corpus state, memory, review APIs, or a portfolio-specific runtime.
SIMPLE_REPOSITORY_SCENARIOS = {
    "/risk": {
        "question": "Should this repository change its release script?",
        "evidence": ("release script", "failing smoke test", "maintainer note"),
        "expected_distinction": "risk assessment != risk acceptance",
        "terminal": "INDETERMINATE",
    },
    "/reflect": {
        "question": "What did issue #7 teach us after its tests passed?",
        "evidence": ("issue #7 objective", "test result", "implementation notes"),
        "expected_distinction": "reflection is not fresh independent review",
        "terminal": "NO_JUSTIFIED_RESULT",
    },
    "/challenge": {
        "question": "Challenge the assumption that the README change is sufficient.",
        "evidence": ("README diff", "documented requirement", "link check"),
        "expected_distinction": "NO_MATERIAL_CHALLENGE_FOUND is not APPROVED",
        "terminal": "NO_MATERIAL_CHALLENGE_FOUND",
    },
}


class IntentPilotTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.router = (WORKFLOWS / "README.md").read_text(encoding="utf-8").lower()
        cls.readme = (ROOT / "README.md").read_text(encoding="utf-8").lower()
        cls.guide = (ROOT / "guides" / "project-bootstrap.md").read_text(encoding="utf-8").lower()
        cls.agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8").lower()
        cls.risk = (WORKFLOWS / "assess-risk.md").read_text(encoding="utf-8").lower()
        cls.reflect = (WORKFLOWS / "reflect-on-work.md").read_text(encoding="utf-8").lower()
        cls.challenge = (WORKFLOWS / "challenge-assumptions.md").read_text(encoding="utf-8").lower()

    def test_public_surfaces_advertise_pilot_commands(self):
        for command in PUBLIC_COMMANDS:
            for surface in (self.router, self.readme, self.guide, self.agents):
                self.assertIn(command, surface)

    def test_router_keeps_pilot_intents_read_only_and_distinct(self):
        self.assertIn("/risk [target-or-question]", self.router)
        self.assertIn("/reflect [target-or-episode]", self.router)
        self.assertIn("/challenge [target-or-proposal]", self.router)
        self.assertIn("risk assessment does not accept risk", self.router)
        self.assertIn("cannot satisfy fresh independent review", self.router)
        self.assertIn("cannot approve a candidate", self.router)

    def test_risk_preserves_assessment_acceptance_and_invariant_boundaries(self):
        self.assertIn("risk assessment != risk acceptance", self.risk)
        self.assertIn("risk acceptance != invariant satisfaction", self.risk)
        self.assertIn("cannot make a violated hard requirement true", self.risk)
        self.assertIn("indeterminate", self.risk)
        self.assertIn("no authority to accept risk", self.risk)

    def test_reflection_cannot_launder_self_assessment_into_review_or_scope(self):
        self.assertIn("reflection is not fresh independent review", self.reflect)
        self.assertIn("cannot satisfy fresh independent review", self.reflect)
        self.assertIn("cannot", self.reflect)
        self.assertIn("expand active scope", self.reflect)
        self.assertIn("no_justified_result", self.reflect)

    def test_challenge_cannot_launder_adversarial_reasoning_into_approval(self):
        self.assertIn("no_material_challenge_found", self.challenge)
        self.assertIn("is not approved", self.challenge)
        self.assertIn("cannot approve", self.challenge)
        self.assertIn("cannot", self.challenge)
        self.assertIn("satisfy a qualified review gate", self.challenge)

    def test_pilot_uses_dedicated_workflows_not_generic_intent_runtime(self):
        for workflow in (self.risk, self.reflect, self.challenge):
            self.assertIn("read-only", workflow)
            self.assertTrue(any(term in workflow for term in ("indeterminate", "no_justified_result", "no_material_challenge_found")))
        for forbidden in ("intent registry", "intent engine", "claim database", "type checker"):
            self.assertNotIn(forbidden, self.router)

    def test_simple_repository_scenarios_are_portable_and_make_commands_distinct(self):
        expected_questions = {
            "/risk": "what material risk",
            "/reflect": "what did this episode teach",
            "/challenge": "which assumptions",
        }
        for command, scenario in SIMPLE_REPOSITORY_SCENARIOS.items():
            self.assertIn(command, self.router)
            self.assertTrue(scenario["question"])
            self.assertGreaterEqual(len(scenario["evidence"]), 3)
            self.assertNotIn("watchtower", repr(scenario).lower())
            self.assertNotIn("corpus", repr(scenario).lower())
            self.assertNotIn("memory", repr(scenario).lower())
            self.assertNotIn("github api", repr(scenario).lower())
            workflow = {
                "/risk": self.risk,
                "/reflect": self.reflect,
                "/challenge": self.challenge,
            }[command]
            self.assertIn(expected_questions[command], workflow)
            self.assertIn(scenario["expected_distinction"].lower(), workflow)
            self.assertIn(scenario["terminal"].lower(), workflow)

    def test_composition_preserves_target_scope_provenance_and_currentness(self):
        composition_cases = (
            {
                "name": "stale exact target",
                "input": {"target": "commit-a", "provenance": "test result", "current": False, "scope": "commit-a"},
                "consumer_target": "commit-b",
                "required": "stale_input",
            },
            {
                "name": "narrow evidence",
                "input": {"target": "file-a", "provenance": "file check", "current": True, "scope": "file-a"},
                "consumer_target": "repository",
                "required": "scope_preserved",
            },
            {
                "name": "same target current evidence",
                "input": {"target": "issue-7", "provenance": "issue evidence", "current": True, "scope": "issue-7"},
                "consumer_target": "issue-7",
                "required": "provenance_preserved",
            },
        )

        for case in composition_cases:
            source = case["input"]
            if not source["current"] or source["target"] != case["consumer_target"]:
                disposition = "stale_input"
            elif source["scope"] != case["consumer_target"]:
                disposition = "scope_preserved"
            else:
                disposition = "provenance_preserved"
            self.assertEqual(case["required"], disposition, case["name"])

        for workflow in (self.risk, self.reflect, self.challenge):
            self.assertIn("provenance", workflow)
            self.assertTrue("current" in workflow or "stale" in workflow)
        self.assertIn("scope", self.risk)
        self.assertIn("scope", self.reflect)
        self.assertIn("scope", self.challenge)

    def test_public_syntax_has_observable_operator_value_over_generic_analysis(self):
        # The public commands encode three different questions and terminal semantics;
        # /analyse remains the compatibility fallback rather than erasing those distinctions.
        self.assertIn("/analyse", self.router)
        self.assertIn("generic", self.router)
        questions = {scenario["question"] for scenario in SIMPLE_REPOSITORY_SCENARIOS.values()}
        distinctions = {scenario["expected_distinction"] for scenario in SIMPLE_REPOSITORY_SCENARIOS.values()}
        terminals = {scenario["terminal"] for scenario in SIMPLE_REPOSITORY_SCENARIOS.values()}
        self.assertEqual(3, len(questions))
        self.assertEqual(3, len(distinctions))
        self.assertEqual(3, len(terminals))


if __name__ == "__main__":
    unittest.main()
