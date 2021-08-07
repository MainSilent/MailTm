import time
from threading import Thread

class Listen:
    listen = False

    def run(self):
        while True:
            if not self.listen:
                return

            

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
        time.sleep(interval+1)