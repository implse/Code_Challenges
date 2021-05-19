# Given an array of intervals, create a functions that return a list where overlapping intervals are merged.

# intervals = [(1, 4), (5, 8), (7, 10), (9, 13), (14, 16), (16, 20), (17, 19)]
# merge =     [(1, 4), (5, 13), (14, 20)]


# In place Solution : Time Complexity : O (n log(n)) / Space O(n + n)
def merge_intervals(intervals):
    intervals.sort() # n log(n)
    for i in range(len(intervals) - 1):
        if intervals[i][1] >= intervals[i + 1][0]:
            intervals[i + 1] = (intervals[i][0], max(intervals[i][1], intervals[i + 1][1]))
            intervals[i] = ()
    merge = []
    for interval in intervals:
        if len(interval) != 0:
            merge.append(interval)
    return merge

# Better variable name
def merge_intervals(intervals):
    intervals.sort()
    for i in range(len(intervals) - 1):
        current_start, current_end = intervals[i]
        next_start, next_end = intervals[i + 1]
        if current_end >= next_start:
            intervals[i + 1] = (current_start, max(current_end, next_end))
            intervals[i] = ()
    merge = [interval for interval in intervals if len(interval) != 0 ]
    return merge


intervals = [(1, 4), (5, 8), (7, 10), (9, 13), (14, 16), (16, 20), (17, 19)]
intervals = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
print(merge_intervals(intervals))
