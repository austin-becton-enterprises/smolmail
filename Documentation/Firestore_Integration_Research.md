# Firestore Integration Research

## Purpose

This document explains how to migrate our in-memory Python mock databases (using dictionaries) to a real Firestore NoSQL database hosted on Google Cloud. Our goal is to keep using the existing data models (Contact and Template), and CRUD logic patterns, but persist the data in Firestore instead of memory.

## Is Firestore NoSQL or Python-based?

Firestore is a **NoSQL** cloud database provided by **Google Cloud Platform (GCP)**. It is not a `.py` file or Python-specific technology.

However, Google provides a **Python library** (`google-cloud-firestore`) that lets us connect to and work with Firestore easily from our Python code.

So we **write Python code** to talk to Firestore — for example, using our Contact and Template classes and CRUD logic to insert or retrieve data in Firestore documents.

## Goals

- Use Firestore instead of our mock Python dictionaries (`mock_contacts_db`, `mock_templates_db`)
- Keep using our current Contact and Template models
- Create a new Firestore database
- Load our existing mock data into this new Firestore instance
- Replace our `create_`, `read_`, `update_`, `delete_` functions to work with Firestore

---

##  Setup Firestore in Python

### 1. Install Firestore client library

```bash
pip install google-cloud-firestore
```

### 2. Service Account Authentication

We need a `credentials.json` file from GCP.

1. Go to [console.cloud.google.com](https://console.cloud.google.com)
2. Create a project (if not already done)
3. Enable **Firestore API**
4. Go to **IAM & Admin → Service Accounts**
5. Create a new key (JSON format)
6. Save it as `credentials.json` in your project folder

### 3. Initialize Firestore Client

In Python:

```python
from google.cloud import firestore

db = firestore.Client.from_service_account_json("credentials.json")
```

---

## Mapping What We Have

We already have these:

- `Contact` and `Template` models
- `mock_contacts_db: Dict[int, Contact]`
- `mock_templates_db: Dict[int, Template]`

We'll replace the mock DBs with Firestore collections:

- `contacts` (Firestore collection)
- `templates` (Firestore collection)

### Contact → Firestore Document

```json
{
  "contact_id": 1,
  "name": "Alice Smith",
  "email": "alice@example.com",
  "phone": "555-1234"
}
```

### Template → Firestore Document

```json
{
  "template_id": 101,
  "title": "Welcome",
  "subject": "Welcome to Our Service",
  "body": "Hi {name}, welcome to our service!"
}
```

---

## Firestore CRUD Example

### Create Contact

```python
def create_contact(contact: Contact):
    db.collection("contacts").document(str(contact.contact_id)).set(contact.to_dict())
```

### Read Contact

```python
def read_contact(contact_id: int):
    doc = db.collection("contacts").document(str(contact_id)).get()
    return doc.to_dict() if doc.exists else None
```

### Update Contact

```python
def update_contact(contact_id: int, **kwargs):
    db.collection("contacts").document(str(contact_id)).update(kwargs)
```

### Delete Contact

```python
def delete_contact(contact_id: int):
    db.collection("contacts").document(str(contact_id)).delete()
```

Same structure applies for `Template`.

---


## Summary of Next Steps

- [x] Research Firestore integration with Python
- [x] Confirm we’ll keep existing models
- [x] Plan how to convert mock data into Firestore documents
- [ ] Build new `firestore_service.py` file with create/read/update/delete functions
- [ ] Create tests for these functions

