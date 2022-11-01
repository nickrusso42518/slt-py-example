import yaml
with open("office.yml", "r") as handle:
    try:
        data = yaml.safe_load(handle)
        print(data)
    except yaml.YAMLError as exc:
        print(exc)
