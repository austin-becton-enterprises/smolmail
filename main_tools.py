# main_tools.py

from gmail import API
from gmail_tools import read_email, send_email

def test_read_email(service):
    # Test reading unread emails using the gmail_tools function
    emails = read_email(service)
    if not emails:
        print("No unread emails found.")
    else:
        print(f"Retrieved {len(emails)} unread emails:")
        for email in emails:
            print(f"- From: {email['sender']}")
            print(f"  Subject: {email['subject']}")
            print(f"  Snippet: {email['snippet']}")
            print("---")

def test_send_email(service):
    # Prompt for email address to send a test message
    to = input("Enter your email address to send a test email: ").strip()
    subject = "AI Test Email via gmail_tools"
    body = "This is a test email sent using the new gmail_tools module."
    
    confirmation = input(f"Send email to {to}? (y/n): ").strip().lower()
    if confirmation == 'y':
        result = send_email(service, to, subject, body)
        if result:
            print("Email sent successfully.")
        else:
            print("Email failed to send.")
    else:
        print("⚠️ Email send cancelled.")

if __name__ == '__main__':
    print("=== Gmail Tools Test Runner ===")

    # Authenticate and build the service
    gmail = API()
    service = gmail.service

    # Run tests
    test_read_email(service)
    test_send_email(service)
