# Purpose: Write fresh email on behalf of user  

from smolagents.tools import Tool
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPEN_API_KEY"))

class EmailWriter(Tool):
    name = "write_email"
    description = (
        "It'll take in a prompt from the user and generates an email draft on behalf of the user. "
        "It'll include recipient, subject, and body. "
        "This tool only creates email content — it does not send them."
    )

    inputs = {
        "prompt": {
            "type": "string",
            "description": "Briefly describe what the email is for. Example: 'Email example@gmail.com about an appointment on Tuesday May 16th at 2:30pm.'",
            "nullable": True,
            "default": ""
        }
    }

    output_type = "object" 
    
    def forward(self, prompt: str = "") -> dict:
        if not prompt.strip():
            raise ValueError("Prompt cannot be empty.")

        system_message = (
            #"You are an assistant that writes professional, clear, and polite email drafts "
            #"based on a short description. Return the email as a JSON object with keys: recipient, subject, body."
            "You are an assistant that writes professional, clear, and polite email drafts "
            "based on a short description. Return the email as a JSON object with keys: recipient, subject, body. "
            "Use 'Becton Enterprises' as the sender's name when closing the email."

        )

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        # Expecting GPT to respond with a dict-like string
        content = response.choices[0].message.content.strip()

        try:
            email_data = eval(content)  # In real apps, prefer using `json.loads()` with valid JSON
            recipient = email_data.get("recipient", "")
            subject = email_data.get("subject", "")
            body = email_data.get("body", "")
        except Exception as e:
            raise ValueError(f"Failed to parse email draft: {e}")

        # Return a nicely formatted string
        return (
            f"To: {recipient}\n"
            f"Subject: {subject}\n\n"
            f"{body}"
        )
            