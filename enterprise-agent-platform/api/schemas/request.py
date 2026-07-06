from pydantic import BaseModel


class TestRequest(BaseModel):
    objective: str


class LoginRequest(BaseModel):
    username: str
    password: str