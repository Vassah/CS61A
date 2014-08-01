def square(n):
    return n*n

def product(n, term):
    if n == 0:
        return 1
    return term(n) * product((n - 1), term)

def factorial(n):
    return n * product((n - 1), (lambda x: x))

print(product(4, square))
print(product(3, (lambda x: 2 * x)))
print(product(6, (lambda x: 2)))

print(factorial(4))
print(factorial(6))
