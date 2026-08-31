import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class CapabilityAvailabilityCarrierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.availability = (
            ROOT / "prompts" / "workflows" / "capability-availability-overrides.md"
        ).read_text(encoding="utf-8")
        cls.availability_lower = cls.availability.lower()
        cls.context = (
            ROOT / "prompts" / "workflows" / "resolved-agent-run-context.md"
        ).read_text(encoding="utf-8")
        cls.context_lower = cls.context.lower()
        cls.progression = (
            ROOT / "prompts" / "workflows" / "autonomous-progression.md"
        ).read_text(encoding="utf-8")
        cls.progression_lower = cls.progression.lower()
        cls.projection = (
            ROOT / "prompts" / "workflows" / "executor-capability-projection.md"
        ).read_text(encoding="utf-8")
        cls.projection_lower = cls.projection.lower()
        cls.guide = (
            ROOT / "guides" / "capability-availability-configuration.md"
        ).read_text(encoding="utf-8")
        cls.guide_lower = cls.guide.lower()
        cls.using = (ROOT / "guides" / "using-promptbook.md").read_text(
            encoding="utf-8"
        )
        cls.using_lower = cls.using.lower()
        cls.bootstrap = (ROOT / "BOOTSTRAP").read_text(encoding="utf-8")

    def test_carrier_precedence_is_deterministic(self):
        ordered = (
            "Explicit current-instruction / bounded current-task override",
            "Governing work-item declaration",
            "Repository declaration",
            "Managed Project declaration",
            "Promptbook documented default",
        )
        offsets = [self.availability.index(item) for item in ordered]
        self.assertEqual(offsets, sorted(offsets))
        self.assertIn(
            "work-item-before-repository discovery", self.availability_lower
        )

    def test_each_non_default_carrier_has_discovery_rules(self):
        self.assertIn("current user instruction", self.availability_lower)
        self.assertIn("governing work item", self.availability_lower)
        self.assertIn("preferably `agents.md`", self.availability_lower)
        self.assertIn("persistent project/workspace instructions", self.availability_lower)
        self.assertIn("do not search arbitrary files", self.availability_lower)

    def test_old_conversation_override_cannot_silently_carry(self):
        self.assertIn("old conversational statement", self.availability_lower)
        self.assertIn("must not silently carry", self.availability_lower)
        self.assertIn("unrelated work", self.availability_lower)

    def test_missing_is_distinct_from_defective_configuration(self):
        self.assertIn("absent optional declaration is different", self.availability_lower)
        self.assertIn("absence falls through", self.availability_lower)
        for result in (
            "INVALID_VALUE",
            "CONTRADICTORY",
            "STALE",
            "TARGET_MISMATCH",
            "SOURCE_UNAVAILABLE",
        ):
            self.assertIn(result, self.availability)
        self.assertIn("does not silently widen", self.availability_lower)

    def test_default_remains_enabled(self):
        self.assertIn("pull_request.mark_ready", self.availability)
        self.assertIn("documented default is", self.availability_lower)
        self.assertIn("enabled", self.availability)
        self.assertIn("DEFAULTED", self.availability)

    def test_resolution_record_is_reconstructable(self):
        for field in (
            "capability_key",
            "resolved_value",
            "source_class",
            "source_identity_or_reference",
            "source_precedence",
            "resolved_for_repository",
            "resolved_for_work_identity",
            "freshness_or_version_identity",
            "resolution_result",
        ):
            self.assertIn(field, self.availability)
        self.assertIn("fresh context", self.availability_lower)
        self.assertIn("equivalent resolved record", self.availability_lower)

    def test_run_context_carries_one_resolved_availability_record(self):
        self.assertIn("resolved_capability_availability", self.context)
        self.assertIn("resolve capability availability once", self.context_lower)
        self.assertIn("must not independently search", self.context_lower)
        self.assertIn("/fix", self.context)
        self.assertIn("/go", self.context)

    def test_autonomous_progression_consumes_not_rediscovers(self):
        self.assertIn("resolved_capability_availability", self.progression)
        self.assertIn("do not independently rediscover", self.progression_lower)
        self.assertIn("must not be invoked or probed", self.progression_lower)

    def test_executor_consumes_same_resolved_record(self):
        self.assertIn("Promptbook-resolved capability availability record", self.projection)
        self.assertIn("do not rediscover", self.projection_lower)
        self.assertIn("not a configuration-discovery authority", self.projection_lower)
        self.assertIn("capability_availability_provenance", self.projection)

    def test_managed_project_configuration_is_not_repository_authority(self):
        self.assertIn("execution configuration only", self.guide_lower)
        self.assertIn("does not become repository policy", self.guide_lower)
        self.assertIn("managed project configuration is not repository authority", self.availability_lower)

    def test_public_guide_gives_exact_placement_and_reenable_examples(self):
        self.assertIn("capability-availability-configuration.md", self.using)
        self.assertIn("## Current instruction or bounded task", self.guide)
        self.assertIn("## Governing work item", self.guide)
        self.assertIn("## Repository declaration", self.guide)
        self.assertIn("## Managed Project declaration", self.guide)
        self.assertIn("CAPABILITY_AVAILABILITY", self.guide)
        self.assertIn("pull_request.mark_ready: disabled", self.guide)
        self.assertIn("pull_request.mark_ready: enabled", self.guide)

    def test_optional_project_configuration_does_not_expand_default_bootstrap(self):
        self.assertNotIn("CAPABILITY_AVAILABILITY", self.bootstrap)
        self.assertIn("standard Promptbook bootstrap does not need", self.guide)
        self.assertIn("default bootstrap thin", self.guide_lower)

    def test_enabled_and_unsupported_keys_cannot_widen_authority(self):
        self.assertIn("`enabled` must never grant repository mutation", self.availability_lower)
        for effect in (
            "merge",
            "release",
            "deployment",
            "credential",
            "production",
        ):
            self.assertIn(effect, self.availability_lower)
        self.assertIn("unsupported capability keys", self.availability_lower)
        self.assertIn("do not invent new executable capability semantics", self.guide_lower)


if __name__ == "__main__":
    unittest.main()
