# Given an array of integers, determine whether it contains a Pythagorean triplet.
# Recall that a Pythagorean triplet (a, b, c) is defined by the equation a2+ b2= c2.

# Naive Solution O(n^3)
def Pythagorean_triplet(array):
    ln = len(array)
    if ln < 3:
        return False
    array = [x**2 for x in array]
    for a in range(ln):
        for b in range(a + 1, ln):
            for c in range(b + 1, ln):
                if array[a] + array[b] == array[c]:
                    return True
    return False

# Better Solution O(n^2)
def Pythagorean_triplet(array):
    ln = len(array)
    if ln < 3:
        return False
    # Sorted (n log(n)) + Square O(n)
    array = sorted([x**2 for x in array])
    for c in reversed(range(ln)):
        a = 0
        b = c - 1
        while a < b:
            if array[a] + array[b] == array[c]:
                return True
            elif array[a] + array[b] < array[c]:
                a += 1
            else:
                b -= 1
    return False
