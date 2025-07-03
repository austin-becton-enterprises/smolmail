import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("./firestore_credentials.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

data = {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "created_at": firestore.SERVER_TIMESTAMP
}

# Write contact to Firestore
doc_ref = db.collection("contacts").document("john_doe")  # Or use .add(data) for auto ID
doc_ref.set(data)

print( 'document id:',doc_ref.id)  # Print the document ID

