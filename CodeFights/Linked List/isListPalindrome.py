# https://codefights.com/interview-practice/task/HmNvEkfFShPhREMn4

# Given a singly linked list of integers, determine whether or not it's a palindrome.

# Definition for singly-linked list:
class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

def isListPalindrome(l):
    # Check for Empty list
    if not l or not l.next:
        return True
    # Get the size and the middle point
    size = 0
    node = l
    while node != None:
        size += 1
        node = node.next
    middle = size // 2
    # Place the middle node
    middle_node = l
    for i in range(middle):
        middle_node = middle_node.next
    if size % 2 == 1:
        middle_node = middle_node.next
    # Reverse
    current_node = middle_node
    next_node = current_node.next
    for _ in range(middle - 1):
        next_node.next, current_node, next_node = current_node, next_node,next_node.next
    # Check palindrome
    for _ in range(middle):
        if current_node.value != l.value:
            return False
        current_node = current_node.next
        l = l.next
    return True
