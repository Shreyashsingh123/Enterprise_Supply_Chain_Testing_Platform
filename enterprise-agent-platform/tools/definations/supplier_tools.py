from knowledge_base.retriver import retrieve_suppliers


def simulate_supplier_failure():

    supplier_text = retrieve_suppliers(
        "high risk supplier",
        1
    )[0]

    lines = supplier_text.strip().split("\n")

    supplier_id = lines[0].split(":")[1].strip()
    name = lines[1].split(":")[1].strip()
    country = lines[2].split(":")[1].strip()
    risk_score = lines[3].split(":")[1].strip()

    return {
        "event": "Supplier Failure",
        "supplier_id": supplier_id,
        "supplier_name": name,
        "country": country,
        "risk_score": risk_score,
        "impact": "Supply Chain Disruption"
    }