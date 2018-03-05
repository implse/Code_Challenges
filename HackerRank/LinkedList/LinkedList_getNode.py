# https://www.hackerrank.com/challenges/get-the-value-of-the-node-at-a-specific-position-from-the-tail/problem

# Get Node data of the Nth Node from the end.
# head could be None as well for empty list

class Node(object):

    def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

def GetNode(head, position):
    current = head
    behind = head
    step = 0
    while current.next != None:
        current = current.next
        step += 1
        if step > position:
            behind = behind.next
    return behind.data
