import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class CapabilityAvailabilityOverrideTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.availability = (
            ROOT / "prompts" / "workflows" / "capability-availability-overrides.md"
        ).read_text(encoding="utf-8")
        cls.availability_lower = cls.availability.lower()
        cls.projection = (
            ROOT / "prompts" / "workflows" / "executor-capability-projection.md"
        ).read_text(encoding="utf-8")
        cls.projection_lower = cls.projection.lower()
        cls.progression = (
            ROOT / "prompts" / "workflows" / "autonomous-progression.md"
        ).read_text(encoding="utf-8")
        cls.progression_lower = cls.progression.lower()
        cls.prompt_index = (ROOT / "prompts" / "README.md").read_text(encoding="utf-8")
        cls.using_guide = (ROOT / "guides" / "using-promptbook.md").read_text(
            encoding="utf-8"
        )
        cls.using_guide_lower = cls.using_guide.lower()

    def test_first_supported_flag_is_portable_and_binary(self):
        self.assertIn("pull_request.mark_ready", self.availability)
        self.assertIn("enabled | disabled", self.availability)
        self.assertIn("representation is intentionally portable", self.availability_lower)
        self.assertIn("executor", self.availability_lower)

    def test_precedence_and_default_are_explicit(self):
        for source in (
            "explicit current-user or task-scoped override",
            "repository/task-specific configuration",
            "managed Project configuration",
            "Promptbook documented default",
        ):
            self.assertIn(source, self.availability)
        self.assertIn("the documented default is", self.availability_lower)
        self.assertIn("enabled", self.availability)
        self.assertIn("missing configuration therefore preserves pre-existing behaviour", self.availability_lower)

    def test_unknown_contradictory_or_stale_configuration_fails_conservatively(self):
        for condition in (
            "unknown values",
            "contradictory declarations",
            "stale configuration",
        ):
            self.assertIn(condition, self.availability_lower)
        self.assertIn("must not default to `enabled`", self.availability_lower)
        self.assertIn("fail conservatively", self.availability_lower)

    def test_configuration_can_narrow_but_never_widen_authority(self):
        self.assertIn("capability availability != authority", self.availability)
        self.assertIn("effective_executable_capability", self.availability)
        self.assertIn("authority_permitted_capability", self.availability)
        self.assertIn("configured_available_capability", self.availability)
        self.assertIn("must never grant repository mutation", self.availability_lower)
        self.assertIn("merge", self.availability_lower)
        self.assertIn("release", self.availability_lower)
        self.assertIn("deployment", self.availability_lower)
        self.assertIn("credential", self.availability_lower)

    def test_disabled_mode_suppresses_transition_without_repeated_probe(self):
        disabled = self.availability[
            self.availability.index("### Disabled") : self.availability.index("### Enabled")
        ]
        self.assertIn("do not invoke the draft-to-ready transition", disabled.lower())
        self.assertIn("do not repeatedly invoke", disabled.lower())
        self.assertIn("configured-disabled capability", disabled.lower())

    def test_reviewable_candidate_can_avoid_unnecessary_draft_transition(self):
        disabled = self.availability[
            self.availability.index("### Disabled") : self.availability.index("### Enabled")
        ]
        self.assertIn("implementation is already complete", disabled.lower())
        self.assertIn("required validation has passed", disabled.lower())
        self.assertIn("prefer creating the pull request as non-draft", disabled.lower())
        self.assertIn("do not use that shortcut when draft state expresses a real hold", disabled.lower())

    def test_legitimate_draft_uses_external_required_when_transition_unavailable(self):
        disabled = self.availability[
            self.availability.index("### Disabled") : self.availability.index("### Enabled")
        ]
        self.assertIn("legitimately draft", disabled.lower())
        self.assertIn("`EXTERNAL_REQUIRED`", disabled)
        self.assertIn("Ready for review", disabled)
        self.assertIn("do not merge", disabled.lower())
        self.assertIn("return evidence", disabled.lower())

    def test_enabled_mode_requires_authority_and_observed_state_verification(self):
        enabled = self.availability[
            self.availability.index("### Enabled") : self.availability.index("## Executor projection")
        ]
        self.assertIn("independently authorised", enabled.lower())
        self.assertIn("verify the observed pull-request state", enabled.lower())
        self.assertIn("configuration is not execution evidence", enabled.lower())
        self.assertIn("integration/schema error", enabled.lower())
        self.assertIn("do not report success merely because the flag was enabled", enabled.lower())

    def test_configuration_provenance_is_required_when_it_affects_execution(self):
        for field in (
            "capability_key",
            "resolved_value",
            "source_class",
            "source_identity_or_reference",
            "resolved_for_work_identity",
            "resolved_at_or_freshness_bound",
        ):
            self.assertIn(field, self.availability)
        self.assertIn("re-resolve", self.availability_lower)
        self.assertIn("must not silently carry across", self.availability_lower)

    def test_projection_has_narrow_state_transition_capability_and_availability_intersection(self):
        self.assertIn("work_item_state_transition", self.projection)
        self.assertIn("capability availability", self.projection_lower)
        self.assertIn("cannot widen", self.projection_lower)
        self.assertIn("does not imply", self.projection_lower)

    def test_autonomous_progression_applies_availability_before_execution(self):
        self.assertIn("capability-availability-overrides.md", self.progression)
        self.assertIn("pull_request.mark_ready", self.progression)
        self.assertIn("non-draft", self.progression_lower)
        self.assertIn("configured as unavailable", self.progression_lower)
        self.assertIn("verify", self.progression_lower)

    def test_public_surfaces_explain_disable_and_re_enable(self):
        self.assertIn(
            "workflows/capability-availability-overrides.md", self.prompt_index
        )
        self.assertIn("pull_request.mark_ready", self.using_guide)
        self.assertIn("disabled", self.using_guide_lower)
        self.assertIn("re-enable", self.using_guide_lower)
        self.assertIn("does not grant authority", self.using_guide_lower)


if __name__ == "__main__":
    unittest.main()
