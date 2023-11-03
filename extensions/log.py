import uuid
import json
import os.path

from datetime import datetime


MSG_LOG_FILE = "./logs/message_log.json"


def setup_logfile():
    if os.path.isfile(MSG_LOG_FILE):
        with open(MSG_LOG_FILE, "w") as f:
            f.write(r"{}")
    else:
        open(MSG_LOG_FILE, "x")
        with open(MSG_LOG_FILE, "w") as f:
            f.write(r"{}")


def generate_uuid() -> uuid.UUID:
    return uuid.uuid4()


def log_msg(uuid: uuid.UUID, msg: str, resp: str) -> None:
    with open(MSG_LOG_FILE, "r") as f:
        _data = json.load(f)

    _data[str(uuid)] = {
        "msg": msg,
        "resp": resp,
        "time": datetime.now().strftime("%d %B, %Y [%H:%M:%S]"),
    }

    with open(MSG_LOG_FILE, "w") as f:
        json.dump(_data, f, indent=4)
