
# Gmail AI System – Code Overview and Documentation

This document explains the structure and function of the key modules in the Gmail AI service. It is intended to help new developers understand how the system works, how components interact, and how to extend or use each part.

---

## Module Overviews

### `app/core/gmail_api.py`
Handles authentication and Gmail API interaction. Provides core functions for listing, retrieving, and sending emails.

### `app/core/gmail_facade.py`
Acts as a wrapper (facade) for the Gmail API, providing a cleaner interface (`GmailService`) to interact with email functions.

### `app/utils/log_config.py`
Sets up a standardized logger used across all modules.

### `app/utils/log.txt`
Stores logs related to email operations (sending/receiving/errors).

### `app/tests/test_gmail_facade.py`
Unit tests for the `GmailService` facade. Ensures that message creation, sending, and reading behave as expected. These tests typically use mocks for Gmail API interactions.

### `main_service.py`
Development script used to test the system by manually calling `read` and `send` email functions.

---

## Detailed Method Documentation

### File: `gmail_api.py`

#### `authenticate(self)`
Authenticates the user via OAuth. Uses saved token if available or launches a login flow.

- **Parameters:** None  
- **Returns:** None (sets `self.service`)  
- **Usage:**
```python
api = API()
api.authenticate()
```

---

#### `list_messages(self, max_results: int = 5) -> list`
Lists recent email message IDs.

- **Parameters:** `max_results` – number of emails to return  
- **Returns:** List of message dictionaries  
- **Usage:**
```python
api.list_messages(10)
```

---

#### `get_message(self, message_id: str) -> dict`
Fetches full content of an email.

- **Parameters:** `message_id` – ID of the email  
- **Returns:** Message dictionary with headers/body  
- **Usage:**
```python
api.get_message('abc123')
```

---

#### `send_email(self, to: str, subject: str, body: str) -> dict`
Sends a plain-text email.

- **Parameters:** `to`, `subject`, `body`  
- **Returns:** Response dict from Gmail API  
- **Usage:**
```python
api.send_email("to@example.com", "Subject", "Body")
```

---

### File: `gmail_facade.py`

#### `GmailService.read_most_recent_emails(self)`
Fetches a few unread emails and extracts key info.

- **Returns:** List of email summaries (dicts with sender, subject, etc.)  
- **Usage:**
```python
service.read_most_recent_emails()
```

---

#### `GmailService.create_message(self, to, subject, body)`
Builds MIME message for Gmail.

- **Returns:** Encoded message dict  
- **Usage:**
```python
service.create_message("to@example.com", "Hi", "Test message")
```

---

#### `GmailService.send_email(self, to, subject, body)`
Creates and sends an email in one step.

- **Returns:** Gmail API response dict  
- **Usage:**
```python
service.send_email("to@example.com", "Subject", "Hello!")
```

---

### File: `log_config.py`

#### `setup_logger(log_file)`
Configures and returns a logger that writes to the given log file.

- **Parameters:** `log_file` – string path to output log file  
- **Returns:** `logging.Logger` instance  
- **Usage:**
```python
logger = setup_logger("log.txt")
```

---

### File: `log.txt`

This file logs all Gmail interactions. Example contents:
```
2025-06-25 14:36:09 - INFO - Fetching unread messages...
2025-06-25 14:36:11 - INFO - Email sent to Customer1 <customer1.becton@gmail.com>
```

Used for debugging and tracking system behavior.

---

### File: `test_gmail_facade.py`

#### Purpose:
To validate that the `GmailService` class behaves correctly. Each function tests a different method of the service, typically by mocking the Gmail API service object.

#### Test Coverage:

- `test_create_message`:  
  Ensures plain-text message creation returns base64-encoded payload.

- `test_create_message_html`:  
  Confirms HTML email messages are correctly constructed and encoded.

- `test_send_email`:  
  Mocks `send_email` function to verify correct message structure and API call.

- `test_send_email_html`:  
  Similar to `test_send_email`, but for HTML content.

- `test_read_recent_emails`:  
  Simulates unread emails and checks if the summaries returned match expected fields.

- `test_get_message`:  
  Ensures full message fetches return correctly through the API.

---

### File: `main_service.py`

#### `test_read_email(service)`
Calls GmailService to fetch and print unread emails.

- **Parameters:** `service` – instance of GmailService  
- **Returns:** None  
- **Usage:**
```python
test_read_email(gmail_service)
```

---

#### `test_send_email(service, to)`
Prompts user for email subject/body and sends a test email.

- **Parameters:** `service`, `to` – recipient email  
- **Returns:** None  
- **Usage:**
```python
test_send_email(gmail_service, "someone@example.com")
```

---

## Workflow Summary

1. `gmail_api.py` handles Gmail API authentication and raw operations.
2. `gmail_facade.py` offers an easier-to-use interface (`GmailService`).
3. `log_config.py` ensures consistent logging across modules.
4. `main_service.py` runs test functions for developers.
5. `log.txt` stores logs of all events and errors.
6. `test_gmail_facade.py` ensures GmailService functions as expected.

This modular structure supports a future AI system that will analyze unread emails and respond using prebuilt templates.
