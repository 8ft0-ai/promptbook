import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLIC_COMMANDS = {
    "/go",
    "/review",
    "/plan",
    "/implement",
    "/fix",
    "/handoff",
    "/status",
}


class ReviewCompletionContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fresh = (
            ROOT / "prompts" / "workflows" / "fresh-independent-review.md"
        ).read_text(encoding="utf-8")
        cls.fresh_lower = cls.fresh.lower()
        cls.router = (ROOT / "prompts" / "workflows" / "README.md").read_text(
            encoding="utf-8"
        )
        cls.router_lower = cls.router.lower()
        cls.remediate = (
            ROOT / "prompts" / "engineering" / "remediate-review-findings.md"
        ).read_text(encoding="utf-8")
        cls.remediate_lower = cls.remediate.lower()

    def test_review_derives_and_completes_bounded_surface(self):
        self.assertIn(
            "derive a bounded decision-critical review surface for the exact candidate",
            self.fresh_lower,
        )
        for source in (
            "governing contract and acceptance criteria",
            "material candidate/diff",
            "repository-local instructions",
            "trust, safety, authority and evidence boundaries",
            "dependency/runtime semantics",
        ):
            self.assertIn(source, self.fresh_lower)
        self.assertIn(
            "review domain -> pass | blocker | not_applicable", self.fresh_lower
        )
        self.assertIn(
            "do not claim the review surface is complete while an applicable "
            "decision-critical domain remains unexamined",
            self.fresh_lower,
        )
        self.assertIn("rather than applying a universal checklist", self.fresh_lower)
        self.assertIn("exhaustive repository-wide audit", self.fresh_lower)

    def test_first_blocker_does_not_end_substantive_review(self):
        self.assertIn(
            "discovering a material blocker determines that approval is impossible, "
            "but it does not end the substantive inspection",
            self.fresh_lower,
        )
        self.assertIn(
            "continue through the bounded decision-critical review surface for the exact "
            "candidate before recording the disposition",
            self.fresh_lower,
        )
        self.assertIn(
            "discovering a material blocker ends approval eligibility but does not "
            "end the substantive inspection",
            self.router_lower,
        )

    def test_negative_disposition_reports_complete_blocker_set(self):
        self.assertIn(
            "for `changes required`, report all material blockers discovered across "
            "that completed surface",
            self.fresh_lower,
        )
        self.assertIn(
            "including every material blocker discovered across the completed "
            "bounded review surface",
            self.fresh_lower,
        )
        self.assertIn(
            "for `changes required`, report all material blockers discovered across "
            "that completed surface",
            self.router_lower,
        )

    def test_completion_claim_requires_completed_surface(self):
        self.assertIn("`i found no other material blocker`", self.fresh_lower)
        self.assertIn(
            "any equivalent completion claim, is valid only after the bounded "
            "surface has been completed",
            self.fresh_lower,
        )

    def test_fresh_rereview_verifies_fix_and_rechecks_full_surface(self):
        self.assertIn("fresh re-review after `/fix`", self.fresh_lower)
        self.assertIn("verify the prior remediations", self.fresh_lower)
        self.assertIn(
            "derive and complete the full currently applicable decision-critical "
            "review surface again",
            self.fresh_lower,
        )
        self.assertIn(
            "do not restrict re-review to the previous findings", self.fresh_lower
        )
        self.assertIn(
            "do not carry candidate-a coverage forward as proof that candidate b's "
            "surface was completed",
            self.fresh_lower,
        )

    def test_review_escape_excludes_legitimate_later_change(self):
        self.assertIn("classify a review escape narrowly", self.fresh_lower)
        self.assertIn(
            "already applicable and materially unchanged", self.fresh_lower
        )
        for exclusion in (
            "intervening remediation introduced it",
            "governing requirement became applicable only later",
            "material candidate change created a new review domain",
            "new external evidence legitimately changed the decision",
            "not yet reviewed or out of scope rather than complete",
        ):
            self.assertIn(exclusion, self.fresh_lower)

    def test_fix_remains_minimum_safe_and_bounded(self):
        self.assertIn(
            "for every valid bounded finding, derive the smallest safe correction",
            self.remediate_lower,
        )
        self.assertIn(
            "do not broaden scope, redesign adjacent components",
            self.remediate_lower,
        )
        self.assertIn(
            "complete identified blocker set without another routine approval",
            self.fresh_lower,
        )
        self.assertIn(
            "must not proactively redesign adjacent components", self.fresh_lower
        )

    def test_human_facing_output_stays_concise(self):
        self.assertIn(
            "coverage evidence may remain internal or implicit", self.fresh_lower
        )
        self.assertIn("do not emit a verbose checklist by default", self.fresh_lower)
        self.assertIn("the human-facing review may remain concise", self.fresh_lower)
        self.assertIn(
            "do not dump the internal coverage model unless it is materially needed",
            self.fresh_lower,
        )

    def test_existing_review_boundaries_and_commands_are_unchanged(self):
        self.assertIn("zero github write-back", self.router_lower)
        self.assertIn("suppress every review-record mutation", self.fresh_lower)
        self.assertIn(
            "review result never creates mutation authority", self.fresh_lower
        )
        self.assertIn(
            "must not claim a fresh independent review", self.fresh_lower
        )
        self.assertIn("single-maintainer", self.fresh_lower)

        shorthand = self.router.split("## Shorthand commands", 1)[1].split(
            "## Continuation policy", 1
        )[0]
        commands = set(re.findall(r"^- `(/[-a-z]+)(?: [^`]*)?`", shorthand, re.M))
        self.assertEqual(PUBLIC_COMMANDS, commands)


if __name__ == "__main__":
    unittest.main()
