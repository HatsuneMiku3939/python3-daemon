import time
import logging
import random

import os
from logger import Logger

class SingingMiku:
    SONG_LIST = ["Miku Miku Ni Shite Ageru","World is Mine", "39" ]

    def __init__(self, id, log_file=None):
        self.id = id
        self.log_file = log_file
        self.__stop = False

        self.logger = Logger('worker-{0}'.format(self.id), self.log_file)

    def main(self):
        self.logger.log('start', {
            'worker_id': self.id,
            'pid': os.getpid()
        })
        random.seed(self.id)
        while not self.__stop:
            song = random.choice(self.SONG_LIST)
            self.logger.log('sing', {
                'song': song
            })

            time.sleep(1)

        self.logger.log('stop', {
            'worker_id': self.id,
            'pid': os.getpid()
        })
        return 0

    def stop(self):
        self.__stop = True
