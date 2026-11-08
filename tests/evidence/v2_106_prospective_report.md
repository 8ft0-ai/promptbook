# Promptbook #106 — prospective paired V1/V2 replay

Synthetic executable tools + real NVIDIA NIM inference; no real consumer, cloud, production, pull-request, review or merge effects. Date: 8 November 2026.

Baseline: 305c351b32343b5c7c3d9132f611e2727595259b
Frozen prospective scenario commit: b64ec71a938eec041da6a79ce532974cdbb1a5d9
Evaluated V2 implementation and recorder: bc8548001a78cc6e258d03c54938db5a78f60b5d
Frozen fixture SHA-256: 9d6ca564322a946ed0b2b8e61eab36c9fd59a75a4848b82e421b91b193518e08
Full compressed transcript: [v2_106_prospective_raw.json.gz](v2_106_prospective_raw.json.gz)
Raw transcript SHA-256: 835a16240ab8b6693193155216bac7322f33f68e90e3fd0ecc5ba95be8ceb6cf
Model/host metrics: [v2_106_prospective_summary.json](v2_106_prospective_summary.json)

## Verification and reproducibility

Run: python3 tests/tools/verify_v2_106_evidence.py --repo . --fixtures tests/fixtures/v2_106_prospective_replay.json --raw tests/evidence/v2_106_prospective_raw.json.gz
The compressed JSON contains every exact per-turn model request body, returned model response, provider token usage, instruction source read and SHA-256, and local host-effect receipt. It can be inspected by gzip-decompressing the archive and parsing it as JSON.
To rerun, execute tests/tools/v2_106_replay.py --engine live with the baseline, candidate and frozen fixtures shown above. Supply the NVIDIA_API_KEY securely in the shell; the runner does not persist credentials. The alternative fixture engine is for recorder validation only, not inference evidence.

## Empirical results

| Metric | V1 | V2 |
|---|---:|---:|
| Host-accepted synthetic cases | 10/11 | 11/11 |
| Provider-reported input tokens | 1,646,944 | 639,645 |
| Synthetic requested actions | 48 | 46 |
| Owner decision requests | 1 | 1 |
| False terminal blockers | 0 | 0 |

Observed model input-token reduction: 61.2 percent. This is provider usage from actual model requests in this synthetic harness, not an estimated reduction from source length.

| Scenario | V1 | V2 |
|---|---|---|
| authorised_preparation | PASS | PASS |
| recoverable_technical_defect | PASS | PASS |
| reconnaissance_to_delivery | PASS | PASS |
| tracking_only_negative | PASS | PASS |
| future_deployment_approval | PASS | PASS |
| fresh_review_stale_readonly | PASS | PASS |
| bounded_step | PASS | PASS |
| handoff_not_goal | FAIL | PASS |
| high_risk_strong_closure | PASS | PASS |
| closure_current_exact_review_negative | PASS | PASS |
| closure_current_exact_review_positive | PASS | PASS |

V1 overextended the bounded handoff deliverable into an unnecessary local PR. V2 stopped at the requested engineering deliverable. Both versions preserved the tracked negative authority boundaries. V2 inspected the stale-closure case twice, loaded the specialist contract once and reached the fresh-review gate.

## Limitations and outstanding gates

The verifier passed 199 source, request, response, read-order, local-file receipt, provider usage and acceptance checks across 22 paired records. The raw gzip file contains no NVIDIA API key or Authorization header value.
The nine inherited scenario descriptions were frozen only after initial V2 development; two additional adversarial cases were frozen before this remediation. This is a prospective remediation replay, not a retroactive pre-V2 baseline freeze.
The model responses are captured but are not cryptographically signed by NVIDIA. The verifier establishes internal consistency and source provenance, not provider-origin attestation or guaranteed bit-for-bit model repeatability.
The comparison is synthetic. No live consumer goal completion, actual ChatGPT instruction loading, NVIDIA billing amount, provider monetary cost or post-merge operational acceptance was measured.
A genuinely fresh independent review of the final PR head, separate merge authority and post-merge consumer smoke testing remain required before Issue #106 can be closed.
