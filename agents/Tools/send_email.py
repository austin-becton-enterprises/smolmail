"""
Tool: EmailSender
Purpose: writes and sends email on behalf of the user 
"""
from smolagents.tools import Tool
import app.sample_data.mock_data as mockData
from app.core.gmail_api import API

class EmailSender(): 
    name = "send_email"
    description ={
        "After reading and writing an email,"
        "this tool will finalize the email"
        "this tool will send an email with a subject and message to the recipient's email address."
    }
   
    inputs = {
        "recipient_email": "The email address to send the email to (e.g. john@example.com).",
        "subject": "The subject line of the email (e.g. 'Meeting Reminder').",
        "message": "The body of the email to be sent.",
        "signature": "Optional: Signature to include at the end of the email (e.g. 'Best, Emma')."
    }

    output_type = "string"
    def __init__(self):
        super().__init__()
        self.api = API()

    def forward(self, recipient_email: str, subject: str, message: str) -> str:
        if not recipient_email or not subject or not message:
            return "Recipient email, subject, and message cannot be empty."
        try:
            # Here you would add the actual email sending logic
            # For now, we just simulate success
            return f"Email sent successfully to {recipient_email}"
        except Exception as e:
            return f"Failed to send email: {str(e)}"