# Given a list of float number, insert "+", "-", "*" or "/" between each consecutive pair of numbers to
# find the maximum value you can get. For simplicity, assume that all operators are of equal precedence
# order and evaluation happens from left to right.
#
# Example:
# (1, 12, 3) -> 1 + 12 * 3 = 39

def max_value(nums):
    if nums is None:
        return float("-inf")

    def directed_max_value(summed, choose):
        # Base Case
        if choose == len(nums):
            max_found[0] = max(max_found[0], summed)
            return
        # Recursive Case
        directed_max_value(summed + nums[choose], choose + 1)
        directed_max_value(summed - nums[choose], choose + 1)
        directed_max_value(summed * nums[choose], choose + 1)
        if nums[choose] != 0:
            directed_max_value(summed / nums[choose], choose + 1)

    max_found = [float("-inf")]
    directed_max_value(nums[0], 1)
    return max_found[0]


print(max_value([1, 12, 3]))
