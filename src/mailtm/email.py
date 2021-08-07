import json
import string
import random
import requests
from .message import Listen

def username_gen(length=24, chars= string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(length))  

def password_gen(length=8, chars= string.ascii_letters + string.digits + string.punctuation):
        return ''.join(random.choice(chars) for _ in range(length))  

class Email(Listen):
    token = ""
    domain = ""
    address = ""

    def __init__(self):
        if not self.domains():
            print("Failed to get domains")

    def domains(self):
        url = "https://api.mail.tm/domains"
        response = requests.request("GET", url)

        try:
            data = json.loads(response.text)
            for domain in data['hydra:member']:
                if domain['isActive']:
                    self.domain = domain['domain']
                    return True

            raise Exception("No Domain")
        except:
            return False

    def register(self, username=None, password=None, domain=None):
        self.domain = domain if domain else self.domain
        username = username if username else username_gen()
        password = password if password else password_gen()

        url = "https://api.mail.tm/accounts"
        payload = json.dumps({
            "address": f"{username}@{self.domain}",
            "password": password
        })
        headers = { 'Content-Type': 'application/json' }
        response = requests.request("POST", url, headers=headers, data=payload)

        data = json.loads(response.text)
        try:
            self.address = data['address']
        except:
            self.address = f"{username}@{self.domain}"

        self.get_token(password)

        if not self.address:
            raise Exception("Failed to make an address")

    def get_token(self, password):
        url = "https://api.mail.tm/token"
        payload = json.dumps({
            "address": self.address,
            "password": password
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.request("POST", url, headers=headers, data=payload)
        try:
            self.token = json.loads(response.text)['token']
        except:
            raise Exception("Failed to get token")
        

if __name__ == "__main__":
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

    # Stop listening
    # test.stop()