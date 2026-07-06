from knowledge_base.retriver import retrieve_inventory


def simulate_inventory_shortage():

    result = retrieve_inventory(
        "low stock inventory",
        1
    )

    item = result[0]

    lines = item.strip().split("\n")
    sku = lines[0].split(":")[1].strip()
    product = lines[1].split(":")[1].strip()
    current_stock = lines[2].split(":")[1].strip()
    reorder_point = lines[3].split(":")[1].strip()

    return {
        "event": "Inventory Shortage",
        "sku": sku,
        "product": product,
        "current_stock": current_stock,
        "reorder_point": reorder_point,
        "impact": "Potential Stockout"
}