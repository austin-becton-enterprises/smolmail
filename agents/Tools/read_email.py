"""
Tool: EmailReader
Purpose: Parses and understands emails from an inbox
"""
from smolagents.tool import Tool
# this is where you'll define your test emails


class EmailReader(Tool):
    name = "read_email"
    description = "Reads emails from a specificed inboxed and returns them."
    input = {}
    output_type = "string"

    def forward(self): 
        # return email, mpossibly formatted (email, subject, body) or
        # return just the relevanpipt information

        # *** WE WILL NOT NEED TO CREATE A DUMMY_DATA, THE DATA TEAM ALREADY HAS,
        # *** WE CAN EITHER GO THROUGH THEIR CODE AND MAKE SURE WE REFERENCE THE CORRECT DATA
        # *** OR WE CAN MESSAGE LIANA OR SIMRAN ABOUT IT
        
        return 0 
    