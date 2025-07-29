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
Tool: EmailReader
Purpose: Parses and understands emails from an inbox
"""
from smolagents.tools import Tool
from app.sample_data import mock_data as mockData


class EmailReader(Tool):
    name = "read_email"
    description = (
        "Parses and returns email from specified inbox. "
        "Supports retrieving all emails, the latest email, or a specific email by index. "
        "Returns the sender, object, and body content of the email. "
    )
    inputs = {
        "mode": {
            "type": "string",
            "enum": ["all", "latest", "specific"],
            "description": "Choose 'all' to read all emails, 'latest' for the newest, or 'specific' for a specific index."
        },
        "index": {
            "type": "integer",
            "description": "The index of the specific email to read (used only when mode is 'specific').",
            "default": 0,
            "nullable": True
        }
    }

    output_type = "string"

    # helper method that takes in a single email (as a dictionary) and returns a nicely formatted string.
    def format_email(self, email: dict, idx: int = None) -> str:
        header = f"Email {idx}" if idx is not None else ""      # idx = index of the email, if none then skipped
        return (
            f"{header}\n"
            f"From: {email['email']}\n"
            f"Subject: {email['subject']}\n"
            f"Body: {email['body']}\n"
        )
    
    
    def forward(self, mode: str, index: int = 0) -> str: 
        emails = mockData.get_dummy_emails()    # grabs the mock data 

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
                return f"Invalid index. Please choose between 0 and {len(emails) - 1}."
        else: 
            return "invalid mode. Choose 'all', 'latest', or specific'."
        
        #hellotest
            return "Invalid mode. Choose 'all', 'latest', or 'specific'."
