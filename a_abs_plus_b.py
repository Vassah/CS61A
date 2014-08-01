def a_plus_abs_b(a, b):
    if b < 0:
        return a - b
    return a + b

print(a_plus_abs_b(5, 6))
print(a_plus_abs_b(5, -6))
