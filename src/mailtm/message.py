import json
import time
from threading import Thread

class Listen:
    listen = False
    message_ids = []

    def message_list(self):
        url = "https://api.mail.tm/messages"
        headers = { 'Authorization': 'Bearer ' + self.token }
        response = self.session.get(url, headers=headers)
        response.raise_for_status()
        
        data = response.json()
        return  [
                    msg for i, msg in enumerate(data['hydra:member']) 
                        if data['hydra:member'][i]['id'] not in self.message_ids
                ]

    def message(self, idx):
        url = "https://api.mail.tm/messages/" + idx
        headers = { 'Authorization': 'Bearer ' + self.token }
        response = self.session.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def source(self, idx):
        url = "https://api.mail.tm/sources/" + idx
        headers = { 'Authorization': 'Bearer ' + self.token }
        response = self.session.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def run(self):
        while self.listen:
            for message in self.message_list():
                self.message_ids.append(message['id'])
                message = self.message(message['id'])
                self.listener(message)

            time.sleep(self.interval)

    def start(self, listener, interval=3):
        if self.listen:
            self.stop()

        self.listener = listener
        self.interval = interval
        self.listen = True

        # Start listening thread
        self.thread = Thread(target=self.run)
        self.thread.start()
    
    def stop(self):
        self.listen = False
        self.thread.join()