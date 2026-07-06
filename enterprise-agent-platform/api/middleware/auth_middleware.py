# from fastapi import Request
# from fastapi.responses import JSONResponse

# from auth.security import (
#     verify_access_token
# )

# PUBLIC_ROUTES = {
#     "/",
#     "/auth/login",
#     "/docs",
#     "/openapi.json",
#     "/redoc"
# }


# async def auth_middleware(
#     request: Request,
#     call_next
# ):

#     if request.url.path not in PUBLIC_ROUTES:

#         auth_header = request.headers.get(
#             "Authorization"
#         )

#         if not auth_header:

#             return JSONResponse(
#                 status_code=401,
#                 content={
#                     "message":
#                     "Authorization header missing"
#                 }
#             )

#         if not auth_header.startswith(
#             "Bearer "
#         ):

#             return JSONResponse(
#                 status_code=401,
#                 content={
#                     "message":
#                     "Invalid authorization format"
#                 }
#             )

#         token = auth_header.replace(
#             "Bearer ",
#             ""
#         )

#         payload = verify_access_token(
#             token
#         )

#         if payload is None:

#             return JSONResponse(
#                 status_code=401,
#                 content={
#                     "message":
#                     "Invalid or expired token"
#                 }
#             )

#         request.state.user = payload

#     response = await call_next(
#         request
#     )

#     return response
from fastapi import Request

async def auth_middleware(
    request: Request,
    call_next
):
    response = await call_next(request)
    return response