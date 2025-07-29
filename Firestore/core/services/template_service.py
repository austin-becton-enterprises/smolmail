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


from ..firestore_service import FirestoreService
from utils.helpers import input_non_empty, generate_unique_id

class TemplateService:
    def __init__(self):
        self.fs = FirestoreService()
        self.logged_in_client_id = None

    def login(self, client_id):
        success = self.fs.login_client(client_id)
        if success:
            self.logged_in_client_id = client_id
        return success

    def logout(self):
        self.fs.logout_client()
        self.logged_in_client_id = None
        print("Logged out.")

    def create_template(self):
        if not self.logged_in_client_id:
            print("Please login first.")
            return

        while True:
            template_id = input("Template ID (leave blank to auto-generate): ").strip()
            if not template_id:
                template_id = generate_unique_id("template", lambda tid: self.fs.read_template(tid) is not None)
                print(f"Generated Template ID: {template_id}")
                break
            elif self.fs.read_template(template_id):
                print(f"Template ID '{template_id}' already exists.")
            else:
                break

        template_desc = input_non_empty("Template Description: ")
        print("Enter Template Code (use {placeholders} for client fields):")
        template_code = input_non_empty("Template Code: ")

        template_data = {
            "template_desc": template_desc,
            "template_code": template_code
        }

        self.fs.create_template(template_id, template_data)
        print(f"Template '{template_id}' created.")

    def list_templates(self):
        docs = self.fs.list_templates()
        return [doc.to_dict() for doc in docs]

    def read_template(self, template_id):
        return self.fs.read_template(template_id)

    def update_template(self, template_id, updates):
        self.fs.update_template(template_id, updates)
        print(f"Template '{template_id}' updated.")

    def delete_template(self, template_id):
        self.fs.delete_template(template_id)
        print(f"Template '{template_id}' deleted.")

    def render_template(self, template_id):
        template = self.fs.read_template(template_id)
        client = self.fs.read_client(self.logged_in_client_id)
        if not template:
            print("Template not found.")
            return
        if not client:
            print("Client data not found.")
            return
        try:
            rendered = self.fs.render_template(template['template_code'], client)
            print("\n--- Rendered Template ---")
            print(rendered)
            print("-------------------------")
        except Exception as e:
            print(f"Error rendering template: {e}")

    def log_email(self, template_id, metadata=None):
        email_id = self.fs.log_email(template_id, metadata)
        print(f"Email logged with ID: {email_id}")

    def get_emails(self):
        docs = self.fs.get_emails_for_logged_in_client()
        return [doc.to_dict() for doc in docs]
