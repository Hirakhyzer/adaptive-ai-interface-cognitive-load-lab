from __future__ import annotations

from .schema import InteractionSignals, LoadLevel, TaskContext


def estimate_cognitive_load(context: TaskContext, signals: InteractionSignals) -> tuple[LoadLevel, float]:
    """Estimate a simple non-clinical cognitive-load category.

    The score is intentionally transparent and synthetic. It is not intended to
    infer mental health, stress, ability, or productivity in real settings.
    """

    context_score = (
        0.35 * context.complexity
        + 0.25 * context.information_density
        + 0.20 * context.error_risk
        + 0.20 * context.urgency
    )
    signal_score = min(
        1.0,
        0.16 * signals.hesitation_count
        + 0.14 * signals.revision_count
        + 0.10 * signals.interruption_count
        + 0.12 * signals.help_requests
        + 0.02 * signals.response_time,
    )
    score = round(min(1.0, 0.62 * context_score + 0.38 * signal_score), 3)

    if score >= 0.67:
        return "high", score
    if score >= 0.38:
        return "medium", score
    return "low", score
