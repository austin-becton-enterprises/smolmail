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


import unittest
from gmail import API
from gmail_service import (
    create_message,
    read_most_recent_emails,
    send_email
)


class TestGmailService(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Initialize the Gmail API service once for all tests."""
        cls.gmail = API()
        cls.service = cls.gmail.service

    def test_authentication_status(self):
        """Check if the Gmail API is authenticated."""
        self.assertTrue(self.gmail.is_authenticated())

    def test_create_message_valid(self):
        """Verify that create_message returns a proper raw base64-encoded payload."""
        msg = create_message("test@example.com", "Test Subject", "Test Body")
        self.assertIn('raw', msg)
        self.assertIsInstance(msg['raw'], str)
        self.assertGreater(len(msg['raw']), 0)

    def test_send_email_success(self):
        """Test sending a basic email to the dev/test account."""
        to = "ai.becton.0@gmail.com"
        subject = "Unit Test Email"
        body = "This is a test email from the automated test suite."
        result = send_email(self.service, to, subject, body)
        self.assertIsNotNone(result)
        self.assertIn('id', result)

    def test_send_email_invalid_address(self):
        """Send email to an invalid address and expect failure (log error, return None)."""
        to = "invalid-email"  # Not a valid format
        subject = "Fail Test"
        body = "Should not send"
        result = send_email(self.service, to, subject, body)
        self.assertIsNone(result)

    def test_read_emails_returns_list(self):
        """Verify that reading emails returns a list with expected keys."""
        emails = read_most_recent_emails(self.service)
        self.assertIsInstance(emails, list)
        if emails:
            first = emails[0]
            self.assertIn('subject', first)
            self.assertIn('From', first)
            self.assertIn('snippet', first)

    def test_list_messages_returns_ids(self):
        """Test listing message IDs from inbox."""
        messages = self.gmail.list_messages()
        self.assertIsInstance(messages, list)
        if messages:
            self.assertIn('id', messages[0])

    def test_get_message_by_id(self):
        """Test fetching the full content of one recent message."""
        messages = self.gmail.list_messages()
        if messages:
            msg_id = messages[0]['id']
            message = self.gmail.get_message(msg_id)
            self.assertIn('payload', message)


if __name__ == '__main__':
    unittest.main()
