from pydantic import BaseModel

class Scenario(BaseModel):
    title: str
    description: str
    severity: str

class ScenarioList(BaseModel):
    scenarios: list[Scenario] 