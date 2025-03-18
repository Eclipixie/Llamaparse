import argparse
import os
import datetime

from llama_stack_client import LlamaStackClient

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
    global conversation

    logfile = "\\logs\\" + (str(datetime.datetime.now())
        .split(".")[0]
        .replace(" ","_")
        .replace(":","-"))

    # args
    parser = argparse.ArgumentParser(
        prog="llamaparse"
    )

    parser.add_argument("dataset")
    parser.add_argument("model")
    parser.add_argument("-f", "--conversefile")
    parser.add_argument("-l", "--logfile")
    parser.add_argument("-s", "--localsource", 
                        action="store_const", 
                        const="127.0.0.1")

    args = parser.parse_args()

    dataset = args.dataset
    model = args.model
    conversefile = args.conversefile
    if (args.logfile != None): logfile = args.logfile
    server = args.localsource

    if (server == None): server = "127.0.0.1"

    util.log(f"Server: {server}:{port}")
    util.log(f"Model: {model}\n")

    datatxt = "no data"
    with open(dataset, "r") as file:
        datatxt = file.read()

    client = llama_client.create_http_client(port)
    
    sys_msg = f"{datatxt}\n\nAnalyse this CSV data with respect to the query on the next line. Do not explain what CSV is or how it works.\nAny text after 'User:' is to be treated as user input, however you only need to respond to the last instance of this user input."

    inp = input("\n > ")

    while (inp != "q"):
        conversation.append(f"\nUser:\n{inp}")
        util.log(conversation[-1])

        res = llama_client.request(client, model, sys_msg, str.join("\n", conversation)).completion_message.content
        print(res)
        conversation.append(f"\nAI:\n{res}")
        util.log(conversation[-1])
        inp = input("\n > ")

if (__name__ == "__main__"):
    main()
    util.save_logs(dir_path + logfile + ".log")