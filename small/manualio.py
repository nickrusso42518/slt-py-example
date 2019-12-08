import yaml
try:
    handle = open("nick.yml", "r")
    data = yaml.safe_load(handle)
    print(data)
except yaml.YAMLError as error:
    print(error)
finally:
    handle.close()
