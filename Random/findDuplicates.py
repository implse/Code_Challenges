# You are given an array of length n + 1 whose elements belong to the set {1, 2, ..., n}.
# By the pigeonhole principle, there must be a duplicate. Find it in linear time and space.

def duplicate(lst):
    i = 0
    while i < len(lst):
        if lst[i] != i:
            j = lst[i]
            if lst[j] == lst[i]:
                return j
            lst[i], lst[j] = lst[j], lst[i]
        else:
            i += 1
    raise "No duplicates"

# Test
d = [3, 5, 8, 6, 1, 3, 9, 4, 2, 7]

print(duplicate(d))
