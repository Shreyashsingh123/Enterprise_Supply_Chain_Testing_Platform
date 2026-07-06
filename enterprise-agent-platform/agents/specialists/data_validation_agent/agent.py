from .model import validationResult
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[3]

DATA_DIR = (
    BASE_DIR
    / "knowledge_base"
    / "synthetic_data"
)

FILES = {
    "suppliers": DATA_DIR / "suppliers.csv",
    "inventory": DATA_DIR / "inventory.csv",
    "orders": DATA_DIR / "orders.csv",
    "shipments": DATA_DIR / "shipments.csv",
    "disruptions": DATA_DIR / "disruptions.csv",
}

async def validate_data():

    findings = []
    passed = True

    for file_name, file_path in FILES.items():

        df = pd.read_csv(file_path)

        missing = df.isnull().sum().sum()
        duplicates = df.duplicated().sum()

        if missing == 0:
            findings.append(
                f"{file_name}: No missing values"
            )
        else:
            findings.append(
                f"{file_name}: {missing} missing values"
            )
            passed = False

        if duplicates == 0:
            findings.append(
                f"{file_name}: No duplicate records"
            )
        else:
            findings.append(
                f"{file_name}: {duplicates} duplicate records"
            )
            passed = False

    return validationResult(
        passed=passed,
        findings=findings
    )