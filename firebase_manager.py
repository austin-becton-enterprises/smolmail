import firebase_admin
from firebase_admin import credentials, firestore
from universal_crud import create, read, update, delete

# Initialize Firebase once
if not firebase_admin._apps:
    cred = credentials.Certificate("firestore_credentials.json")  
    firebase_admin.initialize_app(cred)

db = firestore.client()

class FirebaseWrapper:
    """
    Wraper Class to convert firestore document dictionary 
    into object with attributes
    """
    def __init__(self, id, data):
        self.id = id
        for k, v in data.items():
            setattr(self, k, v)

def load_collection(collection_name):
    """
    Load documents from FireStore collection 
    into local dictionary where keys are 
    doc ID and values are Wrapper Object 
    """
    docs = db.collection(collection_name).stream()
    return {doc.id: FirebaseWrapper(doc.id, doc.to_dict()) for doc in docs}

def create_firestore(collection_name, item):

    local_dict = load_collection(collection_name)
    success, result = create(local_dict, item)
    if not success:
        return False, result
    db.collection(collection_name).document(item.id).set(item.__dict__)
    return True, result

def read_firestore(collection_name, item_id):
    local_dict = load_collection(collection_name)
    return read(local_dict, item_id)

def update_firestore(collection_name, item_id, **updates):
    local_dict = load_collection(collection_name)
    success, result = update(local_dict, item_id, **updates)
    if not success:
        return False, result
    db.collection(collection_name).document(item_id).update(updates)
    return True, result

def delete_firestore(collection_name, item_id):
    local_dict = load_collection(collection_name)
    success, result = delete(local_dict, item_id)
    if not success:
        return False, result
    db.collection(collection_name).document(item_id).delete()
    return True, result
