# https://codefights.com/interview-practice/task/HmNvEkfFShPhREMn4

# Given a singly linked list of integers, determine whether or not it's a palindrome.

# Definition for singly-linked list:
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



# Test : 0 -> 1 -> 2 -> 1 -> 0
one = ListNode(0)
one.next = ListNode(1)
one.next.next = ListNode(2)
one.next.next.next = ListNode(1)
one.next.next.next.next = ListNode(0)

print(isListPalindrome(one))

# # print list
# def printList(l):
#     node = l
#     while node != None:
#         print(node.value)
#         node = node.next
#     return l
# # printList(one)
# r = reverseList(one)
# printList(r)
