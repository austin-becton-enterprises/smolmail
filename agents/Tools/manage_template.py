"""
Tool: ManageTemplateTool
Purpose: List and retrieve email templates.
"""
from smolagents.tools import Tool

mock_templates = {
    "friendly": "Hi {name},\n\n{body}\n\nCheers,\nYour Team",
    "formal": "Dear {name},\n\n{body}\n\nSincerely,\nYour Company"
}

class ManageTemplateTool(Tool):
    name = "manage_templates"
    description = "Lists or retrieves specific email templates by name."

    input = {
        "action": {
            "type": "string",
            "enum": ["list", "get"],
            "description": "Use 'list' to get available templates, 'get' to retrieve a specific one."
        },
        "template_name": {
            "type": "string",
            "description": "Name of the template to retrieve (required if action is 'get').",
            "default": ""
        }
    }

    output_type = "string"

    def forward(self, action: str, template_name: str = "") -> str:
        if action == "list":
            return "Available templates: " + ", ".join(mock_templates.keys())
        elif action == "get":
            template = mock_templates.get(template_name)
            return template if template else f"Template '{template_name}' not found."
        return "Invalid action."