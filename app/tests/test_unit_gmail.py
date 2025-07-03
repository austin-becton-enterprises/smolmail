import unittest
from unittest.mock import MagicMock
from googleapiclient.errors import HttpError
from app.core.gmail_facade import GmailService


class TestGmailService(unittest.TestCase):
    def setUp(self):
        self.mock_service = MagicMock()
        self.gmail_service = GmailService(self.mock_service)

    def test_read_most_recent_emails_no_messages(self):
        self.mock_service.users().messages().list().execute.return_value = {}

        emails = self.gmail_service.read_most_recent_emails()

        self.assertEqual(emails, [])
        print("Test_read_most_recent_emails_no_messages passed")

    def test_read_most_recent_emails_with_messages(self):
        self.mock_service.users().messages().list().execute.return_value = {
            'messages': [{'id': 'msg1'}, {'id': 'msg2'}]
        }

        def get_mock(userId='me', id=None):
            mock_resp = MagicMock()
            mock_resp.execute.return_value = {
                'payload': {
                    'headers': [
                        {'name': 'Subject', 'value': f'Subject {id}'},
                        {'name': 'From', 'value': f'sender{id}@example.com'}
                    ]
                },
                'snippet': f'Snippet {id}'
            }
            return mock_resp

        self.mock_service.users().messages().get.side_effect = get_mock

        emails = self.gmail_service.read_most_recent_emails()

        self.assertEqual(len(emails), 2)
        self.assertEqual(emails[0]['subject'], 'Subject msg1')
        self.assertEqual(emails[1]['From'], 'sendermsg2@example.com')
        print("Test_read_most_recent_emails_with_messages passed")

    def test_read_most_recent_emails_http_error(self):
        # Create a mock response with .reason to avoid AttributeError
        mock_resp = MagicMock()
        mock_resp.reason = "Mocked Error"
        http_error = HttpError(resp=mock_resp, content=b'')

        self.mock_service.users().messages().list().execute.side_effect = http_error

        emails = self.gmail_service.read_most_recent_emails()
        self.assertEqual(emails, [])
        print("Test_read_most_recent_emails_http_error passed")

    def test_send_email_success(self):
        self.mock_service.users().messages().send().execute.return_value = {'id': '123'}

        result = self.gmail_service.send_email(
            to="test@example.com",
            subject="Test Subject",
            body="Test Body"
        )

        self.assertIsNotNone(result)
        self.assertEqual(result['id'], '123')
        print("Test_send_email_success passed")

    def test_send_email_http_error(self):
        mock_resp = MagicMock()
        mock_resp.reason = "Mocked Send Error"
        http_error = HttpError(resp=mock_resp, content=b'')

        self.mock_service.users().messages().send().execute.side_effect = http_error

        result = self.gmail_service.send_email(
            to="test@example.com",
            subject="Test Subject",
            body="Test Body"
        )

        self.assertIsNone(result)
        print("Test_send_email_http_error passed")


if __name__ == '__main__':
    unittest.main()
