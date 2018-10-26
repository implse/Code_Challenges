# You have two integer arrays, a and b, and an integer target value v.
# Determine whether there is a pair of numbers, where one number is taken from a and the other from b,
# that can be added together to get a sum of v. Return true if such a pair exists, otherwise return false


# For a = [1, 2, 3], b = [10, 20, 30, 40], and v = 42, the output should be
# sumOfTwo(a, b, v) = true.

# Brute Force
def sumOfTwo(a, b, v):
    for i in a:
        for j in b:
            if i + j == v:
                return True
    return False

# Better Solution
def sumOfTwo(a, b, v):
    hash_list = dict()
    for i in b:
        hash_list[i] = 0
    for j in a:
        if (v - j) in hash_list:
            return True
    return False

# Test
a = [1, 2, 3]
b = [10, 20, 30, 40]
v = 42

print(sumOfTwo(a, b, v))
