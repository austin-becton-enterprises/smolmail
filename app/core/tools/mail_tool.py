from smolagents.tools import Tool as BaseTool

class MailTool(BaseTool):
    name = "Mail_Tool"
    description = "Generates a reply message given an email snippet."
    inputs = {
        "snippet": {
            "type": "string",
            "description": "The email content to generate a reply for."
        }
    }
    output_type = "string"

    def forward(self, snippet: str) -> str:
        # Dummy example. Replace with logic or call to LLM if needed
        return f"Thank you for your message. Regarding: '{snippet}', I will get back to you shortly."