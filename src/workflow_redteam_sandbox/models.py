"""Result models for workflow red-team scenarios."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class Finding:
    scenario_id: str
    severity: str
    rule: str
    detail: str

    def to_dict(self) -> dict[str, str]:
        return {
            "scenario_id": self.scenario_id,
            "severity": self.severity,
            "rule": self.rule,
            "detail": self.detail,
        }


@dataclass(frozen=True)
class ScenarioResult:
    scenario_id: str
    score: int
    status: str
    findings: list[Finding] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "scenario_id": self.scenario_id,
            "score": self.score,
            "status": self.status,
            "findings": [finding.to_dict() for finding in self.findings],
        }


@dataclass(frozen=True)
class SuiteResult:
    suite_id: str
    score: int
    status: str
    results: list[ScenarioResult]

    def to_dict(self) -> dict[str, Any]:
        return {
            "suite_id": self.suite_id,
            "score": self.score,
            "status": self.status,
            "results": [result.to_dict() for result in self.results],
        }
