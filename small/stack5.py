def print_name():
    raise NotImplementedError('ran out of time')

def run_loop(repeat):
    for i in range(repeat):
        try:
            print_name()
        except NotImplementedError as exc:
            print(exc)

run_loop(3)
