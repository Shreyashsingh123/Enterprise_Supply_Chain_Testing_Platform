from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent

REPORT_DIR = BASE_DIR / "reports"

REPORT_DIR.mkdir(exist_ok=True)

def save_report(report: str):

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    file_path = REPORT_DIR / f"report_{timestamp}.txt"

    print("=" * 50)
    print("BASE_DIR:", BASE_DIR)
    print("REPORT_DIR:", REPORT_DIR)
    print("FILE_PATH:", file_path)
    print("EXISTS:", REPORT_DIR.exists())
    print("=" * 50)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(report)

    print("REPORT SAVED SUCCESSFULLY")

    return str(file_path)