# https://codefights.com/interview-practice/task/gX7NXPBrYThXZuanm

# Given a singly linked list of integers l and an integer k,
# remove all elements from list l that have a value equal to k.

# For l = [3, 1, 2, 3, 4, 5] and k = 3, the output should be
# removeKFromList(l, k) = [1, 2, 4, 5]

# For l = [1, 2, 3, 4, 5, 6, 7] and k = 10, the output should be
# removeKFromList(l, k) = [1, 2, 3, 4, 5, 6, 7]

class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

def removeKFromList(l, k):
    current = l
    previous = None
    while current != None:
        if current.value != k:
            break
        current = current.next
    l = current
    while current != None:
        if current.value == k:
            if previous:
                previous.next = current.next
            current = current.next
            continue
        previous = current
        current = current.next
    return l