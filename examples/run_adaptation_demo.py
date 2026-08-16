from cognitive_load_interface import (
    AdaptiveInterfacePolicy,
    InteractionSignals,
    TaskContext,
    UserPreferences,
    evaluate_adaptation,
)


def main() -> None:
    context = TaskContext(
        task_id="complex-dashboard-review",
        complexity=0.82,
        urgency=0.63,
        information_density=0.78,
        error_risk=0.70,
    )
    signals = InteractionSignals(
        response_time=8.5,
        hesitation_count=3,
        revision_count=1,
        interruption_count=2,
        help_requests=1,
    )
    preferences = UserPreferences(
        allow_focus_mode=True,
        prefer_detailed_explanations=False,
        max_notification_batching=True,
    )

    policy = AdaptiveInterfacePolicy()
    decision = policy.decide(context, signals, preferences)
    metrics = evaluate_adaptation(decision)

    print("Adaptation decision")
    print(decision)
    print("\nSynthetic evaluation indicators")
    print(metrics)


if __name__ == "__main__":
    main()
