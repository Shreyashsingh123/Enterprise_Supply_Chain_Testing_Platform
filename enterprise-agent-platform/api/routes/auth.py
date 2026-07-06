from fastapi import APIRouter

from schemas.request import (
    LoginRequest
)

from schemas.response import (
    LoginResponse
)

from auth.auth_handler import (
    authenticate_user
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post(
    "/login",
    response_model=LoginResponse
)
async def login(
    request: LoginRequest
):

    token = authenticate_user(
        request.username,
        request.password
    )

    if not token:

        return LoginResponse(
            access_token="",
            token_type=""
        )

    return LoginResponse(
        access_token=token,
        token_type="bearer"
    )