from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parents[2]

LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

AUDIT_FILE = LOG_DIR / "audit.log"


def audit_log(event: str):

    print(f"AUDIT => {event}")
    print(f"LOG FILE => {AUDIT_FILE}")

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    with open(
        AUDIT_FILE,
        "a",
        encoding="utf-8"
    ) as f:

        f.write(
            f"{timestamp} | {event}\n"
        )