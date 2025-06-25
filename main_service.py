# main_tools.py

from gmail import API
from gmail_service import read_most_recent_emails, send_email
from log_config import setup_logger

logger = setup_logger()

def test_read_email(service):
    # Test reading unread emails using the gmail_service function
    try:
        emails = read_most_recent_emails(service)
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
                test_send_email(service,email['From'])
    except Exception as e:
        logger.error(f"Error reading emails: {e}", exc_info=True)
        print(f"Error reading emails: {e}")


def test_send_email(service,to):
    try:
        # to = input("Enter your email address to send a test email: ").strip()
        subject = "AI Test Email via gmail_service"
        body = "This is a test email sent using the new gmail_service module."
        
        confirmation = input(f"Send email to {to}? (y/n): ").strip().lower()
        if confirmation == 'y':
            result = send_email(service, to, subject, body)
            if result:
                logger.info(f"Email sent successfully to {to}.")
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
    service = gmail.service

    # Run tests
    test_read_email(service)
