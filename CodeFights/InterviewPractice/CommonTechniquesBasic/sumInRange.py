# You have an array of integers nums and an array queries, where queries[i] is a pair of indices (0-based).

# Find the sum of the elements in nums from the indices at queries[i][0] to queries[i][1] (inclusive) for each query,
# then add all of the sums for all the queries together. Return that number modulo 109 + 7.

# For nums = [3, 0, -2, 6, -3, 2] and queries = [[0, 2], [2, 5], [0, 5]], the output should be
# sumInRange(nums, queries) = 10.

# Brute Force
def sumInRange(nums, queries):
    sum = 0
    for q in queries:
        for i in range(q[0], q[1]+1):
            sum += nums[i]
    return sum % (10**9 + 7)

# Prefix Sum
def sumInRange(nums, queries):
    prefix_sums = [0 for x in range(len(nums)+1)]
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]
        prefix_sums[i+1] = sum
    sum = 0
    for i, j in queries:
        sum  += prefix_sums[j+1] - prefix_sums[i]
    return sum

# Make an array of prefix sums

# Iterate through the array, keeping a running total as you go.
# The length of the array should be nums.length + 1.
# Initialize with zero. At the ith step, store the value in an array prefix[i+1],
# so that prefix[i] contains the sum of all the numbers up to, but not including, i.
# The sum of all the numbers from i to j will be prefix[j+1] - prefix[i].

# nums =   [3, 0, -2, 6, -3, 2]
# prefix = [0, 3,  3, 1,  7, 4, 6]
# [0,2] = prefix[2+1] - prefix[0] = 1 - 0 = 1
# [2,5] = prefix[5+1] - prefix[2] = 6 - 3 = 3
# [0,5] = prefix[5+1] - prefix[0] = 6 - 0 = 6
