"""
Tool: ValidationTool
Purpose: Validates input data using mock validation logic.
"""
from smolagents.tools import Tool

class ValidationTool(Tool):
    name = "validate_input"
    description = "Checks whether the provided input data meets basic validation rules."

    input = {
        "data": {
            "type": "object",
            "description": "Dictionary of key-value pairs to validate."
        }
    }

    output_type = "string"

    def forward(self, data: dict) -> str:
        if not isinstance(data, dict):
            return "Invalid input. Expected a dictionary."

        issues = []
        for key, value in data.items():
            if value in [None, "", [], {}]:
                issues.append(f"Field '{key}' is empty or missing.")
            elif isinstance(value, str) and len(value.strip()) == 0:
                issues.append(f"Field '{key}' is a blank string.")

        return (
            "Validation passed ✅" if not issues
            else "Validation issues found:\n- " + "\n- ".join(issues)
        )