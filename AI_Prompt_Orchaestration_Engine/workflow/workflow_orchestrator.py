import uuid
from dataclasses import dataclass, field
from typing import List

from executor.step_executor import StepExecutor


@dataclass
class WorkflowConfig:
    workflow_name: str
    step_executors: List[StepExecutor] = field(default_factory=list)


class WorkflowOrchestrator:

    def __init__(self, workflow_config: WorkflowConfig):
        self._workflow_config = workflow_config

    def run(self, workflow_input: str) -> str:
        workflow_trace_id = str(uuid.uuid4())

        result = self._execute_steps(workflow_input, workflow_trace_id)

        return result

    def _execute_steps(self, workflow_input: str, workflow_trace_id: str) -> str:
        current_output = workflow_input
        for step_executor in self._workflow_config.step_executors:
            current_output = step_executor.run(current_output, workflow_trace_id)
        return current_output