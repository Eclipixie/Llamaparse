import argparse
import os
import datetime

import llama_client

import util

dir_path = os.path.dirname(os.path.realpath("__init__.py"))

conversefile = ""
logfile = ""

server = ""
port = "8321"

conversation = []

def main():
    # globals
    global conversefile
    global logfile
    global server
    global port

    logfile = "\\logs\\" + (str(datetime.datetime.now())
        .split(".")[0]
        .replace(" ","_")
        .replace(":","-"))

    # args
    parser = argparse.ArgumentParser(
        prog="llamaparse"
    )

    parser.add_argument("dataset")
    parser.add_argument("-f", "--conversefile")
    parser.add_argument("-l", "--logfile")
    parser.add_argument("-s", "--localsource", 
                        action="store_const", 
                        const="127.0.0.1")

    args = parser.parse_args()

    dataset = args.dataset
    conversefile = args.conversefile
    if (args.logfile != None): logfile = args.logfile
    server = args.localsource

    if (server == None): server = "127.0.0.1"

    client = llama_client.create_http_client(port)
    llama_client.request(client, "hello")

if (__name__ == "__main__"):
    main()
    util.save_logs(dir_path + logfile)