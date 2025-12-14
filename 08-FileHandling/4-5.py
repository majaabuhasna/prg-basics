import emails

try:
    with open('email.txt', 'r', encoding='utf-8') as file:
        content = file.read()

    sender = emails.email_sender(content)
    recipient = emails.email_recipient(content)
    subject = emails.email_subject(content)
    body = emails.email_body(content)

    print('=== EMAIL DATA ===')
    print(f'Sender: {sender}')
    print(f'Recipient: {recipient}')
    print(f'Subject: {subject}')
    print(f'Body: {body}')

except FileNotFoundError:
    print('File not found')