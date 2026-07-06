from knowledge_base.retriver import retrieve_shipments


def simulate_port_closure():

    result = retrieve_shipments(
        "delayed shipment",
        1
    )

    shipment = result[0]

    return {
        "event": "Port Closure",
        "shipment": shipment,
        "impact": "Shipment Delay"
    }