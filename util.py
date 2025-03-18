import datetime

logs = ""

def log(text: str, verbose: bool = False):
    global logs

    if (verbose): print(text)
    arr = text.split("\n")
    for i in range(len(arr)):
        logs += f"[{str(datetime.datetime.now()).split(".")[0]}] {arr[i]}\n"

def save_logs(file):
    global logs

    with open(file, "x") as f:
        f.writelines(logs)