import argparse

import util

conversefile = ""
logfile = ""

def main():
    # globals
    global conversefile
    global logfile

    # args
    parser = argparse.ArgumentParser(
        prog="llamaparse"
    )

    parser.add_argument("dataset")
    parser.add_argument("-f", "--conversefile")
    parser.add_argument("-l", "--logfile")

    args = parser.parse_args()

    dataset = args.dataset
    conversefile = args.conversefile
    logfile = args.logfile

if (__name__ == "__main__"):
    main()
    util.save_logs(logfile)