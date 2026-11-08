
import shutil
import tempfile
import unittest
from pathlib import Path

from v2_execution_probe import (
    SimulatedCase, ContractBoundary, pre_action_sources,
    execute_simulated, SPECIAL_ROUTER, CORE_ROUTER, ARCH_CLOSURE,
)

ROOT=Path(__file__).resolve().parents[1]

class V2PathSensitiveTests(unittest.TestCase):
    def run_case(self,**values):
        case=SimulatedCase(**values)
        outcome=execute_simulated(ROOT,case)
        return outcome,case

    def test_high_risk_strong_claim_guards_authoring_before_effect(self):
        outcome,c=self.run_case(high_risk=True,strong_completeness=True,
            attempted_actions=("inspect","author_candidate","create_pr"))
        self.assertEqual(outcome,"CLOSURE_REQUIRED")
        self.assertEqual(c.effects,[])
        self.assertIn(SPECIAL_ROUTER,c.reads)
        self.assertIn(ARCH_CLOSURE,c.reads)
        self.assertLess(c.reads.index(SPECIAL_ROUTER),c.reads.index(ARCH_CLOSURE))
        self.assertIn("pre_authoring_closure_gate",c.observations)

    def test_high_risk_has_current_independent_closure_and_authority(self):
        outcome,c=self.run_case(high_risk=True,strong_completeness=True,
            current_independent_closure=True,
            attempted_actions=("author_candidate","run_tests","create_pr","mark_complete"))
        self.assertEqual(outcome,"COMPLETE")
        self.assertEqual(c.effects,["author_candidate","create_pr"])
        self.assertIn(ARCH_CLOSURE,c.reads)

    def test_nontrigger_paths_do_not_load_architecture_details(self):
        for kwargs in [
            {},{"high_risk":True},{"strong_completeness":True},
            {"current_independent_closure":False}]:
            with self.subTest(kwargs=kwargs):
                outcome,c=self.run_case(**kwargs,
                    attempted_actions=("author_candidate","run_tests","create_pr","mark_complete"))
                self.assertEqual(outcome,"COMPLETE")
                self.assertNotIn(SPECIAL_ROUTER,c.reads)
                self.assertNotIn(ARCH_CLOSURE,c.reads)
                self.assertIn("guides/conditional/context-go.md",c.reads)

    def test_missing_high_risk_contract_fails_closed(self):
        with tempfile.TemporaryDirectory() as tmp:
            # A deliberately minimal test checkout with missing specialist.
            base=Path(tmp)
            for rel in [CORE_ROUTER,"prompts/workflows/autonomous-progression.md",
                        "prompts/workflows/resolved-agent-run-context.md",
                        "guides/conditional/context-go.md"]:
                p=base/rel;p.parent.mkdir(parents=True,exist_ok=True)
                shutil.copy2(ROOT/rel,p)
            c=SimulatedCase(high_risk=True,strong_completeness=True,
                            attempted_actions=("author_candidate",))
            with self.assertRaisesRegex(ContractBoundary,"required module unavailable"):
                execute_simulated(base,c)
            self.assertEqual(c.effects,[])

    def test_missing_preaction_predicate_not_repaired_by_union(self):
        with tempfile.TemporaryDirectory() as tmp:
            base=Path(tmp)
            for rel in [CORE_ROUTER,"prompts/workflows/autonomous-progression.md",
                        "prompts/workflows/resolved-agent-run-context.md",
                        "guides/conditional/context-go.md",SPECIAL_ROUTER,ARCH_CLOSURE]:
                p=base/rel;p.parent.mkdir(parents=True,exist_ok=True)
                shutil.copy2(ROOT/rel,p)
            router=base/CORE_ROUTER
            text=router.read_text()
            start=text.index("## Mandatory pre-authoring architecture gate")
            end=text.index("## Routing",start)
            router.write_text(text[:start]+text[end:])
            c=SimulatedCase(high_risk=True,strong_completeness=True,
                            attempted_actions=("author_candidate",))
            with self.assertRaisesRegex(ContractBoundary,"high-risk gate not before"):
                execute_simulated(base,c)
            self.assertEqual(c.effects,[])

    def test_preapproved_preparation_stops_only_at_later_deployment(self):
        outcome,c=self.run_case(attempted_actions=(
            "inspect","author_candidate","run_tests","create_pr","deploy"))
        self.assertEqual(outcome,"REQUIRE_OWNER")
        self.assertEqual(c.effects,["author_candidate","create_pr"])
        self.assertIn("tests_pass",c.observations)
        self.assertIn("deployment_permission_missing",c.observations)

    def test_tracking_only_does_not_create_implementation_authority(self):
        outcome,c=self.run_case(implementation_authorised=False,
                        attempted_actions=("inspect","author_candidate","create_pr"))
        self.assertEqual(outcome,"REQUIRE_OWNER")
        self.assertEqual(c.effects,[])

    def test_failed_validation_blocks_completion_until_authorised_recovery(self):
        outcome,c=self.run_case(injected_test_failure=True,
            attempted_actions=("author_candidate","run_tests","mark_complete"))
        self.assertEqual(outcome,"BLOCKED")
        self.assertEqual(c.effects,["author_candidate"])
        self.assertIn("failed_validation_blocks_completion",c.observations)
        # An authorised routine fix permits re-validation; only after the
        # failure is genuinely cleared can the test fixture report complete.
        outcome,recovered=self.run_case(injected_test_failure=False,
            attempted_actions=("fix","run_tests","mark_complete"))
        self.assertEqual(outcome,"COMPLETE")
        self.assertIn("fix",recovered.effects)
        self.assertIn("tests_pass",recovered.observations)

    def test_fresh_review_read_only_and_stale_head_never_write(self):
        for kwargs,reason in [
            ({"read_only":True},"review_write_forbidden"),
            ({"exact_head":"a"*40,"observed_head":"b"*40},"stale_head")]:
            with self.subTest(reason=reason):
                outcome,c=self.run_case(operation="/review",
                                         attempted_actions=("inspect","write_review"),**kwargs)
                self.assertEqual(outcome,"FORBID")
                self.assertNotIn("write_review",c.effects)
                self.assertIn(reason,c.observations)
                self.assertIn("guides/conditional/context-review.md",c.reads)
                self.assertNotIn("guides/conditional/context-go.md",c.reads)

    def test_requested_implementation_and_tests_end_before_extra_pr(self):
        outcome,c=self.run_case(requested_deliverable_is_implementation_and_tests=True,
            attempted_actions=("inspect","author_candidate","run_tests","create_pr"))
        self.assertEqual(outcome,"COMPLETE")
        self.assertEqual(c.effects,["author_candidate"])
        self.assertIn("requested_deliverable_verified",c.observations)
        self.assertNotIn("create_pr",c.effects)

    def test_pr_pending_fresh_review_is_not_goal_completion(self):
        outcome,c=self.run_case(pending_required_review=True,
            attempted_actions=("author_candidate","run_tests","create_pr","mark_complete"))
        self.assertEqual(outcome,"REVIEW_REQUIRED")
        self.assertIn("fresh_review_still_required",c.observations)
        self.assertNotIn("verified_goal",c.observations)

    def test_bounded_requested_deliverable_must_not_expand_to_pr(self):
        progression=(ROOT/"prompts/workflows/autonomous-progression.md").read_text().lower()
        router=(ROOT/"prompts/workflows/README.md").read_text().lower()
        self.assertIn("do not invent a pr, review, publication or adjacent scope",progression)
        self.assertIn("return complete immediately",router)
        self.assertIn("after each observed execution or validation result",router.replace("**", ""))
        self.assertIn("opened pr awaiting mandatory independent review",progression)
        self.assertIn("after every observed tool result, check whether all acceptance evidence",progression)
        self.assertIn("first inspect authoritative objective and artefact evidence",router)
        self.assertLess(router.index("first inspect authoritative objective"),
                        router.index("specialised routing conditions"))

    def test_step_one_transition_and_handoff_not_completion(self):
        outcome,c=self.run_case(operation="/step",
            attempted_actions=("inspect","author_candidate","create_pr","mark_complete"))
        self.assertEqual(outcome,"ONE_TRANSITION")
        self.assertEqual(c.effects,[])
        self.assertNotIn("verified_goal",c.observations)
        outcome,g=self.run_case(attempted_actions=("inspect",))
        self.assertEqual(outcome,"IN_PROGRESS")
        self.assertEqual(g.effects,[])
        self.assertNotIn("verified_goal",g.observations)

if __name__=="__main__":
    unittest.main()
