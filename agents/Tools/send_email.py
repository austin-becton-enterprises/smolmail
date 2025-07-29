# -----------------------------------------------------------------------------
# Copyright (c) 2025 SmolMail Contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# This project is open-source and maintained by the community.
# Contributions are welcome—please see the CONTRIBUTING.md file for guidelines.
#
# "SmolMail" and the SmolMail logo are trademarks of SmolMail, Inc.
# Use of these trademarks is subject to SmolMail's trademark policy.
#
# Created by Austin Becton
# -----------------------------------------------------------------------------


"""
Tool: EmailSender
Purpose: writes and sends email on behalf of the user 
"""
from smolagents.tools import Tool
import app.sample_data.mock_data as mockData

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

    def forward(self, recipient_email: str, subject: str, message: str) -> str:
        if not recipient_email or not subject or not message:
            return "Recipient email, subject, and message cannot be empty."
        try:
            # Here you would add the actual email sending logic
            # For now, we just simulate success
            return f"Email sent successfully to {recipient_email}"
        except Exception as e:
            return f"Failed to send email: {str(e)}"