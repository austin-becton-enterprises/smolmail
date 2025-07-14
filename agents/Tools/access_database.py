"""
Tool: AccessDatabaseTool
Purpose: Simulate database read/write operations for emails or contacts.
"""
from smolagents.tools import Tool

# Simple mock database as a dictionary
mock_db = {
    "contacts": [
        {"name": "Alice", "email": "alice@example.com"},
        {"name": "Bob", "email": "bob@example.com"}
    ]
}

class AccessDatabaseTool(Tool):
    name = "access_database"
    description = "Accesses mock contact database to list or add entries."

    input = {
        "operation": {
            "type": "string",
            "enum": ["list", "add"],
            "description": "Choose 'list' to view contacts or 'add' to insert a new one."
        },
        "data": {
            "type": "object",
            "description": "Data to add (only required for 'add' operation).",
            "default": {}
        }
    }

    output_type = "string"

    def forward(self, operation: str, data: dict = {}) -> str:
        if operation == "list":
            return "\n".join([f"{c['name']} <{c['email']}>" for c in mock_db["contacts"]])
        elif operation == "add":
            if "name" in data and "email" in data:
                mock_db["contacts"].append(data)
                return f"Added contact: {data['name']} <{data['email']}>"
            return "Invalid data. 'name' and 'email' required."
        return "Invalid operation."