# Implement integer exponentiation. That is, implement the pow(x, y) function, where x and y are integers and returns x^y.
# Do this faster than the naïve method of repeated multiplication.
# For example, pow(2, 10) should return 1024.

# Iterative Solution
def pow_iterative(base, exponent):
    result = 1
    # negative exponent
    if exponent < 0:
        base = 1 / base
        exponent *= -1
    for _ in range(exponent):
        result *= base
    return result

print(pow_iterative(2, 10))
print(pow_iterative(2, -10))
print(pow_iterative(2, 0))

# Recursive Solution
def pow_recursive(base, exponent):
    # Negative exponent
    if exponent < 0:
        return pow_recursive(1 / base, exponent * -1)
    # Base case
    if exponent == 0:
        return 1
    return  base * pow_recursive(base, exponent - 1)

print(pow_recursive(2, 10))
print(pow_recursive(2, -10))
print(pow_recursive(2, 0))


# Best Solution O(log exponent)

# We can rewrite x^y as the following :
    # If y is even, then x^y = (x^2) ^ (y/2)
    # If y is odd, then x^y = x * ((x^2) ^ ((y - 1) / 2))

# Iterative
def pow(base, exponent):
    # Negative exponent
    if exponent < 0:
        base = 1 / base
        exponent *= -1

    coeff = 1
    while exponent > 1:
        if exponent % 2 == 0:
            base *= base
            exponent = exponent // 2
        else:
            coeff *= base
            base *= base
            exponent = (exponent - 1) // 2
    return 1 if exponent == 0 else coeff * base

print(pow(2, 10))
print(pow(2, -10))
print(pow(2, 0))

# Recursive
def pow(x, y):
    if y < 0:
        return pow(1 / x, -y)
    elif y == 0:
        return 1
    elif y == 1:
        return x
    elif y % 2 == 0:
        return pow(x * x, y // 2)
    else: # y is odd
        return x * pow(x * x, y // 2)

print(pow(2, 10))
print(pow(2, -10))
print(pow(2, 0))
