# Testing email_reply
from email_reply import general_email_reply, ai_email_reply
from Firestore.firestore_main import firestoremain
from Firestore.core.firestore_service import FirestoreService

# main_tools.py

from app.core.gmail_api import API
from app.core.gmail_facade import GmailService
from app.utils.log_config import setup_logger

logger = setup_logger()

def test_read_email(gmail_service, fs_service):
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
                test_send_email(gmail_service, fs_service, email['From'], email['id'])
    except Exception as e:
        logger.error(f"Error reading emails: {e}", exc_info=True)
        print(f"Error reading emails: {e}")

def test_send_email(gmail_service, fs_service, to=None, id=None):
    try:
        if not to:
            to = input("Enter email address to send a test email: ").strip()

        name = input("Enter recipient name (optional): ").strip() or None
        issue = input("Enter issue (optional): ").strip() or None
        additional_info = input("Any additional info (optional): ").strip() or None

        # Default values
        selected_template_id = "custom"
        body = None

        # Try to fetch first available template
        templates = fs_service.list_templates()
        if templates:
            first_template = templates[0]
            selected_template_id = first_template.get("template_id", "custom")
            template_code = first_template.get("template_code", "")

            try:
                body = template_code.format(name=name, issue=issue, additional_info=additional_info)
                print(f"📄 Using template: {selected_template_id}")
            except Exception as e:
                logger.warning(f"Template rendering failed: {e}. Falling back to default.")
                body = None

        # Fallback if no valid template or rendering failed
        if not body:
            body = general_email_reply(name=name, issue=issue, additional_info=additional_info)
            print("⚠️ Using default email reply template.")

        subject = f"Re: {issue or 'Support Request'}"

        confirmation = input(f"\nSend email to {to}? \n\n{body}\n\n(y/n): ").strip().lower()
        if confirmation == 'y':
            result = gmail_service.send_email(to, subject, body)
            if result:
                if id:
                    gmail_service.mark_as_read(id)
                logger.info(f"Email sent successfully to {to}.")
                print("✅ Email sent successfully.")

                metadata = {
                    "to": to,
                    "subject": subject,
                    "template_id": selected_template_id,
                    "issue": issue,
                    "name": name,
                    "additional_info": additional_info,
                }

                try:
                    email_id = fs_service.log_email(template_id=selected_template_id, metadata=metadata)
                    logger.info(f"Logged email to Firestore with ID: {email_id}")
                    print(f"📬 Email logged in Firestore with ID: {email_id}")
                except Exception as log_err:
                    logger.error(f"Failed to log email: {log_err}", exc_info=True)
                    print(f"⚠️ Failed to log email: {log_err}")
            else:
                logger.error(f"Email failed to send to {to}.")
                print("❌ Email failed to send.")
        else:
            logger.info("Email send cancelled by user.")
            print("⚠️ Email send cancelled.")
    except Exception as e:
        logger.error(f"Error sending email: {e}", exc_info=True)
        print(f"Error sending email: {e}")


def main():
    fs_service = FirestoreService()
    while True:
        print("\n=== Select Application ===")
        print("1. Gmail Tools")
        print("2. Firestore App")
        print("0. Exit")

        y = input("Enter option [1/2/0]: ").strip()

        if y == '1':
            client_id = input("Enter Client ID to log email activity: ").strip()
            if fs_service.login_client(client_id):
                client_data = fs_service.read_client(client_id)
                if not client_data:
                    print("❌ Failed to fetch client data.")
                    return

                print(f"✅ Logged in as {client_id}")
                
                # Extract credential path from Firestore
                client_credentials = client_data.get("client_credentials")
                print(f"🔐 Using Gmail credentials: {client_credentials}")

                # Initialize Gmail API using client-specific credentials
                gmail = API(creds_path=client_credentials)
                gmail_service = GmailService(gmail.service)

                test_read_email(gmail_service, fs_service)
            else:
                print("❌ Client not found.")
        elif y == '2':
            firestoremain()
        elif y == '0':
            print("Goodbye!")
            break
        else:
            print("❌ Invalid input. Please enter 1, 2, or 0.")

if __name__ == '__main__':
    main()
