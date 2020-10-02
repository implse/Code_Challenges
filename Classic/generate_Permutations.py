# Given an array of integers, create a function that returns all possible permutations.

# Time O(n * n!) / Space O (n * n!)
def getPermutations(nums):
    # Base case
    if len(nums) < 2:
        return [nums]
    else:
        all_permutations = []
        for i in range(len(nums)):
            remaining = nums[::1] # deep copy
            chosen = remaining.pop(i)
            # Rercursive case : explore
            permutations = getPermutations(remaining)
            for permutation in permutations:
                all_permutations.append([chosen] + permutation)
    return all_permutations

nums = [1, 2, 3]
print(getPermutations(nums))


# Given an input string like "abc" return all possible permutations

def getPermutations(str):
    chars = list(str)
    # Base case
    if len(chars) == 0:
        return [chars]
    else:
        all_permutations = []
        for i in range(len(chars)):
            remaining = chars[::1]
            chosen = remaining.pop(i)
            # Recursive case
            permutations = getPermutations(remaining)
            for permutation in permutations:
                all_permutations.append([chosen] + permutation)
    return all_permutations

str = "abc"
print(["".join(p) for p in getPermutations(str)])
