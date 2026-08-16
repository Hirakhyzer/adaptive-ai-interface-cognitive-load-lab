from __future__ import annotations

from .schema import AdaptationDecision


def evaluate_adaptation(decision: AdaptationDecision) -> dict[str, float | str]:
    """Return simple synthetic evaluation indicators for a decision."""

    support_score = {
        "concise": 0.62,
        "balanced": 0.72,
        "guided": 0.82,
        "focus": 0.86,
        "recovery": 0.80,
    }[decision.interface_mode]
    interruption_risk = {
        "normal": 0.70,
        "batched": 0.42,
        "urgent_only": 0.22,
    }[decision.notification_level]
    explanation_support = {
        "minimal": 0.45,
        "standard": 0.68,
        "step_by_step": 0.86,
    }[decision.explanation_depth]

    return {
        "task_id": decision.task_id,
        "mode": decision.interface_mode,
        "support_score": round(support_score, 2),
        "interruption_risk": round(interruption_risk, 2),
        "explanation_support": round(explanation_support, 2),
        "visual_density": decision.visual_density,
    }
