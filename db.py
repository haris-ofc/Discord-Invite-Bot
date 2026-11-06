import json
import os
import threading

FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.json")
_lock = threading.Lock()

try:
    with open(FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    data = {"guilds": {}}


def save() -> None:
    with _lock:
        tmp = FILE + ".tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(data, f)
        os.replace(tmp, FILE)


def guild(gid: int) -> dict:
    return data["guilds"].setdefault(
        str(gid), {"log_channel": None, "stats": {}, "members": {}}
    )


def stat(gid: int, uid: int) -> dict:
    return guild(gid)["stats"].setdefault(
        str(uid), {"regular": 0, "fake": 0, "left": 0, "bonus": 0}
    )


def total(s: dict) -> int:
    return s["regular"] + s["bonus"] - s["left"] - s["fake"]
