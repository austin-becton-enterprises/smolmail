# Code Overview: Gmail Service and Main Test Runner

This document explains the purpose and structure of two key modules in the system: `gmail_service.py` and `main_service.py`. These files are responsible for handling Gmail integration and testing basic email functionality. They serve as the foundation for enabling the AI agent to read incoming emails and send responses using email templates.

---

## `gmail_service.py` — Overview

This module contains all the core logic needed to interact with the Gmail API for reading and sending emails. It provides a simplified interface that other parts of the system — such as the AI agent — can call to fetch email data and send replies.

### Key Responsibilities:
- Connect to Gmail using an authenticated service
- Fetch recent unread emails
- Build MIME-format email messages and encode them
- Send emails using the Gmail API
- Handle errors returned by the Gmail API


### Functions:




---

## `main_service.py` — Overview

This script is used to manually test the Gmail functionality provided in `gmail_service.py`. It allows a developer to run the system interactively to verify that reading and sending emails work as expected.

### Key Responsibilities:
- Authenticate the Gmail API connection
- Provide command-line tools to test email reading
- Prompt the user to send a test email
- Print the results of these operations

### Functions:
