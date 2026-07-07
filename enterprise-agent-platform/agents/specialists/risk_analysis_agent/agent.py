from pydantic_ai import Agent
from .model import RiskAssessment
from .prompt import RISK_PROMPT

import os
from dotenv import load_dotenv

load_dotenv()

MODEL_NAME = os.getenv("MODEL_NAME", "llama-3.3-70b-versatile")

risk_agent = None
try:
    risk_agent = Agent(
        model=f"groq:{MODEL_NAME}",
        output_type=RiskAssessment,
        system_prompt=RISK_PROMPT,
        retries=3,
    )
except Exception:
    risk_agent = None