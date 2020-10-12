# Given an array of intervals, create a functions that return a list where overlapping intervals are merged.

# intervals = [(1, 4), (5, 8), (7, 10), (9, 13), (14, 16), (16, 20), (17, 19)]
# merge =     [(1, 4), (5, 13), (14, 20)]


# Time Complexity : O (n)
def merge_intervals(intervals):
    intervals.sort()
    for i in range(len(intervals) - 1):
        if intervals[i][1] >= intervals[i + 1][0]:
            intervals[i + 1] = (intervals[i][0], max(intervals[i][1], intervals[i + 1][1]))
            intervals[i] = ()
    merge = []
    for interval in intervals:
        if len(interval) != 0:
            merge.append(interval)
    return merge

intervals = [(1, 4), (5, 8), (7, 10), (9, 13), (14, 16), (16, 20), (17, 19)]
print(merge_intervals(intervals))
