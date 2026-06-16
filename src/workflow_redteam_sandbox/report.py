"""Text rendering for workflow red-team results."""

from __future__ import annotations

from .models import SuiteResult


def render_text(result: SuiteResult) -> str:
    lines = [
        "Autonomous Workflow Red-Team Sandbox",
        f"Suite: {result.suite_id}",
        f"Score: {result.score}/100",
        f"Status: {result.status}",
        "",
    ]
    for scenario in result.results:
        lines.append(f"{scenario.status.upper()} {scenario.scenario_id}: {scenario.score}/100")
        for finding in scenario.findings:
            lines.append(f"  - {finding.severity.upper()} {finding.rule}: {finding.detail}")
    return "\n".join(lines).rstrip()
