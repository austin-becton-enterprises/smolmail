from gmail_service import send_email
from log_config import setup_logger

#Initialize loger 
logger = setup_logger

#General automated response email reply template
def general_email_reply(name=str|None, issue=str|None, additional_info=str|None, sender_name=str|"Support Team", company_name=str|"Company") -> str:
    greeting = f"Hello {name}," if name else "Hello,"
    body = (
        f"{greeting}\n\n"
        "Thank you for reaching out to us.\n"
    )
    
    if issue:
        body += f"We understand that you are experiencing the following: {issue}\n\n"
    else:
        body += "\n"

    body += (
        "Our team is currently reviewing your message and will get back to you shortly.\n\n"
    )

    if additional_info:
        body += f"Additional information: {additional_info}\n\n"

    body += (
        "If you have any more questions or details to share, please feel free to reply to this email.\n\n"
        "Best regards,\n"
        f"{sender_name}\n"
        f"{company_name}"
    )

    return body

#AI agent response email template 
def ai_email_reply( name= str|None, ai_response= str|None, sender_name="Support"|str, company_name=str|"Company") -> str:
    greeting = f"Hello {name}," if name else "Hello,"
    body = (
        f"{greeting}\n\n"
        "Following up on our previous message, here is some additional information:\n\n"
    )

    if ai_response:
        body += f"{ai_response}\n\n"
    else:
        body += "Our AI assistant is still processing your query and will get back to you shortly.\n\n"

    body += (
        "If you have further questions or need further assistance, please feel free to reply to this message.\n\n"
        "Best regards,\n"
        f"{sender_name}\n"
        f"{company_name}"
    )

    return body
