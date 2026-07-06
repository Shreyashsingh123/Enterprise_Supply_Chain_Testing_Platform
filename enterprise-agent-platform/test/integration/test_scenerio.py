import asyncio
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT))

from agents.specialists.scenario_generator_agent.agent import (
    scenario_agent
)

async def main():

    result = await scenario_agent.run(
        """
        Generate a supplier disruption scenario
        """
    )

    print(result.output)

asyncio.run(main())