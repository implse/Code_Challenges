# https://www.hackerrank.com/challenges/find-the-merge-point-of-two-joined-linked-lists/problem

# Given pointers to the head nodes of 2 linked lists that merge together at some point,
# find the Node where the two lists merge.
# It is guaranteed that the two head Nodes will be different, and neither will be NULL.

class Node(object):
    def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

def FindMergeNode(headA, headB):
    currentA = headA
    while currentA != None:
        currentB = headB
        while currentB != None:
            if currentA.data == currentB.data and headA.data != currentA.data:
                return currentA.data
            currentB = currentB.next
        currentA = currentA.next
