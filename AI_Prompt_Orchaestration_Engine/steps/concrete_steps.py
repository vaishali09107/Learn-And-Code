from steps.base_step import BaseStep


class GenerateStep(BaseStep):

    @property
    def step_name(self) -> str:
        return "GENERATE"

    def execute(self, step_input: str) -> str:
        return f"Generated: {step_input}"


class SummarizeStep(BaseStep):

    @property
    def step_name(self) -> str:
        return "SUMMARIZE"

    def execute(self, step_input: str) -> str:
        return f"Summary of: {step_input}"


class TranslateStep(BaseStep):

    @property
    def step_name(self) -> str:
        return "TRANSLATE"

    def execute(self, step_input: str) -> str:
        return f"Translated: {step_input}"


class RefineToneStep(BaseStep):

    @property
    def step_name(self) -> str:
        return "REFINE_TONE"

    def execute(self, step_input: str) -> str:
        return f"Refined tone of: {step_input}"


class AnalyzeCsvStep(BaseStep):

    @property
    def step_name(self) -> str:
        return "ANALYZE_CSV"

    def execute(self, step_input: str) -> str:
        return f"CSV Analysis: {step_input}"


class GenerateInsightsStep(BaseStep):

    @property
    def step_name(self) -> str:
        return "GENERATE_INSIGHTS"

    def execute(self, step_input: str) -> str:
        return f"Insights from: {step_input}"


class EnrichContextStep(BaseStep):

    @property
    def step_name(self) -> str:
        return "ENRICH_CONTEXT"

    def execute(self, step_input: str) -> str:
        return f"Context enriched: {step_input}"


class PostProcessStep(BaseStep):

    @property
    def step_name(self) -> str:
        return "POST_PROCESS"

    def execute(self, step_input: str) -> str:
        return f"Post-processed: {step_input}"