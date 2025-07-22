from smolagents.agents import ToolCallingAgent
from smolagents.models import InferenceClientModel
from app.core.tools.mail_tool import MailTool

class MailAgent:
    def __init__(self):
        model = InferenceClientModel()  # or any OpenAI-compatible wrapper
        tools = [MailTool()]
        self.agent = ToolCallingAgent(model=model, tools=tools)

    def run(self, snippet: str) -> str:
        # Ask the agent to generate a reply
        prompt = f"Generate a reply to this email snippet:\n\n{snippet}"
        return self.agent.run(prompt)