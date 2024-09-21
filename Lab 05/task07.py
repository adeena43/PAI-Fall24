import re

def extract_emails(text):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

    emails = re.findall(email_pattern, text)
    return emails

text = """
Hello, please contact us at fastkhinu@example.com for further information.
You can also reach out to adinafraz01@example.co.uk and syed_farhan23@sub.example.org.
For urgent issues, email admin@website.net or hr@company.com.
"""

emails = extract_emails(text)
print("Extracted Email Addresses: ")
for email in emails:
    print(email)
