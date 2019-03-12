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
