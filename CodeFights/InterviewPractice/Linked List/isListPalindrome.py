# https://codefights.com/interview-practice/task/HmNvEkfFShPhREMn4

# Given a singly linked list of integers, determine whether or not it's a palindrome.

# Definition for singly-linked list:
class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

# Time O(n) / Sapce O(1)
def isListPalindrome(l):
    # find middle node
    slow = l
    fast = l
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    first_half = l
    second_half = reverse(slow)

    # Compare first half and second half
    while first_half and second_half:
        if first_half.value != second_half.value:
            return False
        first_half = first_half.next
        second_half = second_half.next
    return True


def reverse(l):
    current_node = l
    previous_node = None
    next_node = None
    while current_node:
        next_node = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = next_node
    return previous_node
