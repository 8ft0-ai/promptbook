"""Source-sensitive, disposable contract probe for Promptbook V2.

This is a *test instrument*, not a production policy interpreter. It verifies
that the documented route is selected after authoritative inspection, relevant
conditional sources are actually read, and host-side effects respect the
resulting gate. Deliberate source mutations must fail before any write.
"""
from dataclasses import dataclass, field
from pathlib import Path
from tempfile import TemporaryDirectory
from hashlib import sha256
import re

CORE_ROUTER = 'prompts/workflows/README.md'
CORE_PROGRESSION = 'prompts/workflows/autonomous-progression.md'
CORE_CONTEXT = 'prompts/workflows/resolved-agent-run-context.md'
GO_CONTEXT = 'guides/conditional/context-go.md'
REVIEW_CONTEXT = 'guides/conditional/context-review.md'
REVIEW_WORKFLOW = 'prompts/workflows/fresh-independent-review.md'
SPECIAL_ROUTER = 'guides/conditional/router-special-routing.md'
ARCH_CLOSURE = 'prompts/workflows/architecture-closure-analysis.md'

class ContractBoundary(RuntimeError):
    """A missing/misplaced/invalid source contract stops the test action."""

@dataclass
class SimulatedCase:
    operation: str = '/go'
    high_risk: bool = False
    strong_completeness: bool = False
    closure_evidence: dict | None = None
    implementation_authorised: bool = True
    deployment_authorised: bool = False
    pending_required_review: bool = False
    requested_deliverable_is_implementation_and_tests: bool = False
    exact_head: str = 'a' * 40
    observed_head: str = 'a' * 40
    read_only: bool = False
    reviewer_fresh: bool = False
    injected_test_failure: bool = False
    attempted_actions: tuple = ()
    reads: list = field(default_factory=list)
    effects: list = field(default_factory=list)
    observations: list = field(default_factory=list)
    effect_receipts: list = field(default_factory=list)
    trace: list = field(default_factory=list)


def _read(root, case, path):
    target = (root / path).resolve()
    if not target.is_relative_to(root.resolve()) or not target.is_file():
        raise ContractBoundary('required module unavailable: ' + path)
    case.reads.append(path)
    case.trace.append({'kind':'read','path':path})
    return target.read_text(encoding='utf-8')


def _contains(text, *clauses):
    normalized = re.sub(r'\s+', ' ', text).casefold().replace('**', '')
    for clause in clauses:
        if re.sub(r'\s+', ' ', clause).casefold() not in normalized:
            raise ContractBoundary('missing / moved mandatory source rule: ' + clause)


def _named_link(text, label, source):
    # Derive the referenced target from the Markdown actually loaded, not a
    # simulator-maintained path map. The resolved source must match its role.
    match = re.search(r'\[' + re.escape(label) + r'\]\(([^)#]+)\)', text)
    if not match:
        raise ContractBoundary('missing route link: ' + label)
    target = (Path(source).parent / match.group(1)).as_posix()
    from posixpath import normpath
    return normpath(target)


def pre_action_sources(root: Path, case: SimulatedCase):
    """Select core instruction reads; DO NOT select architecture detail yet.

    This stage precedes observed inspection. A high-risk gate cannot truthfully
    assert its predicates or approval from author-supplied flags alone.
    """
    root = Path(root)
    router = _read(root, case, CORE_ROUTER)
    gate = router.find('## Mandatory pre-authoring architecture gate')
    ordinary = router.find('## Routing')
    if not (0 < gate < ordinary):
        raise ContractBoundary('pre-authoring gate absent or after ordinary routing')
    section = router[gate:ordinary]
    _contains(section,
              'first inspect authoritative objective and artefact evidence',
              'determine whether both conditions hold',
              'materially high-risk architecture',
              'strong closed-world',
              'before candidate authoring, implementation or publication',
              'if both apply', 'when either predicate is demonstrably false',
              'current independently derived architecture-closure artefact')
    if _named_link(section, 'Specialised routing conditions', CORE_ROUTER) != SPECIAL_ROUTER:
        raise ContractBoundary('specialist route target substituted')
    if _named_link(section, 'Architecture closure analysis', CORE_ROUTER) != ARCH_CLOSURE:
        raise ContractBoundary('closure target substituted')
    if case.operation in ('/go', '/step'):
        progression = _read(root, case, CORE_PROGRESSION)
        _read(root, case, CORE_CONTEXT)
        _contains(progression, 'mandatory pre-authoring architecture gate',
                  'before candidate authoring')
        go = _read(root, case, GO_CONTEXT)
        _contains(go, 'current_closure_review_disposition=APPROVED_FOR_CANDIDATE_PROJECTION',
                  'same closure identity', 'separate candidate-authoring authority')
    elif case.operation == '/review':
        review = _read(root, case, REVIEW_CONTEXT)
        _read(root, case, REVIEW_WORKFLOW)
        _contains(review, 'read-only', 'fresh', 'exact')
    else:
        raise ContractBoundary('unsupported operation')
    return 'AWAIT_AUTHORITATIVE_INSPECTION'


def _current_closure(evidence):
    if not isinstance(evidence, dict):
        return False
    artifact, review, authority = (evidence.get(k) or {} for k in
                                   ('artifact', 'review', 'authoring_authority'))
    return (bool(artifact.get('independently_derived')) and
            bool(artifact.get('snapshot')) and
            bool(artifact.get('governing_contract')) and
            bool(artifact.get('scope')) and
            review.get('snapshot') == artifact.get('snapshot') and
            review.get('governing_contract') == artifact.get('governing_contract') and
            review.get('scope') == artifact.get('scope') and
            review.get('disposition') == 'APPROVED_FOR_CANDIDATE_PROJECTION' and
            bool(review.get('fresh_independent_context')) and
            authority.get('snapshot') == artifact.get('snapshot') and
            authority.get('scope') == artifact.get('scope') and
            authority.get('granted') is True)


def _activate_after_inspect(root, case):
    if not (case.high_risk and case.strong_completeness):
        return False
    # The routing predicate can only be assessed from the observed inspect
    # receipt. Specialist files are selected and read *after* that receipt.
    sr = _read(root, case, SPECIAL_ROUTER)
    closure = _read(root, case, ARCH_CLOSURE)
    _contains(sr, 'materially high-risk architecture', 'strong closed-world',
              'before closure-ready candidate authoring/publication')
    _contains(closure, 'genuinely fresh architecture-closure review',
              'exact artefact', 'approved closure snapshot',
              'candidate authoring')
    case.observations.append('closure_contract_loaded_after_inspection')
    case.trace.append({'kind':'gate','name':'architecture_closure','approved':_current_closure(case.closure_evidence)})
    return True


def _write(workspace, case, name, content):
    target = workspace / name
    before = sha256(target.read_bytes()).hexdigest() if target.exists() else None
    target.write_text(content, encoding='utf-8')
    receipt = dict(file=name, before=before, after=sha256(target.read_bytes()).hexdigest(),
                   bytes=target.stat().st_size)
    case.effect_receipts.append(receipt)
    case.trace.append({'kind':'write', **receipt})


def execute_simulated(root: Path, case: SimulatedCase, workspace: Path | None = None):
    """Sequential host-side replay in one stateful workspace; no external writes."""
    root = Path(root)
    pre_action_sources(root, case)
    owned = TemporaryDirectory(prefix='promptbook-v2-path-') if workspace is None else None
    try:
        work = Path(owned.name) if owned else Path(workspace)
        work.mkdir(parents=True, exist_ok=True)
        inspected = False
        triggered = False
        closure_draft = False
        test_failed = False
        fixed = False
        tests_passed = False
        resource_present = case.injected_test_failure
        for action in case.attempted_actions:
            if not inspected and action != 'inspect':
                case.observations.append('authoritative_inspection_required')
                return 'INSPECTION_REQUIRED'
            if action == 'inspect':
                inspected = True
                case.observations.append('authoritative_inspection_observed')
                case.trace.append({'kind':'inspect','source':'authoritative_task'})
                triggered = _activate_after_inspect(root, case)
            elif action == 'architecture_closure':
                if not triggered:
                    return 'FORBID'
                closure_draft = True
                case.observations.append('closure_draft_not_approval')
            elif action in ('author_candidate', 'create_pr', 'fix'):
                if not case.implementation_authorised:
                    return 'REQUIRE_OWNER'
                if triggered and not _current_closure(case.closure_evidence):
                    case.observations.append('exact_independent_closure_approval_required')
                    return 'CLOSURE_REQUIRED'
                if action == 'fix':
                    if not test_failed:
                        return 'FORBID'
                    fixed = True
                    _write(work, case, 'config.txt', 'corrected after observed failure')
                elif action == 'author_candidate':
                    _write(work, case, 'candidate.txt', 'authorised candidate')
                else:
                    if not tests_passed or not (work / 'candidate.txt').exists():
                        return 'FORBID'
                    _write(work, case, 'pr.json', '{"reviewed": false}')
                case.effects.append(action)
                case.trace.append({'kind':'effect','action':action})
            elif action == 'run_tests':
                if case.injected_test_failure and not fixed:
                    test_failed = True
                    case.observations.append('tests_fail_observed')
                else:
                    tests_passed = True
                    case.observations.append('tests_pass_observed')
                    if (case.requested_deliverable_is_implementation_and_tests and
                            (work / 'candidate.txt').exists()):
                        return 'COMPLETE'
            elif action == 'teardown':
                resource_present = False
                case.observations.append('teardown_verified')
            elif action == 'verify':
                if not tests_passed or resource_present:
                    return 'FORBID'
                case.observations.append('restoration_verified')
            elif action == 'write_review':
                if case.operation != '/review' or case.read_only or not case.reviewer_fresh:
                    case.observations.append('review_write_forbidden')
                    return 'FORBID'
                if case.exact_head != case.observed_head:
                    case.observations.append('stale_head')
                    return 'FORBID'
                _write(work, case, 'review.json', '{"head": "' + case.exact_head + '"}')
                case.effects.append(action)
                case.trace.append({'kind':'effect','action':action})
            elif action == 'deploy':
                if not case.deployment_authorised:
                    return 'REQUIRE_OWNER'
                case.effects.append(action)
                case.trace.append({'kind':'effect','action':action})
            elif action == 'merge':
                return 'REQUIRE_OWNER'
            elif action == 'request_fresh_review':
                return 'REVIEW_REQUIRED'
            elif action == 'mark_complete':
                if case.pending_required_review and (work / 'pr.json').exists():
                    return 'REVIEW_REQUIRED'
                if triggered and not _current_closure(case.closure_evidence):
                    return 'CLOSURE_REQUIRED'
                if not tests_passed:
                    return 'BLOCKED'
                return 'COMPLETE'
            else:
                raise ValueError('unknown test action: ' + action)
            if case.operation == '/step':
                case.observations.append('one_transition_limit')
                return 'ONE_TRANSITION'
        return 'IN_PROGRESS'
    finally:
        if owned:
            owned.cleanup()
