from fastapi import APIRouter

from schemas.request import TestRequest
from schemas.response import TestResponse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT))

from agents.orchestrator.agent import WorkflowOrchestrator

router = APIRouter(
    prefix="/testing",
    tags=["Testing"]
)


@router.post(
    "/run",
    response_model=TestResponse
)
async def run_test(
    request: TestRequest
):

    orchestrator = WorkflowOrchestrator()

    result = await orchestrator.run_workflow(
        request.objective
    )

    return TestResponse(
        status=result["status"],
        report=result["report"],
        report_path=result.get(
            "report_path",
            ""
        )
    )
    