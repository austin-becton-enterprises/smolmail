# Contact model
class Contact:
    def __init__(self, contact_id, name, email, phone=None):
        self.contact_id = contact_id
        self.name = name
        self.email = email
        self.phone = phone

    def to_dict(self):
        return {
            "contact_id": self.contact_id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone
        }

# Template model
class Template:
    def __init__(self, template_id, title, body):
        self.template_id = template_id
        self.title = title
        self.body = body

    def to_dict(self):
        return {
            "template_id": self.template_id,
            "title": self.title,
            "body": self.body
        }

# Mock databases
mock_contacts_db = {}
mock_templates_db = {}

# CRUD for Contact
def create_contact(contact_id, name, email, phone=None):
    if contact_id in mock_contacts_db:
        return f"Contact with ID {contact_id} already exists."
    contact = Contact(contact_id, name, email, phone)
    mock_contacts_db[contact_id] = contact
    return f"Contact {name} created."

def read_contact(contact_id):
    contact = mock_contacts_db.get(contact_id)
    return contact.to_dict() if contact else "Contact not found."

def update_contact(contact_id, name=None, email=None, phone=None):
    contact = mock_contacts_db.get(contact_id)
    if not contact:
        return "Contact not found."
    if name:
        contact.name = name
    if email:
        contact.email = email
    if phone:
        contact.phone = phone
    return f"Contact {contact_id} updated."

def delete_contact(contact_id):
    if contact_id in mock_contacts_db:
        del mock_contacts_db[contact_id]
        return f"Contact {contact_id} deleted."
    return "Contact not found."

# CRUD for Template
def create_template(template_id, title, body):
    if template_id in mock_templates_db:
        return f"Template with ID {template_id} already exists."
    template = Template(template_id, title, body)
    mock_templates_db[template_id] = template
    return f"Template '{title}' created."

def read_template(template_id):
    template = mock_templates_db.get(template_id)
    return template.to_dict() if template else "Template not found."

def update_template(template_id, title=None, body=None):
    template = mock_templates_db.get(template_id)
    if not template:
        return "Template not found."
    if title:
        template.title = title
    if body:
        template.body = body
    return f"Template {template_id} updated."

def delete_template(template_id):
    if template_id in mock_templates_db:
        del mock_templates_db[template_id]
        return f"Template {template_id} deleted."
    return "Template not found."

# TESTING
if __name__ == "__main__":
    print(create_contact(1, "Alice Smith", "alice@example.com"))
    print(read_contact(1))
    print(update_contact(1, phone="123-456-7890"))
    print(read_contact(1))
    print(delete_contact(1))
    print(read_contact(1))

    print("---")

    print(create_template(101, "Welcome", "Hi {name}, welcome to our service!"))
    print(read_template(101))
    print(update_template(101, body="Hello {name}, glad to have you onboard!"))
    print(read_template(101))
    print(delete_template(101))
    print(read_template(101))
