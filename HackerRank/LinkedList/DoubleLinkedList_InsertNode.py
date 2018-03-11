# https://www.hackerrank.com/challenges/insert-a-node-into-a-sorted-doubly-linked-list/problem

# Insert a node into a sorted doubly linked list
# head could be None as well for empty list

class Node(object):
    def __init__(self, data=None, next_node=None, prev_node = None):
       self.data = data
       self.next = next_node
       self.prev = prev_node

def SortedInsert(head, data):
    new_node = Node(data)

    if head == None:
        head = new_node
        return head
    else:
        current = head
        while data > current.data:
            if current.next == None:
                current.next = new_node
                new_node.prev = current
                return head

            current = current.next

        prev_node = current.prev
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = current
        current.prev = new_node

        return head
