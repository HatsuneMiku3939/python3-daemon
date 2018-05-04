import os
import time
import logging
import signal

from worker import Worker

class Master:
    def __init__(self, num_workers, foreground, log_file):
        self.__stop = False
        self.workers = []

        self.num_workers = num_workers
        self.foreground = foreground
        self.log_file = log_file

        logging.basicConfig(level=logging.INFO, format='%(message)s')
        self.logger = logging.getLogger("Master")
        self.log_file = log_file

        if self.foreground:
            self.log_file = None

        if log_file:
            splited = self.log_file.split('.')
            master_log_file = ".".join([splited[0], 'master', splited[1]])

            self.log_handler = logging.FileHandler(master_log_file)
            self.logger.addHandler(self.log_handler)

    def main(self):
        self.logger.info("Start Master, PID {0}".format(os.getpid()))

        signal.signal(signal.SIGINT, self.stop)
        signal.signal(signal.SIGTERM, self.stop)

        for id in range(self.num_workers):
            pid = os.fork()

            if pid == 0:
                if self.foreground:
                    worker_log_file = None
                else:
                    splited = self.log_file.split('.')
                    worker_log_file = ".".join([splited[0], str(id), splited[1]])

                worker = Worker(id, worker_log_file)
                exit_code = worker.main()
                exit(exit_code)
            else:
                self.logger.info("Start worker-{0} PID {1}".format(id, pid))
                self.workers.append({"id": id, "pid": pid})

        while not self.__stop:
            time.sleep(1)

        self.logger.info("Stop Master, PID {0}".format(os.getpid()))

    def stop(self, signum, frame):
        self.__stop = True
        self.logger.info("Receive Signal {0}".format(signum))

        for worker in self.workers:
            self.logger.info("Send Signal {0} to worker-{1} PID {2}".format(signal.SIGTERM, worker['id'], worker['pid']))
            os.kill(worker['pid'], signal.SIGTERM)
