def factorial(n):
    total = 1
    for i in range(n):
        print(f'iter: {i+1}, total before: {total}')
        total *= i + 1
        print(f'iter: {i+1}, total after: {total}')
    return total

print(factorial(5))
print(factorial(8))
