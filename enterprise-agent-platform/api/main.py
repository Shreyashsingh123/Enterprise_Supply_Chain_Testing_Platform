from fastapi import FastAPI

from routes.testing import (
    router as testing_router
)

from routes.auth import (
    router as auth_router
)

from routes.reports import (
    router as reports_router
)

from middleware.auth_middleware import (
    auth_middleware
)

app = FastAPI(
    title="Supply Chain Multi-Agent Platform"
)

# Register Middleware

app.middleware("http")(
    auth_middleware
)

# Register Routes

app.include_router(
    testing_router
)

app.include_router(
    reports_router
)

app.include_router(
    auth_router
)


@app.get("/")
async def home():

    return {
        "message":
        "Supply Chain Multi-Agent Platform Running"
    }