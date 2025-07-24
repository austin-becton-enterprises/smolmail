# main.py

from agents import EmailAgent
from agents.Tools.logger_tool import LoggerTool
from agents.Tools.manage_templates import ManageTemplates
from agents.Tools.read_email import ReadEmail
from agents.Tools.send_email import SendEmail
from agents.Tools.write_email import WriteEmail

def main():
    # Instantiate each tool
    tools = [
        LoggerTool(),
        ManageTemplates(),
        ReadEmail(),
        SendEmail(),
        WriteEmail(),
    ]

    # Create the agent with the tools
    agent = EmailAgent(tools=tools)

    # Example test input (you can modify this)
    user_input = "Send an email to simran@example.com with subject 'Hello' and body 'How are you?'"
    response = agent.run(user_input)
    print(response)

if __name__ == "__main__":
    main()
