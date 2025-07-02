# Firestore Setup & Research Notes
---

## What is Firestore?

Firestore is a **NoSQL, document-based database** by Google that's part of Firebase and also available on Google Cloud. It stores data in **collections of documents**, which are structured like JSON objects.

It's designed for:
- Real-time apps
- Serverless environments
- Web/mobile/backend integrations
- Scalability without much infrastructure management

---
## Why Firestore for Our Project?

Since we’re already using Google services (Gmail API, OAuth, etc.), Firestore integrates seamlessly with the existing stack. It supports Python, offers a generous free tier, and simplifies cloud database setup without needing to manage a traditional SQL server.

---

## Should We Create a New GCP Project for Firestore?

Yes — **for the purpose of testing and mimicking a real client setup**, we are creating a **new Google Cloud project specifically for Firestore**. This simulates the scenario where a potential client provides their own GCP project and database.

However, the key point is:

> **Our code must be written to support multiple GCP projects** — it should be flexible enough to work with any service account and credentials provided by a client, not just our own static project.

---

## Setup Steps (Using a New GCP Project)

1. Go to: [https://console.cloud.google.com](https://console.cloud.google.com)  
2. Create a **new** GCP project  
3. Search for “Firestore” in the left-hand menu  
4. Click **“Create database”**  
   - Choose **Test mode** or **Production mode**  
   - Select a region (e.g., `us-central1`)  
5. Create a **new service account** in that project with Firestore access  
6. Download the `credentials.json` file and test using the Firestore Python SDK  

This setup helps us simulate how a client might bring their own GCP project and ensures our system is flexible and portable.

## Authentication & Access

1. **Create a new service account** within the new GCP project you created for Firestore:
   - Go to **IAM & Admin > Service Accounts**
   - Click **“Create Service Account”**
   - Grant it the role: **"Cloud Datastore User"** or **"Firestore User"**

2. **Generate and download the `credentials.json` key** for that service account:
   - In the service account settings, go to **"Keys" → "Add Key" → "Create new key"**
   - Choose **JSON** format and download the key file

3. Add the downloaded `credentials.json` file to your project root or secure location

---

## Python Setup and Testing

### Install Firestore client library:

```bash
pip install google-cloud-firestore
```
### Example: Basic Usage in Python

```python
from google.cloud import firestore

# Initialize Firestore client (uses credentials from environment)
db = firestore.Client()

# Add a document
db.collection("contacts").document("john_doe").set({
    "name": "John Doe",
    "email": "john@example.com",
    "tags": ["partner", "developer"]
})

# Read documents
docs = db.collection("contacts").stream()
for doc in docs:
    print(f"{doc.id} => {doc.to_dict()}")

# Update a document
db.collection("contacts").document("john_doe").update({
    "email": "john.doe@newmail.com"
})

# Delete a document
db.collection("contacts").document("john_doe").delete()
```
---

## Data Modeling in Firestore

Firestore is flexible, but not relational. It’s good to plan out collections:

- `contacts` — stores each contact as a document
- `templates` — email templates
- `emails` — sent/received emails, optional metadata
- `logs` — optional, for tracking status or errors

**Avoid overly nested data** and **don’t treat it like SQL.**

---

## Firestore Pros and Cons

### Pros:
- Real-time syncing (optional)
- Serverless and auto-scaling
- Generous free tier
- Works well with GCP tools
- Flexible JSON-like structure

### Cons:
- No complex joins (not relational)
- Query limitations (e.g. no multiple inequality filters)
- Write/read cost model (careful with high-volume reads)

---





