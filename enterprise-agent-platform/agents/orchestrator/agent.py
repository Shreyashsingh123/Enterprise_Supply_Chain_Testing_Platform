from agents.specialists.risk_analysis_agent.tools import (get_risk_context)

from agents.specialists.data_validation_agent.agent import (validate_data)

from agents.specialists.compliance_agent.agent import (run_compliance_check)

from agents.report_storage import save_report

from governance.audit.audit_logger import (audit_log)

from governance.guardrails.hallucination_guard import (check_hallucination)

from governance.guardrails.output_guard import (validate_report)

from .crew import SupplyChainCrew

from .policies import (STOP_ON_VALIDATION_FAILURE,STOP_ON_COMPLIANCE_FAILURE)

class WorkflowOrchestrator:

    def __init__(self):

        self.crew = SupplyChainCrew()
    async def run_workflow(self,objective: str):
        try:
            audit_log(
                f"Workflow Started | Objective: {objective}")

            # STEP 1 - PLAN
            plan = await self.crew.planner.run(
                objective
            )
            audit_log(
                "Planner Completed"
            )
            # STEP 2 - SCENARIO
            scenario = await self.crew.scenario.run(
                str(plan.output)
            )

            all_scenarios = (
                scenario.output.scenarios
            )

            audit_log(
                f"{len(all_scenarios)} Scenarios Generated"
            )

            # STEP 3 - RISK + EXECUTION

            all_risks = []
            all_executions = []

            for current_scenario in all_scenarios:

                context = get_risk_context(
                    current_scenario.description
                )

                risk_input = f"""
    Scenario:
    {current_scenario.description}

    Context:
    {context}
    """

                risk = await self.crew.risk.run(
                    risk_input
                )

                all_risks.append(
                    risk.output
                )

                audit_log(
                    f"Risk Generated: {risk.output.risk_name}"
                )

                execution_input = f"""
    Risk Name:
    {risk.output.risk_name}

    Impact:
    {risk.output.impact}
    """

                execution = await self.crew.execution.run(
                    execution_input
                )

                if isinstance(
                    execution,
                    list
                ):

                    all_executions.extend(
                        execution
                    )

                else:

                    all_executions.append(
                        execution
                    )

            audit_log(
                "All Scenario Executions Completed"
            )

            # STEP 4 - VALIDATION

            validation = await validate_data()

            audit_log(
                "Validation Completed"
            )

            if (
                not validation.passed
                and STOP_ON_VALIDATION_FAILURE
            ):

                return {
                    "status": "failed",
                    "report":
                    f"Validation Failed: {validation.findings}",
                    "report_path": ""
                }

            # STEP 5 - COMPLIANCE

            compliance = await run_compliance_check()

            audit_log(
                "Compliance Completed"
            )
            if (
                not compliance.passed
                and STOP_ON_COMPLIANCE_FAILURE
            ):

                return {
                    "status": "failed",
                    "report":
                    f"Compliance Failed: {compliance.findings}",
                    "report_path": ""
                }

            # STEP 6 - REPORTING

            report = await self.crew.reporting.generate_report(
                plan=plan.output,
                scenario=all_scenarios[0],
                risk=all_risks[0],
                validation=validation,
                compliance=compliance,
                execution=all_executions
            )

            audit_log(
                "Report Generated"
            )

            # GUARDRAILS

            check_hallucination(
                report
            )

            validate_report(
                report
            )

            audit_log(
                "Output Guardrails Passed"
            )

            # SAVE REPORT

            report_path = save_report(
                report
            )

            audit_log(
                f"Report Saved: {report_path}"
            )

            return {
                "status": "success",
                "report": report,
                "report_path": report_path
            }
        except Exception as e:
            audit_log(
            f"Workflow Failed: {str(e)}"
        )
            return {
            "status": "error",
            "report": str(e),
            "report_path": ""
        }