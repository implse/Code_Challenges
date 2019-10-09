# Given an integer n, replace its bits starting from the bit at position
# a to the bit at position b, inclusive, with the bits of integer k.
# Count from the least significant bit to the most significant bit,
# starting from 0.

def insertBits(n, a, b, k):
    n = str(bin(n)[2:])
    long_n = (32 - len(n)) * "0" + n
    k = str(bin(k << a)[2:])
    long_k = (32 - len(k)) * "0" + k
    a_insert = 32 - a
    b_insert = 32 - b - 1
    insert = long_n[:b_insert] + long_k[b_insert:a_insert] + long_n[a_insert:]
    return int(insert, 2)
