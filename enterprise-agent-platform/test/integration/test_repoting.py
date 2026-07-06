import asyncio
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT))

from agents.specialists.reporting_agent.agent import (
    reporting_agent
)


class Plan:
    objective = "Inventory Resilience"


class Scenario:
    title = "Supplier Failure"


class Risk:
    impact = "Inventory Shortage"
    mitigation = "Activate Backup Supplier"


class Compliance:
    findings = [
        "ISO 9001 Passed",
        "SOX Passed"
    ]
class Validation:
    findings = [
        "No missing values",
        "No duplicate records"
    ]

async def main():

    report = await reporting_agent.generate_report(
        plan=Plan(),
        scenario=Scenario(),
        risk=Risk(),
        validation=Validation(),
        compliance=Compliance(),
        execution={"status": "SUCCESS"}
    )

    print(report)


asyncio.run(main())