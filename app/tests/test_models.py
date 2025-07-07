from contact_template_models import (
    create_contact,
    read_contact,
    update_contact,
    delete_contact,
    create_template,
    read_template,
    update_template,
    delete_template
)
from smolmail.app.sample_data.mock_data import get_dummy_contacts, get_dummy_templates

# === Load and test dummy contacts ===
print("=== Contact Tests ===")
contacts = get_dummy_contacts()
for contact in contacts:
    print(create_contact(
        contact_id=contact["contact_id"],
        name=contact["name"],
        email=contact["email"],
        phone=contact["phone"]
    ))
    print(read_contact(contact["contact_id"]))

# Test update on one contact
print(update_contact(1, phone="999-9999"))
print(read_contact(1))

# Test delete
print(delete_contact(1))
print(read_contact(1))  # should show not found

# === Load and test dummy templates ===
print("\n=== Template Tests ===")
templates = get_dummy_templates()
for template in templates:
    print(create_template(
        template_id=template["template_id"],
        title=template["title"],
        subject=template["subject"],
        body=template["body"]
    ))
    print(read_template(template["template_id"]))

# Test update on one template
print(update_template(101, subject="Updated Subject", body="Updated body message"))
print(read_template(101))

# Test delete
print(delete_template(101))
print(read_template(101))  # should show not found
