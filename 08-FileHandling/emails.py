import re

def email_sender(text):
    pattern = 'From:.*<([^>]+)>'
    match = re.search(pattern,text)

    if match:
        return match.group(1)
    return None

def email_recipient(text):
    pattern = 'To:.*<([^>]+)>'
    match = re.search(pattern,text)

    if match:
        return match.group(1)
    return None

def email_subject(text):
    pattern = 'Subject: (.*)'
    match = re.search(pattern,text)

    if match:
        return match.group(1)
    return None

def email_body(text):
    pattern = '\n\n(.*)'

    match = re.search(pattern,text,re.DOTALL)

    if match:
        return match.group(1).strip()
    return None