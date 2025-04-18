import time
import threading
from config import config

class Scheduler:
    def __init__(self, task, interval_seconds):
        self.task = task
        self.interval = interval_seconds
        self.thread = threading.Thread(target=self.run)
        self.stop_event = threading.Event()

    def start(self):
        self.thread.start()

    def run(self):
        while not self.stop_event.is_set():
            self.task()
            self.stop_event.wait(self.interval)

    def stop(self):
        self.stop_event.set()
        self.thread.join()

def auto_restart(bot_start_function, interval_seconds):
    """
    Função para auto reiniciar o bot a cada intervalo definido.
    """
    while True:
        bot_start_function()
        time.sleep(interval_seconds)
