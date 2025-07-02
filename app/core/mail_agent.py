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
        prompt = f"""
        You are a helpful and professional assistant tasked with writing warm, engaging, and personalized email replies.

        Here is the message you received:

        ---
        {snippet}
        ---

        Please write a thoughtful and polite reply addressing the sender’s message. Use a friendly tone and make the response feel human and conversational.

        - Avoid generic phrases like "I will get back to you shortly. or Thank you for your message. Regarding:"
        - Add relevant details or questions if appropriate.
        - Sign off politely with a suitable closing.
        - Don't give specifics about any project.
        - Ask More Questions related to the snippets
        - We are the Becton Team
        - We deal with making AI Agents, Automation

        Reply ONLY with the content of the email. Do NOT include any explanations or disclaimers.
        """
        return self.agent.run(prompt)