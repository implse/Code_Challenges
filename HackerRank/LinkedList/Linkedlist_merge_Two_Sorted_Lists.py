# https://www.hackerrank.com/challenges/merge-two-sorted-linked-lists/problem

# You’re given the pointer to the head nodes of two sorted linked lists.
# The data in both lists will be sorted in ascending order.
# Change the next pointers to obtain a single, merged linked list which also has data in ascending order.
# Either head pointer given may be null meaning that the corresponding list is empty.

class Node(object):
    def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

def MergeLists(headA, headB):
    dummy = Node()
    tail = dummy
    while headA and headB:
        if headA.data < headB.data:
            tail.next = headA
            headA = headA.next
        else:
            tail.next = headB
            headB = headB.next
        tail = tail.next
    tail.next = headA or headB
    return dummy.next
