# Resolved agent run context

## Purpose

Define the reusable Promptbook contract for deriving the effective execution state of a governed agent operation from current authoritative inputs. The first supported operation is `/review`.

Promptbook is the canonical owner of this workflow contract. The context is ephemeral derived state, not a new durable authority source and not a replacement for repository-native instructions, issue or pull-request authority, immutable Git identity, CI evidence, or other durable records.

## When to use

Use this contract before substantive `/review` adjudication so the review operates from explicit repository/work authority, immutable candidate identity, capability boundaries, instruction provenance, and required evidence rather than remembered conversation state.

Future workflows may reuse the same model only when their own authority and capability semantics are deliberately defined. This first slice does not generalise `/review` permissions to `/fix`, `/go`, or other operations.

## Prompt

```text
Before substantive review adjudication, resolve an ephemeral Resolved Agent Run Context from current authoritative inputs.

Bind the operation to the repository, work item, immutable candidate where applicable, resolved authority sources, applicable repository instructions and their provenance, effective and prohibited capabilities, owner-decision boundaries, and required evidence.

Treat the resolved context as derived execution state rather than a new authority source. Do not fill missing authority or evidence from conversation memory. Intersect available capabilities with the read-only review boundary, adding only the narrow review-publication capability explicitly carried by the governing review mode.

Collect bounded reconstructable evidence, distinguish static observation from executed and durable evidence, bind material findings and the disposition to the immutable candidate, and re-resolve candidate-specific state if that identity changes.
```

## Core rule

A governed operation must execute from explicit, reconstructable authority and capability state rather than treating the conversation transcript as executable state.

The conversation may carry intent and navigation, but correctness must be reconstructable from current authoritative sources. Prior summaries and remembered conclusions are navigation aids only when the underlying authority or evidence can be refreshed directly.

## Required context

For `/review`, resolve at least:

```text
operation
repository_identity
work_item_identity
immutable_candidate_identity
resolved_authority_sources
applicable_repository_instructions
effective_capabilities
prohibited_capabilities
owner_decision_boundaries
required_evidence
```

The representation may be textual or structured. It need not be committed for every run. Whatever representation is used, equivalent authoritative inputs must resolve to equivalent effective authority, candidate identity, capability boundaries, and evidence requirements.

## Inputs

Resolve the context from the authoritative inputs that apply to the operation. At minimum, consider:

- platform safety and explicit current-user authority;
- the Promptbook workflow selected for the operation;
- repository-local instructions and mandatory policy;
- the governing issue, pull request, design, specification, or other work-item authority;
- the immutable candidate being assessed;
- current CI, checks, review state, and other decision-critical durable evidence.

Conversation history may help locate those sources, but it is not a substitute for refreshing them when correctness depends on current state.

## Authority resolution

Resolve the context from current authoritative inputs in precedence order appropriate to the repository and operation.

Record enough provenance to identify where each applicable instruction or material rule came from. A resolved context does not create authority absent from those sources.

If a required authority source cannot be resolved, fail closed or hand off according to the governing workflow rather than filling the gap from conversation memory.

## Immutable candidate

Where the review target has an immutable Git identity, bind the context to the exact candidate commit or equivalent immutable revision actually inspected.

Candidate-specific review authority and evidence are valid only for that candidate. If the candidate identity changes, invalidate the prior candidate-specific context and re-resolve before relying on earlier findings or publishing a review disposition.

Immediately before review publication, refresh the candidate identity and reconcile any movement. Never publish a stale candidate-specific disposition merely because the conversation still contains the earlier conclusion.

## Review capability profile

For the first `/review` slice, the effective capability model is logically equivalent to:

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
- PR mutation except the review-record publication explicitly authorised by the governing `/review` mode
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

## Required evidence

Resolve the evidence necessary to support the requested disposition before adjudicating. Evidence should be proportionate, bounded, and reconstructable. Depending on the claim, it may include:

- an exact command or tool invocation and result status;
- bounded relevant output;
- a CI or check result bound to the candidate;
- a reproducible test;
- a static source observation;
- an applicable repository-rule or authority citation.

Do not fabricate executed evidence where only static analysis occurred. Identify static observations as static. If a material claim requires execution that was not performed, represent that absence rather than implying the execution succeeded.

## Evidence-bearing findings

A material review finding should be reconstructable as the logical equivalent of:

```text
claim
affected_code_or_location
applicable_authority_or_rule
observation
evidence
immutable_candidate_identity
priority
confidence
```

The human-facing review may remain concise. It does not need to print a verbose schema for every observation, but the decisive reasoning must retain enough provenance to reconstruct why the disposition applies to the bound candidate.

For evidence, distinguish at least:

- `STATIC` — source, configuration, metadata, or rule observation without executing the claimed behaviour;
- `EXECUTED` — a command, test, check, or tool action was actually run and its result observed;
- `DURABLE` — repository-hosted CI, review, check, or other retained evidence was inspected.

A finding may use more than one evidence class. Do not upgrade one class into another merely to strengthen the conclusion.

## What it does

Makes the effective `/review` execution state explicit and reconstructable without introducing a new durable per-run artefact. It separates authority from capability, binds candidate-specific reasoning to immutable identity, preserves repository-instruction provenance, and requires evidence-bearing findings whose decisive support can be distinguished as static, executed, or durable.

It also keeps the existing Promptbook review-recording model intact: ordinary router `/review` may publish only the requested review record, while `/review --read-only` remains zero-write.

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
6. identify the evidence required for a safe disposition.

During review, collect only evidence permitted by the effective capability set and relevant to the governing contract. Before publication, refresh candidate identity and any decision-critical evidence that can stale.

## Delegation invariant

Future delegated or child execution contexts must never gain authority merely through delegation:

```text
child_authority ⊆ parent_authority
```

This issue does not introduce subagent infrastructure; the invariant is recorded so future implementations preserve the same authority model.

## Boundaries / limitations

This first contract does not define `/fix` or `/go` run contexts, a Switchboard schema, operating-system or network sandboxing, Guardian-style approval automation, native subagents, agentctl policy ownership, or Watchtower workflow ownership.

External mechanisms may enforce capability restrictions or collect evidence, but they do not become owners of Promptbook workflow policy.

## Status

`tested`
