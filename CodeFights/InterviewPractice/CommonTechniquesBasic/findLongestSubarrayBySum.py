# You have an unsorted array arr of non-negative integers and a number s.
# Find a longest contiguous subarray in arr that has a sum equal to s.

# Return two integers that represent its inclusive bounds.

# If there are several possible answers, return the one with the smallest left bound.

# If there are no answers, return [-1].

# Your answer should be 1-based, meaning that the first position of the array is 1 instead of 0.

# Naïve solution
def findLongestSubarrayBySum(s, arr):
    index_range = [1, 1]
    solution = False
    for i in range(len(arr)):
        result = arr[i]
        if arr[i] == s:
            index_range = [i+1, i+1]
            solution = True
        for j in range(i+1, len(arr)):
            result += arr[j]
            if result == s and (index_range[1] - index_range[0] < ((j+1) - (i+1))):
                index_range = [i+1, j+1]
                solution = True
                if len(arr) == ((index_range[1] - index_range[0])+1):
                    return index_range
    return index_range if solution else [-1]
