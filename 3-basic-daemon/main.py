import os
import sys

import argparse

from miku import SingingMiku

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--pid", help="pid filename", required=True)
    parser.add_argument("--log", help="log filename", default=None)
    args = parser.parse_args()

    # double fork, first fork
    pid = os.fork()
    if pid > 0:
        # parent procrss
        # just exit
        exit(0)
    else:
        # decouple from parent envronment
        os.chdir('/')
        os.setsid()
        os.umask(0)

        # second fork
        pid = os.fork()
        if pid > 0:
            exit(0)
        else:
            sys.stdout.flush()
            sys.stderr.flush()

            si = open(os.devnull, 'r')
            so = open(os.devnull, 'a+')
            se = open(os.devnull, 'a+')

            os.dup2(si.fileno(), sys.stdin.fileno())
            os.dup2(so.fileno(), sys.stdout.fileno())
            os.dup2(se.fileno(), sys.stderr.fileno())

            with open(args.pid, "w") as pid_file:
                pid_file.write(str(os.getpid()))

            singing_miku = SingingMiku(args.log)
            exit_code = singing_miku.main()
            exit(exit_code)
