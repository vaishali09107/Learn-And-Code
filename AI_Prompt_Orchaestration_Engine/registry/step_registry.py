from typing import Dict, Type

from steps.base_step import BaseStep
from steps.concrete_steps import (
    AnalyzeCsvStep,
    EnrichContextStep,
    GenerateInsightsStep,
    GenerateStep,
    PostProcessStep,
    RefineToneStep,
    SummarizeStep,
    TranslateStep,
)

_STEP_REGISTRY: Dict[str, Type[BaseStep]] = {
    "GENERATE": GenerateStep,
    "SUMMARIZE": SummarizeStep,
    "TRANSLATE": TranslateStep,
    "REFINE_TONE": RefineToneStep,
    "ANALYZE_CSV": AnalyzeCsvStep,
    "GENERATE_INSIGHTS": GenerateInsightsStep,
    "ENRICH_CONTEXT": EnrichContextStep,
    "POST_PROCESS": PostProcessStep,
}


def resolve_step(step_type: str) -> BaseStep:
    step_class = _STEP_REGISTRY.get(step_type)
    if step_class is None:
        raise ValueError(f"Unknown step type: '{step_type}'. Registered types: {list(_STEP_REGISTRY)}")
    return step_class()


def register_step(step_type: str, step_class: Type[BaseStep]) -> None:
    _STEP_REGISTRY[step_type] = step_class