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
            