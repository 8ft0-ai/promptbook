import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ROOT / "prompts" / "workflows"

PUBLIC_COMMANDS = ("/risk", "/reflect", "/challenge")


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
        self.assertIn("is not `approved`", self.challenge)
        self.assertIn("cannot approve", self.challenge)
        self.assertIn("cannot", self.challenge)
        self.assertIn("satisfy a qualified review gate", self.challenge)

    def test_pilot_uses_dedicated_workflows_not_generic_intent_runtime(self):
        for workflow in (self.risk, self.reflect, self.challenge):
            self.assertIn("authority boundary", workflow)
            self.assertIn("terminal behaviour", workflow)
        for forbidden in ("intent registry", "intent engine", "claim database", "type checker"):
            self.assertNotIn(forbidden, self.router)


if __name__ == "__main__":
    unittest.main()
