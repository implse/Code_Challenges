# https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list/problem

# Insert Node at a specific position in a linked list
# head input could be None as well for empty list
# return back the head of the linked list.

class Node(object):
    def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

def InsertNth(head, data, position):
    new_n = Node(data)
    if position == 0:
        new_n.next = head
        head = new_n
    else:
        current = head
        for i in range(position-1):
            current = current.next
        new_n.next = current.next
        current.next = new_n
    return head
