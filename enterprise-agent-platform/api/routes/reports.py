from fastapi import APIRouter
from pathlib import Path

router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)

REPORT_DIR = Path("reports")


@router.get("/")
async def get_reports():

    if not REPORT_DIR.exists():

        return {
            "reports": []
        }

    reports = [
        file.name
        for file in REPORT_DIR.glob("*.txt")
    ]

    return {
        "reports": reports
    }


@router.get("/{filename}")
async def get_report(
    filename: str
):

    if ".." in filename or "/" in filename:

        return {
            "error": "Invalid filename"
        }

    file_path = REPORT_DIR / filename

    if not file_path.exists():

        return {
            "error": "Report not found"
        }

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as f:

        content = f.read()

    return {
        "filename": filename,
        "content": content
    }