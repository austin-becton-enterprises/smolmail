## Collections Overview
This document outlines the scope of what data will be stored in the database. .
### Users
- Stores user accounts and profile information.
- Each user has a unique ID, contact info, role, and status.

### Emails
- Stores email messages associated with users.
- Emails include sender, recipient, subject, body, labels.

### AutoReplies
- Stores user-defined email auto eply templates.
- Templates include message content, activation and status


## Relationships

- Each **email** document references a **user** using `userId`
- Each **autoReply** document references a **user** via `userId` 
- Users can have multiple emails and multiple autoReply templates

