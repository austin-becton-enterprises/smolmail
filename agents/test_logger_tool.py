from agents.Tools.logger_tool import ToolLogger

def test_log_tool_usage():
    logger = ToolLogger()
    result = logger.forward(
        tool_name="manage_templates",
        inputs={"action": "create", "template_name": "Welcome"},
        output="Template created",
        summary="Created a welcome email template"
    )
    print(result)

if __name__ == "__main__":
    test_log_tool_usage()
