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


import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("./firestore_credentials.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

clients = [
    {
        "client_id": "client_001",
        "client_name": "Alpha Corp",
        "client_address": "123 Alpha Street, New York",
        "client_phno": "+1-555-1111",
        "client_email": "info@alphacorp.com",
        "client_zipcode": "10001"
    },
    {
        "client_id": "client_002",
        "client_name": "Beta Solutions",
        "client_address": "789 Innovation Ave, Silicon Valley",
        "client_phno": "+1-555-2233",
        "client_email": "contact@betasolutions.com",
        "client_zipcode": "94301"
    },
    {
        "client_id": "client_003",
        "client_name": "Green Leaf Inc.",
        "client_address": "321 Eco St, Portland",
        "client_phno": "+1-555-7777",
        "client_email": "support@greenleaf.com",
        "client_zipcode": "97201"
    }
]

for client in clients:
    db.collection("clients").document(client["client_id"]).set(client)
    print("Inserted client:", client["client_id"])


templates = [
    {
        "template_id": "template_001",
        "template_desc": "Invoice Reminder",
        "template_code": "<p>Hello {{client_name}}, your invoice is ready.</p>"
    },
    {
        "template_id": "template_002",
        "template_desc": "Welcome Email",
        "template_code": "<h1>Welcome {{client_name}}</h1><p>We're glad to have you!</p>"
    },
    {
        "template_id": "template_003",
        "template_desc": "Weekly Digest",
        "template_code": "<h2>Your Weekly Update</h2><p>Check out this week's highlights!</p>"
    }
]

for template in templates:
    db.collection("templates").document(template["template_id"]).set(template)
    print(" Inserted template:", template["template_id"])

email_templates = [
    {"client_id": "client_001", "template_id": "template_001"},
    {"client_id": "client_002", "template_id": "template_002"},
    {"client_id": "client_003", "template_id": "template_001"},
    {"client_id": "client_003", "template_id": "template_003"},
]

for link in email_templates:
    db.collection("email_templates").add(link)
    print(f"Linked {link['client_id']} to {link['template_id']}")


