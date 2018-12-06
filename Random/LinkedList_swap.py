# Given the head of a singly linked list, swap every two nodes and return its head.

# For example, given 1 -> 2 -> 3 -> 4, return 2 -> 1 -> 4 -> 3.

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

def swap_by_two(node):
    while node and node.next:
        node.value, node.next.value = node.next.value, node.value
        node = node.next.next
    return node
