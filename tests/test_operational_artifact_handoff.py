import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "prompts" / "workflows" / "operational-artifact-handoff.md"
AUTONOMOUS = ROOT / "prompts" / "workflows" / "autonomous-progression.md"
HANDOVER = ROOT / "prompts" / "workflows" / "next-session-handover.md"


class OperationalArtifactHandoffTests(unittest.TestCase):
    def test_consuming_workflows_bind_the_shared_contract(self):
        for path in (AUTONOMOUS, HANDOVER):
            text = path.read_text(encoding="utf-8")
            lower = text.lower()
            self.assertIn("operational-artifact-handoff.md", text)
            self.assertIn("genuinely atomic", lower)
            self.assertIn("transcript-independent", lower)
            self.assertIn("materialised/downloadable artifact", lower)
            self.assertIn("result", lower)
            self.assertIn("evidence", lower)
            self.assertIn("unavailable", lower)
            self.assertIn("large fragile transcript", lower)

    def test_selection_authority_integrity_and_evidence_scenarios(self):
        text = CONTRACT.read_text(encoding="utf-8")
        lower = text.lower()

        scenarios = {
            "atomic inline command": (
                "genuinely atomic",
                "keep genuinely atomic commands inline",
            ),
            "multi-stage shell or python diagnostic": (
                "multi-stage variable or environment setup",
                "multi-command diagnostics or reconciliation",
                "substantial embedded programs",
            ),
            "heredoc or interpreter risk": (
                "heredocs or nested quoting",
                "shell/interpreter transitions",
            ),
            "downloads staging into configured artifact home": (
                "browser downloads location may be treated as an inbox",
                "${chatgpt_artifact_home:-$home/chatgpt}",
            ),
            "creation timestamp versus execution timestamp": (
                "artifact creation time",
                "execution/evidence time",
            ),
            "checksum mismatch": (
                "sha-256",
                "require a mismatch to fail closed",
            ),
            "destination collision": (
                "fail closed on destination collisions",
                "do not silently overwrite",
            ),
            "read-only authority preservation": (
                "a read-only task must remain read-only",
                "artifact delivery changes the hand-off mechanism, not authority",
            ),
            "separately authorised mutation with fail-closed guards": (
                "a separately authorised mutation must still fail closed",
                "authority guard",
            ),
            "bounded evidence hand-back": (
                "bounded continuation evidence",
                "result",
                "evidence",
            ),
            "30-day expiry and tidy dry-run default": (
                "30-day expiry",
                "dry-run-first",
                "ordinary operational artifacts must not autonomously delete other artifacts",
            ),
            "unavailable-download degraded path": (
                "if downloadable-file delivery is unavailable",
                "do not silently fall back to a large fragile transcript-dependent executable program",
                "already-governed repository-owned or shared tooling",
                "independently safe atomic commands",
            ),
        }

        for name, expected_phrases in scenarios.items():
            with self.subTest(name=name):
                for phrase in expected_phrases:
                    self.assertIn(phrase, lower)

    def test_defaults_are_portable_recommendations_not_authority(self):
        lower = CONTRACT.read_text(encoding="utf-8").lower()

        for phrase in (
            "recommended defaults/examples rather than universal workflow law",
            "model- and operating-system-neutral",
            "sha-256 establishes byte identity/integrity only",
            "not proof of trust, safety, review, authenticity, supply-chain provenance, or execution authority",
            "other clients and operating systems may use an equivalent configured user-local home",
            "do not assume posix path syntax",
            "macos, linux, windows, desktop, web, and mobile clients",
            "preserve operating-system and client security protections",
            "keep/ is not permanent engineering storage",
            "promoted through normal governance into repository-owned or explicitly governed shared tooling",
        ):
            self.assertIn(phrase, lower)


if __name__ == "__main__":
    unittest.main()
