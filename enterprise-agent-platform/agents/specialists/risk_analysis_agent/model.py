from pydantic import BaseModel

class RiskAssessment(BaseModel):
    risk_name:str
    severity:str
    impact:str
    mitigation:str