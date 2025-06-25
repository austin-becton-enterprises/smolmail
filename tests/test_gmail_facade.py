class GmailService:
    def __init__(self, service):
        """
        Initialize GmailService with a Gmail API service instance.
        """
        self.service = service

    def create_message(self, to: str, subject: str, body: str) -> dict:
        """
        Create a MIME-encoded plain text email message.
        """
        from email.mime.text import MIMEText
        import base64

        message = MIMEText(body)
        message['to'] = to
        message['subject'] = subject
        raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
        return {'raw': raw}

    def create_message_html(self, to: str, subject: str, html_body: str) -> dict:
        """
        Create a MIME-encoded HTML email message.
        """
        from email.mime.text import MIMEText
        import base64

        message = MIMEText(html_body, 'html')
        message['to'] = to
        message['subject'] = subject
        raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
        return {'raw': raw}

    def send_email(self, to: str, subject: str, body: str) -> dict:
        """
        Send a plain text email.
        """
        message = self.create_message(to, subject, body)
        return self.service.users().messages().send(userId='me', body=message).execute()

    def send_email_html(self, to: str, subject: str, html_body: str) -> dict:
        """
        Send an HTML email.
        """
        message = self.create_message_html(to, subject, html_body)
        return self.service.users().messages().send(userId='me', body=message).execute()

    def read_recent_emails(self, label_ids=['INBOX', 'UNREAD'], max_results=5) -> list:
        """
        Retrieve recent unread emails with basic info.
        """
        response = self.service.users().messages().list(
            userId='me',
            labelIds=label_ids,
            maxResults=max_results
        ).execute()

        messages = response.get('messages', [])
        results = []
        for msg in messages:
            msg_detail = self.service.users().messages().get(userId='me', id=msg['id']).execute()
            headers = msg_detail['payload'].get('headers', [])
            subject = next((h['value'] for h in headers if h['name'] == 'Subject'), '(No Subject)')
            sender = next((h['value'] for h in headers if h['name'] == 'From'), '(Unknown Sender)')
            snippet = msg_detail.get('snippet', '')
            results.append({
                'id': msg['id'],
                'subject': subject,
                'From': sender,
                'snippet': snippet
            })
        return results

    def get_message(self, message_id: str) -> dict:
        """
        Retrieve the full Gmail API message object.
        """
        return self.service.users().messages().get(userId='me', id=message_id).execute()
