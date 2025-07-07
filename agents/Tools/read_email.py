"""
Tool: EmailReader
Purpose: Parses and understands emails from an inbox
"""
from smolagents.tools import Tool
import mock_data as mockData

class EmailReader(Tool):
    name = "read_email"
    description = "Reads emails from a specificed inbox and returns them.It can retrieve emails from the inbox and extract information such as the subject, sender, and text content."

    input = {
        "mode": {
            "type": "string",
            "enum": ["all", "latest", "specific"],
            "description": "Choose 'all' to read all emails, 'latest' for the newest, or 'specific' for a specific index."
        },
        "index": {
            "type": "integer",
            "description": "The index of the specific email to read (used only when mode is 'specific').",
            "default": 0
        }
    }
    examples = [
        {
            "inputs": { "email_id": "17c8e4b1a2f1e0d2" },
            "expected_output": {
                "subject": "Invoice for July Services",
                "sender": "billing@example.com",
                "body": "Dear Customer, please find attached the invoice for services rendered in July. Thank you for your business.",
                "attachments": ["invoice_july.pdf"]
            }
        },
        {
            "inputs": { "sender": "person1@client.com" },
            "expected_output": {
                "subject": "Meeting Request",
                "sender": "person1@client.com",
                "body": "Hi, can we schedule a meeting some time next week? I am available on Monday and Wednesday."
            }
        }
    ]

    output_type = "string"

    # helper method that takes in a single email (as a dictionary) and returns a nicely formatted string.
    def format_email(self, email: dict, idx: int = None) -> str:
        header = f"Email {idx}" if idx is not None else ""      # idx = index of the email, if none then skipped
        return (
            f"{header}\n"
            f"From: {email['sender']}\n"
            f"Subject: {email['subject']}\n"
            f"Body: {email['body']}\n"
        )

    
    def forward(self, mode: str, index: int = 0) -> str: 
        emails = mockData.get_dummy_templates    # grabs the mock data 

        if not emails:                  
            return "inbox is empty" 
        
        max_emails = 10     # sets a max for email to be displayed for mode = 'all'
        # this is how it decides what to output based what the is mode(all, latest, specific)
        if mode == "all":
            limited_emails = emails[:max_emails]
            return "\n\n".join([
                self.format_email(email, idx) for idx, email in enumerate(limited_emails)
            ])
        elif mode =="latest":
            return self.format_email(emails[-1])
        # index is only used if mode = 'specific'
        elif mode == "specific": 
            if 0 <= index < len(emails):
                return self.format_email(emails[index], index)
            else: 
                return f"Invalid index. Please choose betwen 0 and {len(emails) - 1}."
        else: 
            return "invalid mode. Choose 'all', 'latest', or specific'."