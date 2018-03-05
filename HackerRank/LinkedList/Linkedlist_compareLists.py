# https://www.hackerrank.com/challenges/compare-two-linked-lists/problem

# You’re given the pointer to the head nodes of two linked lists.
# Compare the data in the nodes of the linked lists to check if they are equal.
# The lists are equal only if they have the same number of nodes and corresponding nodes contain the same data.
# Either head pointer given may be null meaning that the corresponding list is empty.

class Node(object):
    def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

def CompareLists(headA, headB):
    if headA == None and headB == None:
        return 1
    if headA == None and headB != None or headA != None and headB == None or headA.data != headB.data:
        return 0
    return CompareLists(headA.next, headB.next)
