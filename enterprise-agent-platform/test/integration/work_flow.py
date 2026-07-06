import asyncio
import sys
from pathlib import Path

from opentelemetry import context

ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT))

from agents.specialists.test_planner_agent.agent import planner_agent
from agents.specialists.scenario_generator_agent.agent import scenario_agent
from agents.specialists.risk_analysis_agent.agent import risk_agent
from agents.specialists.execution_agent.agent import execution_agent
from agents.specialists.reporting_agent.agent import reporting_agent
from agents.specialists.risk_analysis_agent.tools import  get_risk_context
from agents.specialists.data_validation_agent.agent import  validate_data
from agents.specialists.compliance_agent.tools import (
    get_compliance_rules
)
from agents.specialists.compliance_agent.agent import (
    run_compliance_check
)


async def main():

    # STEP 1 - Planner
    plan = await planner_agent.run(
        "Create Inventory Resilience Test Plan"
    )
    print("✅ PLAN OK")

    scenario = await scenario_agent.run(
        str(plan.output)
    )
    print("✅ SCENARIO OK")


    first_scenario = scenario.output.scenarios[0]
    first_scenario = scenario.output.scenarios[0]

    context = get_risk_context(
    first_scenario.description
)

    risk_input = f"""
    Scenario:
    {first_scenario.description}

    Context:
    {context}
    """

    risk = await risk_agent.run(
        risk_input
    )

    validation = await validate_data()

    print("✅ VALIDATION OK")

    if not validation.passed:
        print("\n❌ Validation Failed")
        return

    rules = get_compliance_rules()

    compliance_input = f"""
    Compliance Rules:
    {rules}

    Scenario:
    {first_scenario.description}

    Risk Name:
    {risk.output.risk_name}

    Severity:
    {risk.output.severity}

    Impact:
    {risk.output.impact}

    Mitigation:
    {risk.output.mitigation}
    """
    compliance = await run_compliance_check()

    print("✅ COMPLIANCE OK")

    if not compliance.passed:
        print("\n❌ Compliance Failed")
        return
        
    execution = await execution_agent.run(
        risk.output.risk_name
    )

    print("✅ EXECUTION OK")

    print("ENTERING REPORTING")

    report = await reporting_agent.generate_report(
        plan=plan.output,
        scenario=first_scenario,
        risk=risk.output,
        validation=validation,
        compliance=compliance,
        execution=execution
    )

    print("REPORT CREATED")

    print("\n===== PLAN =====")
    print(plan.output)

    print("\n===== SCENARIO =====")
    print(first_scenario)

    print("\n===== RISK =====")
    print(risk.output)

    print("\n===== VALIDATION =====")
    print(validation)

    print("\n===== COMPLIANCE =====")
    print(compliance)

    print("\n===== EXECUTION =====")
    print(execution)

    print("\n===== FINAL REPORT =====")
    print(report)


if __name__ == "__main__":
    asyncio.run(main())