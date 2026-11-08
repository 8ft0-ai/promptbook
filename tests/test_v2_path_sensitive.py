"""Effect-order, source-selection and negative-mutation tests for V2 #106.

Content-conservation assertions live separately in v2_contract_source.py;
passing a source-text union does NOT establish a valid operation route.
"""
import shutil
import tempfile
import unittest
from pathlib import Path

from v2_execution_probe import (
    SimulatedCase, ContractBoundary, execute_simulated, pre_action_sources,
    SPECIAL_ROUTER, CORE_ROUTER, ARCH_CLOSURE, GO_CONTEXT,
)

ROOT = Path(__file__).resolve().parents[1]
SOURCES = (
    CORE_ROUTER, 'prompts/workflows/autonomous-progression.md',
    'prompts/workflows/resolved-agent-run-context.md', GO_CONTEXT,
    'guides/conditional/context-review.md',
    'prompts/workflows/fresh-independent-review.md',
    SPECIAL_ROUTER, ARCH_CLOSURE,
)


def closure_proof(snapshot='sha-A', reviewed='sha-A', disposition='APPROVED_FOR_CANDIDATE_PROJECTION',
                  independent=True, authorise=True):
    return {
        'artifact': {'snapshot':snapshot, 'scope':'system-A', 'governing_contract':'issue-106',
                     'independently_derived':True},
        'review': {'snapshot':reviewed, 'scope':'system-A', 'governing_contract':'issue-106',
                   'disposition':disposition, 'fresh_independent_context':independent},
        'authoring_authority': {'snapshot':snapshot, 'scope':'system-A', 'granted':authorise},
    }


class V2PathSensitiveTests(unittest.TestCase):
    def replay(self, **kwargs):
        case=SimulatedCase(**kwargs)
        return execute_simulated(ROOT,case),case

    def stage(self):
        temp=tempfile.TemporaryDirectory(prefix='v2-route-negative-')
        root=Path(temp.name)
        for rel in SOURCES:
            dst=root/rel
            dst.parent.mkdir(parents=True,exist_ok=True)
            shutil.copy2(ROOT/rel,dst)
        return temp,root

    def test_high_risk_stages_inspection_before_specialist_reads_and_authoring(self):
        result,c=self.replay(high_risk=True,strong_completeness=True,
            attempted_actions=('inspect','architecture_closure','request_fresh_review'))
        self.assertEqual(result,'REVIEW_REQUIRED')
        kinds=[(e['kind'],e.get('path') or e.get('action')) for e in c.trace]
        inspection=next(i for i,e in enumerate(c.trace) if e['kind']=='inspect')
        specialist=next(i for i,e in enumerate(c.trace) if e.get('path')==SPECIAL_ROUTER)
        closure=next(i for i,e in enumerate(c.trace) if e.get('path')==ARCH_CLOSURE)
        self.assertLess(inspection,specialist)
        self.assertLess(specialist,closure)
        self.assertNotIn('author_candidate',c.effects)
        self.assertIn('closure_draft_not_approval',c.observations)

    def test_high_risk_without_inspection_cannot_load_or_author(self):
        result,c=self.replay(high_risk=True,strong_completeness=True,
            attempted_actions=('author_candidate',))
        self.assertEqual(result,'INSPECTION_REQUIRED')
        self.assertNotIn(SPECIAL_ROUTER,c.reads)
        self.assertEqual(c.effects,[])

    def test_current_exact_independent_closure_allows_scoped_projection(self):
        result,c=self.replay(high_risk=True,strong_completeness=True,
            closure_evidence=closure_proof(),pending_required_review=True,
            attempted_actions=('inspect','author_candidate','run_tests','create_pr','mark_complete'))
        self.assertEqual(result,'REVIEW_REQUIRED')
        self.assertEqual(c.effects,['author_candidate','create_pr'])
        self.assertEqual(len(c.effect_receipts),2)
        self.assertTrue(all(x['after'] for x in c.effect_receipts))

    def test_wrong_snapshot_freshness_or_projection_authority_denies(self):
        cases=(closure_proof(reviewed='sha-B'),closure_proof(independent=False),
               closure_proof(authorise=False),closure_proof(disposition='CHANGES REQUIRED'),None)
        for proof in cases:
            with self.subTest(proof=proof):
                result,c=self.replay(high_risk=True,strong_completeness=True,
                    closure_evidence=proof,attempted_actions=('inspect','author_candidate'))
                self.assertEqual(result,'CLOSURE_REQUIRED')
                self.assertEqual(c.effects,[])

    def test_non_trigger_paths_never_load_architecture_details(self):
        for pair in ((False,False),(True,False),(False,True)):
            with self.subTest(pair=pair):
                result,c=self.replay(high_risk=pair[0],strong_completeness=pair[1],
                    attempted_actions=('inspect','author_candidate','run_tests','mark_complete'))
                self.assertEqual(result,'COMPLETE')
                self.assertNotIn(SPECIAL_ROUTER,c.reads)
                self.assertNotIn(ARCH_CLOSURE,c.reads)

    def test_missing_conditional_file_fails_closed_after_inspection(self):
        temp,root=self.stage()
        try:
            (root/SPECIAL_ROUTER).unlink()
            c=SimulatedCase(high_risk=True,strong_completeness=True,
                            attempted_actions=('inspect','author_candidate'))
            with self.assertRaises(ContractBoundary):
                execute_simulated(root,c)
            self.assertEqual(c.effects,[])
            self.assertEqual(c.trace[-1]['kind'],'inspect')
        finally:temp.cleanup()

    def test_removing_or_reordering_pre_authoring_gate_is_detected(self):
        for operation in ('delete','move_late','weaken_conjunction','wrong_link'):
            with self.subTest(operation=operation):
                temp,root=self.stage()
                try:
                    p=root/CORE_ROUTER
                    content=p.read_text()
                    a=content.index('## Mandatory pre-authoring architecture gate')
                    b=content.index('## Routing',a)
                    if operation=='delete':content=content[:a]+content[b:]
                    if operation=='move_late':content=content[:a]+content[b:]+content[a:b]
                    if operation=='weaken_conjunction':content=content.replace('**both** conditions','**either** condition',1)
                    if operation=='wrong_link':content=content.replace('](../../guides/conditional/router-special-routing.md)','](../../guides/conditional/router-decision.md)',1)
                    p.write_text(content)
                    c=SimulatedCase(high_risk=True,strong_completeness=True,
                                    attempted_actions=('inspect','author_candidate'))
                    with self.assertRaises(ContractBoundary):execute_simulated(root,c)
                    self.assertEqual(c.effects,[])
                finally:temp.cleanup()

    def test_removing_exact_review_clause_is_detected_before_effect(self):
        temp,root=self.stage()
        try:
            p=root/GO_CONTEXT
            p.write_text(p.read_text().replace('APPROVED_FOR_CANDIDATE_PROJECTION','MAYBE_APPROVED'))
            c=SimulatedCase(high_risk=True,strong_completeness=True,
                closure_evidence=closure_proof(),attempted_actions=('inspect','author_candidate'))
            with self.assertRaises(ContractBoundary):execute_simulated(root,c)
            self.assertEqual(c.effects,[])
        finally:temp.cleanup()

    def test_recover_same_failed_workspace_after_observed_failure(self):
        with tempfile.TemporaryDirectory() as d:
            c=SimulatedCase(injected_test_failure=True,attempted_actions=(
                'inspect','author_candidate','run_tests','fix','run_tests','teardown','verify','mark_complete'))
            result=execute_simulated(ROOT,c,workspace=Path(d))
            self.assertEqual(result,'COMPLETE')
            self.assertEqual(c.observations.count('tests_fail_observed'),1)
            self.assertEqual(c.observations.count('tests_pass_observed'),1)
            self.assertEqual(c.effects,['author_candidate','fix'])
            self.assertEqual((Path(d)/'config.txt').read_text(),'corrected after observed failure')
            self.assertEqual(len(c.effect_receipts),2)

    def test_fix_without_observed_failure_forbidden(self):
        result,c=self.replay(injected_test_failure=True,attempted_actions=('inspect','fix'))
        self.assertEqual(result,'FORBID')
        self.assertEqual(c.effects,[])

    def test_read_only_stale_and_nonfresh_review_never_write(self):
        for options in ({'read_only':True,'reviewer_fresh':True},
                        {'reviewer_fresh':False},
                        {'reviewer_fresh':True,'exact_head':'a'*40,'observed_head':'b'*40}):
            with self.subTest(options=options):
                with tempfile.TemporaryDirectory() as d:
                    c=SimulatedCase(operation='/review',attempted_actions=('inspect','write_review'),**options)
                    self.assertEqual(execute_simulated(ROOT,c,Path(d)),'FORBID')
                    self.assertFalse(list(Path(d).iterdir()))
                    self.assertNotIn(GO_CONTEXT,c.reads)

    def test_later_deployment_approval_does_not_block_earlier_preparation(self):
        result,c=self.replay(attempted_actions=(
            'inspect','author_candidate','run_tests','create_pr','deploy'))
        self.assertEqual(result,'REQUIRE_OWNER')
        self.assertEqual(c.effects,['author_candidate','create_pr'])
        self.assertIn('tests_pass_observed',c.observations)

    def test_tracking_only_cannot_author(self):
        result,c=self.replay(implementation_authorised=False,attempted_actions=('inspect','author_candidate'))
        self.assertEqual(result,'REQUIRE_OWNER')
        self.assertEqual(c.effects,[])

    def test_step_one_transition_then_intrinsic_stop(self):
        result,c=self.replay(operation='/step',attempted_actions=('inspect','author_candidate'))
        self.assertEqual(result,'ONE_TRANSITION')
        self.assertEqual(c.effects,[])

    def test_completed_bounded_deliverable_not_extended_to_pr(self):
        result,c=self.replay(requested_deliverable_is_implementation_and_tests=True,
            attempted_actions=('inspect','author_candidate','run_tests','create_pr'))
        self.assertEqual(result,'COMPLETE')
        self.assertEqual(c.effects,['author_candidate'])

    def test_pr_waiting_fresh_review_is_not_completed_goal(self):
        result,c=self.replay(pending_required_review=True,
            attempted_actions=('inspect','author_candidate','run_tests','create_pr','mark_complete'))
        self.assertEqual(result,'REVIEW_REQUIRED')
        self.assertEqual(c.effects,['author_candidate','create_pr'])

if __name__=='__main__':unittest.main()
