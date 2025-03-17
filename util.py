logs = []

def log(text, verbose: bool = False):
    if (verbose): print(text)
    logs.append(text + "\n")

def save_logs(file):
    with open(file, "x") as f:
        f.writelines(logs)