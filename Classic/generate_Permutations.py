# Given an array of integers, create a function that returns all its possible permutations without duplicates.


# Time O(n * n!) / Space O (n * n!)
def getPermutations(nums):
    # Base case
    if len(nums) < 2:
        return [nums]
    else:
        permutations = []
        for i in range(len(nums)):
            remaining = nums.copy()
            remaining.pop(i)
            # Rercursive case
            remainingPermutations = getPermutations(remaining)
            removeElement = [nums[i]]
            for permutation in remainingPermutations:
                permutations.append(removeElement + permutation)
    return permutations

nums = [2, 5, 3]
print(getPermutations(nums))
