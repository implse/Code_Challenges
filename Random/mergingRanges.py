# Write a function merge_ranges that takes a list of multiple meeting time ranges
# and return a list of condensed ranges.(Do not assume the meeting are in order)

t_range = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)] # return [(0, 1), (3, 8), (9, 12)]


# Time O(n log n) / Space O(n)
def merge_ranges(meetings):
    # Sort by start time
    sorted_meetings = sorted(meetings)
    # Init a list of merge_meetings with the first meeting
    merge_meetings = [sorted_meetings[0]]
    for current_start, current_end in sorted_meetings[1:]:
        last_start, last_end = merge_meetings[-1]
        # Merge if overlap
        if current_start <= last_end:
            merge_meetings[-1] = (last_start, max(last_end, current_end))
        else:
            merge_meetings.append((current_start, current_end))
    return merge_meetings


print(merge_ranges(t_range))
