from __future__ import annotations

from .load_estimator import estimate_cognitive_load
from .schema import AdaptationDecision, InteractionSignals, TaskContext, UserPreferences


class AdaptiveInterfacePolicy:
    """Transparent rule-based policy for HCI prototype experiments."""

    def decide(
        self,
        context: TaskContext,
        signals: InteractionSignals,
        preferences: UserPreferences | None = None,
    ) -> AdaptationDecision:
        preferences = preferences or UserPreferences()
        load_level, score = estimate_cognitive_load(context, signals)
        rationale = [f"estimated load score={score}", f"load level={load_level}"]

        if signals.revision_count >= 3:
            mode = "recovery"
            explanation = "step_by_step"
            notification = "batched"
            density = 0.45
            rationale.append("recent revisions trigger recovery support")
        elif load_level == "high" and preferences.allow_focus_mode:
            mode = "focus"
            explanation = "step_by_step" if preferences.prefer_detailed_explanations else "standard"
            notification = "urgent_only" if preferences.max_notification_batching else "batched"
            density = 0.38
            rationale.append("high load uses reduced visual density")
        elif load_level == "high":
            mode = "guided"
            explanation = "step_by_step"
            notification = "batched"
            density = 0.55
            rationale.append("focus mode disabled, using guided support")
        elif load_level == "medium":
            mode = "balanced"
            explanation = "standard"
            notification = "batched" if signals.interruption_count > 1 else "normal"
            density = 0.68
            rationale.append("medium load uses balanced explanation")
        else:
            mode = "concise"
            explanation = "standard" if preferences.prefer_detailed_explanations else "minimal"
            notification = "normal"
            density = 0.82
            rationale.append("low load keeps interface compact")

        return AdaptationDecision(
            task_id=context.task_id,
            load_level=load_level,
            interface_mode=mode,
            explanation_depth=explanation,
            notification_level=notification,
            visual_density=round(density, 2),
            autonomy_note="User can inspect, override, or disable adaptation.",
            rationale=rationale,
        )
