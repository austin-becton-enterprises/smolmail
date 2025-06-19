# contact_template_models.py

class Contact:
    def __init__(self, contact_id, name, email, phone=None):
        self.contact_id = contact_id
        self.name = name
        self.email = email
        self.phone = phone

class Template:
    def __init__(self, template_id, title, body):
        self.template_id = template_id
        self.title = title
        self.body = body

# Mock databases
contacts_db = {}
templates_db = {}

# Contact CRUD operations
def create_contact(contact):
    contacts_db[contact.contact_id] = contact

def read_contact(contact_id):
    return contacts_db.get(contact_id)

def update_contact(contact_id, **kwargs):
    contact = contacts_db.get(contact_id)
    if contact:
        for key, value in kwargs.items():
            setattr(contact, key, value)

def delete_contact(contact_id):
    if contact_id in contacts_db:
        del contacts_db[contact_id]

# Template CRUD operations
def create_template(template):
    templates_db[template.template_id] = template

def read_template(template_id):
    return templates_db.get(template_id)

def update_template(template_id, **kwargs):
    template = templates_db.get(template_id)
    if template:
        for key, value in kwargs.items():
            setattr(template, key, value)

def delete_template(template_id):
    if template_id in templates_db:
        del templates_db[template_id]
