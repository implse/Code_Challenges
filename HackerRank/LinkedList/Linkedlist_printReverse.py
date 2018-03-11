# https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list-in-reverse/problem

 # Print elements of a linked list in reverse order as standard output
 # head could be None as well for empty list

class Node(object):
    def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

def ReversePrint(head):
    current = head
    if current == None:
        return
    ReversePrint(current.next)
    print(current.data)
