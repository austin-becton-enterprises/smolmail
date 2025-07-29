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


from typing import Optional, Dict, Union

# Contact model
class Contact:
    def __init__(self, contact_id: int, name: str, email: str, phone: Optional[str] = None) -> None:
        self.contact_id = contact_id
        self.name = name
        self.email = email
        self.phone = phone

    def to_dict(self) -> Dict[str, Union[int, str, None]]:
        return {
            "contact_id": self.contact_id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone
        }

# Template model
class Template:
    def __init__(self, template_id: int, title: str, subject: str, body: str) -> None:
        self.template_id = template_id
        self.title = title
        self.subject = subject
        self.body = body

    def to_dict(self) -> Dict[str, Union[int, str]]:
        return {
            "template_id": self.template_id,
            "title": self.title,
            "subject": self.subject,
            "body": self.body
        }

# Mock databases
mock_contacts_db: Dict[int, Contact] = {}
mock_templates_db: Dict[int, Template] = {}

# CRUD for Contact
def create_contact(contact_id: int, name: str, email: str, phone: Optional[str] = None) -> str:
    if contact_id in mock_contacts_db:
        return f"Contact with ID {contact_id} already exists."
    contact = Contact(contact_id, name, email, phone)
    mock_contacts_db[contact_id] = contact
    return f"Contact {name} created."

def read_contact(contact_id: int) -> Union[Dict[str, Union[int, str, None]], str]:
    contact = mock_contacts_db.get(contact_id)
    return contact.to_dict() if contact else "Contact not found."

def update_contact(contact_id: int, name: Optional[str] = None, email: Optional[str] = None, phone: Optional[str] = None) -> str:
    contact = mock_contacts_db.get(contact_id)
    if not contact:
        return "Contact not found."
    if name:
        contact.name = name
    if email:
        contact.email = email
    if phone:
        contact.phone = phone
    return f"Contact {contact_id} updated."

def delete_contact(contact_id: int) -> str:
    if contact_id in mock_contacts_db:
        del mock_contacts_db[contact_id]
        return f"Contact {contact_id} deleted."
    return "Contact not found."

# CRUD for Template
def create_template(template_id: int, title: str, subject: str, body: str) -> str:
    if template_id in mock_templates_db:
        return f"Template with ID {template_id} already exists."
    template = Template(template_id, title, subject, body)
    mock_templates_db[template_id] = template
    return f"Template '{title}' created."

def read_template(template_id: int) -> Union[Dict[str, Union[int, str]], str]:
    template = mock_templates_db.get(template_id)
    return template.to_dict() if template else "Template not found."

def update_template(template_id: int, title: Optional[str] = None, subject: Optional[str] = None, body: Optional[str] = None) -> str:
    template = mock_templates_db.get(template_id)
    if not template:
        return "Template not found."
    if title:
        template.title = title
    if subject:
        template.subject = subject
    if body:
        template.body = body
    return f"Template {template_id} updated."

def delete_template(template_id: int) -> str:
    if template_id in mock_templates_db:
        del mock_templates_db[template_id]
        return f"Template {template_id} deleted."
    return "Template not found."
