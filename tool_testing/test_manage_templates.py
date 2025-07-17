from agents.Tools.manage_templates import TemplateManager
from app.sample_data import mock_data as mockData

# Instantiate the TemplateManager tool
template_manager = TemplateManager()

print("--- Testing TemplateManager ---")

# 1. Test mode = 'list'
print("\n--- Mode: 'list' (All available templates) ---")
print(template_manager.forward(mode="list"))

# 2. Test mode = 'get' by template_id (valid ID)
print("\n--- Mode: 'get' by ID (Template ID 101) ---")
print(template_manager.forward(mode="get", template_id=101))

# 3. Test mode = 'get' by template_title (valid title, case-insensitive)
print("\n--- Mode: 'get' by Title (Case-insensitive: 'thank you') ---")
print(template_manager.forward(mode="get", template_title="thank you"))

# 4. Test mode = 'get' by template_id (non-existent ID)
print("\n--- Mode: 'get' by ID (Non-existent ID 999) ---")
print(template_manager.forward(mode="get", template_id=999))

# 5. Test mode = 'get' by template_title (non-existent title)
print("\n--- Mode: 'get' by Title (Non-existent Title 'Non-Existent Template') ---")
print(template_manager.forward(mode="get", template_title="Non-Existent Template"))

# 6. Test mode = 'get' without template_id or template_title
print("\n--- Mode: 'get' without ID or Title ---")
print(template_manager.forward(mode="get"))

# 7. Test invalid mode
print("\n--- Invalid Mode: 'retrieve' ---")
print(template_manager.forward(mode="retrieve"))

# 8. Simulated test: empty templates list (you'd need mocking or a separate function to test this in practice)
print("\n--- Testing with no templates available (requires mocking or manual change to mock_data) ---")
# You can simulate this by commenting out the return templates in get_dummy_templates()
# and returning an empty list for now, but skipping it here

print("\n--- End of TemplateManager Tests ---")
