from typing import Any, Dict

class Tool:
    def __init__(self, name: str, description: str, function: Any):
        self.name = name
        self.description = description
        self.function = function

    def execute(self, *args, **kwargs) -> Any:
        return self.function(*args, **kwargs)

def example_tool_function(param1: str, param2: int) -> str:
    return f"Received {param1} and {param2}"

# Define tools for agents
tools: Dict[str, Tool] = {
    "example_tool": Tool(
        name="Example Tool",
        description="This tool demonstrates how to create a tool for agents.",
        function=example_tool_function
    ),
}