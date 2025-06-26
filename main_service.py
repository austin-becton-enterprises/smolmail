#Testubg email_reply
from email_reply import general_email_reply, ai_email_reply

# main_tools.py

from gmail import API
from gmail_service import read_most_recent_emails, send_email

def test_read_email(service):
    # Test reading unread emails using the gmail_service function
    emails = read_most_recent_emails(service)
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
    to = input("Enter email address to send a test email: ").strip()

    #Inputs
    name = input ("Enter recipient name (optional): ").strip() or None
    issue = input("Enter issue (optional): ").strip() or None
    additional_info = input("Any additional info (optional): ").strip() or None

    #Generate body using email_template
    body = general_email_reply(name=name, issue=issue, additional_info=additional_info)
    subject = f"Re: {issue or 'Support Request'}"
    
    confirmation = input(f"Send email to {to}? \n\n{body}\n\n(y/n): ").strip().lower()
    if confirmation == 'y':
        result = send_email(service, to, issue, body)
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
    #test_read_email(service)
    test_send_email(service)
