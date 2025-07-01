# main_tools.py
from app.core.mail_agent import MailAgent
from app.core.gmail_api import API
from app.core.gmail_facade import GmailService
from app.utils.log_config import setup_logger
import time

logger = setup_logger()

def test_read_email(gmail_service):
    # Test reading unread emails using the gmail_service function
    try:
        emails = gmail_service.read_most_recent_emails()
        if not emails:
            logger.info("No unread emails found.")
            print("No unread emails found.")
        else:
            logger.info(f"Retrieved {len(emails)} unread emails.")
            print(f"Retrieved {len(emails)} unread emails:")
            print(emails)
            for email in emails:
                print(f"- From: {email['From']}")
                print(f"  Subject: {email['subject']}")
                print(f"  Snippet: {email['snippet']}")
                print("---")
                test_send_email(
                    gmail_service,
                    to=email['From'],
                    id=email['id'],
                    snippet=email
                )
    except Exception as e:
        logger.error(f"Error reading emails: {e}", exc_info=True)
        print(f"Error reading emails: {e}")


def test_send_email(gmail_service,to,id,snippet):
    try:
        agent = MailAgent()
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
        result = agent.run({"snippet": prompt})
        subject = "Reply from AI Assistant"
        body = result  # Set AI result as the email body
        logger.info(f"AI Response: {result}")
        # confirmation = input(f"Send email to {to}? (y/n): ").strip().lower()
        # if confirmation == 'y':
        result = gmail_service.send_email(to, subject, body)
        if result:
            logger.info(f"Email sent successfully to {to}.")
            gmail_service.mark_as_read(id)
            print("Email sent successfully.")
        else:
            logger.error(f"Email failed to send to {to}.")
            print("Email failed to send.")
        # else:
            # logger.info("Email send cancelled by user.")
            # print("⚠️ Email send cancelled.")
    except Exception as e:
        logger.error(f"Error sending email: {e}", exc_info=True)
        print(f"Error sending email: {e}")


if __name__ == '__main__':
    print("=== Gmail Tools Test Runner ===")
    # Authenticate and build the service
    gmail = API()
    gmail_service = GmailService(gmail.service)

    # Run tests
    while True:
        test_read_email(gmail_service)
        time.sleep(5)  # Wait 5 seconds before checking again