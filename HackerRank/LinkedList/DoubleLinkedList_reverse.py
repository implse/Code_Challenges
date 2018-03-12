# https://www.hackerrank.com/challenges/reverse-a-doubly-linked-list/problem

# You’re given the pointer to the head node of a doubly linked list.
# Reverse the order of the nodes in the list.
# The head node might be NULL to indicate that the list is empty.

class Node(object):
    def __init__(self, data=None, next_node=None, prev_node = None):
       self.data = data
       self.next = next_node
       self.prev = prev_node

def Reverse(head):
    current = head
    if current == None or current.next == None:
        return current
    else:
        while current != None:
            prev_node = current.prev
            current.prev = current.next
            current.next = prev_node
            current = current.prev
        prev_node = prev_node.prev
        return prev_node
