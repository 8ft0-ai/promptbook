import importlib.util
import re
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "validate_promptbook", ROOT / "scripts" / "validate_promptbook.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)

PUBLIC_COMMANDS = {
    "/go",
    "/review",
    "/plan",
    "/implement",
    "/fix",
    "/handoff",
    "/status",
}
COMMAND_RE = re.compile(r"`(/[-a-z]+)(?:\s[^`]*)?`")


def declared_commands(text: str, heading: str) -> set[str]:
    return {
        match.group(1)
        for match in COMMAND_RE.finditer(MODULE.section(text, heading))
    }


class PromptbookValidationTests(unittest.TestCase):
    def test_repository_is_valid(self):
        self.assertEqual([], MODULE.validate_repository(ROOT))

    def test_unknown_status_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "prompt.md"
            path.write_text(
                "# Test\n\n"
                "## Purpose\nX\n\n## When to use\nX\n\n"
                "## Prompt\n```text\nDo X\n```\n\n"
                "## Inputs\nNone.\n\n## What it does\nX\n\n"
                "## Boundaries / limitations\nX\n\n## Status\n`unknown`\n",
                encoding="utf-8",
            )
            errors = MODULE.validate_prompt_file(path)
            self.assertTrue(any("status must be one of" in error for error in errors))

    def test_undeclared_placeholder_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "prompt.md"
            path.write_text(
                "# Test\n\n"
                "## Purpose\nX\n\n## When to use\nX\n\n"
                "## Prompt\n```text\nReview <TARGET>\n```\n\n"
                "## Inputs\nNone.\n\n## What it does\nX\n\n"
                "## Boundaries / limitations\nX\n\n## Status\n`tested`\n",
                encoding="utf-8",
            )
            errors = MODULE.validate_prompt_file(path)
            self.assertTrue(any("placeholder <TARGET>" in error for error in errors))

    def test_private_identifier_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "doc.md"
            errors = MODULE.validate_text_safety(path, "source: ai-prompt-library")
            self.assertTrue(errors)

    def test_prompt_index_lists_all_published_prompts(self):
        prompt_root = ROOT / "prompts"
        index_text = (prompt_root / "README.md").read_text(encoding="utf-8")

        self.assertEqual([], MODULE.validate_prompt_index(prompt_root))
        for target in (
            "workflows/resolved-agent-run-context.md",
            "workflows/executor-capability-projection.md",
            "workflows/operational-artifact-handoff.md",
        ):
            self.assertIn(target, index_text)

        workflow_lines = [
            line
            for line in MODULE.section(index_text, "Workflows").splitlines()
            if line.strip()
        ]
        self.assertTrue(workflow_lines[0].startswith("- [Workflow router"))

    def test_prompt_index_rejects_omitted_published_prompt(self):
        with tempfile.TemporaryDirectory() as tmp:
            prompt_root = Path(tmp) / "prompts"
            workflow_root = prompt_root / "workflows"
            workflow_root.mkdir(parents=True)
            (prompt_root / "README.md").write_text(
                "# Prompts\n\n## Workflows\n\n",
                encoding="utf-8",
            )
            (workflow_root / "missing.md").write_text(
                "# Missing\n\n"
                "## Purpose\nX\n\n## When to use\nX\n\n"
                "## Prompt\n```text\nDo X\n```\n\n"
                "## Inputs\nNone.\n\n## What it does\nX\n\n"
                "## Boundaries / limitations\nX\n\n## Status\n`tested`\n",
                encoding="utf-8",
            )

            errors = MODULE.validate_prompt_index(prompt_root)
            self.assertTrue(
                any(
                    "published prompt missing from index: workflows/missing.md" in error
                    for error in errors
                )
            )

    def test_prompt_index_excludes_readme_support_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            prompt_root = Path(tmp) / "prompts"
            workflow_root = prompt_root / "workflows"
            workflow_root.mkdir(parents=True)
            (prompt_root / "README.md").write_text("# Prompts\n", encoding="utf-8")
            (workflow_root / "README.md").write_text(
                "# Workflow support index\n",
                encoding="utf-8",
            )

            self.assertEqual([], MODULE.published_prompt_files(prompt_root))
            self.assertEqual([], MODULE.validate_prompt_index(prompt_root))

    def test_workflow_router_contract(self):
        text = (ROOT / "prompts" / "workflows" / "README.md").read_text(encoding="utf-8")
        lower = text.lower()

        for target in (
            "autonomous-progression.md",
            "documentation-assessment.md",
            "fresh-independent-review.md",
            "next-session-handover.md",
            "../engineering/plan-an-issue.md",
            "../engineering/implement-an-approved-issue.md",
            "../engineering/remediate-review-findings.md",
        ):
            self.assertIn(target, text)

        for terminal_state in (
            "EXTERNAL_REQUIRED",
            "DECISION_REQUIRED",
            "BLOCKED",
            "COMPLETE",
        ):
            self.assertIn(terminal_state, text)

        self.assertEqual(PUBLIC_COMMANDS, declared_commands(text, "Shorthand commands"))

        self.assertIn("fresh", lower)
        self.assertIn("not genuinely fresh", lower)
        self.assertIn("handover", lower)
        self.assertIn("approval", lower)
        self.assertIn("execution authority", lower)
        self.assertIn("return control to the governing workflow", lower)
        self.assertIn("minimum-safe remediation", lower)
        self.assertIn("final deliverable", lower)
        self.assertIn("does not itself create mutation authority", lower)
        self.assertIn("commands do not grant authority beyond the narrow operation authority", lower)
        self.assertIn("ordinary `/review` includes the narrow authority", lower)
        self.assertIn("zero github write-back", lower)
        self.assertIn("read-only", lower)
        self.assertIn("routine `proceed` confirmation", lower)
        self.assertIn("one concrete complete external action", lower)
        self.assertIn("complete copy/paste script or exact commands", lower)
        self.assertIn("exact browser/ui steps", lower)
        self.assertIn("exact evidence/output", lower)
        self.assertIn("do not make the human ask how to continue", lower)
        self.assertIn("only as evidence for the named check", lower)
        self.assertIn("resume the governing workflow automatically", lower)
        self.assertIn("refresh only the decision-critical state", lower)
        self.assertIn("machine-verifiable checks", lower)
        self.assertIn("on `fail`, preserve fail-closed behaviour", lower)

        for pattern in MODULE.PRIVATE_PATTERNS.values():
            self.assertNotIn(pattern, text)

    def test_documentation_assessment_workflow_contract(self):
        workflow = (
            ROOT / "prompts" / "workflows" / "documentation-assessment.md"
        ).read_text(encoding="utf-8")
        workflow_lower = workflow.lower()
        router = (ROOT / "prompts" / "workflows" / "README.md").read_text(encoding="utf-8")
        router_lower = router.lower()
        single = (
            ROOT / "prompts" / "documentation" / "repository-assessment.md"
        ).read_text(encoding="utf-8")
        prompt_index = (ROOT / "prompts" / "README.md").read_text(encoding="utf-8")

        self.assertIn("v0.1.2", workflow)
        self.assertIn("c1e1982dd448b3574bb7e14667363ba9db326c5c", workflow)
        self.assertIn("exact commit", workflow_lower)
        self.assertIn("do not follow external `main`", workflow_lower)
        self.assertIn("level 2", workflow_lower)
        self.assertIn("level 1", workflow_lower)
        self.assertIn("level 3", workflow_lower)
        self.assertIn("DECISION_REQUIRED — Documentation assessment task set", workflow)
        self.assertIn("Recommended: ACCEPT", workflow)
        self.assertIn("ACCEPT — approve", workflow)
        self.assertIn("CHANGE — revise", workflow)
        self.assertIn("REJECT — stop", workflow)
        self.assertIn("continue without routine `proceed` confirmations", workflow_lower)
        self.assertIn("assessment does not create target-repository mutation authority", workflow_lower)
        self.assertIn("normal promptbook planning/implementation lifecycle", workflow_lower)
        self.assertIn("do not create or invoke a parallel external governance lifecycle", workflow_lower)
        self.assertIn("issueops", workflow_lower)
        self.assertIn("mandatory durable assessment publication", workflow_lower)
        self.assertIn("mutation-class machinery", workflow_lower)

        self.assertIn("documentation-assessment.md", router)
        self.assertIn(
            "representative reader tasks must be discovered, validated, or assessed together",
            router_lower,
        )
        self.assertIn("reader/task discovery or multi-task validation", router_lower)
        self.assertIn("no multi-task discovery or validation is needed", router_lower)
        self.assertIn("ordinary bounded documentation edits", router_lower)
        self.assertIn("known corrections", router_lower)
        self.assertIn("explicit drafting tasks", router_lower)
        self.assertIn("../documentation/repository-assessment.md", router)
        self.assertEqual(PUBLIC_COMMANDS, declared_commands(router, "Shorthand commands"))

        self.assertIn("level-1/single-task", single.lower())
        self.assertIn("../workflows/documentation-assessment.md", single)
        self.assertIn("workflows/documentation-assessment.md", prompt_index)

    def test_single_maintainer_router_contract(self):
        text = (ROOT / "prompts" / "workflows" / "README.md").read_text(encoding="utf-8")
        lower = text.lower()

        self.assertIn("single-maintainer repositories", lower)
        self.assertIn("same repository owner/github identity", lower)
        self.assertIn("platform limitation is not a terminal state by itself", lower)
        self.assertIn("durable repository-local comment", lower)
        self.assertIn("may still operate through the same maintainer account", lower)
        self.assertIn("branch protection", lower)
        self.assertIn("does not itself create mutation authority", lower)

    def test_decision_capsule_router_contract(self):
        text = (ROOT / "prompts" / "workflows" / "README.md").read_text(encoding="utf-8")
        lower = text.lower()

        self.assertIn("## Decision capsules", text)
        self.assertIn("recommendation-first", lower)
        self.assertIn("Recommended: A", text)
        self.assertIn("Recommended: ACCEPT", text)
        for intent in ("`ACCEPT`", "`REJECT`", "`CHOOSE <option>`", "`CHANGE <instruction>`"):
            self.assertIn(intent, text)
        self.assertIn("natural-language", lower)
        self.assertIn("voice", lower)
        self.assertIn("exactly one unresolved decision", lower)
        self.assertIn("do not silently migrate", lower)
        self.assertIn("consume accepted authority once", lower)
        self.assertIn("does not implicitly close the issue", lower)
        self.assertIn("requests revision", lower)
        self.assertIn("without another `proceed` confirmation", lower)
        self.assertIn("repository-local policy", lower)
        self.assertIn("validation", lower)
        self.assertIn("security controls", lower)

    def test_autonomous_progression_decision_capsule_contract(self):
        text = (
            ROOT / "prompts" / "workflows" / "autonomous-progression.md"
        ).read_text(encoding="utf-8")
        lower = text.lower()

        self.assertIn("recommendation-first decision capsule", lower)
        self.assertIn("a / b / c", lower)
        self.assertIn("accept / reject / change", lower)
        self.assertIn("semantic intents, not required command syntax", lower)
        self.assertIn("natural-language", lower)
        self.assertIn("voice", lower)
        self.assertIn("do not guess", lower)
        self.assertIn("proposal/revision identity", lower)
        self.assertIn("do not migrate stale approval", lower)
        self.assertIn("consume accepted authority once", lower)
        self.assertIn("resume autonomous progression immediately", lower)
        self.assertIn("reject rejects only the presented proposal", lower)
        self.assertIn("change requests a revision", lower)

    def test_external_required_handoff_contract(self):
        autonomous = (
            ROOT / "prompts" / "workflows" / "autonomous-progression.md"
        ).read_text(encoding="utf-8")
        autonomous_lower = autonomous.lower()
        handover = (
            ROOT / "prompts" / "workflows" / "next-session-handover.md"
        ).read_text(encoding="utf-8")
        handover_lower = handover.lower()

        self.assertIn("one concrete external action", autonomous_lower)
        self.assertIn("complete copy/paste script or exact commands", autonomous_lower)
        self.assertIn("exact browser or ui steps", autonomous_lower)
        self.assertIn("exact evidence or output", autonomous_lower)
        self.assertIn("do not make the human ask how to perform the external action", autonomous_lower)
        self.assertIn("syntactically complete and self-contained", autonomous_lower)
        self.assertIn("capability limitation with sufficient existing authority", autonomous_lower)
        self.assertIn("reuse that handoff", autonomous_lower)
        self.assertIn("evidence for the named check", autonomous_lower)
        self.assertIn("does not create new mutation, merge, production, close, or acceptance authority", autonomous_lower)
        self.assertIn("resume the governing workflow automatically", autonomous_lower)
        self.assertIn("refresh only the decision-critical state", autonomous_lower)
        self.assertIn("do not delegate an already-established machine-verifiable check", autonomous_lower)
        self.assertIn("on fail, preserve fail-closed behaviour", autonomous_lower)

        self.assertIn("fresh review, new chat/session, or another agent context", handover_lower)
        self.assertIn("human-operated external execution", handover_lower)
        self.assertIn("complete copy/paste script or exact commands", handover_lower)
        self.assertIn("exact browser/ui steps", handover_lower)
        self.assertIn("exact output/evidence", handover_lower)
        self.assertIn("truncated scripts", handover_lower)
        self.assertIn("do not require the human to ask how to perform the external action", handover_lower)
        self.assertIn("do not turn an already-authorised capability transfer into a new decision request", handover_lower)
        self.assertIn("reuse it after refreshing any guards", handover_lower)
        self.assertIn("directly copyable as the next prompt", handover_lower)
        self.assertIn("directly executable as the required action", handover_lower)

    def test_fresh_review_composition_contract(self):
        text = (
            ROOT / "prompts" / "workflows" / "fresh-independent-review.md"
        ).read_text(encoding="utf-8")
        lower = text.lower()

        self.assertIn("single disposition is the review record", lower)
        self.assertIn("explicitly requested as the final deliverable", lower)
        self.assertIn("return control to that workflow", lower)
        self.assertIn("minimum-safe remediation", lower)
        self.assertIn("review result never creates mutation authority", lower)
        self.assertIn("must not claim a fresh independent review", lower)
        self.assertIn("already-authorised merge, verification, and close-out", lower)

        for pattern in MODULE.PRIVATE_PATTERNS.values():
            self.assertNotIn(pattern, text)

    def test_single_maintainer_fresh_review_contract(self):
        text = (
            ROOT / "prompts" / "workflows" / "fresh-independent-review.md"
        ).read_text(encoding="utf-8")
        lower = text.lower()

        self.assertIn("not automatically of the github account", lower)
        self.assertIn("same maintainer account", lower)
        self.assertIn("recording limitation rather than a governance stop by itself", lower)
        self.assertIn("durable pr comment", lower)
        self.assertIn("must not claim a fresh independent review", lower)
        self.assertIn("same github maintainer identity", lower)
        self.assertIn("distinct reviewer identity", lower)
        self.assertIn("review result never creates mutation authority", lower)

    def test_project_bootstrap_contract(self):
        path = ROOT / "guides" / "project-bootstrap.md"
        text = path.read_text(encoding="utf-8")
        lower = text.lower()

        self.assertIn("AGENTS.md", text)
        self.assertIn("prompts/workflows/README.md", text)
        self.assertIn("8ft0-ai/promptbook@vX.Y.Z", text)
        self.assertIn("stable release", lower)
        self.assertIn("track `main`", lower)
        self.assertIn("narrow authority intrinsic to the operation", lower)
        self.assertIn("does not grant unrelated authority", lower)
        self.assertIn("`/review --read-only [target]`", text)
        self.assertIn("read-only", lower)

        for terminal_state in (
            "EXTERNAL_REQUIRED",
            "DECISION_REQUIRED",
            "BLOCKED",
            "COMPLETE",
        ):
            self.assertIn(terminal_state, text)

        self.assertEqual(PUBLIC_COMMANDS, declared_commands(text, "Shorthand commands"))

        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        using = (ROOT / "guides" / "using-promptbook.md").read_text(encoding="utf-8")
        self.assertIn("guides/project-bootstrap.md", readme)
        self.assertIn("project-bootstrap.md", using)

        for pattern in MODULE.PRIVATE_PATTERNS.values():
            self.assertNotIn(pattern, text)

    def test_single_maintainer_bootstrap_guidance(self):
        text = (ROOT / "guides" / "project-bootstrap.md").read_text(encoding="utf-8")
        lower = text.lower()

        self.assertIn("single-maintainer projects", lower)
        self.assertIn("does not need to invent a second github identity", lower)
        self.assertIn("fresh chat/session", lower)
        self.assertIn("durable repository-local comment", lower)
        self.assertIn("must not bypass branch protection", lower)
        self.assertIn("same github account", lower)
        self.assertIn("separation-of-duties", lower)

    def test_decision_capsule_guide_contract(self):
        path = ROOT / "guides" / "decision-capsules.md"
        text = path.read_text(encoding="utf-8")
        lower = text.lower()

        self.assertIn("Recommendation and choices first", text)
        self.assertIn("Recommended: A", text)
        self.assertIn("Recommended: ACCEPT", text)
        for intent in ("`ACCEPT`", "`REJECT`", "`CHOOSE <option>`", "`CHANGE <instruction>`"):
            self.assertIn(intent, text)
        self.assertIn("keyboard, touch", lower)
        self.assertIn("voice", lower)
        self.assertIn("one concrete unresolved decision", lower)
        self.assertIn("do not migrate the earlier response", lower)
        self.assertIn("consumed once", lower)
        self.assertIn("does not automatically close the issue", lower)
        self.assertIn("not implicit approval", lower)
        self.assertIn("fail closed", lower)
        self.assertIn("/go", text)
        self.assertIn("repository-local instructions", lower)

        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        using = (ROOT / "guides" / "using-promptbook.md").read_text(encoding="utf-8")
        router = (ROOT / "prompts" / "workflows" / "README.md").read_text(encoding="utf-8")
        self.assertIn("guides/decision-capsules.md", readme)
        self.assertIn("decision-capsules.md", using)
        self.assertIn("../../guides/decision-capsules.md", router)

    def test_public_command_docs_stay_aligned(self):
        surfaces = (
            (ROOT / "README.md", "Quick commands"),
            (ROOT / "guides" / "project-bootstrap.md", "Shorthand commands"),
            (ROOT / "prompts" / "workflows" / "README.md", "Shorthand commands"),
            (ROOT / "AGENTS.md", "Public interface maintenance"),
        )

        for path, heading in surfaces:
            text = path.read_text(encoding="utf-8")
            self.assertEqual(
                PUBLIC_COMMANDS,
                declared_commands(text, heading),
                f"public command vocabulary drifted in {path}",
            )

    def test_bootstrap_copy_stays_aligned_with_guide(self):
        bootstrap = (ROOT / "BOOTSTRAP").read_text(encoding="utf-8").strip()
        guide = (ROOT / "guides" / "project-bootstrap.md").read_text(encoding="utf-8")

        self.assertIn(
            f"```text\n{bootstrap}\n```",
            guide,
            "BOOTSTRAP must match the copyable project bootstrap block in the guide",
        )

    def test_agents_declares_public_interface_maintenance(self):
        text = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        lower = text.lower()

        self.assertIn("prompts/workflows/README.md", text)
        self.assertIn("README.md", text)
        self.assertIn("guides/project-bootstrap.md", text)
        self.assertIn("BOOTSTRAP", text)
        self.assertIn("regression coverage", lower)
        self.assertIn("ci fails on accidental drift", lower)
        self.assertIn("fresh-review", lower)


if __name__ == "__main__":
    unittest.main()
