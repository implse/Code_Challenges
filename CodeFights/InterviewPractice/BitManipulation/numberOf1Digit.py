Write a function that takes an unsigned (positive) integer and returns
the number of 1 bits its binary representation contains.
This value is also known as the integer's Hamming weight.

# Kernighan's Algorithm
def numberOf1Bits(n):
    res = 0
    while n != 0:
        n = n & (n - 1)
        res += 1
    return res

# Solution 1
def numberOf1Bits__(n):
    res = 0
    while n != 0:
        res += n & 1
        n = n >> 1
    return res
