import json
import time
import requests
from threading import Thread

class Listen:
    listen = False
    message_ids = []

    def message_list(self):
        url = "https://api.mail.tm/messages"
        headers = { 'Authorization': 'Bearer ' + self.token }
        response = requests.request("GET", url, headers=headers)
        
        try:
            data = json.loads(response.text)
            return  [
                        msg for idx, msg in enumerate(data['hydra:member']) 
                            if data['hydra:member'][idx]['id'] not in self.message_ids
                    ]
        except Exception as e:
            return []

    def message(self, id):
        ...

    def run(self):
        while True:
            if not self.listen:
                return

            for message in self.message_list():
                self.message_ids.append(message['id'])
                print(message)

            time.sleep(self.interval)

    def start(self, interval=4):
        if self.listen:
            self.stop()

        self.interval = interval
        self.listen = True

        # Start listening thread
        Thread(target=self.run).start()
    
    def stop(self):
        self.listen = False
        time.sleep(self.interval+1)