# gmail_service.py

from log_config import setup_logger
import base64
from email.mime.text import MIMEText
from typing import List, Dict, Optional
from googleapiclient.discovery import Resource
from googleapiclient.errors import HttpError

# Constants
USER_ID_ME = 'me'

# Header keys
HEADER_SUBJECT = 'Subject'
HEADER_FROM = 'From'

# Dictionary keys
KEY_MESSAGES = 'messages'
KEY_ID = 'id'
KEY_SNIPPET = 'snippet'
KEY_PAYLOAD = 'payload'
KEY_HEADERS = 'headers'
KEY_TO = 'to'
KEY_SUBJECT = 'subject'
KEY_RAW = 'raw'

# Gmail labels
LABEL_INBOX = 'INBOX'
LABEL_UNREAD = 'UNREAD'

# Logging configuration
logger = setup_logger()

def read_most_recent_emails(service: Resource, label_ids: List[str] = [LABEL_INBOX, LABEL_UNREAD], max_results: int = 5) -> List[Dict]:
    """
    Fetches recent emails based on label filters.
    """
    try:
        logger.info("Fetching unread messages...")
        response = service.users().messages().list(
            userId=USER_ID_ME,
            labelIds=label_ids,
            maxResults=max_results
        ).execute()

        messages = response.get(KEY_MESSAGES, [])
        if not messages:
            logger.info("No unread messages found.")
            return []

        email_data = []
        for msg in messages:
            msg_detail = service.users().messages().get(userId=USER_ID_ME, id=msg[KEY_ID]).execute()
            headers = msg_detail[KEY_PAYLOAD][KEY_HEADERS]
            subject = next((h['value'] for h in headers if h['name'] == HEADER_SUBJECT), "(No Subject)")
            sender = next((h['value'] for h in headers if h['name'] == HEADER_FROM), "(Unknown Sender)")
            snippet = msg_detail.get(KEY_SNIPPET, "")

            logger.info(f"Read message: Subject='{subject}', From='{sender}'")
            email_data.append({
                KEY_ID: msg[KEY_ID],
                KEY_SUBJECT: subject,
                HEADER_FROM: sender,
                KEY_SNIPPET: snippet
            })

        return email_data

    except HttpError as error:
        logger.error(f"Error reading email: {error}")
        return []

def create_message(to: str, subject: str, body: str) -> Dict[str, str]:
    """
    Builds a MIME email message and encodes it for Gmail API.
    """
    message = MIMEText(body)
    message[KEY_TO] = to
    message[KEY_SUBJECT] = subject
    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
    return {KEY_RAW: raw}

def send_email(service: Resource, to: str, subject: str, body: str) -> Optional[Dict]:
    """
    Sends an email using the Gmail API.
    """
    try:
        message = create_message(to, subject, body)
        sent = service.users().messages().send(userId=USER_ID_ME, body=message).execute()
        logger.info(f"Email sent to {to} | Message ID: {sent[KEY_ID]}")
        return sent
    except HttpError as error:
        logger.error(f"Error sending email to {to}: {error}")
        return None
