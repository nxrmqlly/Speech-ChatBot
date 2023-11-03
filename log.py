import uuid
import json

from datetime import datetime


def generate_uuid() -> uuid.UUID:
    return uuid.uuid4()


def _log_msg(uuid: uuid.UUID, msg: str, resp: str) -> None:
    with open("msg_log.json", "r") as f:
        _data = json.load(f)

    _data[str(uuid)] = {
        "msg": msg,
        "resp": resp,
        "time": datetime.now().strftime("%d %B, %Y [%H:%M:%S]"),
    }

    with open("msg_log.json", "w") as f:
        json.dump(_data, f, indent=4)
