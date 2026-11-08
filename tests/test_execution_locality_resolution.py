from v2_contract_source import read_effective_contract
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROUTER = ROOT / "prompts" / "workflows" / "README.md"
CONTEXT = ROOT / "prompts" / "workflows" / "resolved-agent-run-context.md"
AUTONOMOUS = ROOT / "prompts" / "workflows" / "autonomous-progression.md"
AVAILABILITY = ROOT / "prompts" / "workflows" / "capability-availability-overrides.md"
PROJECTION = ROOT / "prompts" / "workflows" / "executor-capability-projection.md"
GUIDE = ROOT / "guides" / "go-lifecycle.md"


class ExecutionLocalityResolutionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.router = read_effective_contract(ROUTER)
        cls.context = read_effective_contract(CONTEXT)
        cls.autonomous = read_effective_contract(AUTONOMOUS)
        cls.availability = read_effective_contract(AVAILABILITY)
        cls.projection = read_effective_contract(PROJECTION)
        cls.guide = read_effective_contract(GUIDE)
        cls.router_lower = cls.router.lower()
        cls.context_lower = cls.context.lower()
        cls.autonomous_lower = cls.autonomous.lower()
        cls.availability_lower = cls.availability.lower()
        cls.projection_lower = cls.projection.lower()
        cls.guide_lower = cls.guide.lower()

    def test_locality_occurs_after_authority_and_availability_before_owner_handoff(self):
        ordering = self.context[
            self.context.index("resolve repository/work/action authority") :
            self.context.index("That availability record is derived execution state")
        ]
        authority = ordering.index("classify the exact action through the operation gateway")
        availability = ordering.index("resolve capability availability once")
        locality = ordering.index("resolve execution locality")
        execution = ordering.index("execute directly or project")
        self.assertLess(authority, availability)
        self.assertLess(availability, locality)
        self.assertLess(locality, execution)
        self.assertIn("before selecting a human-operated `EXTERNAL_REQUIRED` hand-off", self.context)

    def test_portable_locality_classes_and_no_fourth_executor_class(self):
        for locality in (
            "`connected/native`",
            "`hosted/hermetic`",
            "`owner-local/bounded-executor`",
        ):
            self.assertIn(locality, self.context)
            self.assertIn(locality, self.autonomous)
        self.assertIn("not a fourth executor class", self.context_lower)
        self.assertIn("owner-operated execution is not a fourth executor class", self.guide_lower)

    def test_current_connected_capability_success_does_not_require_external_handoff(self):
        self.assertIn("connected/native", self.context_lower)
        self.assertIn("execute and observe", self.context_lower)
        self.assertIn("current or equivalent governed connected capability", self.context_lower)
        self.assertIn("one unavailable capability or preferred connector does not by itself reach `external_required`", self.guide_lower)

    def test_unavailable_current_mechanism_may_use_equivalent_governed_connected_capability(self):
        self.assertIn("current or equivalent governed connected capability", self.context_lower)
        self.assertIn("another eligible execution locality", self.autonomous_lower)
        self.assertIn("another already-governed no-widening locality", self.router_lower)

    def test_hermetic_hosted_execution_is_allowed_only_without_owner_private_dependency(self):
        self.assertIn("hosted/hermetic", self.context_lower)
        self.assertIn("without owner-private state", self.context_lower)
        self.assertIn("`hosted/hermetic` execution when the required truth or effect can be established", self.autonomous_lower)
        self.assertIn("hosted/hermetic", self.guide_lower)

    def test_owner_local_truth_boundary_requires_material_dependency(self):
        for dependency in (
            "local filesystem or working-copy state",
            "private authenticated provider context",
            "local-only tooling or state",
            "browser/session-local state",
        ):
            self.assertIn(dependency, self.context_lower)
        self.assertIn("historical convenience", self.context_lower)
        self.assertIn("historical convenience or previous owner-shell usage is not enough", self.guide_lower)

    def test_bounded_owner_local_executor_precedes_owner_operated_handoff(self):
        locality_section = self.context[
            self.context.index("## `/go` execution-locality resolution") :
            self.context.index("## `/go` bounded approval consumption")
        ]
        bounded = locality_section.index(
            "separately governed bounded owner-local executor exists and is eligible?"
        )
        external = locality_section.index(
            "human-operated EXTERNAL_REQUIRED may be selected when a complete safe hand-off exists"
        )
        self.assertLess(bounded, external)
        self.assertIn("then a separately governed `owner-local/bounded-executor`", self.autonomous_lower)

    def test_genuine_owner_local_requirement_without_executor_uses_external_required(self):
        self.assertIn("human-operated EXTERNAL_REQUIRED may be selected when a complete safe hand-off exists", self.context)
        self.assertIn("the already-authorised required action cannot be performed through any eligible governed execution locality", self.autonomous_lower)
        self.assertIn("operational artifact hand-off", self.autonomous_lower)

    def test_disabled_capability_narrows_without_becoming_authority_or_automated_bypass(self):
        self.assertIn("capability availability != authority", self.availability)
        self.assertIn("does not, by itself, prove that owner-operated execution is required", self.availability_lower)
        self.assertIn("same suppressed logical effect is not restored by selecting a different automated executor or locality", self.availability_lower)
        self.assertIn("configured capability suppression cannot be bypassed", self.guide_lower)

    def test_executor_broader_support_cannot_widen_projected_capability(self):
        self.assertIn("capabilities_at_alternate_locality", self.projection)
        self.assertIn("⊆", self.projection)
        self.assertIn("does not inherit any wider capability merely because the alternate executor supports more effects", self.projection_lower)
        self.assertIn("changing execution locality preserves the same invariant", self.projection_lower)

    def test_alternate_locality_needing_wider_effects_is_ineligible(self):
        for wider_effect in (
            "credential",
            "network",
            "mutation",
            "provider",
        ):
            self.assertIn(wider_effect, self.projection_lower)
        self.assertIn("an alternate locality that would require wider", self.projection_lower)
        self.assertIn("is ineligible", self.context_lower)

    def test_atomic_external_command_remains_proportionate(self):
        self.assertIn("genuinely atomic, transcript-independent command inline", self.autonomous_lower)
        self.assertIn("operational-artifact-handoff.md", self.autonomous)

    def test_no_safe_locality_or_handoff_is_blocked_not_invented_execution(self):
        self.assertIn(
            "no safe action, eligible execution locality, eligible isolated review context",
            self.autonomous_lower,
        )
        self.assertIn("blocked when no safe action, eligible locality", self.guide_lower)
        self.assertIn("do not search arbitrary files for executables", self.context_lower)
        self.assertIn("manufacture a broad shell/argv escape hatch", self.context_lower)

    def test_decision_required_remains_for_genuine_judgement_or_authority(self):
        self.assertIn("decision_required", self.router_lower)
        self.assertIn("genuine human judgement/authority decision", self.autonomous_lower)
        self.assertIn("do not manufacture a new owner-authority decision merely because a mechanism is unavailable", self.autonomous_lower)

    def test_fresh_context_external_required_is_preserved_as_distinct_case(self):
        self.assertIn("fresh-review context resolution remains distinct from execution locality", self.router_lower)
        self.assertIn("a genuine fresh-context boundary is a distinct kind of external_required stop", self.autonomous_lower)
        self.assertIn("fresh-review context resolution is deliberately separate again", self.guide_lower)

    def test_failure_results_drive_fail_closed_locality_reresolution(self):
        self.assertIn("`PROFILE_DENIED`", self.context)
        self.assertIn("`CAPABILITY_DISABLED`", self.context)
        self.assertIn("`EXECUTOR_UNSUPPORTED`", self.context)
        self.assertIn("`UNAVAILABLE`", self.context)
        self.assertIn("`STALE_PROFILE`", self.context)
        self.assertIn("`GUARD_MISMATCH`", self.context)
        self.assertIn("profile_denied", self.projection_lower)
        self.assertIn("capability_disabled", self.projection_lower)
        self.assertIn("executor_unsupported", self.projection_lower)

    def test_unchanged_locality_failure_cannot_loop_indefinitely(self):
        self.assertIn("do not retry the same unchanged failed locality indefinitely", self.context_lower)
        self.assertIn("do not retry the same unchanged failed locality indefinitely", self.autonomous_lower)
        self.assertIn("avoid an execution loop", self.context_lower)

    def assert_capability_discovery_gate(self, core, locality):
        # Deliberately inspect the *loaded* ordinary-path source and its linked
        # conditional contract, not a text union of unrelated specialist files.
        execute = core.split("3. EXECUTE:", 1)[1].split("4. VERIFY:", 1)[0]
        ordered = (
            "check relevant available execution capabilities",
            "then attempt an eligible mechanism",
            "A tool not yet discovered is not a tool verified unavailable",
            "then resume execution after recovery",
            "Require concrete evidence of unavailability or denial before an environment blocker",
        )
        for requirement in ordered:
            self.assertIn(requirement, execute)
        indices = [execute.index(requirement) for requirement in ordered]
        self.assertEqual(indices, sorted(indices), "discovery/attempt/recovery must precede blocker")
        for requirement in (
            "including connected remote hosts and existing checkouts",
            "authentication, dependency and environment-selection failures within current authority",
            "do not demand exhaustive tool searches, unsafe workarounds or broader permissions",
            "Executor discovery, failed execution mechanism",
            "](../../guides/conditional/progression-locality.md)",
        ):
            self.assertIn(requirement, core)
        for requirement in (
            "relevant session-advertised tools, connected execution mechanisms",
            "Check eligible remote hosts and existing checkouts",
            "not yet discovered is distinct from confirmed unavailable",
            "Attempt a suitable permitted executor and record its actual result",
            "then resume the same authorised goal rather than stopping at reconnaissance",
            "concrete failed/denied attempts or authoritative unavailability evidence",
            "Avoid exhaustive tool catalogues, guessed remote dispatch, credential disclosure",
        ):
            self.assertIn(requirement, locality)

    def test_capability_discovery_precedes_unsupported_environment_blocker(self):
        core = AUTONOMOUS.read_text(encoding="utf-8")
        locality = (ROOT / "guides/conditional/progression-locality.md").read_text(
            encoding="utf-8"
        )
        self.assert_capability_discovery_gate(core, locality)
        # An authorised action must not be classified as environment-blocked
        # solely from an undiscovered tool; the executor is attempted first.
        self.assertLess(
            core.index("then attempt an eligible mechanism"),
            core.index("Require concrete evidence of unavailability or denial"),
        )
        self.assertIn("Technical capability never grants permission.", core)

    def test_discovery_gate_negative_source_mutations_are_detected(self):
        core = AUTONOMOUS.read_text(encoding="utf-8")
        locality = (ROOT / "guides/conditional/progression-locality.md").read_text(
            encoding="utf-8"
        )
        mutations = (
            (core.replace("check relevant available execution capabilities", "assume no shell", 1), locality),
            (core.replace("then attempt an eligible mechanism", "then report BLOCKED", 1), locality),
            (core.replace("A tool not yet discovered is not a tool verified unavailable", "An undiscovered tool is unavailable", 1), locality),
            (core.replace("then resume execution after recovery", "then request an owner prompt", 1), locality),
            (core.replace("Require concrete evidence of unavailability or denial before an environment blocker", "Report an environment blocker immediately", 1), locality),
            (core.replace("do not demand exhaustive tool searches, unsafe workarounds or broader permissions", "search all tools and try broad privileges", 1), locality),
            (core.replace("](../../guides/conditional/progression-locality.md)", "](../../guides/conditional/progression-recovery.md)", 1), locality),
            (core, locality.replace("Attempt a suitable permitted executor and record its actual result", "Guess that no executor exists", 1)),
            (core, locality.replace("concrete failed/denied attempts or authoritative unavailability evidence", "assumptions", 1)),
            (core, locality.replace("then resume the same authorised goal rather than stopping at reconnaissance", "then stop after reconnaissance", 1)),
        )
        for index, (mutated_core, mutated_locality) in enumerate(mutations):
            with self.subTest(mutation=index):
                with self.assertRaises((AssertionError, ValueError, IndexError)):
                    self.assert_capability_discovery_gate(mutated_core, mutated_locality)

    def test_discovery_before_invention_uses_authoritative_execution_surfaces(self):
        self.assertIn("authoritative repository/task execution or operator surfaces", self.context_lower)
        self.assertIn("prefer an established maintained capability", self.context_lower)
        self.assertIn("typed arguments or data", self.context_lower)
        self.assertIn("not a global catalogue of repository tools", self.guide_lower)


if __name__ == "__main__":
    unittest.main()
