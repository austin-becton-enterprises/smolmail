"""
Tool: EmailSender
Purpose: writes and sends email on behalf of the user 
"""
from smolagents.tools import Tool
import app.sample_data.mock_data as mockData
from datetime import datetime

class EmailSender:
    name = "send_email"
    description = (
        "After reading and writing an email, "
        "this tool will finalize the email, "
        "this tool will send an email with a subject and message to the recipient's email address."
    )

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
        }
    }

    output_type = "string"

    def forward(self, recipient_email: str, subject: str, message: str) -> str:
        if not recipient_email or not subject or not message:
            return "Recipient email, subject, and message cannot be empty."
        try:
            # Here you would add the actual email sending logic
            # For now, we just simulate success
            current_time = datetime.now().strftime("%I:%M %p")
            return f"Email sent successfully to {recipient_email} at {current_time}"
        except Exception as e:
            return f"Failed to send email: {str(e)}"