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


from gmail import API
import pprint
import tool_testing.test_reader_tool as readerTool
from tool_testing.test_write_tool import generate_email_from_prompt
from dotenv import load_dotenv
import os

load_dotenv()   # load .env 

def test_authentication():
    gmail = API()
    assert gmail.is_authenticated(), "Authentication failed"
    print("Authentication test passed.")
    return gmail

def test_list_messages(gmail):
    messages = gmail.list_messages(3)
    assert isinstance(messages, list), "list_messages did not return a list"
    print(f"list_messages test passed. Retrieved {len(messages)} messages.")
    return messages

def test_get_message(gmail, message_id):
    message = gmail.get_message(message_id)
    assert 'id' in message, "get_message response is missing 'id'"
    print(f"get_message test passed for ID: {message_id}")
    return message

def test_send_email(gmail):
    to = input("Enter your email address to send a test email: ").strip()
    subject = "Gmail API Test Email"
    body = "This is a test email sent using the Gmail API."
    
    confirmation = input(f"Send email to {to}? (y/n): ").strip().lower()
    if confirmation == 'y':
        response = gmail.send_email(to, subject, body)
        assert 'id' in response, "Email not sent successfully"
        print("send_email test passed.")
        pprint.pprint(response)
    else:
        print("⚠️ Skipped sending email.")


def test_reader_tool():
    readerTool.start()


# testing write email OpenAI API KEY
def test_api_key():
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        print("OpenAI API key loaded sucessfully.")
    else:
        print("Failed to load OpenAI API key.")

def test_write_tool():
    prompt = "Email John at johnfk@gmail.com about an upcoming appointment on Tuesday May 16th at 2:30pm"

    try:
        output = generate_email_from_prompt(prompt)
        print("\nGenerated email draft:\n")
        print(output)
    except Exception as e:
        print(f"Failed to generate email: {e}")


if __name__ == '__main__':
    print("=== Gmail API Test Runner ===")

    # Step 1: Authenticate
    gmail = test_authentication()

    # Step 2: List recent messages
    messages = test_list_messages(gmail)

    # Step 3: Get the first message content
    if messages:
       test_get_message(gmail, messages[0]['id'])
    else:
       print("No messages found.")

    # Step 4: Send a test email (optional)
    test_send_email(gmail)

    # Step 5: test read email tool
    print("Running EmailReader tool tests...\n")
    test_reader_tool()

    # Step 6: test write email tool
    test_api_key()
    test_write_tool()


