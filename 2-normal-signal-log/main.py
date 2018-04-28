import time
import logging

import os
import signal

import argparse

class SingingMiku:
    SONG_LIST = ["Miku Miku Ni Shite Ageru","World is Mine", "39" ]

    def __init__(self, log_file=None):
        logging.basicConfig(level=logging.INFO, format='%(message)s')
        self.logger = logging.getLogger("SingingMiku")
        self.log_file = log_file

        if log_file:
            self.log_handler = logging.FileHandler(self.log_file)
            self.logger.addHandler(self.log_handler)

        self.__stop = False

        signal.signal(signal.SIGINT, self.stop)
        signal.signal(signal.SIGTERM, self.stop)

    def main(self):
        i = 0
        self.logger.info("Start Singing, PID {0}".format(os.getpid()))
        while not self.__stop:
            self.logger.info(self.SONG_LIST[i % len(self.SONG_LIST)])
            i += 1
            time.sleep(1)


    def stop(self, signum, frame):
        self.__stop = True
        self.logger.info("Receive Signal {0}".format(signum))
        self.logger.info("Stop Singing")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--log", help="log filename", default=None)
    args = parser.parse_args()

    singing_miku = SingingMiku(args.log)
    singing_miku.main()

