# https://www.hackerrank.com/challenges/reverse-a-linked-list/problem

# You’re given the pointer to the head node of a linked list. Change the next pointers of the nodes so that their order is reversed.
# The head pointer given may be null meaning that the initial list is empty.

class Node(object):
    def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

def Reverse(head):
    current_node = head
    next_node = None
    previous_node = None
    while current_node != None:
        next_node = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = next_node
    head = previous_node
    return head
