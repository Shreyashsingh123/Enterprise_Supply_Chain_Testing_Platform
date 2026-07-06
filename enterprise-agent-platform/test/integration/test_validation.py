import asyncio
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT))
from agents.specialists.data_validation_agent.agent import data_validate_agent

async def main():
    result = await data_validate_agent.run(
        "Inventory disruption scenario"
    )

    print(result.output)

asyncio.run(main())