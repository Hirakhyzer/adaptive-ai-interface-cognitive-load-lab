from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal

LoadLevel = Literal["low", "medium", "high"]
InterfaceMode = Literal["concise", "balanced", "guided", "focus", "recovery"]
ExplanationDepth = Literal["minimal", "standard", "step_by_step"]
NotificationLevel = Literal["normal", "batched", "urgent_only"]


@dataclass(frozen=True)
class TaskContext:
    """Synthetic task context for controlled HCI experiments."""

    task_id: str
    complexity: float
    urgency: float
    information_density: float
    error_risk: float

    def __post_init__(self) -> None:
        for name in ("complexity", "urgency", "information_density", "error_risk"):
            value = getattr(self, name)
            if not 0 <= value <= 1:
                raise ValueError(f"{name} must be between 0 and 1")


@dataclass(frozen=True)
class InteractionSignals:
    """Non-clinical synthetic signals used for interface research."""

    response_time: float
    hesitation_count: int
    revision_count: int
    interruption_count: int
    help_requests: int = 0

    def __post_init__(self) -> None:
        if self.response_time < 0:
            raise ValueError("response_time must be non-negative")
        for name in ("hesitation_count", "revision_count", "interruption_count", "help_requests"):
            if getattr(self, name) < 0:
                raise ValueError(f"{name} must be non-negative")


@dataclass(frozen=True)
class UserPreferences:
    """Transparent user controls for adaptation behaviour."""

    allow_focus_mode: bool = True
    prefer_detailed_explanations: bool = False
    max_notification_batching: bool = True


@dataclass(frozen=True)
class AdaptationDecision:
    """Interface adaptation output with an auditable rationale."""

    task_id: str
    load_level: LoadLevel
    interface_mode: InterfaceMode
    explanation_depth: ExplanationDepth
    notification_level: NotificationLevel
    visual_density: float
    autonomy_note: str
    rationale: list[str] = field(default_factory=list)
