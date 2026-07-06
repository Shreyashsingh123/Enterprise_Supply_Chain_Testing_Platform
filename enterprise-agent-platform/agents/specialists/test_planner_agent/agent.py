from pydantic_ai import Agent
from .model import TestPlan
from .prompt import PLANNER_PROMPT
import os
from dotenv import load_dotenv
load_dotenv()
MODEL_NAME=os.getenv("MODEL_NAME")
planner_agent=Agent(
    model=f"groq:{MODEL_NAME}",
    output_type=TestPlan,
    system_prompt=PLANNER_PROMPT,
    retries=3
)