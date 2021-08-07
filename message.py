import time
from threading import Thread

class Listen:
    listen = False

    def run(self):
        while True:
            if not listen:
                return

            time.sleep(self.interval)

    def start(self, interval=4):
        if self.listen:
            self.stop()

        self.interval = interval
        self.listen = True
        self.run(interval)
    
    def stop(self):
        self.listen = False
        time.sleep(interval+1)