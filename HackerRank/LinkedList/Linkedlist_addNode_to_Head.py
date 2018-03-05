# https://www.hackerrank.com/challenges/insert-a-node-at-the-head-of-a-linked-list/problem

 # Insert Node at the begining of a linked list
 # head input could be None as well for empty list
  # return back the head of the linked list

class Node(object):
    def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

def Insert(head, data):
    new_n = Node(data)
    if head == None:
        head = new_n
    else:
        new_n.next = head
        head = new_n
    return head
