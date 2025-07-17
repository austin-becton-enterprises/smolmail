from agents.Tools.write_email import EmailWriter
from agents.Tools.send_email import EmailSender
#from agents.Tools.logger_tool import ToolLogger
#from agents.Tools.client_search_tool import ClientSearchTool
#from agents.Tools.client_data import dummy_clients
from agents.Tools.read_email import EmailReader  # Added EmailReader import

import re

class EmailAgent:
    def __init__(self):
        self.writer = EmailWriter()
        self.sender = EmailSender()
       # self.logger = ToolLogger()
        #self.client_search = ClientSearchTool(dummy_clients)
        self.reader = EmailReader()  # Instantiate EmailReader

    def extract_email(self, text: str) -> str:
        match = re.search(r'[\w\.-]+@[\w\.-]+', text)
        return match.group(0) if match else ""

    def run(self, prompt: str, signature: str = "Best, Becton Enterprises") -> str:
        # Step 1: Write email draft from prompt
        print("[Agent] Writing email...")
        draft = self.writer.forward(prompt=prompt)

        self.logger.forward(
            tool_name="write_email",
            inputs={"prompt": prompt},
            output=str(draft),
            summary="Generated an email draft from user prompt."
        )

        # Step 2: Extract or lookup recipient email
        recipient_email = self.extract_email(prompt)
        if not recipient_email:
            print("[Agent] No email found in prompt. Attempting client search...")
            if " to " in prompt:
                name_in_prompt = prompt.split(" to ")[-1].split(" ")[0]
            else:
                name_in_prompt = ""
            client_result = self.client_search.forward({"name": name_in_prompt})
            if client_result.get("status") == "success":
                recipient_email = client_result["data"]["email"]
                print(f"[Agent] Found recipient email via client search: {recipient_email}")
            else:
                return "Failed to find recipient email in prompt or client search."

        subject = draft.get("subject", "No Subject")
        message = draft.get("body", "No Message") + f"\n\n{signature}"

        # Step 3: Send email
        print(f"[Agent] Sending email to {recipient_email}...")
        send_result = self.sender.forward(
            recipient_email=recipient_email,
            subject=subject,
            message=message
        )

        self.logger.forward(
            tool_name="send_email",
            inputs={
                "recipient_email": recipient_email,
                "subject": subject,
                "message": message
            },
            output=send_result,
            summary="Sent email via Gmail test account."
        )

        return send_result

    def read_emails(self, mode: str = "latest", index: int = 0) -> str:
        print(f"[Agent] Reading emails with mode='{mode}', index={index}...")
        result = self.reader.forward(mode=mode, index=index)
        self.logger.forward(
            tool_name="read_email",
            inputs={"mode": mode, "index": index},
            output=result,
            summary="Read emails from inbox."
        )
        return result
