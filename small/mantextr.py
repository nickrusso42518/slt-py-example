try:
    handle = open("office.txt", "r")
    data = handle.read()
    print(data)
except IOError as exc:
    print(exc)
finally:
    handle.close()
