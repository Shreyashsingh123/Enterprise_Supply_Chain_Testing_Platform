from tools.registry import TOOL_REGISTRY


def execute_tool(tool_name: str):

    tool = TOOL_REGISTRY.get(tool_name)

    if not tool:
        raise ValueError(
            f"Tool '{tool_name}' not found"
        )

    return tool()