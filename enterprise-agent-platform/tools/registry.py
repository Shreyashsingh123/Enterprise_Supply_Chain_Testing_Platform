from .definations.supplier_tools import (
    simulate_supplier_failure
)

from .definations.logistics_tools import (
    simulate_port_closure
)

from .definations.inventory_tools import (
    simulate_inventory_shortage
)

TOOL_REGISTRY = {
    "supplier_failure": simulate_supplier_failure,
    "port_closure": simulate_port_closure,
    "inventory_shortage": simulate_inventory_shortage
}