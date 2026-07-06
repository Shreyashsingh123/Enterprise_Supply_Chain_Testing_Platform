from .tools import execute_tool

class ExecutionAgent:

    async def run(
        self,
        scenario_description: str):

        scenario = scenario_description.lower()

        results = []

        if (
            "cyber attack" in scenario
            or "cyber" in scenario
            or "ransomware" in scenario
            or "malware" in scenario
            or "data breach" in scenario
            or "security breach" in scenario
        ):

            results.append(
                {
                    "event": "Cyber Attack",
                    "affected_systems": [
                        "Inventory Management System",
                        "Supplier Communication Platform",
                        "Shipment Tracking System"
                    ],
                    "impact": (
                        "Operational disruption, "
                        "data integrity risk, "
                        "and potential supply chain downtime"
                    )
                }
            )

        if (
            "supplier failure" in scenario
            or "supplier bankruptcy" in scenario
            or "supplier insolvency" in scenario
            or "supplier disruption" in scenario
            or "supplier" in scenario
            or "vendor" in scenario
            or "insolvency" in scenario
            or "bankruptcy" in scenario
        ):

            results.append(
                execute_tool(
                    "supplier_failure"
                )
            )
        if (
            "port closure" in scenario
            or "transportation delay" in scenario
            or "shipment delay" in scenario
            or "logistics disruption" in scenario
            or "port congestion" in scenario
            or "customs hold" in scenario
            or "transportation" in scenario
            or "logistics" in scenario
        ):

            results.append(
                execute_tool(
                    "port_closure"
                )
            )

        if (
            "natural disaster" in scenario
            or "earthquake" in scenario
            or "flood" in scenario
            or "hurricane" in scenario
            or "typhoon" in scenario
            or "pandemic" in scenario
        ):

            results.append(
                {
                    "event": "Natural Disaster",
                    "affected_regions": [
                        "Supplier Network",
                        "Warehouses",
                        "Transportation Hubs"
                    ],
                    "impact": (
                        "Severe disruption across "
                        "supply chain operations"
                    )
                }
            )

        if (
            "inventory shortage" in scenario
            or "stockout" in scenario
            or "overstock" in scenario
            or "demand spike" in scenario
        ):

            results.append(
                execute_tool(
                    "inventory_shortage"
                )
            )


        if not results:

            results.append(
                {
                    "event": "Generic Supply Chain Risk",
                    "impact": "Operational Disruption",
                    "status": "Simulation Completed"
                }
            )

        return results


execution_agent = ExecutionAgent()