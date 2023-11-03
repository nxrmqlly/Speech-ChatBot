import requests
import json
import re
import pyttsx3

from extensions.log import generate_uuid, log_msg, setup_logfile
from extensions.speech import recg_speech
from os import getenv, system
from dotenv import load_dotenv
from typing import Dict

load_dotenv("./secret.env")


def get_resp(msg: str) -> Dict | None:
    uuid = generate_uuid()

    raw = requests.get(
        "http://api.brainshop.ai/get/",
        {
            "bid": getenv("BS_ID"),
            "key": getenv("BS_KEY"),
            "uid": uuid,
            "msg": msg,
        },
    )

    _resp = json.loads(raw.content)["cnt"]

    log_msg(uuid, msg, _resp)

    return _resp


def _run():
    # * Init TTS
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.setProperty("voice", engine.getProperty("voices")[0])

    while True:
        # // TODO: Speech recognition
        try:
            print("\n✅ > Speak Now\n")

            _msg = recg_speech()
            print(f"💬 > {_msg}")

            resp = re.sub(
                r"<([a-z]+)(?![^>]*\/>)[^>]*> *[a-zA-Z0-9]+ *<(\/[a-z]+)>",
                "",
                get_resp(_msg),
            )

            print(f"🤖 > {resp}")

            # * TTS
            engine.say(resp)
            engine.runAndWait()

        except KeyboardInterrupt:
            quit(0)


if __name__ == "__main__":
    system("cls")
    setup_logfile()
    _run()
