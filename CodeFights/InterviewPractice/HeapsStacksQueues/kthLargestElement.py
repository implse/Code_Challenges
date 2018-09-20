# Find the kth largest element in an unsorted array. This will be the kth largest element in sorted order,
# not the kth distinct element.

from heapq import heappush, heappop

def kthLargestElement(nums, k):
    m = []
    for n in nums:
        heappush(m, n)
    for i in range(len(m) - 1, k - 1, -1):
        heappop(m)
    return heappop(m)
