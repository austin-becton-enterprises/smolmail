from contact_template_models import *

# Create and add contacts
contact1 = Contact(contact_id=1, name="Alice Smith", email="alice@example.com")
create_contact(contact1)

# Create and add templates
template1 = Template(template_id=101, title="Welcome", body="Hi {name}, welcome to our service!")
create_template(template1)

# Test read
print(read_contact(1).__dict__)
print(read_template(101).__dict__)
