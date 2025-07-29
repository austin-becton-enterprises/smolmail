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


# reader tool test 
from agents.Tools.read_email import EmailReader

def start():
    reader = EmailReader()

    # testing mode = all
    print("--- All Emails ---")
    print(reader.forward(mode="all"))

    # testing mode = latest
    print("--- Latest Email ---")
    print(reader.forward(mode="latest"))

    # testing mode = specific
    print("--- Specific Email ---")
    print(reader.forward(mode="specific", index=1))

    # testing mode = 'specific' and index = invalid
    print("\n=== Invalid Index ===")
    print(reader.forward(mode="specific", index=100))

    # testing mode = invalid 
    print("\n=== Invalid Mode ===")
    print(reader.forward(mode="nonsense"))