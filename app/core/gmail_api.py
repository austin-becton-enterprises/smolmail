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


from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os.path


class API:
    SCOPES = ['https://www.googleapis.com/auth/gmail.send','https://www.googleapis.com/auth/gmail.modify']

    def __init__(self, creds_path='credentials.json', token_path='token.json'):
        """Initializes the API class with credentials and token file paths.
        Calls the authentication method to log in and set up the Gmail API service.
        """
        self.creds_path = creds_path
        self.token_path = token_path
        self.creds = None
        self.service = None
        self.authenticate()

    def authenticate(self):
        """Authenticates the user using OAuth 2.0.
        Refreshes or recreates token if needed, then builds Gmail API service.
        """
        if os.path.exists(self.token_path):
            self.creds = Credentials.from_authorized_user_file(self.token_path, self.SCOPES)
            if not self.creds.valid:
                print("Token invalid or expired. Re-authenticating...")
                flow = InstalledAppFlow.from_client_secrets_file(self.creds_path, self.SCOPES)
                self.creds = flow.run_local_server(port=0)
                with open(self.token_path, 'w') as token:
                    token.write(self.creds.to_json())
        else:
            print("No token found. Authenticating for the first time...")
            flow = InstalledAppFlow.from_client_secrets_file(self.creds_path, self.SCOPES)
            self.creds = flow.run_local_server(port=0)
            with open(self.token_path, 'w') as token:
                token.write(self.creds.to_json())

        self.service = build('gmail', 'v1', credentials=self.creds)

    def list_messages(self, max_results: int = 5) -> list:
        """Lists the most recent message IDs from the user's inbox."""
        result = self.service.users().messages().list(userId='me', maxResults=max_results).execute()
        return result.get('messages', [])

    def get_message(self, message_id: str):
        """Retrieves the full content of a specific email by its message ID."""
        message = self.service.users().messages().get(userId='me', id=message_id, format='full').execute()
        return message

    def is_authenticated(self) -> bool:
        """Checks whether the current credentials are valid and not expired."""
        return self.creds and self.creds.valid

    def send_email(self, to: str, subject: str, body: str) -> dict:
        """Sends an email using the Gmail API."""
        import base64
        from email.mime.text import MIMEText

        message = MIMEText(body)
        message['to'] = to
        message['subject'] = subject

        raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
        body = {'raw': raw}

        sent_message = self.service.users().messages().send(userId='me', body=body).execute()
        return sent_message

    # def send_email_html(self, to: str, subject: str, html_body: str):
    #     """
    #     Sends an email with HTML content.
    #     """
    #     import base64
    #     from email.mime.text import MIMEText
    #
    #     message = MIMEText(html_body, 'html')
    #     message['to'] = to
    #     message['subject'] = subject
    #
    #     raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
    #     body = {'raw': raw}
    #
    #     sent_message = self.service.users().messages().send(userId='me', body=body).execute()
    #     return sent_message


if __name__ == '__main__':
    gmail = API()
    print("Authenticated:", gmail.is_authenticated())
