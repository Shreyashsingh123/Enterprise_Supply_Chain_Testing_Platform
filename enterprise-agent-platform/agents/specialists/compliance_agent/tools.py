import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[3]

RULES_FILE = (
    BASE_DIR
    / "knowledge_base"
    / "compliance_rules.json"
)

def get_compliance_rules():

    with open(
        RULES_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)