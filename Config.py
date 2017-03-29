import json

def GetSettings():
    with open('config.json', 'r') as f:
        settings = json.load(f)
    return settings

settings = GetSettings()