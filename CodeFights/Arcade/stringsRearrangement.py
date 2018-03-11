# https://codefights.com/arcade/intro/level-7/PTWhv2oWqd6p4AHB9

# Given an array of equal-length strings, check if it is possible to rearrange the
# strings in such a way that after the rearrangement the strings at consecutive
# positions would differ by exactly one character.

# For inputArray = ["aba", "bbb", "bab"], the output should be
# stringsRearrangement(inputArray) = false;

# All rearrangements don't satisfy the description condition.

# For inputArray = ["ab", "bb", "aa"], the output should be
# stringsRearrangement(inputArray) = true.


# Solution with itertools
from itertools import permutations

def stringsRearrangement(inputArray):
    all_perm = permutations(inputArray)
    for p in all_perm:
        consecutive = True
        for i in range(len(p) - 1):
            if not charDiff(p[i], p[i+1]):
                consecutive = False
                break
        if consecutive:
            return True
    return False

def charDiff(str1, str2):
    diff_count = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            diff_count += 1
    return diff_count == 1


# Solution with permutations function based on Heap's
import copy
def stringsRearrangement(inputArray):
    all_perm = allPerm(inputArray, len(inputArray))
    for p in all_perm:
        consecutive = True
        for i in range(len(p) - 1):
            if not charDiff(p[i], p[i+1]):
                consecutive = False
                break
        if consecutive:
            return True
    return False

def charDiff(str1, str2):
    diff_count = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            diff_count += 1
    return diff_count == 1

# Heap's Algorithm
def allPerm(data, n):
    permutations = []
    # Simple swap list values function
    def swap(arr, index1, index2):
        arr[index1], arr[index2] = arr[index2], arr[index1]
    # Permutations function
    def perm(data, n):
        if n == 1:
            a = copy.deepcopy(data)
            permutations.append(a)
        else:
            for i in range(0, n-1):
                perm(data, n-1)
                if n%2 == 0:
                    swap(data, i, n-1)
                else:
                    swap(data, 0, n-1)
            perm(data, n-1)
    perm(data, n)
    return permutations
