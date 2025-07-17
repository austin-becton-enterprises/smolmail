# Purpose: Write fresh email on behalf of user  

from smolagents.tools import Tool

class EmailWriter(Tool):
    name = "write_email"
    description = (
        "It'll take in a prompt from the user and generates an email draft on behalf of the user. "
        "It'll include recipient, subject, and body. This tool only creates email content — it does not send them."
    )

    inputs = {
        "prompt": {
            "type": "string",
            "description": "Briefly describe what the email is for. Example: 'Email example@gmail.com about an appointment on Tuesday May 16th at 2:30pm.'",
            "nullable": True,
            "default": ""
        }
    }

    output_type = "object" 
    
    def forward(self, prompt: str = "") -> dict:
        from tool_testing.test_write_tool import generate_email_from_prompt
        return generate_email_from_prompt(prompt)
            