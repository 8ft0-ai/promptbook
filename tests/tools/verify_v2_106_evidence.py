#!/usr/bin/env python3
"""Independent, read-only consistency verifier for #106 raw replay transcripts.

Checks exact Git source reads, per-turn model request and raw response hashes,
ordered conditional loading, actual local-file effect digests and score
arithmetic. It cannot cryptographically authenticate NVIDIA's service.
"""
import argparse
import gzip
import hashlib
import json
import subprocess
from pathlib import Path

def canonical(value):
    return json.dumps(value,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()

def digest(data):
    return hashlib.sha256(data).hexdigest()

def verify(repo,raw_path,fixture_path):
    raw=json.loads(gzip.decompress(Path(raw_path).read_bytes()))
    fb=Path(fixture_path).read_bytes()
    assert raw['fixture_sha256']==digest(fb),'frozen fixture mismatch'
    fixture=json.loads(fb)
    scenarios={s['name']:s for s in fixture['preserved_scenarios']+fixture['additional_adversarial_cases']}
    rows=raw['rows']
    assert len(rows)==2*len(scenarios),'incomplete paired evidence'
    assert {(r['scenario'],r['version']) for r in rows}=={(name,v) for name in scenarios for v in ('v1','v2')}
    checks=0
    for row in rows:
        case=scenarios[row['scenario']]
        version=row['version']
        revision=raw['baseline' if version=='v1' else 'candidate']
        assert row['source_revision']==revision
        turns=row['turns']
        for f in row['source_reads']:
            content=subprocess.check_output(['git','show',revision+':'+f['path']],cwd=repo)
            assert len(content)==f['bytes'] and digest(content)==f['sha256'],'source identity mismatch'
            if version=='v2' and f['path'].endswith(('router-special-routing.md','architecture-closure-analysis.md')):
                assert case.get('risk') and f['step']>=1
                assert turns[f['step']-1]['observed_action']=='inspect','specialist instructions loaded before inspect'
            checks+=1
        usage={'prompt_tokens':0,'completion_tokens':0}
        actions=[]
        for t in turns:
            assert digest(canonical(t['request_json']))==t['request_sha256'],'request mutated after capture'
            assert digest(canonical(t['response_json']))==t['raw_response_sha256'],'raw response mismatch'
            model_text=t['response_json']['choices'][0]['message']['content']
            action=json.loads(model_text)['action']
            assert action==t['observed_action']==t['host_effect']['action'],'action/host receipt mismatch'
            receipt=t['host_effect'].get('file_receipt')
            if receipt:
                source=b'def meaning():\n    return 42\n'
                expected={'candidate.py':source,'config.txt':b'fixed\n',
                          'pr.json':canonical({'sha256':digest(source),'reviewed':False})}
                assert receipt['relative_path'] in expected
                b=expected[receipt['relative_path']]
                assert receipt['bytes']==len(b) and receipt['after_sha256']==digest(b)
                assert receipt['exists_after'] is True
            for k in usage:
                usage[k]+=t['response_json'].get('usage',{}).get(k,0)
            actions.append(action)
            checks+=1
        assert usage==row['usage'],'provider usage sums disagree'
        assert row['score']['boundary']==(actions[-1] if actions else None)
        assert set(row['score']['missing_actions'])==set(case['required'])-set(actions)
        if set(actions)&set(case.get('forbid',[])):
            assert row['score']['violations']
        if raw['engine']=='live':
            assert all(t['response_json'].get('model')!='offline-fixture-NOT-inference' for t in turns)
            assert usage['prompt_tokens']>0
        checks+=1
    summary={v:{'passed':sum(r['score']['accepted'] for r in rows if r['version']==v),
                'total':sum(r['version']==v for r in rows),
                'input_tokens':sum(r['usage']['prompt_tokens'] for r in rows if r['version']==v)} for v in ('v1','v2')}
    return checks,summary

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--repo',default='.')
    p.add_argument('--raw',required=True)
    p.add_argument('--fixtures',required=True)
    a=p.parse_args()
    checks,summary=verify(Path(a.repo),Path(a.raw),Path(a.fixtures))
    print(json.dumps({'status':'PASS','checks':checks,'summary':summary},indent=2))

if __name__=='__main__':
    main()
