import time


class GameTimer:
    def __init__(self):
        self.start = 0
        self.pause = 0
        self.paused = False
        self.started = False

    def start_timer(self):
        self.started = True
        self.paused = False
        self.start = time.time()
        self.pause = 0

    def stop_timer(self):
        self.started = False
        self.paused = False
        self.start = 0
        self.pause = 0

    def pause_timer(self):
        if self.started == True and self.paused == False:
            self.paused = True
            self.pause = time.time()
            self.start = 0

    def unpause_timer(self):
        if self.started == True and self.paused == True:
            self.paused = False
            self.start = time.time()
            self.pause = 0

    def get_time(self):
        my_time = 0
        if self.started == True:
            if self.paused == True:
                my_time = self.pause
            else:
                my_time = (time.time() - self.start) * 1000
        return my_time

    def is_started(self):
        return self.started

    def is_paused():
        return self.started and self.paused
