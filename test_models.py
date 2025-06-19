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

# === Test Contact CRUD ===
print("=== Contact Tests ===")
print(create_contact(1, "Alice Smith", "alice@example.com"))
print(read_contact(1))
print(update_contact(1, phone="555-1234"))
print(read_contact(1))
print(delete_contact(1))
print(read_contact(1))  # should show not found

# === Test Template CRUD ===
print("\n=== Template Tests ===")
print(create_template(101, "Welcome", "Hi {name}, welcome to our service!"))
print(read_template(101))
print(update_template(101, body="Hello {name}, glad to have you onboard!"))
print(read_template(101))
print(delete_template(101))
print(read_template(101))  # should show not found
