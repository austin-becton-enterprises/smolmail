"""
Tool: TemplateManager
Purpose: Retrieves and manages message templates for consistent and structured AI-generated replies.
"""
from smolagents.tools import Tool
import app.sample_data.mock_data as mockData
from app.core.gmail_api import API

class TemplateManager(Tool):
    """
    A tool to retrieve and manage message templates. It can list all available
    templates or fetch a specific one by its ID or title for use in email replies.
    """
    name = "template_manager"
    description = (
        "Manages message templates. Use this tool to list available templates or "
        "retrieve the content (subject and body) of a specific template by its ID or title."
    )

    inputs = {
        "mode": {
            "type": "string",
            "enum": ["list", "get"],
            "description": "Use 'list' to see all available templates, or 'get' to retrieve a specific one."
        },
        "template_id": {
            "type": "integer",
            "description": "The unique ID of the template to retrieve (used only when mode is 'get').",
            "default": None,
            "nullable": True
            
        },
        "template_title": {
            "type": "string",
            "description": "The title of the template to retrieve (used only when mode is 'get').",
            "default": None,
            "nullable": True
        }
    }

    output_type = "string"
   
    def __init__(self):
        super().__init__()
        self.api = API()


    def format_template_content(self, template: dict) -> str:
        """Helper method to format a single template's content into a readable string."""
        return (
            f"Subject: {template['subject']}\n"
            f"Body: {template['body']}"
        )

    def forward(self, mode: str, template_id: int = None, template_title: str = None) -> str:
        """
        Executes the tool's logic to list or retrieve templates.

        Args:
            mode: The operation to perform ('list' or 'get').
            template_id: The ID of the template to retrieve.
            template_title: The title of the template to retrieve.

        Returns:
            A string containing either a list of templates or the formatted content of a single template.
        """
        templates = mockData.get_dummy_templates()

        if not templates:
            return "No message templates are available."

        # --- List Mode ---
        if mode == "list":
            # Formats each template's ID and title into a line item
            template_list = [f"ID: {t['template_id']}, Title: '{t['title']}'" for t in templates]
            return "Available templates:\n" + "\n".join(template_list)

        # --- Get Mode ---
        elif mode == "get":
            if not template_id and not template_title:
                return "Error: You must provide a 'template_id' or a 'template_title' when using 'get' mode."

            found_template = None
            # Search by ID first, as it's a unique identifier
            if template_id is not None:
                for t in templates:
                    if t['template_id'] == template_id:
                        found_template = t
                        break
            # If not found by ID, search by title (case-insensitive)
            elif template_title is not None:
                for t in templates:
                    if t['title'].lower() == template_title.lower():
                        found_template = t
                        break
            
            if found_template:
                return self.format_template_content(found_template)
            else:
                identifier = template_id if template_id is not None else f"'{template_title}'"
                return f"Error: Template with identifier {identifier} not found. Use 'list' mode to see all available templates."

        # --- Invalid Mode ---
        else:
            return "Invalid mode. Please choose between 'list' or 'get'."