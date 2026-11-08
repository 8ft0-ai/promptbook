"""Regression: the replay recorder must freeze each turn's wire payload.

The first exploratory recorder retained a mutable messages-list reference:
later conversation turns changed earlier recorded requests. This test fails on
that defect without making external inference calls or changing host files.
"""
import importlib.util
import hashlib
import json
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[1]
SCRIPT=ROOT/'tests/tools/v2_106_replay.py'
spec=importlib.util.spec_from_file_location('v2_106_replay',SCRIPT)
runner=importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)

class V2RecorderTests(unittest.TestCase):
    def test_each_wire_request_is_immutable_after_later_turns(self):
        fixture=json.loads((ROOT/'tests/fixtures/v2_106_prospective_replay.json').read_text())
        case=next(x for x in fixture['preserved_scenarios'] if x['name']=='authorised_preparation')
        def local_read(_repo,_revision,path):
            return (ROOT/path).read_bytes()
        with patch.object(runner,'git_read',side_effect=local_read):
            row=runner.run_case(ROOT,case,'v2','synthetic-test',runner.MODEL_DEFAULT,
                                runner.ENDPOINT_DEFAULT,None,'fixture',8,5)
        self.assertTrue(row['score']['accepted'])
        self.assertEqual(len(row['turns']),5)
        previous_length=0
        for t in row['turns']:
            data=runner.packed(t['request_json'])
            self.assertEqual(hashlib.sha256(data).hexdigest(),t['request_sha256'])
            self.assertEqual(hashlib.sha256(runner.packed(t['response_json'])).hexdigest(),
                             t['raw_response_sha256'])
            self.assertGreaterEqual(len(t['request_json']['messages']),previous_length)
            previous_length=len(t['request_json']['messages'])
        self.assertLess(len(row['turns'][0]['request_json']['messages']),
                        len(row['turns'][-1]['request_json']['messages']))
    def test_versioned_fixture_is_prospective_not_retroactive(self):
        fixture=json.loads((ROOT/'tests/fixtures/v2_106_prospective_replay.json').read_text())
        self.assertEqual(len(fixture['preserved_scenarios']),9)
        self.assertEqual(len(fixture['additional_adversarial_cases']),2)
        self.assertIn('NOT a retroactive',fixture['provenance'])

if __name__=='__main__':unittest.main()
