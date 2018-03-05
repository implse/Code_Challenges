# https://www.hackerrank.com/challenges/delete-a-node-from-a-linked-list/problem

# Delete Node at a given position in a linked list
# return back the head of the linked list.

class Node(object):
    def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

def Delete(head, position):
    if position == 0:
        return head.next
    else:
        current = head
        prev_n = None
        next_n = None
        for i in range(position):
            prev_n = current
            current = current.next
        next_n = current.next
        prev_n.next = next_n
    return head
