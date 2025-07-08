from gmail import API
import pprint

def test_authentication():
    gmail = API()
    assert gmail.is_authenticated(), "Authentication failed"
    print("Authentication test passed.")
    return gmail

def test_list_messages(gmail):
    messages = gmail.list_messages(3)
    assert isinstance(messages, list), "list_messages did not return a list"
    print(f"list_messages test passed. Retrieved {len(messages)} messages.")
    return messages

def test_get_message(gmail, message_id):
    message = gmail.get_message(message_id)
    assert 'id' in message, "get_message response is missing 'id'"
    print(f"get_message test passed for ID: {message_id}")
    return message

def test_send_email(gmail):
    to = input("Enter your email address to send a test email: ").strip()
    subject = "Gmail API Test Email"
    body = "This is a test email sent using the Gmail API."
    
    confirmation = input(f"Send email to {to}? (y/n): ").strip().lower()
    if confirmation == 'y':
        response = gmail.send_email(to, subject, body)
        assert 'id' in response, "Email not sent successfully"
        print("send_email test passed.")
        pprint.pprint(response)
    else:
        print("⚠️ Skipped sending email.")

if __name__ == '__main__':
    print("=== Gmail API Test Runner ===")

    # Step 1: Authenticate
    gmail = test_authentication()

    # Step 2: List recent messages
    messages = test_list_messages(gmail)

    # Step 3: Get the first message content
    if messages:
        test_get_message(gmail, messages[0]['id'])
    else:
        print("No messages found.")

    # Step 4: Send a test email (optional)
    test_send_email(gmail)

