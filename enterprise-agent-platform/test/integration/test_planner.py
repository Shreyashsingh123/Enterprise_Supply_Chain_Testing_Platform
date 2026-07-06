import asyncio
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT))

import asyncio
from agents.specialists.test_planner_agent.agent import planner_agent

async def main():
    result = await planner_agent.run(
        "Create Inventory Resilience Test Plan"
    )

    print(result.output)

asyncio.run(main())