from pydantic import BaseModel

class validationResult(BaseModel):
    passed:bool
    findings:list[str]
