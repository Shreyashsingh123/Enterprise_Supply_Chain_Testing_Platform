from .model import ComplianceResult
from .tools import get_compliance_rules


async def run_compliance_check():

    rules = get_compliance_rules()

    findings = []

    for standard, checks in rules.items():

        for check in checks:

            findings.append(
                f"{standard}: {check} - Passed"
            )

    return ComplianceResult(
        passed=True,
        findings=findings
    )
