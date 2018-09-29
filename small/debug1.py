def factorial(n):
    total = 0
    for i in range(n):
        total *= i + 1
    return total

print(factorial(5))
print(factorial(8))
