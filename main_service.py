# Testing email_reply
from email_reply import general_email_reply, ai_email_reply
from Firestore.firestore_main import firestoremain

# main_tools.py

from app.core.gmail_api import API
from app.core.gmail_facade import GmailService
from app.utils.log_config import setup_logger

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
            for email in emails:
                print(f"- From: {email['From']}")
                print(f"  Subject: {email['subject']}")
                print(f"  Snippet: {email['snippet']}")
                print("---")
                test_send_email(gmail_service, email['From'], email['id'])
    except Exception as e:
        logger.error(f"Error reading emails: {e}", exc_info=True)
        print(f"Error reading emails: {e}")

def test_send_email(gmail_service, to=None, id=None):
    try:
        # Prompt for email address to send a test message if not provided
        if not to:
            to = input("Enter email address to send a test email: ").strip()

        # Inputs
        name = input("Enter recipient name (optional): ").strip() or None
        issue = input("Enter issue (optional): ").strip() or None
        additional_info = input("Any additional info (optional): ").strip() or None

        # Generate body using email_template
        body = general_email_reply(name=name, issue=issue, additional_info=additional_info)
        subject = f"Re: {issue or 'Support Request'}"

        confirmation = input(f"Send email to {to}? \n\n{body}\n\n(y/n): ").strip().lower()
        if confirmation == 'y':
            result = gmail_service.send_email(to, subject, body)
            if result:
                logger.info(f"Email sent successfully to {to}.")
                if id:
                    gmail_service.mark_as_read(id)
                print("Email sent successfully.")
            else:
                logger.error(f"Email failed to send to {to}.")
                print("Email failed to send.")
        else:
            logger.info("Email send cancelled by user.")
            print("⚠️ Email send cancelled.")
    except Exception as e:
        logger.error(f"Error sending email: {e}", exc_info=True)
        print(f"Error sending email: {e}")

def main():
    while True:
        print("\n=== Select Application ===")
        print("1. Gmail Tools")
        print("2. Firestore App")
        print("0. Exit")

        y = input("Enter option [1/2/0]: ").strip()

        if y == '1':
            print("=== Gmail Tools Test Runner ===")
            gmail = API()
            gmail_service = GmailService(gmail.service)
            test_read_email(gmail_service)
        elif y == '2':
            firestoremain()
        elif y == '0':
            print("Goodbye!")
            break
        else:
            print("❌ Invalid input. Please enter 1, 2, or 0.")

if __name__ == '__main__':
    main()
