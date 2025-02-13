import argparse
import os
import datetime

import requests

import util

dir_path = os.path.dirname(os.path.realpath("__init__.py"))

conversefile = ""
logfile = ""

server = ""
port = "11434"

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
    # server += port + "/api/generate"

    server = f"http://{server}:{port}"
    print(server)
    data = '{"query":"can you hear me?"}'
    headers = {"Content-Type": "application/json"}
    print(data)
    response = requests.post(server, json=data, headers=headers)
    print(response.status_code, response.reason)

if (__name__ == "__main__"):
    main()
    util.save_logs(dir_path + logfile)