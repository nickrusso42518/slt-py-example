def print_name():
    print("nick russo"[99])

def run_loop(repeat):
    for i in range(repeat):
        try:
            print_name()
        except IndexError:
            print("oops!")

run_loop(3)
