import logging
import time
import json
from datetime import datetime

import pytz
from dateutil.tz import tzlocal

class Logger:
    def __init__(self, name, log_file):
        self.log_file = log_file
        self.name = name

        self.local_tz = tzlocal()

        logging.basicConfig(level=logging.INFO, format='%(message)s')
        self.logger = logging.getLogger(self.name)

        if self.log_file:
            self.log_handler = logging.FileHandler(self.log_file)
            self.logger.addHandler(self.log_handler)

    def __timestamp(self):
        return str(datetime.now(tz=self.local_tz).isoformat())

    def log(self, event, event_value):
        log = {
            'timestamp': self.__timestamp(),
            'component': self.name,
            'log': {
                'event': event,
                'event_value': event_value
             }
        }
        self.logger.info(json.dumps(log))

