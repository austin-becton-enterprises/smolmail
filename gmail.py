# gmail.py

#Python packages from the Gmail API library you installed:
#Credentials handles the saved token.
#InstalledAppFlow runs the login window.
#build creates a Gmail service so you can make API calls.
#os.path checks if files (like token.json) exist.

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os.path

#The API class will:
#Set the required Gmail permissions (called scopes)
#Authenticate using credentials.json and token.json
#Build a service you’ll use to talk to Gmail
class API:
    SCOPES = ['https://www.googleapis.com/auth/gmail.readonly', 
              'https://www.googleapis.com/auth/gmail.send']
# ^SCOPES = What permissions the app will ask for (read inbox + send email)

    def __init__(self, creds_path='credentials.json', token_path='token.json'):
        self.creds_path = creds_path
        self.token_path = token_path
        self.creds = None
        self.service = None
        self.authenticate()
#^This stores file paths, creates creds and service placeholders, then calls a function to log in (self.authenticate()).


    def authenticate(self):
        if os.path.exists(self.token_path):
            self.creds = Credentials.from_authorized_user_file(self.token_path, self.SCOPES)
        else:
            flow = InstalledAppFlow.from_client_secrets_file(self.creds_path, self.SCOPES)
            self.creds = flow.run_local_server(port=0)
            with open(self.token_path, 'w') as token:
                token.write(self.creds.to_json())
        self.service = build('gmail', 'v1', credentials=self.creds)
#^This checks if you already logged in before (token exists). If not, it opens a browser window to log in with Gmail.

    def list_messages(self, max_results=5):
        result = self.service.users().messages().list(userId='me', maxResults=max_results).execute()
        return result.get('messages', [])
#^This returns a list of the most recent email IDs in your inbox.

    def send_email(self, to, subject, body):
        import base64
        from email.mime.text import MIMEText

        message = MIMEText(body)
        message['to'] = to
        message['subject'] = subject

        raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
        body = {'raw': raw}

        sent_message = self.service.users().messages().send(userId='me', body=body).execute()
        return sent_message
#^This creates a MIME email, encodes it, and sends it using the Gmail API.
