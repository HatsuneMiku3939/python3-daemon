import signal

from miku import SingingMiku

class Worker:
    def __init__(self, id, log_file):
        self.id = id
        self.log_file = log_file

    def main(self):
        signal.signal(signal.SIGINT, self.stop)
        signal.signal(signal.SIGTERM, self.stop)

        self.singing_miku = SingingMiku(self.id, self.log_file)
        res = self.singing_miku.main()
        return res

    def stop(self, signum, frame):
        self.singing_miku.stop()

