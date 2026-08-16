# Adaptive Interface Framework

The framework is organized around four layers: task context, interaction signals, cognitive load estimation, and adaptation policy.

## 1. Task context

Task context describes the research scenario. Example variables include complexity, urgency, information density, and error risk.

## 2. Interaction signals

Interaction signals are synthetic and non-clinical. They include response time, hesitation count, revision count, interruption count, and help requests.

## 3. Load estimation

The estimator maps context and signal values into a simple low, medium, or high load category. The current estimator is rule-based and intentionally transparent for teaching and auditability.

## 4. Adaptation policy

The policy selects interface behaviour:

| Output | Meaning |
|---|---|
| Interface mode | Concise, balanced, guided, focus, or recovery. |
| Explanation depth | Minimal, standard, or step-by-step. |
| Notification level | Normal, batched, or urgent-only. |
| Visual density | Approximate amount of information shown at once. |

## Design principles

- Explain why adaptation happened.
- Allow users to inspect and override changes.
- Avoid hidden scoring of users.
- Use synthetic experiments before any participant-facing study.
- Treat adaptation as assistance rather than evaluation of ability.
