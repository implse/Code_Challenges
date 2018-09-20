# Given a sorted integer array that does not contain any duplicates, return a summary of the number ranges it contains.

# For nums = [-1, 0, 1, 2, 6, 7, 9],
# composeRanges(nums) = ["-1->2", "6->7", "9"].

def findEnd(arr, start_index):
    prev = start_index
    for i in range(start_index + 1, len(arr)):
        if arr[prev] != arr[i] - 1:
            return i - 1
        prev = i
    return prev

def composeRanges(nums):
    start_index = 0
    end_index = 0
    output_range = []
    while start_index < len(nums):
        end_index = findEnd(nums, start_index)
        if start_index != end_index and start_index < len(nums) - 1:
            output_range.append(str(nums[start_index])+"->"+str(nums[end_index]))
        else:
            output_range.append(str(nums[start_index]))
        start_index = end_index + 1
    return output_range
