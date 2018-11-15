# Two Sum

# Simple
def twoSum(nums, target):
    diff = 0
    for i in range(len(nums)):
        diff = target - nums[i]
        for j in range(i+1, len(nums)):
            if diff == nums[j]:
                return [i, j]
# Optimize
def twoSum(nums, target):
    indicies = {}
    ln = len(nums)
    for i in range(ln):
        if (target - nums[i]) in indicies:
            return [indicies[target - nums[i]], i]
        else:
            indicies[nums[i]] = i
