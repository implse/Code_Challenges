# https://codefights.com/interview-practice/task/HmNvEkfFShPhREMn4

# Given a singly linked list of integers, determine whether or not it's a palindrome.

class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

def reverseList(r):
    current_node = r
    next_node = None
    previous_node = None
    while current_node != None:
        next_node = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = next_node
    r = previous_node
    return r

def isListPalindrome(l):
    b = reverseList(l)
    nodeA = l
    nodeB = b
    while nodeA != None:
        if nodeA.value != nodeB.value:
            return False
            break
        nodeA = nodeA.next
        nodeB = nodeB.next
    return True
