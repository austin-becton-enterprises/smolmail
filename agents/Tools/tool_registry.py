"""
Tool: ToolRegistry
Purpose: Automatically loads and registers all Tool classes in the application.
"""
from smolagents import Tool
from agents.Tools.generate_email_tool import WriteGenerateEmailTool
from agents.Tools.manage_template import ManageTemplateTool
from access_database import AccessDatabaseTool
from validation_tool import ValidationTool

registered_tools = [
    EmailReader(),
    WriteGenerateEmailTool(),
    ManageTemplateTool(),
    AccessDatabaseTool(),
    ValidationTool()
]

def get_tool_names():
    return [tool.name for tool in registered_tools]

def test_tools_loaded():
    expected = {
        "write_email",
        "manage_templates",
        "access_database",
        "validate_input"
    }
    assert set(get_tool_names()) == expected, "Mismatch in registered tools"

if __name__ == "__main__":
    print("Registered tools:")
    for name in get_tool_names():
        print(f" - {name}")