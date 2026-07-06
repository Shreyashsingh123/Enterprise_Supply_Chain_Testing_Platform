import asyncio
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT))

from agents.specialists.execution_agent.agent import (
    execution_agent
)

async def main():

    result = await execution_agent.run(
        "Supplier SUP001 unavailable for 14 days"
    )

    print(result)

asyncio.run(main())