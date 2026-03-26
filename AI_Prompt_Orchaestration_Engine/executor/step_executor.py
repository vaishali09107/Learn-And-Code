from typing import Callable, Optional

from steps.base_step import BaseStep

MAX_RETRY_ATTEMPTS = 3


class StepExecutor:

    def __init__(
        self,
        primary_step: BaseStep,
        fallback_step: Optional[BaseStep] = None,
        retry_attempts: int = 0,
        condition: Optional[Callable[[str], bool]] = None,
    ):
        if retry_attempts < 0 or retry_attempts > MAX_RETRY_ATTEMPTS:
            raise ValueError(f"retry_attempts must be between 0 and {MAX_RETRY_ATTEMPTS}")

        self._primary_step = primary_step
        self._fallback_step = fallback_step
        self._retry_attempts = retry_attempts
        self._condition = condition

    def run(self, step_input: str, workflow_trace_id: str) -> str:
        if not self._should_run(step_input):
            return step_input

        result = self._execute_with_retry(step_input, workflow_trace_id)
        return result

    def _should_run(self, step_input: str) -> bool:
        if self._condition is None:
            return True
        return self._condition(step_input)

    def _execute_with_retry(self, step_input: str, workflow_trace_id: str) -> str:
        attempts = 0
        last_exception: Optional[Exception] = None

        while attempts <= self._retry_attempts:
            try:
                result = self._primary_step.execute(step_input)
                return result
            except Exception as exc:
                last_exception = exc
                attempts += 1

        return self._run_fallback(step_input, workflow_trace_id, last_exception)

    def _run_fallback(
        self, step_input: str, workflow_trace_id: str, original_error: Optional[Exception]
    ) -> str:
        if self._fallback_step is None:
            raise RuntimeError(
                f"Step '{self._primary_step.step_name}' failed with no fallback. "
                f"Original error: {original_error}"
            )

        return self._fallback_step.execute(step_input)