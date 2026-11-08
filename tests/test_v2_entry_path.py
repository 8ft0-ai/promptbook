
"""Promptbook V2 goal-first entry-path and conditional-safety regression tests.

These are deterministic contract tests. They do not assert model execution
success, token usage, or independent-review eligibility.
"""
import re
import unittest
from pathlib import Path

from v2_contract_source import DETAILS, read_effective_contract

ROOT=Path(__file__).resolve().parents[1]
WF=ROOT/"prompts"/"workflows"
ADV=ROOT/"guides"/"conditional"
BASELINE_SOURCE_BYTES=173311  # 305c351b32343b5c7c3d9132f611e2727595259b

class V2EntryPathTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.router=(WF/"README.md").read_text()
        cls.progression=(WF/"autonomous-progression.md").read_text()
        cls.context=(WF/"resolved-agent-run-context.md").read_text()
        cls.core=cls.router+"\n"+cls.progression+"\n"+cls.context

    def test_normal_entry_is_smaller_and_total_source_is_subtractive(self):
        entry_bytes=sum((WF/p).stat().st_size for p in
                        ("README.md","autonomous-progression.md",
                         "resolved-agent-run-context.md"))
        all_bytes=entry_bytes+sum(p.stat().st_size for p in ADV.glob("*.md"))
        self.assertLess(entry_bytes, 40000, "ordinary mandatory entry path regressed")
        self.assertLess(all_bytes, BASELINE_SOURCE_BYTES,
                        "V2 must reduce maintained source, not just move it")
        self.assertGreater(BASELINE_SOURCE_BYTES-entry_bytes, 100000)

    def test_each_specialist_module_has_one_discoverable_core_link(self):
        contents={
            "prompts/workflows/README.md":self.router,
            "prompts/workflows/autonomous-progression.md":self.progression,
            "prompts/workflows/resolved-agent-run-context.md":self.context,
        }
        declared=set()
        for core, modules in DETAILS.items():
            for name in modules:
                link="../../guides/conditional/"+name+".md"
                self.assertEqual(contents[core].count("]("+link+")"),1,
                                 (core,name))
                declared.add(name)
                self.assertTrue((ADV/(name+".md")).is_file())
        actual={p.stem for p in ADV.glob("*.md") if p.name!="README.md"}
        self.assertSetEqual(declared,actual)
        self.assertIn("do not pre-load",self.router.lower())
        self.assertIn("do not load every specialist",self.progression.lower())
        self.assertIn("unrelated profiles must not be preloaded",self.context.lower())

    def test_all_specialist_contracts_have_concrete_triggers(self):
        for name in sorted({name for values in DETAILS.values() for name in values}):
            module=(ADV/(name+".md")).read_text()
            self.assertIn("**Conditional contract:**",module)
            self.assertGreater(len(module.split("**Conditional contract:**",1)[1].split("\n")[0]),45)

    def test_no_second_execution_policy_or_ambient_permission(self):
        text=self.core.lower()
        for necessary in (
            "one goal-driven execution loop",
            "ephemeral derived state",
            "technical capability never grants permission",
            "missing or contradictory permission fails closed",
            "original requested outcome",
            "a later approval must not prevent authorised work",
            "a completed handoff",
            "genuinely fresh",
        ):
            self.assertIn(necessary,text)
        self.assertNotIn("switchboard v2",text)

    def test_synthetic_failure_reproductions_have_explicit_positive_and_negative_routes(self):
        # Source/semantics tests only: real receiving-agent executions remain
        # a separate operational acceptance requirement under issue #106.
        scenarios={
            "preparation_before_future_approval":(
                self.progression.lower(),
                ["a later approval must not prevent authorised work",
                 "reconnaissance is preparation",
                 "under /go (until_boundary)"],
            ),
            "remediable_failure":(
                self.progression.lower(),
                ["diagnose and resolve routine prerequisites",
                 "bounded defects within existing authority",
                 "stop at a demonstrated"],
            ),
            "tracking_only_or_missing_implementation_authority":(
                self.progression.lower()+"\n"+self.context.lower(),
                ["missing or contradictory permission fails closed",
                 "proposed action is not permission"],
            ),
            "handoff_not_objective":(
                self.router.lower()+"\n"+self.progression.lower(),
                ["a completed sub-workflow, successful handoff record",
                 "a completed handoff, created pr, green ci run"],
            ),
            "bounded_step":(
                self.progression.lower(),
                ["(one_transition)","one governed transition"]),
        }
        for name,(contract,requirements) in scenarios.items():
            with self.subTest(name=name):
                for marker in requirements:self.assertIn(marker,contract)

    def test_exact_identity_and_review_gates_are_explicitly_reachable(self):
        combined=self.core+"\n"+read_effective_contract(WF/"README.md")
        for requirement in (
            "fresh independent review",
            "complete substantive",
            "CLOSURE_REVIEW_REQUIRED",
            "GOVERNING_DISPOSITION_REQUIRED",
            "exact",
            "GitHub",
            "read-only",
        ):
            self.assertIn(requirement.lower(),combined.lower())

if __name__=="__main__":
    unittest.main()
