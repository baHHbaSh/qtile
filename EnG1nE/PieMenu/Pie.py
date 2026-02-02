import json

from lib.App import*

SavestNode = {
    "Main":{

    }
}

try:
    with open("Apps.json", encoding="utf-8") as f:
        SavestNode = json.load(f)
except:
    with open("Apps.json", "w", encoding="utf-8") as f:
        json.dump(SavestNode, f)

Application(SavestNode).Launch()