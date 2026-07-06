def calculate_risk_score(severity: str):

    mapping = {
        "Low": 25,
        "Medium": 60,
        "High": 90
    }

    return mapping.get(severity, 0)