import json
from pathlib import Path

class DataManager:

    data = {}
    source = {
        "icon" : Path(__file__).resolve().parent/"source"/"Icon.ico"
    }

    def g():
        print("1")