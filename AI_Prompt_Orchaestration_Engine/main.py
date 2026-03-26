from executor.step_executor import StepExecutor
from registry.step_registry import resolve_step
from workflow.workflow_orchestrator import WorkflowConfig, WorkflowOrchestrator


def _build_product_description_workflow() -> WorkflowOrchestrator:
    step_executors = [
        StepExecutor(primary_step=resolve_step("GENERATE")),
        StepExecutor(primary_step=resolve_step("REFINE_TONE")),
        StepExecutor(primary_step=resolve_step("SUMMARIZE")),
        StepExecutor(
            primary_step=resolve_step("TRANSLATE"),
            fallback_step=resolve_step("SUMMARIZE"),
            retry_attempts=2,
        ),
    ]
    config = WorkflowConfig(
        workflow_name="product_description_workflow",
        step_executors=step_executors,
    )
    return WorkflowOrchestrator(config)


def _build_csv_analysis_workflow() -> WorkflowOrchestrator:
    step_executors = [
        StepExecutor(primary_step=resolve_step("ANALYZE_CSV")),
        StepExecutor(primary_step=resolve_step("GENERATE_INSIGHTS")),
        StepExecutor(primary_step=resolve_step("SUMMARIZE")),
    ]
    config = WorkflowConfig(
        workflow_name="csv_analysis_workflow",
        step_executors=step_executors,
    )
    return WorkflowOrchestrator(config)


def _build_user_query_workflow() -> WorkflowOrchestrator:
    step_executors = [
        StepExecutor(primary_step=resolve_step("ENRICH_CONTEXT")),
        StepExecutor(primary_step=resolve_step("GENERATE")),
        StepExecutor(
            primary_step=resolve_step("POST_PROCESS"),
            condition=lambda output: "Generated" in output,
        ),
    ]
    config = WorkflowConfig(
        workflow_name="user_query_workflow",
        step_executors=step_executors,
    )
    return WorkflowOrchestrator(config)


if __name__ == "__main__":
    product_workflow = _build_product_description_workflow()
    product_result = product_workflow.run("wireless headphones")
    print(f"Product Workflow Result: {product_result}\n")

    csv_workflow = _build_csv_analysis_workflow()
    csv_result = csv_workflow.run("sales_data.csv")
    print(f"CSV Workflow Result: {csv_result}\n")

    query_workflow = _build_user_query_workflow()
    query_result = query_workflow.run("What are the best headphones?")
    print(f"User Query Workflow Result: {query_result}\n")