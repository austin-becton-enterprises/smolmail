# GmailAPI Research

This research document outlines everything required for our Python code to access and interact with the Gmail API. This includes sending emails, reading emails from the inbox, handling multiple test email accounts, and utilizing an official Python client library provided by Google.

---

## Gmail API Overview

The Gmail API allows applications to interact with users' Gmail accounts and perform tasks like reading messages, sending emails, managing labels, and more.

Official Documentation: https://developers.google.com/gmail/api

---

## Initial Setup Requirements

### a) Google Cloud Project
- Create a Google Cloud Project
- Enable the Gmail API for that project

### b) OAuth 2.0 Credentials
- Go to APIs & Services > Credentials
- Create OAuth 2.0 Client ID credentials
- Download the credentials.json file

This file is necessary for authorization and must be included in the Python project

### c) Consent Screen
- Configure the OAuth consent screen under APIs & Services > OAuth consent screen
- Set the appropriate scopes:
  - https://www.googleapis.com/auth/gmail.readonly
  - https://www.googleapis.com/auth/gmail.send
  - (and others as needed)

---

## Python Gmail API Library

Google provides an official Python library:

- google-api-python-client
- google-auth-httplib2
- google-auth-oauthlib

Install them using:

```bash
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

---

## Authentication & Token Handling

Before Python code can read or send Gmail messages, it has to prove to Google that it has permission to do so — this is where authentication and tokens come in.

### Single Account Flow
- On the first run, the user is prompted to authenticate via browser
- A token.json file is created locally after authentication
- This token allows subsequent access without logging in again

### Multiple Accounts
- If you're testing with more than one email account, you'll want to keep the login tokens separate
- Example:
  - token_user1.json → stores login info for testaccount1@gmail.com
  - token_user2.json → stores it for testaccount2@gmail.com
- The code should load the right token file depending on which Gmail account you're working with

### Tokens and Credentials Summary
- credentials.json: permanent config to initiate OAuth flow
- token.json: generated per user after OAuth is completed

---

## Inbox Access (Reading Emails)

Use Gmail API methods to access the inbox

### Sample Method: Read Emails

```python
service.users().messages().list(userId='me', labelIds=['INBOX'], maxResults=10).execute()
```

This returns message IDs. To get content:

```python
service.users().messages().get(userId='me', id=message_id, format='full').execute()
```

---

## Sending Emails

Use MIME (Multipurpose Internet Mail Extensions) and Gmail API to construct and send an email

### Example:

```python
import base64
from email.mime.text import MIMEText

message = MIMEText('This is the body')
message['to'] = 'recipient@example.com'
message['subject'] = 'Test Subject'

raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
body = {'raw': raw}

service.users().messages().send(userId='me', body=body).execute()
```

---

## Anticipated Features for AI Tools

- Inbox polling: Check inbox periodically to detect new messages  
- Email filtering: Based on sender, subject, or label  
- Parsing attachments and HTML content  
- Label management: Add custom labels to track AI-processed emails  
- Automated responses: Read content and reply using predefined templates  
- Support multiple users: Maintain separate sessions or tokens per account  

---

## Next Steps

- Set up Google Cloud Project and enable Gmail API  
- Configure OAuth consent screen and credentials  
- Set up credential/token management for multi-user testing  
- Install required Python libraries  

---

## Getting Started

Follow these steps to set up your development environment:

### 1. Clone the Repository

```bash
git clone https://github.com/austin-becton-enterprises/smolmail.git
cd smolmail
```

### 2. Create and Activate Virtual Environment

- On macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

- On Windows (Command Prompt):

```bash
py -m venv .venv
.venv\Scripts\activate.bat
```

- On Windows (PowerShell):

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Resources

- https://developers.google.com/workspace/gmail/api/quickstart/python  
- https://github.com/googleapis/google-api-python-client  
- https://developers.google.com/identity/protocols/oauth2 .
