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


def get_dummy_contacts() -> list[dict]:
    return [
        {
            "contact_id": 1,
            "name": "Alice Smith",
            "email": "alice@example.com",
            "phone": "555-1234"
        },
        {
            "contact_id": 2,
            "name": "Bob Johnson",
            "email": "bob@example.com",
            "phone": "555-5678"
        },
        {
            "contact_id": 3,
            "name": "Cathy Lee",
            "email": "cathy@example.com",
            "phone": "555-9012"
        },
        {
            "contact_id": 4,
            "name": "David Kim",
            "email": "david.kim@example.com",
            "phone": None
        }
    ]

def get_dummy_templates() -> list[dict]:
    return [
        {
            "template_id": 101,
            "title": "Welcome",
            "subject": "Welcome to Our Service",
            "body": "Hi {name}, welcome to our service!"
        },
        {
            "template_id": 102,
            "title": "Follow Up",
            "subject": "Just Checking In",
            "body": "Hey {name}, just following up on our last conversation."
        },
        {
            "template_id": 103,
            "title": "Reminder",
            "subject": "Don't Miss Out",
            "body": "Hi {name}, don't forget about your upcoming appointment!"
        },
        {
            "template_id": 104,
            "title": "Thank You",
            "subject": "Thanks for Reaching Out",
            "body": "Hello {name}, thanks for getting in touch with us!"
        }
    ]

def get_dummy_emails() -> list[dict]:
    return[
        {
            "email": "alice@example.com",
            "subject": "Meeting Tomorrow",
            "body": "Hi, just a reminder about our meeting tomorrow at 10am."
        },
        {
            "email": "bob@example.com",
            "subject": "Follow-up",
            "body": "Can you send me the files we discussed?"
        },
        {
            "email": "cathy@example.com",
            "subject": "Weekend Plans",
            "body": "Are we still on for hiking this weekend?"
        }
    ]
