# Context Review

**Conditional contract:** Load for substantive independent review, write-back or isolated-review eligibility.

## `/review` required context

For `/review`, resolve at least:

```text
operation
repository_identity
work_item_identity
review_target_identity
review_target_snapshot_identity_when_mutable
review_target_type
immutable_candidate_identity_when_applicable
architecture_closure_identity_when_applicable
review_record_target
resolved_authority_sources
applicable_repository_instructions
effective_capabilities
prohibited_capabilities
owner_decision_boundaries
resolved_fresh_review_context
required_evidence
```

`resolved_fresh_review_context` is required only when the `/review` operation is entered through delegated fresh-context resolution. Ordinary review performed directly in a current context that is already genuinely fresh need not create a child-context record.

`review_target_identity` identifies the durable object or immutable object locator being adjudicated. When that object can be edited in place without changing its locator, `review_target_snapshot_identity_when_mutable` is also required and must bind an edit-sensitive content/version witness sufficient to distinguish materially different bodies; locator equality is not snapshot equality. `review_target_type` distinguishes ordinary candidate/design/evidence review from `ARCHITECTURE_CLOSURE` review. `immutable_candidate_identity_when_applicable` is required for candidate review but is explicitly `NOT_APPLICABLE` for a pre-candidate closure review; do not manufacture a future candidate identity merely to satisfy the generic review model. `architecture_closure_identity_when_applicable` is required when `review_target_type=ARCHITECTURE_CLOSURE` and must identify the exact closure **snapshot**, not merely its issue/comment locator. `review_record_target` identifies the permitted durable publication location when write-back applies; for a GitHub issue/comment closure artefact this is the owning issue thread. A closure-review result is stale for a different or materially changed closure snapshot. `APPROVED_FOR_CANDIDATE_PROJECTION` is review evidence only and cannot add candidate-write or later-lifecycle capability to the `/review` profile.

## Immutable review target and candidate binding

Bind `review_target_identity` to the immutable object identity or durable locator actually inspected, and when the target is mutable bind `review_target_snapshot_identity_when_mutable` to the exact inspected content/version snapshot. For candidate review, bind the context to the exact candidate commit or equivalent immutable revision through `immutable_candidate_identity_when_applicable`. For pre-candidate architecture-closure review, candidate identity is `NOT_APPLICABLE` while the exact closure snapshot remains the review target.

Review-target-specific authority and evidence are valid only for that exact snapshot. If a mutable target's locator remains the same but its content/version witness changes, invalidate the prior target-specific context exactly as if the locator changed. When candidate identity applies and changes, invalidate the prior candidate-specific context and re-resolve before relying on candidate-bound evidence.

Immediately before review publication and again before later consumption of the review result, refresh the exact review-target snapshot identity and reconcile material movement. Refresh the candidate identity as well when applicable. Never publish or consume a stale target-specific disposition merely because the durable locator or conversation still contains the earlier conclusion.

## Review capability profile

For `/review`, the effective capability model is logically equivalent to:

```text
ALLOW
- repository read
- issue / PR read
- review-comment read
- CI / check evidence read
- other explicitly authorised read-only evidence collection

FORBID
- repository mutation
- branch mutation
- PR/work-item mutation except the single review-record publication explicitly authorised by the governing `/review` mode
- merge
- release
- unrelated external execution

BOUNDARY
- any action requiring authority beyond the resolved review context requires an explicit owner decision or other separately established authority
```

Access and permission are distinct. A tool being technically available does not add it to `effective_capabilities`.

Where an execution substrate can enforce capabilities, intersect the resolved operation capabilities with a read-only review profile:

```text
review_capabilities =
    resolved_capabilities
    ∩
    READ_ONLY_REVIEW_CAPABILITIES
```

Ordinary router `/review` may additionally carry only the narrow review-publication capability already defined by the router. `/review --read-only` carries no review-record mutation capability.

## Fresh-review child-context resolution

Fresh-review context resolution applies only when a fresh independent review is required and the current context is not itself eligible to perform that review. It preserves the review boundary by creating or selecting a distinct eligible reasoning context; it never reclassifies the current authoring/remediation context as fresh.

Resolve a bounded record logically equivalent to:

```text
review_target_identity
originating_context_freshness
isolated_context_eligibility
isolation_evidence
child_operation
child_review_capabilities
child_projection_provenance
attempt_identity_or_equivalent
failure_class
result_review_target_identity
result_candidate_identity_when_applicable
result_review_record_identity_when_published
result_disposition_or_evidence
```

The representation may remain ephemeral. Its purpose is to make the fresh-context decision reconstructable enough to prove that the child was eligible, bounded, and tied to the exact reviewed candidate, or that manual fallback was required.

Eligibility requires all of the following:

1. the child receives only a minimal durable review target or equivalent reconstruction reference, not author-side substantive reasoning or a proposed disposition;
2. the child independently bootstraps applicable project/repository authority and reconstructs the exact review target, governing contract, checks/evidence and review state from authoritative sources; candidate identity is required only when the target is a candidate;
3. the information boundary does not expose author-side hidden conversational state, private reasoning, expected conclusion or other substantive adjudication as review evidence;
4. the child resolves as operation `/review` and is constrained by the existing `/review` capability profile and recording mode;
5. repository-local policy does not require a distinct human or formal reviewer that this child context cannot satisfy; and
6. the returned review disposition/evidence is bound to the exact review target actually inspected, with candidate identity additionally bound when applicable.

Project/repository instructions and durable governing records are not prohibited merely because the originating context also saw them. Freshness concerns inherited adjudication, not shared authoritative rules.

Authority is narrowed at the child boundary:

```text
child_review_authority
    ⊆
effective_review_authority
```

The child must not inherit `candidate_write`, bounded remediation mutation, `merge`, `release_publish`, `deploy`, repository-settings mutation, provider mutation, production-data mutation or another author-side capability merely because the originating context possessed it. Creating/selecting the child is not authority and cannot refresh stale parent authority.

If isolation cannot be established, the durable target is ambiguous or insufficient, repository policy requires a genuinely distinct human/formal reviewer, the exact review target moves so the returned result is stale, or the child would require broader capability than `/review` permits, the child is ineligible. Preserve the existing manual fresh-context `EXTERNAL_REQUIRED` hand-off or the stronger repository-policy boundary.

Do not repeatedly create equivalent failed review contexts while the target, isolation evidence and bounded review-capability state remain unchanged. A materially changed target, isolation mechanism, policy or capability state may justify a new resolution attempt.

Fresh-review context resolution is distinct from `/go` execution-locality resolution. `connected/native`, `hosted/hermetic`, and `owner-local/bounded-executor` answer where an authorised effect can execute; they do not by themselves establish independent adjudication.

## `/review` lifecycle

A representative review should be reconstructable as:

```text
production routing
→ resolved repository/work authority
→ immutable review candidate
→ applicable instruction provenance
→ effective review capabilities
→ required evidence resolution
→ evidence collection
→ evidence-bearing findings
→ evidence-backed disposition
```

Before substantive adjudication:

1. resolve the context from current authoritative inputs;
2. verify that the operation is `/review` and identify its recording mode;
3. bind to the immutable candidate where applicable;
4. establish instruction and authority provenance;
5. intersect available capabilities with the review capability boundary;
6. identify the evidence required for a safe disposition;
7. when review was delegated, verify the resolved fresh-review isolation binding and independently reconstruct decision-critical state from the durable target before adjudication.

During review, collect only evidence permitted by the effective capability set and relevant to the governing contract. Before publication, refresh the exact review-target identity and any decision-critical evidence that can stale, plus candidate identity when applicable.

## Consolidated V2 safeguard

Fresh-review context resolution does not reuse the locality classes; it is an independent information-boundary mechanism, not executable locality or a way to bypass a formal reviewer.
