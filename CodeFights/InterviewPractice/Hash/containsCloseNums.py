# https://codefights.com/interview-practice/task/njfXsvjRthFKmMwLC/description

# Given an array of integers nums and an integer k, determine whether there are two
# distinct indices i and j in the array where nums[i] = nums[j] and the absolute
# difference between i and j is less than or equal to k.

def containsCloseNums(nums, k):
    ln = len(nums)
    hash = dict()
    offset = 0
    for n in range(ln):
        if nums[n] not in hash:
            hash[nums[n]] = n
        else:
            offset = n - hash[nums[n]]
            hash[nums[n]] = n
            if offset <= k:
                return True
    return False
