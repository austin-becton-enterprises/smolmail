"""
Tool: EmailSender
Purpose: writes and sends email on behalf of the user 
"""
from smolagents.tools import Tool
import app.sample_data.mock_data as mockData
from app.core.gmail_api import API

class EmailSender(Tool): 
    name = "send_email"
    description = """
        After reading and writing an email,
        this tool will finalize the email and send it with a subject and message to the recipient's email address.
    """
   
    inputs = {
        "recipient_email": {
            "type": "string",
            "description": "The email address to send the email to (e.g. john@example.com)."
        },
        "subject": {
            "type": "string",
            "description": "The subject line of the email (e.g. 'Meeting Reminder')."
        },
        "message": {
            "type": "string",
            "description": "The body of the email to be sent."
        },
        "signature": {
            "type": "string",
            "description": "Optional: Signature to include at the end of the email (e.g. 'Best, Emma')."
        }
    }

    output_type = "string"

    def __init__(self):
        super().__init__()
        self.api = API()

    def forward(self, recipient_email: str, subject: str, message: str, signature: str) -> str:
        if not recipient_email or not subject or not message:
            return "Recipient email, subject, and message cannot be empty."
        try:
            full_message = message
            if signature:
                full_message += f"\n\n{signature}"

            # Example of calling Gmail API (stubbed for now)
            # self.api.send_email(to=recipient_email, subject=subject, body=full_message)

            return f"Email sent successfully to {recipient_email} with subject '{subject}'."
        except Exception as e:
            return f"Failed to send email: {str(e)}"
