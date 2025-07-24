from agents.email_agent import EmailAgent
from agents.Tools.logger_tool import ToolLogger
from agents.Tools.manage_templates import TemplateManager
from agents.Tools.read_email import EmailReader
from agents.Tools.write_email import EmailWriter
from agents.Tools.send_email import EmailSender

from openai_model import OpenAIModel  #custom model wrapper class
from openai_config import setup_openai  #Import the config


def main():
    print("Setting up OpenAI API...")
    setup_openai()  # Initialize OpenAI key

    print("Starting EmailAgent with tools...")
    tools = [
        ToolLogger(),
        TemplateManager(),
        EmailReader(),
        EmailWriter(),
        EmailSender(),
    ]

    
    model = OpenAIModel(model_name="gpt-4o")  

    agent = EmailAgent(tools=tools, model=model)

    while True:
        user_input = input("Ask the agent something (or type 'exit'): ")
        if user_input.lower() in ["exit", "quit"]:
            break

        response = agent.run(user_input)
        print("Response:", response)
        print()

if __name__ == "__main__":
    main()
