import firebase_admin
from firebase_admin import credentials, firestore
from google.api_core.exceptions import GoogleAPIError

class FirestoreService:
    def __init__(self, credential_path: str = "./firestore_credentials.json"):
        self._initialize_firestore(credential_path)
        self.logged_in_client_id = None

    def _initialize_firestore(self, path: str):
        try:
            if not firebase_admin._apps:
                cred = credentials.Certificate(path)
                firebase_admin.initialize_app(cred)
            self.db = firestore.client()
        except GoogleAPIError as e:
            print(f"Failed to initialize Firestore: {e}")
            self.db = None

    # ---- Client CRUD ----
    def create_client(self, client_id: str, data: dict):
        data['client_id'] = client_id
        data['created_at'] = firestore.SERVER_TIMESTAMP
        self.db.collection("clients").document(client_id).set(data)

    def read_client(self, client_id: str):
        doc = self.db.collection("clients").document(client_id).get()
        return doc.to_dict() if doc.exists else None

    def update_client(self, client_id: str, updates: dict):
        self.db.collection("clients").document(client_id).update(updates)

    def delete_client(self, client_id: str):
        # Delete templates
        templates = self.db.collection("templates").where("client_id", "==", client_id).stream()
        for tpl in templates:
            tpl.reference.delete()
        # Delete emails
        emails = self.db.collection("emails").where("client_id", "==", client_id).stream()
        for email in emails:
            email.reference.delete()
        # Delete client
        self.db.collection("clients").document(client_id).delete()

    def list_clients(self, limit=10, start_after=None):
        query = self.db.collection("clients").limit(limit)
        if start_after:
            query = query.start_after(start_after)
        return list(query.stream())

    # ---- Template CRUD ----
    def create_template(self, template_id: str, data: dict):
        if not self.logged_in_client_id:
            raise Exception("No client logged in")
        data['template_id'] = template_id
        data['client_id'] = self.logged_in_client_id
        data['created_at'] = firestore.SERVER_TIMESTAMP
        self.db.collection("templates").document(template_id).set(data)

    def read_template(self, template_id: str):
        doc = self.db.collection("templates").document(template_id).get()
        if doc.exists and doc.to_dict().get('client_id') == self.logged_in_client_id:
            return doc.to_dict()
        return None

    def update_template(self, template_id: str, updates: dict):
        doc = self.db.collection("templates").document(template_id).get()
        if doc.exists and doc.to_dict().get('client_id') == self.logged_in_client_id:
            self.db.collection("templates").document(template_id).update(updates)
        else:
            raise Exception("Template not found or access denied")

    def delete_template(self, template_id: str):
        doc = self.db.collection("templates").document(template_id).get()
        if doc.exists and doc.to_dict().get('client_id') == self.logged_in_client_id:
            self.db.collection("templates").document(template_id).delete()
        else:
            raise Exception("Template not found or access denied")

    def list_templates(self, limit=10, start_after=None):
        query = self.db.collection("templates")\
            .where("client_id", "==", self.logged_in_client_id)\
            .limit(limit)
        if start_after:
            query = query.start_after(start_after)
        return list(query.stream())

    # ---- Emails ----
    def log_email(self, template_id: str, metadata: dict = None):
        if not self.logged_in_client_id:
            raise Exception("No client logged in")
        data = {
            "client_id": self.logged_in_client_id,
            "template_id": template_id,
            "status": "sent",
            "sent_at": firestore.SERVER_TIMESTAMP,
            "metadata": metadata or {}
        }
        doc_ref = self.db.collection("emails").document()
        doc_ref.set(data)
        return doc_ref.id

    def get_emails_for_logged_in_client(self, limit=10, start_after=None):
        query = self.db.collection("emails")\
            .where("client_id", "==", self.logged_in_client_id)\
            .limit(limit)
        if start_after:
            query = query.start_after(start_after)
        return list(query.stream())

    # ---- Login ----
    def login_client(self, client_id: str):
        client = self.read_client(client_id)
        if client:
            self.logged_in_client_id = client_id
            return True
        return False

    def logout_client(self):
        self.logged_in_client_id = None

    # ---- Render Template ----
    def render_template(self, template_code: str, client_data: dict):
        try:
            return template_code.format(**client_data)
        except KeyError as e:
            raise Exception(f"Missing client data field for template: {e}")
