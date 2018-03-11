# https://www.hackerrank.com/challenges/delete-duplicate-value-nodes-from-a-sorted-linked-list/problem

# You're given the pointer to the head node of a sorted linked list, where the data in the nodes is in ascending order.
# Delete as few nodes as possible so that the list does not contain any value more than once.
# The given head pointer may be null indicating that the list is empty.

class Node(object):
    def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

def RemoveDuplicates(head):
    current = head
    next_next = None
    while current != None and current.next != None:
        if current.data == current.next.data:
            next_next = current.next.next
            if next_next == None:
                current.next = None
                break
            current.next = next_next
        if current.data != current.next.data:
            current = current.next
    return head
