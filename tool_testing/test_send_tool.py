from agents.Tools.write_email import EmailWriter
from agents.Tools.send_email import EmailSender

def start():
    # Initialize the email writer and sender tools
    write_email = EmailWriter()
    send_email = EmailSender()

    # Use the write tool to generate the email

    draft = write_email.forward("Write an email to david.kim@example.com about a follow-up meeting")

    #send the email using send tool
    result = send_email.forward(draft)

    print(result)  # Output the result of sending the email
    #This will print the success message or any error that occurred during sending.