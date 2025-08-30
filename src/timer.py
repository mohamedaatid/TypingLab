import time

class timer:
    def __init__(self):
        self.start_timer = None
        self.stop_timer = None
    def start_timer(self):
        self.start_timer = time.time()
    def stop_timer(self):
        self.stop_timer = time.time()
    def get_elapsed(self):
        elapsed = self.stop_timer - self.start_timer
        return elapsed