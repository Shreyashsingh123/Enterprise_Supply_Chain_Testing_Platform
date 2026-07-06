from knowledge_base.retriver import (
    retrieve_inventory,
    retrieve_suppliers,
    retrieve_disruptions
)

def get_risk_context(query: str):

    context_parts = []

    query_lower = query.lower()

    if "inventory" in query_lower:
        context_parts.extend(
            retrieve_inventory(query, 5)
        )

    if (
        "supplier" in query_lower
        or
        "supply chain" in query_lower
    ):
        context_parts.extend(
            retrieve_suppliers(query, 5)
        )

    if (
        "cyber" in query_lower
        or
        "disruption" in query_lower
        or
        "disaster" in query_lower
    ):
        context_parts.extend(
            retrieve_disruptions(query, 5)
        )

    return "\n".join(context_parts)