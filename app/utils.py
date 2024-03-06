import os
import json

file_path = os.environ.get("JSON_DB_PATH", "../database/data.json")
if not os.path.exists(file_path):
    with open(file_path, "w") as file:
        json.dump({"foo" : "bar"}, file, indent=2)

def getData():
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return json.load(file)
    else:
        return {}

def writeData(data):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=2)
