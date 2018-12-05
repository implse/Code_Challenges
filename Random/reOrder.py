# Given a pivot x, and a list lst, partition the list into three parts.

# The first part contains all elemenets in lst that are less than x
# The second part contains all elemenets in lst that are equal to x
# The third part contains all elemenets in lst that are larger than x
# Ordering within a part can be arbitrary.

# For example, given x = 10 and lst = [9, 12, 3, 5, 14, 10, 10], one partition may be `[9, 3, 5, 10, 10, 12, 14]

lst = [9, 12, 3, 5, 14, 10, 10]
pivot = 10

# Naïve solution
def reorder(lst, pivot):
    first = list()
    second = list()
    third = list()
    for i in range(len(lst)):
        if lst[i] < pivot:
            first.append(lst[i])
        if lst[i] > pivot:
            third.append(lst[i])
        if lst[i] == pivot:
            second.append(lst[i])
    return first + second + third

print(reorder(lst, pivot))

# In place solution
def reorder(lst, pivot):
    i = 0
    j = 0
    k = len(lst) - 1
    while j < k:
        if lst[j] == pivot:
            j += 1
        elif lst[j] < pivot:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
            j += 1
        else:
            lst[j], lst[k] = lst[k], lst[j]
            k -= 1
    return lst

print(reorder(lst, pivot))
