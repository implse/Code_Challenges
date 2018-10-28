# Given an array of integers, find the maximum possible sum you can get from one of its contiguous subarrays.
# The subarray from which this sum comes must contain at least 1 element.

# Brute Force O(n^2)
import math
def arrayMaxConsecutiveSum2(inputArray):
    max_sum = math.inf * -1
    for start_index in range (len(inputArray)):
        sum = 0
        for i in range (start_index, len(inputArray)):
            sum += inputArray[i]
            max_sum = max(sum, max_sum)
    return max_sum

# Kadane's Algorithm
def arrayMaxConsecutiveSum2(inputArray):
    max_current = inputArray[0]
    max_global = inputArray[0]
    for i in range(1,len(inputArray) - 1):
        max_current = max(inputArray[i], max_current + inputArray[i])
        if max_current > max_global:
            max_global = max_current
    return max_global

# Test
inputArray = [-2, 2, 5, -11, 6]
print(arrayMaxConsecutiveSum2(inputArray))
