from pydantic_ai import Agent
from .model import RiskAssessment
from .prompt import RISK_PROMPT

import os
from dotenv import load_dotenv

load_dotenv()

MODEL_NAME = os.getenv(
    "MODEL_NAME"
)

risk_agent = Agent(
    model=f"groq:{MODEL_NAME}",
    output_type=RiskAssessment,
    system_prompt=RISK_PROMPT,
    retries=3
)