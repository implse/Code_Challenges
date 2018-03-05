# https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle/problem

# A linked list is said to contain a cycle if any node is visited more than once while traversing the list.
# It has one parameter: a pointer to a Node object named head that points to the head of a linked list.
# Your function must return a boolean denoting whether or not there is a cycle in the list.
# If there is a cycle, return true otherwise, return false.

class Node(object):
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next = next_node

def has_cycle(head):
    current = head
    nn_node = head
    while current and nn_node and nn_node.next:
        current = current.next
        nn_node = nn_node.next.next
        if current.data == nn_node.value:
            return True
    return False
