from cognitive_load_interface import AdaptiveInterfacePolicy, InteractionSignals, TaskContext, UserPreferences


def test_high_load_uses_focus_when_allowed():
    context = TaskContext("case-high", complexity=0.95, urgency=0.8, information_density=0.9, error_risk=0.8)
    signals = InteractionSignals(response_time=9.0, hesitation_count=4, revision_count=1, interruption_count=3)
    decision = AdaptiveInterfacePolicy().decide(context, signals, UserPreferences(allow_focus_mode=True))

    assert decision.load_level == "high"
    assert decision.interface_mode == "focus"
    assert decision.notification_level == "urgent_only"
    assert "override" in decision.autonomy_note.lower()


def test_revisions_trigger_recovery_mode():
    context = TaskContext("case-recovery", complexity=0.5, urgency=0.3, information_density=0.4, error_risk=0.4)
    signals = InteractionSignals(response_time=4.0, hesitation_count=1, revision_count=3, interruption_count=0)
    decision = AdaptiveInterfacePolicy().decide(context, signals)

    assert decision.interface_mode == "recovery"
    assert decision.explanation_depth == "step_by_step"


def test_low_load_remains_concise():
    context = TaskContext("case-low", complexity=0.1, urgency=0.1, information_density=0.2, error_risk=0.1)
    signals = InteractionSignals(response_time=1.5, hesitation_count=0, revision_count=0, interruption_count=0)
    decision = AdaptiveInterfacePolicy().decide(context, signals)

    assert decision.load_level == "low"
    assert decision.interface_mode == "concise"
