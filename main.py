import json
import requests

class Email:
    domain = ""

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

if __name__ == "__main__":
    test = Email()
    print("Domain: " + test.domain)