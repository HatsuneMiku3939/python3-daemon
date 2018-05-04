import signal

from miku import SingingMiku

class Worker:
    def main(self):
        signal.signal(signal.SIGINT, self.stop)
        signal.signal(signal.SIGTERM, self.stop)

        self.singing_miku = SingingMiku()
        res = self.singing_miku.main()
        return res

    def stop(self, signum, frame):
        self.singing_miku.stop()

