# Purpose: Write an email on behalf of user or auto-draft a reply to emails  

from smolagents.tools import Tool
from openai import OpenAI
# 'os', 'dotenv' used to load environment variables, like your OpenAI API key, safely from a .env file.
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class EmailWriter(Tool):
    name = "write_email"
    description = {
        "Generates an email draft. Supports generating new emails and replying to existing ones. "
        "This tool only creates email content — it does not send them." 
    }

    inputs = {
         "mode": {
            "type": "string",
            "enum": ["compose", "reply"],
            "description": "Use 'compose' to write a new email, or 'reply' to analyze an incoming email and write a reply."
        },
        "recipient": {
            "type": "string",
            "description": "Recipient email address (required in compose mode).",
            "default": ""
        },
        "subject": {
            "type": "string",
            "description": "Email subject line (required in compose mode).",
            "default": ""
        },
        "body": {
            "type": "string",
            "description": "Email body text (required in compose mode).",
            "default": ""
        },
        "incoming_email": {
            "type": "string",
            "description": "The full text of the email to reply to (required in reply mode).",
            "default": ""
        }
    }

    output_type = "object" 
    
    def forward(self, mode: str, recipient: str = "", subject: str = "", body: str = "", incoming_email: str = "") -> dict:
        if mode == "compose":
            if not all([recipient, subject, body]):
                return {"status": "error", "message": "Missing recipient, subject, or body for compose mode."}
            return {
                "recipient": recipient,
                "subject": subject,
                "body": body,
                "status": "draft"
            }

        elif mode == "reply":
            if not incoming_email:
                return {"status": "error", "message": "No email provided to reply to."}
            
            system_prompt = (
                "You're an email assistant. Based on the incoming email below, determine if a reply is necessary. "
                "If not, return {'status': 'ignored'}. If yes, generate a polite and professional reply:\n"
                "{'recipient': '<sender@example.com>', 'subject': 'Re: <original subject>', 'body': '<response>', 'status': 'draft'}"
            )

            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": incoming_email}
                ],
                temperature=0.7
            )

            reply = response.choices[0].message.content

            try:
                return eval(reply) if reply.startswith("{") else {"status": "error", "message": reply}
            except Exception as e:
                return {"status": "error", "message": "Failed to parse LLM output", "raw": reply}

        else:
            return {"status": "error", "message": "Invalid mode. Choose 'compose' or 'reply'."}
