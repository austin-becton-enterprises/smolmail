# Code Overview and Workflow

This document explains the structure and function of the core modules in the Gmail AI service. It is intended to help new developers understand how the system works, how components interact, and where to implement changes or add features.

---

## File: `app/core/gmail_api.py`

### Purpose:
Handles the initial setup and authentication of the Gmail API using OAuth 2.0. This class returns a service object that can be used for email operations (read/send).

### Key Class:
- **`API`**  
  - Sets scopes for reading and sending email
  - Authenticates using saved token or OAuth login
  - Provides access to Gmail API methods

### Key Methods:
- `authenticate()`: Authenticates the user and saves credentials
- `list_messages(max_results)`: Lists recent message IDs
- `get_message(message_id)`: Gets full content of a specific message
- `send_email(to, subject, body)`: Sends an email using the Gmail API

---