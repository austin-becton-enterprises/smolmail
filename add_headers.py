import os

HEADER = """# -----------------------------------------------------------------------------
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

def should_add_header(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        return "SmolMail Contributors" not in content

def add_header_to_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(HEADER + "\n\n" + content)

def add_header_to_all_py_files(root_dir):
    for foldername, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(".py"):
                full_path = os.path.join(foldername, filename)
                if should_add_header(full_path):
                    print(f"Adding header to: {full_path}")
                    add_header_to_file(full_path)

if __name__ == "__main__":
    project_dir = os.path.dirname(os.path.abspath(__file__))
    add_header_to_all_py_files(project_dir)
    print("\n Done adding headers!")
