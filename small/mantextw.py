try:
    handle = open("house.txt", "w")
    handle.write("I live in a 3BD/2BR house which is white and blue in color\n")
except IOError as exc:
    print(exc)
finally:
    handle.close()
