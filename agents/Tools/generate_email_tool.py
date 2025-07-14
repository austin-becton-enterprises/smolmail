"""
Tool: WriteGenerateEmailTool
Purpose: Generate an email using a given template and prompt (AI-powered).
"""
from smolagents.tools import Tool

class WriteGenerateEmailTool(Tool):
    name = "write_email"
    description = "Generates an email from a prompt and a selected template using an AI model."

    input = {
        "prompt": {
            "type": "string",
            "description": "The core message or intent the email should express."
        },
        "template": {
            "type": "string",
            "description": "The template text with placeholders like {body}, {name}, etc."
        }
    }

    output_type = "string"

    def forward(self, prompt: str, template: str) -> str:
        # Mock AI logic: replace placeholder with prompt
        filled_email = template.replace("{body}", prompt)
        return f"Generated Email:\n\n{filled_email}"