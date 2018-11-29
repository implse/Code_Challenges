# https://codefights.com/interview-practice/task/pMvymcahZ8dY4g75q

# Given an array a that contains only numbers in the range from 1 to a.length,
# find the first duplicate number for which the second occurrence has the minimal index.
# In other words, if there are more than 1 duplicated numbers, return the number
# for which the second occurrence has a smaller index than the second occurrence
# of the other number does. If there are no such elements, return -1.

# Time Complexity : O(n) / Space Complexity : O(1)
def firstDuplicate(a):
    ln = len(a)
    for i in a:
        idx = (i - 1) % ln
        if a[idx] > ln:
            return idx + 1
        a[idx] += ln
    return - 1

# Time Complexity : O(n) / Space Complexity : O(n)
def firstDuplicate(a):
    num = {}
    for n in a:
        if n in num:
            return n
        else:
            num[n] = 1
    return -1
