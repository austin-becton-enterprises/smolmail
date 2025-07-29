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


import re

def input_non_empty(prompt):
    while True:
        val = input(prompt).strip()
        if val:
            return val
        print("Input cannot be empty.")

def input_choice(prompt, choices):
    choices_str = "/".join(choices)
    while True:
        val = input(f"{prompt} ({choices_str}): ").strip()
        if val in choices:
            return val
        print(f"Invalid choice. Please select from {choices_str}.")

def input_yes_no(prompt):
    while True:
        val = input(prompt).lower().strip()
        if val in ('y', 'yes'):
            return True
        if val in ('n', 'no'):
            return False
        print("Please answer y/n.")

def is_valid_email(email):
    pattern = r"[^@]+@[^@]+\.[^@]+"
    return re.match(pattern, email)

def is_valid_phone(phone):
    # Very simple check: digits, +, -, spaces allowed
    pattern = r"^[\d\+\-\s]+$"
    return re.match(pattern, phone)

def generate_unique_id(prefix, exists_func):
    import random
    while True:
        candidate = prefix + str(random.randint(1000, 9999))
        if not exists_func(candidate):
            return candidate
