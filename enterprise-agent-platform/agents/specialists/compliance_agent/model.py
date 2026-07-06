from pydantic import BaseModel

class ComplianceResult(BaseModel):
    passed:bool
    findings:list[str]