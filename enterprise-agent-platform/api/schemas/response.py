from pydantic import BaseModel

class TestResponse(BaseModel):

    status: str

    report: str

    report_path: str


class ReportResponse(BaseModel):
    report: str

class LoginResponse(BaseModel):
    access_token: str
    token_type: str