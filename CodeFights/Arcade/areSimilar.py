# https://codefights.com/arcade/intro/level-4/xYXfzQmnhBvEKJwXP

# Two arrays are called similar if one can be obtained from another by swapping
# at most one pair of elements in one of the arrays.

def areSimilar(a, b):
    swap_a = []
    swap_b = []
    for i in range(len(a)):
        if a[i] != b[i]:
            swap_a.append(a[i])
            swap_b.append(b[i])
    if swap_a != swap_b[::-1]:
        return False
    return True
