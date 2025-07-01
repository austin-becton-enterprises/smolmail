"""
Tool: EmailReader
Purpose: Parses and understands emails from an inbox
"""
from smolagents.tools import Tool

# this is where you'll define your test emails

class EmailReader(Tool):
    name = "read_email"
    description = "Reads emails from a specificed inboxed and returns them."
    input = {
        "mode": {
            "type": "string",
            "enum": ["all", "latest", "specific"],
            "description": "Choose 'all' to read all emails, 'latest' for the newest, or 'specific' for a specific index."
        },
        "index": {
            "type": "integer",
            "description": "The index of the specific email to read (used only when mode is 'specific').",
            "default": 0
        }
    }
    
    output_type = "string"

    def forward(self, mode: str, index: int 0) -> str: 
        # return email, mpossibly formatted (email, subject, body) or
        # return just the relevanpipt information

        # *** WE WILL NOT NEED TO CREATE A DUMMY_DATA, THE DATA TEAM ALREADY HAS,
        # *** WE CAN EITHER GO THROUGH THEIR CODE AND MAKE SURE WE REFERENCE THE CORRECT DATA
        # *** OR WE CAN MESSAGE LIANA OR SIMRAN ABOUT IT

        # might want to set a max number, because if theres thousands of emails then it may be a problem 
        # either can read from old-new or new-old
       
        if mode == "all":
            return "returning the whole inbox"
        elif mode =="lates":
            return "returning the latest inbox"
        elif mode == "specific": 
            return "returning email from ..."
        else: 
            return "invalid mode. Choose 'all', 'latest', or specific'."
