# Given an array of integers, create a function that returns all its possible permutations without duplicates.


# Time O(n * n!) / Space O (n * n!)
def getPermutations(nums):
    # Base case
    if len(nums) < 2:
        return [nums]
    else:
        all_permutations = []
        for i in range(len(nums)):
            remaining = nums.copy()
            remaining.pop(i)
            # Rercursive case
            permutations = getPermutations(remaining)
            removeElement = [nums[i]]
            for permutation in permutations:
                all_permutations.append(removeElement + permutation)
    return all_permutations

nums = [2, 5, 3]
print(getPermutations(nums))
