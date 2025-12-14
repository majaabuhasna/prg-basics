import emails

try:
    with open('email.txt', 'r', encoding='utf-8') as file:
        content = file.read()

    sender = emails.email_sender(content)
    recipient = emails.email_recipient(content)
    subject = emails.email_subject(content)
    body = emails.email_body(content)

    print(f'=== EMAIL DATA ===\n')
    print(f'Sender: {sender}\n')
    print(f'Recipient: {recipient}\n')
    print(f'Subject: {subject}\n')
    print(f'Body:\n{body}')

except FileNotFoundError:
    print('File not found')