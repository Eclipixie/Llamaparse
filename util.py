logs = []

def log(text, to_print: bool):
    if (to_print): print(text)
    logs.append(text)

def save_logs(file):
    with open(file, "x") as f:
        f.writelines(logs)