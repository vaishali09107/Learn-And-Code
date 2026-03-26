import pytest

from executor.step_executor import StepExecutor, MAX_RETRY_ATTEMPTS
from registry.step_registry import resolve_step, register_step
from steps.base_step import BaseStep
from steps.concrete_steps import GenerateStep, SummarizeStep, TranslateStep
from workflow.workflow_orchestrator import WorkflowConfig, WorkflowOrchestrator

TRACE_ID = "test-trace-id"


class AlwaysFailStep(BaseStep):

    @property
    def step_name(self) -> str:
        return "ALWAYS_FAIL"

    def execute(self, step_input: str) -> str:
        raise RuntimeError("Simulated failure")


class EchoStep(BaseStep):

    @property
    def step_name(self) -> str:
        return "ECHO"

    def execute(self, step_input: str) -> str:
        return f"Echo: {step_input}"


class TestConcreteSteps:

    def test_generate_step_prefixes_output(self):
        step = GenerateStep()
        assert step.execute("product") == "Generated: product"

    def test_summarize_step_prefixes_output(self):
        step = SummarizeStep()
        assert step.execute("long text") == "Summary of: long text"

    def test_translate_step_prefixes_output(self):
        step = TranslateStep()
        assert step.execute("hello") == "Translated: hello"


class TestStepExecutor:

    def test_runs_primary_step_successfully(self):
        executor = StepExecutor(primary_step=GenerateStep())
        result = executor.run("input", TRACE_ID)
        assert result == "Generated: input"

    def test_uses_fallback_when_primary_fails(self):
        executor = StepExecutor(
            primary_step=AlwaysFailStep(),
            fallback_step=EchoStep(),
        )
        result = executor.run("input", TRACE_ID)
        assert result == "Echo: input"

    def test_raises_when_primary_fails_and_no_fallback(self):
        executor = StepExecutor(primary_step=AlwaysFailStep())
        with pytest.raises(RuntimeError):
            executor.run("input", TRACE_ID)

    def test_skips_step_when_condition_is_false(self):
        executor = StepExecutor(
            primary_step=GenerateStep(),
            condition=lambda x: False,
        )
        result = executor.run("input", TRACE_ID)
        assert result == "input"

    def test_runs_step_when_condition_is_true(self):
        executor = StepExecutor(
            primary_step=GenerateStep(),
            condition=lambda x: True,
        )
        result = executor.run("input", TRACE_ID)
        assert result == "Generated: input"

    def test_invalid_retry_attempts_raises(self):
        with pytest.raises(ValueError):
            StepExecutor(primary_step=GenerateStep(), retry_attempts=-1)

    def test_retry_attempts_exceeding_max_raises(self):
        with pytest.raises(ValueError):
            StepExecutor(primary_step=GenerateStep(), retry_attempts=MAX_RETRY_ATTEMPTS + 1)


class TestWorkflowOrchestrator:

    def test_runs_all_steps_in_order(self):
        config = WorkflowConfig(
            workflow_name="test_workflow",
            step_executors=[
                StepExecutor(primary_step=GenerateStep()),
                StepExecutor(primary_step=SummarizeStep()),
            ],
        )
        orchestrator = WorkflowOrchestrator(config)
        result = orchestrator.run("data")
        assert result == "Summary of: Generated: data"

    def test_empty_workflow_returns_input(self):
        config = WorkflowConfig(workflow_name="empty_workflow", step_executors=[])
        orchestrator = WorkflowOrchestrator(config)
        result = orchestrator.run("data")
        assert result == "data"


class TestStepRegistry:

    def test_resolves_known_step_type(self):
        step = resolve_step("GENERATE")
        assert isinstance(step, GenerateStep)

    def test_raises_for_unknown_step_type(self):
        with pytest.raises(ValueError, match="Unknown step type"):
            resolve_step("NONEXISTENT")

    def test_register_and_resolve_custom_step(self):
        register_step("ECHO", EchoStep)
        step = resolve_step("ECHO")
        assert isinstance(step, EchoStep)