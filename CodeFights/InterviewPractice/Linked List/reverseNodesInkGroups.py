# https://codefights.com/interview-practice/task/XP2Wn9pwZW6hvqH67

# Given a linked list l, reverse its nodes k at a time and return the modified list.
# k is a positive integer that is less than or equal to the length of l.
# If the number of nodes in the linked list is not a multiple of k, then the nodes that are left out at the end should remain as-is.
#
# You may not alter the values in the nodes - only the nodes themselves can be changed.

# clues

# The basic steps are:

# 0. Start at head node, set to current;

# 1. Scan ahead K elements from current position with a separate pointer, ahead.
# If you reach the end, just return, because you do not have to reverse 'partial' groups.

# 2. Reverse the list between your current pointer and the pointer that is K away.
# The only difference from a 'normal' reversing of a linked list is that you need to pay attention to what ahead.next originally pointed to.
# You cannot just assume it was NULL.

# 3. Set current to the original ahead.next node, and go back to step 1

class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

# Recursive Method
def reverseNodesInKGroups(l, k):
    current = l
    head_prev = None
    head_next = None
    step = k
    cycle = size(l)//k
    if cycle < 1:
        head_next = current
        while current != None:
            current = current.next
        return head_next
    while current != None and step > 0:
        head_next = current.next
        current.next = head_prev
        head_prev = current
        current = head_next
        step -= 1
    if head_next != None:
        l.next = reverseNodesInKGroups(head_next, k)
    return head_prev

def size(l):
    size = 0
    current = l
    while current != None:
        size += 1
        current = current.next
    return size
