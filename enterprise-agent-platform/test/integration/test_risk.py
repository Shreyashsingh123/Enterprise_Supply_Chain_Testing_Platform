# test_risk.py
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT))

import asyncio

from agents.specialists.risk_analysis_agent.agent import risk_agent

async def main():

    result = await risk_agent.run("""
    Scenario:
    Supplier Failure

    Context:
    Supplier ID: SUP001
    Risk Score: 91
    Country: China
    """)

    print(result.output)

asyncio.run(main())