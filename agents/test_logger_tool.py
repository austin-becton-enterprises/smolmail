from agents.Tools.logger_tool import ToolLogger

logger = ToolLogger()

print("--- Logging Test ---")

result = logger.forward(
    tool_name="template_manager",
    inputs={"mode": "get", "template_id": 101},
    output="Subject: Welcome to Our Service\nBody: Hi {name}, welcome to our service!",
    summary="Fetched welcome email template"
)

print(result)  # Should print: Log entry created.
