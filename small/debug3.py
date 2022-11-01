def factorial(n):
    total = 1
    for i in range(n):
        total *= i + 1
        # print(f"i={i}, total={total}")
        print(f"{i=}, {total=}")
    return total

print(factorial(5))
print(factorial(8))
