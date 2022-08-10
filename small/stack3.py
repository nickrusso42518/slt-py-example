import sys
def get_endian():
    return sys.byteorder[42518]

def print_result():
    try:
        print (get_endian())
    except IndexError as exc:
        print(exc)

print_result()
