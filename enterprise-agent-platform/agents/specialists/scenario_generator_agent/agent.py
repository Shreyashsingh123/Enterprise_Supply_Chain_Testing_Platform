from .model import Scenario, ScenarioList
from .prompts import SCENARIO_PROMPT
from dotenv import load_dotenv
from pydantic_ai import Agent
import os

load_dotenv()
MODEL_NAME = os.getenv("MODEL_NAME", "llama-3.3-70b-versatile")

scenario_agent = None
try:
    scenario_agent = Agent(
        model=f"groq:{MODEL_NAME}",
        output_type=ScenarioList,
        system_prompt=SCENARIO_PROMPT,
        retries=3,
    )
except Exception:
    scenario_agent = None