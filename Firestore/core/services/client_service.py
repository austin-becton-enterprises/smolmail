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
from utils.helpers import input_non_empty, is_valid_email, is_valid_phone, generate_unique_id

class ClientService:
    def __init__(self):
        self.fs = FirestoreService()

    def register_client(self):
        print("\n--- Register New Client ---")
        while True:
            client_id = input("Client ID (leave blank to auto-generate): ").strip()
            if not client_id:
                client_id = generate_unique_id("client", lambda cid: self.fs.read_client(cid) is not None)
                print(f"Generated Client ID: {client_id}")
                break
            elif self.fs.read_client(client_id):
                print(f"Client ID '{client_id}' already exists.")
            else:
                break

        client_name = input_non_empty("Name: ")
        client_address = input_non_empty("Address: ")

        while True:
            client_phno = input_non_empty("Phone Number: ")
            if is_valid_phone(client_phno):
                break
            print("Invalid phone number format.")

        while True:
            client_email = input_non_empty("Email: ")
            if is_valid_email(client_email):
                break
            print("Invalid email format.")

        client_zipcode = input_non_empty("Zip Code: ")

        client_data = {
            "client_name": client_name,
            "client_address": client_address,
            "client_phno": client_phno,
            "client_email": client_email,
            "client_zipcode": client_zipcode
        }

        self.fs.create_client(client_id, client_data)
        print(f"Client '{client_id}' registered successfully.")

    def list_clients(self):
        docs = self.fs.list_clients()
        return [doc.to_dict() for doc in docs]

    def read_client(self, client_id):
        return self.fs.read_client(client_id)

    def update_client(self, client_id, updates):
        self.fs.update_client(client_id, updates)
        print(f"Client '{client_id}' updated.")

    def delete_client(self, client_id):
        self.fs.delete_client(client_id)
        print(f"Client '{client_id}' deleted.")
