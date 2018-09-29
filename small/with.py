import json
with open('nick.json', 'r') as handle:
    try:
        data = json.load(handle)
        print(data)
    except json.decoder.JSONDecodeError as error:
        print(error)
