import time
import random

import os
from logger import Logger

class SingingMiku:
    SONG_LIST = ["Miku Miku Ni Shite Ageru","World is Mine", "39" ]

    def __init__(self):
        self.__stop = False
        self.logger = Logger('SingingMiku')

    def main(self):
        self.logger.log('start', {
            'pid': os.getpid()
        })
        while not self.__stop:
            song = random.choice(self.SONG_LIST)
            self.logger.log('sing', {
                'song': song
            })

            time.sleep(1)

        self.logger.log('stop', {
            'pid': os.getpid()
        })
        return 0

    def stop(self):
        self.__stop = True
