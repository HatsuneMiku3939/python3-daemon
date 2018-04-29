import os
import sys

import argparse

from miku import SingingMiku

def run(foreground, log_file):
    singing_miku = SingingMiku(foreground, log_file)
    exit_code = singing_miku.main()
    exit(exit_code)

def daemonize(args):
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
            # just exit
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

            run(args.foreground, args.log)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--pid", help="pid filename, required in background mode", default=None)
    parser.add_argument("--log", help="log filename, highly recommended in background mode", default=None)
    parser.add_argument("--foreground", help="runing foregroundu mode", action='store_true')
    args = parser.parse_args()

    if not args.foreground and not args.pid:
        parser.print_help()
        print("in background mode, the following arguments are required: --pid")
        exit(1)

    if args.foreground:
        run(args.foreground, args.log)
    else:
        daemonize(args)
