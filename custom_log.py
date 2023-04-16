from datetime import datetime


def log(call="", status=""):
    with open("log.txt", "a+") as log:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.write(f"[{timestamp}] {call}: {status}\n")
