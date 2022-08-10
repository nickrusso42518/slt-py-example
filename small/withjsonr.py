import json
with open("office.json", "r") as handle:
    try:
        data = json.load(handle)
        print(data)
    except json.decoder.JSONDecodeError as exc:
        print(exc)
