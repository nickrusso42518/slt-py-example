import sys
def get_endian():
    return sys.byteorder

def print_result():
    print (get_endian())

print_result()
