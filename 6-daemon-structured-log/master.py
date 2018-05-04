import os
import time
import signal

from worker import Worker
from logger import Logger

class Master:
    def __init__(self, num_workers, foreground, log_file):
        self.__stop = False
        self.workers = []

        self.num_workers = num_workers
        self.foreground = foreground
        self.log_file = log_file

        if self.foreground:
            self.log_file = None

        if self.log_file:
            splited = self.log_file.split('.')
            self.log_file = ".".join([splited[0], 'master', splited[1]])

        self.logger = Logger('master', self.log_file)

    def main(self):
        self.logger.log("start", {
            "pid": str(os.getpid())
        })

        signal.signal(signal.SIGINT, self.stop)
        signal.signal(signal.SIGTERM, self.stop)

        for id in range(self.num_workers):
            pid = os.fork()

            if pid == 0:
                if self.foreground:
                    worker_log_file = None
                else:
                    worker_log_file = self.log_file.replace('master', str(id))

                worker = Worker(id, worker_log_file)
                exit_code = worker.main()
                exit(exit_code)
            else:
                self.logger.log("fork", {
                    "woker_id": id,
                    "pid": str(os.getpid())
                })
                self.workers.append({"id": id, "pid": pid})

        while not self.__stop:
            time.sleep(1)

        self.logger.log("stop", {
            "pid": str(os.getpid())
        })

    def stop(self, signum, frame):
        self.__stop = True
        self.logger.log("receive_signal", {
            "signal_number": str(signum)
        })

        for worker in self.workers:
            self.logger.log("send_signal", {
                "worker_id": str(worker['id']),
                "pid": str(worker['pid']),
                'signal_number': signal.SIGTERM
            })
            os.kill(worker['pid'], signal.SIGTERM)
