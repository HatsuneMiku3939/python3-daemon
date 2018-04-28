import time
import logging

class SingingMiku:
    SONG_LIST = ["Miku Miku Ni Shite Ageru","World is Mine", "39" ]

    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger("SingingMiku")

    def main(self):
        i = 0
        while True:
            self.logger.info(self.SONG_LIST[i % len(self.SONG_LIST)])
            i += 1
            time.sleep(1)

singing_miku = SingingMiku()
singing_miku.main()

