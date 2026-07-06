from pydantic import BaseModel

class TestPlan(BaseModel):
    objectives:str
    scenarios:list[str]
    success_criteria:list[str]
