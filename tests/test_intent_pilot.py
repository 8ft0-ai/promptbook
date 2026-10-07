import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ROOT / "prompts" / "workflows"

PUBLIC_COMMANDS = ("/risk", "/reflect", "/challenge")

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

COMPOSITION_CONTRACT = {
    "target": ("exact target",),
    "provenance": ("provenance",),
    "scope": ("scope", "narrow"),
    "currentness": ("current", "stale"),
}

AUTHORITY_CONTRACT = {
    "/risk": ("no authority to accept risk", "risk assessment != risk acceptance"),
    "/reflect": ("cannot satisfy fresh independent review", "expand active scope"),
    "/challenge": ("cannot approve", "satisfy a qualified review gate"),
}


def composition_contract_holds(workflow):
    return all(
        all(marker in workflow for marker in markers)
        for markers in COMPOSITION_CONTRACT.values()
    )


def authority_contract_holds(command, workflow):
    return all(marker in workflow for marker in AUTHORITY_CONTRACT[command])


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
        self.assertIn("expand active scope", self.reflect)
        self.assertIn("no_justified_result", self.reflect)

    def test_challenge_cannot_launder_adversarial_reasoning_into_approval(self):
        self.assertIn("no_material_challenge_found", self.challenge)
        self.assertIn("is not approved", self.challenge)
        self.assertIn("cannot approve", self.challenge)
        self.assertIn("satisfy a qualified review gate", self.challenge)

    def test_pilot_uses_dedicated_workflows_not_generic_intent_runtime(self):
        for workflow in (self.risk, self.reflect, self.challenge):
            self.assertIn("read-only", workflow)
            self.assertTrue(any(term in workflow for term in ("indeterminate", "no_justified_result", "no_material_challenge_found")))
        for forbidden in ("intent registry", "intent engine", "claim database", "type checker"):
            self.assertNotIn(forbidden, self.router)

    def test_simple_repository_scenarios_are_portable_and_make_commands_distinct(self):
        semantic_markers = {
            "/risk": ("material risk", "controls", "residual risk"),
            "/reflect": ("compare expectation with outcome", "lessons", "possible follow-up"),
            "/challenge": ("assumptions being tested", "counterexamples", "surviving assumptions"),
        }
        for command, scenario in SIMPLE_REPOSITORY_SCENARIOS.items():
            self.assertIn(command, self.router)
            self.assertTrue(scenario["question"])
            self.assertGreaterEqual(len(scenario["evidence"]), 3)
            for forbidden in ("watchtower", "corpus", "memory", "github api"):
                self.assertNotIn(forbidden, repr(scenario).lower())
            workflow = {"/risk": self.risk, "/reflect": self.reflect, "/challenge": self.challenge}[command]
            for marker in semantic_markers[command]:
                self.assertIn(marker, workflow)
            self.assertIn(scenario["expected_distinction"].lower(), workflow)
            self.assertIn(scenario["terminal"].lower(), workflow)

    def test_composition_contract_is_explicit_in_each_workflow(self):
        for workflow in (self.risk, self.reflect, self.challenge):
            self.assertTrue(composition_contract_holds(workflow))

        # Challenge must state the consequence of a scope mismatch, not merely
        # mention "scope" as a dimension that could be challenged.
        self.assertIn("evidence that is current and valid only for a narrower", self.challenge)
        self.assertIn("must remain narrow through composition", self.challenge)
        self.assertIn("do not silently use it to support a broader conclusion", self.challenge)
        self.assertIn("if a requested conclusion exceeds the evidence's material scope", self.challenge)

    def test_composition_contract_negative_mutations_fail(self):
        # Each mutation removes a material protection from the real workflow
        # contract. The checker must reject every weakened contract.
        mutations = {
            "target": self.challenge.replace("exact target", "subject"),
            "provenance": self.challenge.replace("evidence provenance", "evidence source"),
            "scope": self.challenge.replace("scope", "coverage"),
            "currentness": self.challenge.replace("current", "available").replace("stale", "old"),
        }
        self.assertTrue(composition_contract_holds(self.challenge))
        for name, mutated in mutations.items():
            self.assertFalse(composition_contract_holds(mutated), name)

    def test_scope_mismatch_consequence_negative_mutations_fail(self):
        required_clauses = (
            "must remain narrow through composition",
            "do not silently use it to support a broader conclusion",
            "narrow the conclusion, report the limitation, or return an indeterminate or blocked result",
        )
        for clause in required_clauses:
            self.assertIn(clause, self.challenge)
            weakened = self.challenge.replace(clause, "")
            self.assertNotIn(clause, weakened)

    def test_authority_boundaries_survive_composition_and_negative_mutation(self):
        workflows = {"/risk": self.risk, "/reflect": self.reflect, "/challenge": self.challenge}
        for command, workflow in workflows.items():
            self.assertTrue(authority_contract_holds(command, workflow))
            for marker in AUTHORITY_CONTRACT[command]:
                weakened = workflow.replace(marker, "")
                self.assertFalse(authority_contract_holds(command, weakened), (command, marker))

    def test_public_syntax_has_observable_operator_value_over_generic_analysis(self):
        self.assertIn("/analyse", self.router)
        for command in PUBLIC_COMMANDS:
            self.assertIn(command, self.router)
        questions = {scenario["question"] for scenario in SIMPLE_REPOSITORY_SCENARIOS.values()}
        distinctions = {scenario["expected_distinction"] for scenario in SIMPLE_REPOSITORY_SCENARIOS.values()}
        terminals = {scenario["terminal"] for scenario in SIMPLE_REPOSITORY_SCENARIOS.values()}
        self.assertEqual(3, len(questions))
        self.assertEqual(3, len(distinctions))
        self.assertEqual(3, len(terminals))


if __name__ == "__main__":
    unittest.main()
