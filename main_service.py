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
            print(emails)
            for email in emails:
                print(f"- From: {email['From']}")
                print(f"  Subject: {email['subject']}")
                print(f"  Snippet: {email['snippet']}")
                print("---")
                test_send_email(gmail_service,email['From'],email['id'])
    except Exception as e:
        logger.error(f"Error reading emails: {e}", exc_info=True)
        print(f"Error reading emails: {e}")


def test_send_email(gmail_service,to,id):
    try:
        # to = input("Enter your email address to send a test email: ").strip()
        subject = "AI Test Email via gmail_service"
        body = "This is a test email sent using the new gmail_service module."
        
        confirmation = input(f"Send email to {to}? (y/n): ").strip().lower()
        if confirmation == 'y':
            result = gmail_service.send_email(to, subject, body)
            if result:
                logger.info(f"Email sent successfully to {to}.")
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


if __name__ == '__main__':
    print("=== Gmail Tools Test Runner ===")

    # Authenticate and build the service
    gmail = API()
    gmail_service = GmailService(gmail.service)

    # Run tests
    test_read_email(gmail_service)