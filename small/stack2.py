import sys
def get_endian():
    return sys.byteorder[10]

def print_result():
    print (get_endian())

print_result()
