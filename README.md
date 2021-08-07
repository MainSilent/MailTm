# MailTM API Wrapper

MailTm is a free temporary mail service, This library is useful for automation tasks such as making accounts that needs email verification.

## Installation

Windows:

```
pip install MailTm
```

Linux/Mac OS:

```
pip3 install MailTm
```

## Example

```python
from mailtm import Email

def listener(message):
    print("\nSubject: " + message['subject'])
    print("Content: " + message['text'] if message['text'] else message['html'])

# Get Domains
test = Email()
print("\nDomain: " + test.domain)

# Make new email address
test.register()
print("\nEmail Adress: " + str(test.address))

# Start listening
test.start(listener)
print("\nWaiting for new emails...")
```

# Documentation

`register(username=None, password=None, domain=None)` | Make an email account with random credentials, You can also pass a username, password and domain to use the same account.

`start(listener, interval=3)` | Start listening for new emails, Interval means how many seconds takes to sync.

`stop()` | Stop listening for new emails.