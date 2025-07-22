# write email tool tester

from openai import OpenAI
import os
from dotenv import load_dotenv
import json

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_email_from_prompt(prompt: str) -> str:
    if not prompt.strip():
        raise ValueError("Prompt cannot be empty.")

    system_message = (
        "You are an assistant that writes professional, clear, and polite email drafts "
        "based on a short description. Only return a raw JSON object with keys: recipient, subject, body. "
        "Do NOT include code blocks or any text before or after the JSON." 
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

    content = response.choices[0].message.content.strip()

    try:
        email_data = eval(content)  
        recipient = email_data.get("recipient", "")
        subject = email_data.get("subject", "")
        body = email_data.get("body", "")
    except Exception as e:
        raise ValueError(f"Failed to parse email draft: {e}")

    return (
        f"To: {recipient}\n"
        f"Subject: {subject}\n\n"
        f"{body}"
    )
