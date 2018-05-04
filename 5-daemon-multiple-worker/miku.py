import time
import logging
import random

import os

class SingingMiku:
    SONG_LIST = ["Miku Miku Ni Shite Ageru","World is Mine", "39" ]

    def __init__(self, id, log_file=None):
        logging.basicConfig(level=logging.INFO, format='%(message)s')
        self.logger = logging.getLogger("SingingMiku")
        self.log_file = log_file
        self.id = id

        if log_file:
            self.log_handler = logging.FileHandler(self.log_file)
            self.logger.addHandler(self.log_handler)

        self.__stop = False

    def main(self):
        self.logger.info("Start Singing, PID {0}".format(os.getpid()))
        random.seed(self.id)
        while not self.__stop:
            song = random.choice(self.SONG_LIST)
            self.logger.info(song)

            time.sleep(1)

        self.logger.info("Stop Singing, PID {0}".format(os.getpid()))
        return 0

    def stop(self):
        self.__stop = True
