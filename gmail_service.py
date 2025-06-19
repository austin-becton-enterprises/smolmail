# gmail_service.py

import logging
import base64
from email.mime.text import MIMEText
from typing import List, Dict, Optional
from googleapiclient.discovery import Resource
from googleapiclient.errors import HttpError

# Constant to avoid magic strings
USER_ID_ME = 'me'

# Configure logging for the module
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(asctime)s - %(message)s')

def read_most_recent_emails(service: Resource, label_ids: List[str] = ['INBOX', 'UNREAD'], max_results: int = 5) -> List[Dict]:
    """
    Fetches recent emails based on label filters.

    Args:
        service (Resource): Authorized Gmail API service instance.
        label_ids (List[str]): Gmail label filters (e.g., ['INBOX', 'UNREAD']).
        max_results (int): Maximum number of emails to retrieve.

    Returns:
        List[Dict]: A list of dictionaries with email id, subject, sender, and snippet.
    """
    try:
        logging.info("Fetching unread messages...")
        response = service.users().messages().list(
            userId=USER_ID_ME,
            labelIds=label_ids,
            maxResults=max_results
        ).execute()

        messages = response.get('messages', [])
        if not messages:
            logging.info("No unread messages found.")
            return []

        email_data = []
        for msg in messages:
            msg_detail = service.users().messages().get(userId=USER_ID_ME, id=msg['id']).execute()
            headers = msg_detail['payload']['headers']
            subject = next((h['value'] for h in headers if h['name'] == 'Subject'), "(No Subject)")
            sender = next((h['value'] for h in headers if h['name'] == 'From'), "(Unknown Sender)")
            snippet = msg_detail.get('snippet', "")

            logging.info(f"Read message: Subject='{subject}', From='{sender}'")
            email_data.append({
                'id': msg['id'],
                'subject': subject,
                'sender': sender,
                'snippet': snippet
            })

        return email_data

    except HttpError as error:
        logging.error(f"Error reading email: {error}")
        return []

def create_message(to: str, subject: str, body: str) -> Dict[str, str]:
    """
    Builds a MIME email message and encodes it for Gmail API.

    Args:
        to (str): Recipient email address.
        subject (str): Email subject line.
        body (str): Plain text body of the email.

    Returns:
        Dict[str, str]: Encoded email payload formatted for Gmail API.
    """
    message = MIMEText(body)
    message['to'] = to
    message['subject'] = subject
    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
    return {'raw': raw}

def send_email(service: Resource, to: str, subject: str, body: str) -> Optional[Dict]:
    """
    Sends an email using the Gmail API.

    Args:
        service (Resource): Authorized Gmail API service instance.
        to (str): Recipient email address.
        subject (str): Email subject line.
        body (str): Email body (plain text).

    Returns:
        Optional[Dict]: Sent message object or None if sending failed.
    """
    try:
        message = create_message(to, subject, body)
        sent = service.users().messages().send(userId=USER_ID_ME, body=message).execute()
        logging.info(f"Email sent to {to} | Message ID: {sent['id']}")
        return sent
    except HttpError as error:
        logging.error(f"Error sending email to {to}: {error}")
        return None
